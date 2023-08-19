# Q&A Website

This is a simple Q&A website where users can post questions and answers.

## Technologies Used

- Python
- Django
- HTML
- CSS
- Bootstrap

## Installation

1. Clone the repository
2. Install the required packages using pip: `pip install -r requirements.txt`
3. Run the migrations: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Start the development server: `python manage.py runserver`

## Usage

1. Navigate to `http://localhost:8000` to view the homepage
2. Click on "Ask a Question" to post a new question
3. Click on a question to view its details and post an answer
4. Enter your answer in the "Add an Answer" section and click "Submit"
5. To edit or delete a question or answer, click on the "Edit" or "Delete" button next to it

# Running the Project with Docker Compose

This project is designed to be easily run using Docker Compose, which simplifies the setup of the required services such as the application, PostgreSQL database, and Redis cache. Follow the steps below to get started:

## Prerequisites

Before you begin, make sure you have the following software installed on your system:

- Docker: [Installation Guide](https://docs.docker.com/get-docker/)
- Docker Compose: [Installation Guide](https://docs.docker.com/compose/install/)

## Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/IvanLapchenko/QnA-Website
   cd QnA-Website
   ```
2. **Docker compose application**

   ```bash
   docker compose up
    ```

3. **Create superuser (admin, admin)**

   ```bash
   docker exec -it <id/name of container with django app> bash
   ./create_superuser.sh 
   ```
   
4. **Access the application**

Go to the http://localhost:80/admin, login with username and password for superuser(admin) and add some categories.

You're good to go:)