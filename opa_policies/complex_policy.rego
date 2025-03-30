package auth.combined

default allow = false

# Multi-attribute access control
allow {
    input.action == "read"
    input.user.role == "admin"
    input.resource == "financial_records"
}

allow {
    input.action == "write"
    input.user.role == "manager"
    input.resource == "user_table"
    input.user.department == "hr"
}

# Time-based access control
allow {
    input.action == "read"
    input.user.role == "employee"
    time.now.hour < 9
}