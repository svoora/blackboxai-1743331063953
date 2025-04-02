#!/bin/bash

# Create fresh workspace directory
mkdir -p abac_system_clean/{opa_policies,templates,static,tests}

# Create minimal policy files
cat > abac_system_clean/opa_policies/database_policy.rego <<EOL
package auth.database

default allow = false

allow {
    input.action == "read"
    input.user.role == "admin"
}
EOL

cat > abac_system_clean/opa_policies/api_policy.rego <<EOL
package auth.api

default allow = false

allow {
    input.method == "GET"
    input.path == "/api/data"
    input.user.role == "viewer"
}
EOL

# Create basic backend structure
cat > abac_system_clean/app.py <<EOL
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def status():
    return jsonify({"status": "ready"})

if __name__ == '__main__':
    app.run(port=5000)
EOL

# Create simple frontend
cat > abac_system_clean/templates/index.html <<EOL
<!DOCTYPE html>
<html>
<head>
    <title>ABAC System</title>
</head>
<body>
    <h1>ABAC System Ready</h1>
    <p>New clean workspace setup complete</p>
</body>
</html>
EOL

# Create setup instructions
cat > abac_system_clean/README.md <<EOL
# Clean ABAC System Workspace

## Setup
1. Run: \`bash setup.sh\`
2. Start: \`bash run.sh\`

## Access
- Frontend: http://localhost:8000
- Backend: http://localhost:5000
EOL

echo "New clean workspace created in abac_system_clean directory"