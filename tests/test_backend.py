import pytest
from app import app
from policy_engine import PolicyEngine
from database import users_db, resources_db
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_database_authorization(client):
    """Test database authorization endpoint"""
    test_cases = [
        {
            "username": "admin1",
            "action": "read",
            "resource": "financial_records",
            "expected": True
        },
        {
            "username": "employee1",
            "action": "write",
            "resource": "financial_records",
            "expected": False
        }
    ]

    for case in test_cases:
        response = client.post(
            '/api/authorize/database',
            json=case
        )
        data = json.loads(response.data)
        assert data['result']['allowed'] == case['expected']

def test_api_authorization(client):
    """Test API authorization endpoint"""
    test_cases = [
        {
            "username": "admin1",
            "endpoint": "/api/users",
            "method": "POST",
            "expected": True
        },
        {
            "username": "employee1",
            "endpoint": "/api/users",
            "method": "POST",
            "expected": False
        }
    ]

    for case in test_cases:
        response = client.post(
            '/api/authorize/api',
            json=case
        )
        data = json.loads(response.data)
        assert data['result']['allowed'] == case['expected']

def test_policy_engine():
    """Test PolicyEngine directly"""
    engine = PolicyEngine()
    user = users_db['admin1']
    resource = resources_db['financial_records']
    
    result = engine.evaluate_database_policy(
        user=user,
        action="read",
        resource=resource
    )
    assert result['allowed'] is True

def test_invalid_input(client):
    """Test error handling for invalid input"""
    response = client.post(
        '/api/authorize/database',
        json={"invalid": "data"}
    )
    assert response.status_code == 400