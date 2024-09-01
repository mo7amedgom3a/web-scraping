# Flask Web Application with Redis, Rate Limiting, and Web Scraping

This project is a Flask web application that demonstrates user authentication, rate limiting, logging, caching with Redis, and web scraping using MechanicalSoup. The application is containerized using Docker and Docker Compose for easy setup and deployment.

## Features

1. **User Authentication**: A simple login form where users can log in with predefined credentials.
2. **Redis Cache**: Redis is used to store user sessions and count the number of visits to the login page.
3. **Rate Limiting**: The application limits the number of login attempts from a single IP address to prevent abuse.
4. **Logging**: All significant actions (like successful logins, failed attempts, and rate limit hits) are logged to a file.
5. **Web Scraping**: A Python script using MechanicalSoup automates login and scrapes the dashboard page to verify successful logins.
6. **Error Handling**: If a user exceeds the rate limit, a friendly error page with an "angry cat" image is displayed.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **Redis**: An in-memory data structure store used as a database, cache, and message broker.
- **MechanicalSoup**: A Python library for automating interaction with websites.
- **Docker**: Containerization of the application for easy deployment.
- **Docker Compose**: Tool for defining and running multi-container Docker applications.

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Web Scraping Flask Application

This project is a Flask web application that demonstrates various features such as user authentication, rate limiting, logging, caching with Redis, and web scraping using MechanicalSoup. The application is containerized using Docker and Docker Compose for easy setup and deployment.

### Features

1. **User Authentication**: Users can log in using a simple login form with predefined credentials.
2. **Redis Cache**: Redis is utilized to store user sessions and keep track of the number of visits to the login page.
3. **Rate Limiting**: The application limits the number of login attempts from a single IP address to prevent abuse.
4. **Logging**: All significant actions, including successful logins, failed attempts, and rate limit hits, are logged to a file.
5. **Web Scraping**: A Python script using MechanicalSoup automates the login process and scrapes the dashboard page to verify successful logins.
6. **Error Handling**: If a user exceeds the rate limit, a friendly error page with an "angry cat" image is displayed.

### Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **Redis**: An in-memory data structure store used as a database, cache, and message broker.
- **MechanicalSoup**: A Python library for automating interaction with websites.
- **Docker**: Containerization of the application for easy deployment.
- **Docker Compose**: A tool for defining and running multi-container Docker applications.

### Prerequisites

Before you begin, make sure you have the following installed on your system:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Getting Started

1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/yourprojectname.git
cd flask-redis-app
docker-compose up --build
```

