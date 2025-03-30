document.addEventListener('DOMContentLoaded', function() {
    // Fetch and display system status
    fetchSystemStatus();
    
    // Set up event listeners for navigation
    setupNavigation();
});

function fetchSystemStatus() {
    fetch('/api/policies')
        .then(response => response.json())
        .then(data => {
            const statusContainer = document.getElementById('status-cards');
            
            // Clear existing content
            statusContainer.innerHTML = '';
            
            // Create status cards
            for (const [policyType, policyPath] of Object.entries(data)) {
                const card = document.createElement('div');
                card.className = 'bg-white rounded-lg shadow p-4 border-l-4 border-blue-500';
                card.innerHTML = `
                    <h3 class="font-semibold text-gray-800">${policyType.toUpperCase()} Policy</h3>
                    <p class="text-sm text-gray-600">Path: ${policyPath}</p>
                    <div class="mt-2 flex items-center">
                        <span class="h-2 w-2 rounded-full bg-green-500 mr-2"></span>
                        <span class="text-xs text-gray-500">Active</span>
                    </div>
                `;
                statusContainer.appendChild(card);
            }
        })
        .catch(error => {
            console.error('Error fetching system status:', error);
        });
}

function setupNavigation() {
    // Add active class to current page in navigation
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('nav a');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('text-blue-600', 'font-medium');
            link.classList.remove('text-gray-600');
        }
    });
}

// Policy evaluation functions
async function evaluateDatabasePolicy(user, action, resource) {
    try {
        const response = await fetch('/api/authorize/database', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: user,
                action: action,
                resource: resource
            })
        });
        return await response.json();
    } catch (error) {
        console.error('Error evaluating database policy:', error);
        return { error: error.message };
    }
}

async function evaluateApiPolicy(user, method, endpoint) {
    try {
        const response = await fetch('/api/authorize/api', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: user,
                method: method,
                endpoint: endpoint
            })
        });
        return await response.json();
    } catch (error) {
        console.error('Error evaluating API policy:', error);
        return { error: error.message };
    }
}