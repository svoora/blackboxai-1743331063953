import argparse
import requests
import json
import sys
from typing import Dict, Any

BASE_URL = "http://localhost:5000"

def authorize_database(args):
    """Handle database authorization request"""
    payload = {
        "username": args.username,
        "action": args.action,
        "resource": args.resource
    }
    return _make_request("/api/authorize/database", payload)

def authorize_api(args):
    """Handle API authorization request"""
    payload = {
        "username": args.username,
        "endpoint": args.endpoint,
        "method": args.method
    }
    return _make_request("/api/authorize/api", payload)

def _make_request(endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """Make HTTP request to backend"""
    try:
        response = requests.post(
            f"{BASE_URL}{endpoint}",
            json=data,
            timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def main():
    parser = argparse.ArgumentParser(description="ABAC System CLI Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Database authorization command
    db_parser = subparsers.add_parser("authorize-database", help="Check database access")
    db_parser.add_argument("--username", required=True, help="Username")
    db_parser.add_argument("--action", required=True, help="Action (read/write)")
    db_parser.add_argument("--resource", required=True, help="Resource name")
    db_parser.set_defaults(func=authorize_database)

    # API authorization command
    api_parser = subparsers.add_parser("authorize-api", help="Check API access")
    api_parser.add_argument("--username", required=True, help="Username")
    api_parser.add_argument("--endpoint", required=True, help="API endpoint")
    api_parser.add_argument("--method", default="GET", help="HTTP method")
    api_parser.set_defaults(func=authorize_api)

    args = parser.parse_args()
    result = args.func(args)
    
    print(json.dumps(result, indent=2))
    sys.exit(0 if result.get("allowed", False) else 1)

if __name__ == "__main__":
    main()