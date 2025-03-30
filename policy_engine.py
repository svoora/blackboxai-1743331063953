from typing import Dict, Any
import requests
import json

class PolicyEngine:
    def __init__(self, opa_url: str = "http://localhost:8181"):
        self.opa_url = opa_url
        
    def evaluate_database_policy(self, user: Dict[str, Any], action: str, resource: str) -> Dict[str, Any]:
        """Evaluate database access against OPA policies"""
        input_data = {
            "user": user,
            "action": action,
            "resource": resource
        }
        return self._query_opa("auth/database/allow", input_data)
    
    def evaluate_api_policy(self, user: Dict[str, Any], method: str, path: str, source_ip: str = "127.0.0.1") -> Dict[str, Any]:
        """Evaluate API access against OPA policies"""
        input_data = {
            "user": user,
            "method": method,
            "path": path,
            "source_ip": source_ip
        }
        return self._query_opa("auth/api/allow", input_data)
    
    def _query_opa(self, policy_path: str, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Make request to OPA server"""
        try:
            response = requests.post(
                f"{self.opa_url}/v1/data/{policy_path}",
                json={"input": input_data},
                timeout=5
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                "error": str(e),
                "allowed": False
            }

    def load_policies(self):
        """Load all policy files into OPA"""
        policies = {
            "database": open("opa_policies/database_policy.rego").read(),
            "api": open("opa_policies/api_policy.rego").read(),
            "complex": open("opa_policies/complex_policy.rego").read()
        }
        
        for name, policy in policies.items():
            requests.put(
                f"{self.opa_url}/v1/policies/{name}",
                data=policy,
                headers={"Content-Type": "text/plain"}
            )