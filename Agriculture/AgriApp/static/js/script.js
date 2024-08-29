AOS.init();


// Dummy data to simulate registered users
const registeredUsers = {
    'johnDoe': 'password123',
};

const loginForm = document.getElementById('login-form');
const signupForm = document.getElementById('signup-form');

if (loginForm) {
    loginForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        if (registeredUsers[username] && registeredUsers[username] === password) {
            alert('Login successful!');
            // Redirect to the dashboard or main page
            window.location.href = 'index.html';
        } else {
            alert('Incorrect username or password. Please try again.');
        }
    });
}

if (signupForm) {
    signupForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const username = document.getElementById('signup-username').value;
        const password = document.getElementById('signup-password').value;
        const confirmPassword = document.getElementById('confirm-password').value;

        if (password === confirmPassword) {
            if (registeredUsers[username]) {
                alert('Username already taken. Please choose a different one.');
            } else {
                registeredUsers[username] = password;
                alert('Sign up successful! Please log in.');
                // Redirect to the login page
                window.location.href = 'login.html';
            }
        } else {
            alert('Passwords do not match. Please try again.');
        }
    });
}

