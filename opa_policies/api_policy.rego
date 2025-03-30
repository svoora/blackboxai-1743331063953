package auth.api

default allow = false

# Endpoint-based authorization
allow {
    input.method == "GET"
    input.path == "/api/data"
    input.user.roles[_] == "data_viewer"
}

allow {
    input.method == "POST"
    input.path == "/api/users"
    input.user.roles[_] == "admin"
}

# IP-based restrictions
allow {
    input.method == "GET"
    input.path == "/api/sensitive"
    input.user.roles[_] == "auditor"
    net.cidr_contains("192.168.1.0/24", input.source_ip)
}