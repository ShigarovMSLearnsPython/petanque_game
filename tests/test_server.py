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


def test_request_example(client):
    response = client.get("/signup?telegram_id=42543234")
    assert b'ok' in response.data

