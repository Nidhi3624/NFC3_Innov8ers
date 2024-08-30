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

// API key for India News
const apiKey = 'c9ef3bafa2234c92a57beb93a7c5c648';

// Base URL for fetching news specifically related to Indian farmers, focusing on laws, schemes, prices, and methods
const apiUrl = `https://newsapi.org/v2/everything?q=Indian farmers AND (laws OR schemes OR prices OR methods OR government)&language=en&apiKey=${apiKey}`;

// Fetch news data from the API
fetch(apiUrl)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        const articles = data.articles;

        // Shuffle the articles array to randomize the order
        const shuffledArticles = articles.sort(() => 0.5 - Math.random());

        // Select a subset of articles to display (e.g., first 3 random articles)
        const selectedArticles = shuffledArticles.slice(0, 3);

        // Select the container where the news articles will be inserted
        const newsContainer = document.getElementById('news-articles');
        newsContainer.innerHTML = ''; // Clear previous content

        // Check if there are any articles
        if (selectedArticles.length > 0) {
            selectedArticles.forEach(article => {
                // Create a new column for each article
                const articleHtml = `
                    <div class="col-md-4" data-aos="fade-up">
                        <img src="${article.urlToImage || 'images/default_image.jpg'}" alt="blogpost pic" />
                        <div class="mt-4">
                            <small>Posted in <a href="#">${article.source.name}</a> ${new Date(article.publishedAt).toLocaleDateString()}</small>
                            <h5 class="mt-1 mb-2"><a href="${article.url}" target="_blank">${article.title}</a></h5>
                            <p>
                                ${article.description || 'No description available.'}
                            </p>
                        </div>
                    </div>
                `;

                // Append the article HTML to the news container
                newsContainer.insertAdjacentHTML('beforeend', articleHtml);
            });
        } else {
            newsContainer.innerHTML = '<p>No news articles found for the specified query.</p>';
        }
    })
    .catch(error => {
        console.error('Error fetching the specific Farmers News API:', error);
    });


    