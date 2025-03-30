from typing import Dict, Any

# Mock database implementation
users_db: Dict[str, Dict[str, Any]] = {
    "admin1": {
        "username": "admin1",
        "password": "securepassword",
        "role": "admin",
        "department": "management",
        "permissions": ["read", "write", "delete"]
    },
    "manager1": {
        "username": "manager1",
        "password": "managerpass",
        "role": "manager",
        "department": "hr",
        "permissions": ["read", "write"]
    },
    "employee1": {
        "username": "employee1",
        "password": "employeepass",
        "role": "employee",
        "department": "finance",
        "permissions": ["read"]
    }
}

resources_db: Dict[str, Dict[str, Any]] = {
    "financial_records": {
        "name": "financial_records",
        "department": "finance",
        "sensitivity": "high"
    },
    "user_table": {
        "name": "user_table",
        "department": "hr",
        "sensitivity": "medium"
    }
}

api_endpoints_db: Dict[str, Dict[str, Any]] = {
    "/api/data": {
        "method": "GET",
        "required_role": "data_viewer",
        "resource": "financial_records"
    },
    "/api/users": {
        "method": "POST",
        "required_role": "admin",
        "resource": "user_table"
    }
}

def get_user(username: str) -> Dict[str, Any]:
    return users_db.get(username, {})

def get_resource(resource_name: str) -> Dict[str, Any]:
    return resources_db.get(resource_name, {})

def get_api_endpoint(endpoint: str) -> Dict[str, Any]:
    return api_endpoints_db.get(endpoint, {})