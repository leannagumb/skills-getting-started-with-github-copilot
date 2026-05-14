import pytest
import copy
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture
def client():
    """Test client for FastAPI app"""
    return TestClient(app, follow_redirects=False)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities data before each test"""
    original_activities = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(original_activities)