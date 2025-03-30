# Execution Instructions for ABAC System with OPA

## 1. Prerequisites
Ensure you have the following installed:
- Python 3.11
- OPA (Open Policy Agent)
- Flask
- Tailwind CSS

## 2. Project Setup
1. **Clone the repository** (if applicable) or navigate to the project directory:
   ```bash
   cd abac-system
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required Python packages**:
   ```bash
   pip install flask flask-limiter opa-client pytest
   ```

## 3. Start the Servers
### Start OPA Server
1. Open a terminal and run:
   ```bash
   opa run --server ./opa_policies/
   ```

### Start Flask Backend
2. Open another terminal and run:
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   flask run --port 5000
   ```

### Start Frontend Server
3. Open a third terminal and run:
   ```bash
   python3 -m http.server 8000 -d templates/
   ```

## 4. Access the Application
- Open your web browser and navigate to: `http://localhost:8000`
- You will see the dashboard for managing policies.

## 5. Testing the Application
### Using CLI
- To test database authorization:
   ```bash
   python3 cli.py authorize-database --username=admin1 --action=read --resource=financial_records
   ```

- To test API authorization:
   ```bash
   python3 cli.py authorize-api --username=manager1 --endpoint=/api/users --method=POST
   ```

### Running Tests
- To run unit tests:
   ```bash
   pytest tests/test_backend.py -v
   ```

## 6. Key Endpoints
- **API Docs**: `http://localhost:5000/api/policies`
- **Database Authorization**: POST `http://localhost:5000/api/authorize/database`
- **API Authorization**: POST `http://localhost:5000/api/authorize/api`

## 7. Troubleshooting
- If you encounter port conflicts,
