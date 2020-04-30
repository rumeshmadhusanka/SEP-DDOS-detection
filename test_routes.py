import json

import pytest

from app import app


@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass  # databases and resources have to be freed at the end

    request.addfinalizer(teardown)
    return test_client


def test_default_route(client):
    response = client.get('/')
    a = json.loads(response.data.decode('utf-8'))
    assert a == {'Hello': 'World'}
    assert str(response.status) == '200 OK'


def test_health_route(client):
    response = client.get('/health')
    a = json.loads(response.data.decode('utf-8'))
    assert "cpu" in a.keys()
    assert str(response.status) == '200 OK'
