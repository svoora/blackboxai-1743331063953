package auth.database

default allow = false

# Simple role-based access
allow {
    input.action == "read"
    input.user.role == "admin"
}

# Department-based access
allow {
    input.action == "read"
    input.user.department == input.resource.department
}

# Time-based restrictions
allow {
    input.action == "write"
    input.user.role == "manager"
    time.clock(time.now)[0] >= 9
    time.clock(time.now)[0] <= 17
}