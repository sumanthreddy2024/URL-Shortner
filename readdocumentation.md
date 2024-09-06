URL Shortener API

This is a basic API that allows you to shorten long URLs and redirect to the original URL. It's built using FastAPI and PostgreSQL.

Endpoints

The API has two main endpoints. The first one is the Shorten URL endpoint, which accepts a long URL and returns a shortened URL. You can access this endpoint by sending a POST request to /shorten. The second endpoint is the Redirect to Original URL endpoint, which redirects you to the original URL. You can access this endpoint by sending a GET request to /{short_code}, where {short_code} is the shortened URL.

Getting Started

To use the API, follow these steps:

Step 1: Install Dependencies To start, you need to install the necessary dependencies. You can do this by running the command pip install -r requirements.txt in your terminal.

Step 2: Set up PostgreSQL Database Next, you need to set up a PostgreSQL database and update the DATABASE_URL in database.py with your database credentials.

Step 3: Run the Application Once you've set up the database, you can run the application by executing the command uvicorn main:app --reload in your terminal.

Step 4: Use the Endpoints Finally, you can use the endpoints to shorten URLs and redirect to the original URLs. Simply send a POST request to /shorten with a long URL to get a shortened URL, and then send a GET request to /{short_code} to redirect to the original URL.