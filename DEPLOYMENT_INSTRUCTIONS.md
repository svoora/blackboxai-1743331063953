# ABAC System Deployment Guide for macOS

## 1. Prerequisites Installation

```bash
# Install Homebrew package manager
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install required packages
brew install opa python@3.10

# Set up Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install flask requests gunicorn
```

## 2. System Deployment

```bash
# Start OPA policy engine (run in separate terminal)
opa run --server ./opa_policies/*.rego &

# Start Flask application (development)
python3 app.py

# For production use:
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 3. System Access

- Web Interface: http://localhost:5000
- API Documentation: http://localhost:5000/api/policies
- OPA Admin: http://localhost:8181

## 4. CLI Usage Examples

```bash
# Test database authorization
python3 cli.py authorize-database --username admin1 --action read --resource financial_records

# Test API authorization  
python3 cli.py authorize-api --username admin1 --endpoint /api/data --method GET
```

## 5. Configuration Files

- Policy Files: `./opa_policies/*.rego`
- User Database: `database.py`
- API Endpoints: `app.py`

## 6. Troubleshooting

```bash
# Check running services
lsof -i :5000 # Flask/Gunicorn
lsof -i :8181 # OPA

# View logs
tail -f $(brew --prefix)/var/log/opa.log