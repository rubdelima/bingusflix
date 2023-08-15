from typing import Generator

import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture()
def unit_test_client():
    """
    Create a unit test client for the FastAPI app.
    """
    return TestClient(app)


@pytest.fixture(scope='function')
def client() -> Generator:
    """
    Create a bdd test client foth the FastAPI app.
    """

    with TestClient(app) as c:
        yield c


@pytest.fixture
def context():
    """
    Variable to store context data between steps.
    Note: remember to always return the context
    variable at the end of the each steps.
    """
    b = {}
    yield b
