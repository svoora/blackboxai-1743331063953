from flask import Flask, request, jsonify
from policy_engine import PolicyEngine
from database import get_user, get_resource, get_api_endpoint
import logging

app = Flask(__name__)
policy_engine = PolicyEngine()

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/api/authorize/database', methods=['POST'])
def authorize_database():
    """Authorize database access"""
    try:
        data = request.json
        user = get_user(data['username'])
        resource = get_resource(data['resource'])
        
        if not user or not resource:
            return jsonify({"error": "Invalid user or resource"}), 400
            
        result = policy_engine.evaluate_database_policy(
            user=user,
            action=data['action'],
            resource=resource
        )
        
        logger.info(f"Database authorization result: {result}")
        return jsonify(result)
        
    except Exception as e:
        logger.error(f"Database authorization error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/authorize/api', methods=['POST'])
def authorize_api():
    """Authorize API access"""
    try:
        data = request.json
        user = get_user(data['username'])
        endpoint = get_api_endpoint(data['endpoint'])
        
        if not user or not endpoint:
            return jsonify({"error": "Invalid user or endpoint"}), 400
            
        result = policy_engine.evaluate_api_policy(
            user=user,
            method=data.get('method', 'GET'),
            path=data['endpoint'],
            source_ip=request.remote_addr
        )
        
        logger.info(f"API authorization result: {result}")
        return jsonify(result)
        
    except Exception as e:
        logger.error(f"API authorization error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/policies', methods=['GET'])
def list_policies():
    """List available policies"""
    return jsonify({
        "database": "auth/database/allow",
        "api": "auth/api/allow"
    })

if __name__ == '__main__':
    policy_engine.load_policies()
    app.run(host='0.0.0.0', port=5000, debug=True)