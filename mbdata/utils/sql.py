# Copyright (C) 2013 Lukas Lalinsky
# Distributed under the MIT license, see the LICENSE file for details.

import re
import sqlparse
from sqlparse import tokens as T
from sqlparse.sql import Token, TokenList, Parenthesis, Statement


def group_parentheses(tokens):
    stack = [[]]
    for token in tokens:
        if token.is_whitespace():
            continue
        if token.match(T.Punctuation, '('):
            stack.append([token])
        else:
            stack[-1].append(token)
            if token.match(T.Punctuation, ')'):
                group = stack.pop()
                stack[-1].append(Parenthesis(group))
    return TokenList(stack[0])


class Set(Statement):

    def _find_value(self):
        comparison = self.token_next_match(0, T.Comparison, '=')
        if comparison is None:
            comparison = self.token_next_match(0, T.Keyword, 'TO')
            if comparison is None:
                raise ValueError('unknown format')
        return comparison

    def get_value(self):
        token = self.token_next(self._find_value())
        if token is None or token.match(T.Punctuation, ';'):
            return None
        if token.ttype == T.String.Single:
            return token.value[1:-1]
        if token.ttype == T.Name:
            return token.value
        raise ValueError('unknown format')


class CreateTable(Statement):

    def __init__(self, tokens):
        TokenList.__init__(self, tokens)
        self._group_columns()

    def _group_columns(self):
        body_token = self.token_next_by_instance(0, Parenthesis)
        if body_token is None:
            raise ValueError('unknown format - missing TABLE body')

        tokens = []
        end_of_column = False
        for token in body_token.tokens[1:-1]:
            if end_of_column and not token.value.startswith('--'):
                if tokens and tokens[0].value not in ('CONSTRAINT', 'CHECK'):
                    body_token.group_tokens(CreateTableColumn, tokens)
                tokens = []
                end_of_column = False
            if tokens or not token.value.startswith('--'):
                tokens.append(token)
            if token.match(T.Punctuation, ','):
                end_of_column = True
        if tokens and tokens[0].value not in ('CONSTRAINT', 'CHECK'):
            body_token.group_tokens(CreateTableColumn, tokens)

    def get_name(self):
        table_token = self.token_next_match(0, T.Keyword, 'TABLE')
        if table_token is None:
            raise ValueError('unknown format - missing TABLE')

        token = self.token_next(table_token)
        if token is None:
            raise ValueError('unknown format - missing TABLE name')

        return token.value

    def get_columns(self):
        for token in self.tokens:
            if isinstance(token, Parenthesis):
                for sub_token in token.tokens:
                    if isinstance(sub_token, CreateTableColumn):
                        yield sub_token


class CreateTableColumnCheckConstraint(TokenList):

    def get_name(self):
        constraint_token = self.token_next_match(0, T.Keyword, 'CONSTRAINT')
        if constraint_token is not None:
            name_token = self.token_next(constraint_token)
            if name_token is not None:
                return name_token.value

    def _get_body_tokens(self):
        body_token = self.token_next_by_instance(0, Parenthesis)
        if body_token is not None:
            return TokenList(body_token.tokens[1:-1])

    def get_body(self):
        tokens = []
        for token in self._get_body_tokens().flatten():
            if token.is_whitespace():
                continue
            if token.ttype == T.Comment.Single:
                continue
            #if tokens and not tokens[-1].match(T.Punctuation, '(') and not token.match(T.Punctuation, ')') and not tokens[-1].value == 'E':
            #    tokens.append(Token(T.Whitespace, ' '))
            tokens.append(token)
        return group_parentheses(tokens)


class CreateTableColumn(TokenList):

    def get_name(self):
        name_token = self.token_first()

        return name_token.value

    def get_type(self):
        name_token = self.token_first()

        token = self.token_next(name_token)
        type = token.value

        token = self.token_next(token)
        if token and isinstance(token, Parenthesis):
            type += token.value
            token = self.token_next(token)

        if token and token.normalized == 'WITH':
            t = self.token_next(token)
            if t and t.normalized == 'TIME':
                t = self.token_next(t)
                if t and t.normalized == 'ZONE':
                    type += ' WITH TIME ZONE'
                    token = self.token_next(t)

        if token and token.normalized == 'WITHOUT':
            t = self.token_next(token)
            if t and t.normalized == 'TIME':
                t = self.token_next(t)
                if t and t.normalized == 'ZONE':
                    type += ' WITHOUT TIME ZONE'
                    token = self.token_next(t)

        return type

    def get_default_value(self):
        token = self.token_next_match(0, T.Keyword, 'DEFAULT')
        if token is None:
            return None

        token = self.token_next(token)
        default = token.value

        token = self.token_next(token)
        if token and isinstance(token, Parenthesis):
            default += token.value
            token = self.token_next(token)

        return default

    def get_comments(self):
        comments = []
        token = self.token_next_by_type(0, T.Comment.Single)

        while token is not None:
            comments.append(token.value.strip())
            idx = self.token_index(token) + 1
            token = self.token_next_by_type(idx, T.Comment.Single)

        return comments

    def is_not_null(self):
        token = self.token_next_match(0, T.Keyword, 'NOT NULL')
        if token is None:
            return False
        return True

    def get_check_constraint(self):
        check_token = self.token_next_match(0, T.Keyword, 'CHECK')
        if check_token is None:
            return None

        tokens = []

        constraint_name_token = self.token_prev(check_token)
        if constraint_name_token is not None:
            constraint_token = self.token_prev(constraint_name_token)
            if constraint_token is not None and constraint_token.normalized == 'CONSTRAINT':
                tokens.append(constraint_token)
                tokens.append(constraint_name_token)

        tokens.append(check_token)

        body_token = self.token_next(check_token)
        tokens.append(body_token)

        return self.group_tokens(CreateTableColumnCheckConstraint, tokens)


class CreateType(Statement):

    def get_name(self):
        token = self.token_next_by_type(0, T.Name)
        if token is None:
            raise ValueError('unknown format')

        return token.value

    def get_enum_labels(self):
        enum_token = self.token_next_match(0, T.Name, 'ENUM')
        if enum_token is None:
            raise ValueError('unknown format - missing ENUM')

        parentheses_tokens = self.token_next(enum_token)
        if parentheses_tokens is None or not isinstance(parentheses_tokens, Parenthesis):
            raise ValueError('unknown format - missing parentheses after ENUM')

        labels = []
        for token in parentheses_tokens.tokens:
            if token.ttype == T.String.Single:
                labels.append(token.value[1:-1])
        return labels


def parse_statements(statements):
    for statement in statements:
        clean_tokens = group_parentheses(statement.flatten())
        first_token = statement.token_first()
        if first_token is None:
            continue
        if first_token.normalized == 'SET':
            statement = Set(clean_tokens.tokens)
        elif first_token.normalized == 'CREATE':
            second_token = statement.token_next(first_token)
            if second_token is not None:
                if second_token.normalized == 'TABLE':
                    statement = CreateTable(clean_tokens.tokens)
                elif second_token.normalized == 'TYPE':
                    statement = CreateType(clean_tokens.tokens)
        yield statement

