import pytest
from flask_server import game_server


@pytest.fixture()
def app():
    app = game_server.app
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_first_user(client):
    response = client.get("http://127.0.0.1:5000/signup?id=666&nickname=Devil")
    assert b'OK' in response.data


def test_second_user(client):
    response = client.get("http://127.0.0.1:5000/signup?id=606&nickname=Bob")
    assert b'OK' in response.data


def test_get_all_users(client):
    response = client.get("http://127.0.0.1:5000/all_users")
    assert b'OK' in response.data


def test_p1_ready(client):
    response = client.get("http://127.0.0.1:5000/ready_for_the_game?game_id=111&id=666")
    assert b'OK' in response.data


def test_p2_ready(client):
    response = client.get("http://127.0.0.1:5000/ready_for_the_game?game_id=111&id=606")
    assert b'OK' in response.data


def test_game_test(client):
    response = client.get("http://127.0.0.1:5000/game?game_id=111&p1=606&p2=666")
    assert b'OK' in response.data
