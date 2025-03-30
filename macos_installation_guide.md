# macOS Installation Guide for ABAC System with OPA

## 1. Prerequisites Installation
```bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python and dependencies
brew install python@3.11
pip3 install flask flask-limiter opa-client pytest

# Install OPA
brew install opa

# Install Tailwind CSS
npm install -g tailwindcss
```

## 2. Project Setup
```bash
# Create project structure
mkdir -p abac-system/{opa_policies,templates,static,tests}
cd abac-system
python3 -m venv venv
source venv/bin/activate
```

## 3. File Creation
```bash
# Backend files
touch app.py database.py policy_engine.py cli.py

# OPA policy files
touch opa_policies/{database_policy.rego,api_policy.rego,complex_policy.rego}

# Frontend files
touch templates/{index.html,users.html,database_policies.html,api_policies.html,policy_preview.html}
touch static/{styles.css,script.js}

# Test files
touch tests/test_backend.py
```

## 4. Execution Commands

### Start OPA Server (Terminal 1)
```bash
opa run --server ./opa_policies/
```

### Start Flask Backend (Terminal 2)
```bash
export FLASK_APP=app.py
flask run --port 5000
```

### Start Frontend (Terminal 3)
```bash
python3 -m http.server 8000 -d templates/
```
Access at: `http://localhost:8000`

## 5. Testing
```bash
# Run unit tests
pytest tests/test_backend.py -v

# Test via CLI
python3 cli.py authorize-database --user=john --action=read --resource=financial_records
python3 cli.py authorize-api --user=john --endpoint=/api/data
```

## 6. Troubleshooting

### Port Conflicts
```bash
lsof -i :5000
kill -9 $(lsof -t -i :5000)
```

### Python Path Issues
```bash
echo "alias python3=/opt/homebrew/bin/python3" >> ~/.zshrc
source ~/.zshrc
```

### OPA Permissions
```bash
chmod +x $(which opa)