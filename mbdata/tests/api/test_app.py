from nose.tools import *
from mbdata.tests.api import with_client


@with_client
def test_root(client):
    rv = client.get('/')
    assert_equal(rv.status_code, 404)

