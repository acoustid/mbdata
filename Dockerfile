FROM python:3 AS build

RUN python3 -m venv /opt/poetry && \
    /opt/poetry/bin/pip install poetry && \
    ln -s /opt/poetry/bin/poetry /usr/local/bin/ && \
    poetry --version

ADD . /tmp/mbdata
RUN cd /tmp/mbdata && \
    poetry build -f wheel && \
    ls -l dist/

FROM python:3

RUN apt-get update && \
    apt-get install -y --no-install-recommends postgresql-client dumb-init

COPY --from=build /tmp/mbdata/dist/ /tmp/dist/
RUN python -m pip install "$(ls -1 /tmp/dist/*.whl)[replication,models]" && rm -rf /tmp/dist/

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["mbslave", "sync", "-r"]
