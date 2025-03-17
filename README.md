# Finance Manager API

**Backend Engineer:** Mohammed Albattrawi  
**Location:** Gaza, Palestine  
**Contact:** mohammedalbattrawi@gmail.com | +972594212051  
**LinkedIn:** [https://www.linkedin.com/in/mohammedalbatrawi/]   

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation and Setup](#installation-and-setup)
5. [API Endpoints](#api-endpoints)
6. [Authentication](#authentication)
7. [Caching](#caching)
8. [Testing](#testing)
9. [Contributing](#contributing)
10. [License](#license)

---

## Project Overview

The **Finance Manager API** is a robust backend service designed to manage personal financial transactions. It allows users to:

- Record and categorize expenses and income.
- Upload and store receipt images securely using AWS S3.
- Retrieve transaction histories with filtering, ordering, and pagination.
- Set and monitor budgeting goals.

This project emphasizes secure authentication, efficient data handling, and seamless integration with cloud storage services.

---

## Features

- **User Authentication:** Secure user registration and login using JWT tokens.
- **Transaction Management:** CRUD operations for financial transactions with category tagging.
- **Receipt Uploads:** Direct image uploads to AWS S3 using pre-signed URLs.
- **Filtering & Ordering:** Retrieve transactions based on categories, dates, and amounts.
- **Pagination:** Efficient data retrieval with paginated responses.
- **Budgeting:** Set and track budgeting goals (planned feature).
- **Caching:** Improved performance with Redis caching.

---

## Technologies Used

- **Backend Framework:** Django, Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Cloud Services:** AWS S3 (via LocalStack for local development)
- **Caching:** Redis
- **Authentication:** JSON Web Tokens (JWT)
- **Containerization:** Docker
- **Task Queue:** Celery (planned for background tasks)

---

## Installation and Setup

### Prerequisites

- Python 3.8+
- Docker and Docker Compose
- Redis
- PostgreSQL

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/finance-manager-api.git
   cd finance-manager-api
   ```

2. **Set Up Virtual Environment:**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**

   Create a `.env` file in the project root:

   ```env
   DEBUG=True
   SECRET_KEY=your_secret_key
   DATABASE_URL=postgres://user:password@localhost:5432/finance_manager
   REDIS_URL=redis://localhost:6379/0
   AWS_ACCESS_KEY_ID=your_aws_access_key
   AWS_SECRET_ACCESS_KEY=your_aws_secret_key
   AWS_STORAGE_BUCKET_NAME=your_bucket_name
   ```

5. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

### Authentication

- **Register User:** `POST /api/v1/auth/register/`
- **Login User:** `POST /api/v1/auth/login/`

### Transactions

- **List Transactions:** `GET /api/v1/transactions/`
- **Create Transaction:** `POST /api/v1/transactions/`
- **Retrieve Transaction:** `GET /api/v1/transactions/{id}/`
- **Update Transaction:** `PUT /api/v1/transactions/{id}/`
- **Delete Transaction:** `DELETE /api/v1/transactions/{id}/`

### Receipts

- **Generate Upload URL:** `POST /api/v1/transactions/s3/upload-url/`
- **Generate Download URL:** `GET /api/v1/transactions/s3/download-url/{filename}/`

---

## Authentication

The API uses **JSON Web Tokens (JWT)** for authentication. To access protected endpoints:

1. **Obtain Token:** Send a `POST` request to `/api/v1/auth/login/` with valid user credentials to receive a JWT.
2. **Authorize Requests:** Include the token in the `Authorization` header of subsequent requests:

   ```http
   Authorization: Bearer your_jwt_token
   ```

---

## Caching

To enhance performance, the API implements caching using **Redis**. Frequently accessed data, such as transaction lists and budget details, are cached to reduce database load and improve response times.

---

## Testing

To run the test suite:

```bash
python manage.py test
```

Ensure that all tests pass before deploying or merging new features.

---

## Contributing

We welcome contributions to enhance the Finance Manager API. To contribute:

1. Fork the repository.
2. Create a new feature branch:

   ```bash
   git checkout -b feature/your_feature_name
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add your feature description"
   ```

4. Push to the branch:

   ```bash
   git push origin feature/your_feature_name
   ```

5. Open a Pull Request detailing your changes.
