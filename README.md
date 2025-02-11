BaaS Backend

A Backend-as-a-Service (BaaS) API built with FastAPI and MongoDB, providing user authentication, JWT-based authentication, and secure access to protected routes.

🚀 Features

✅ User Registration (/signup/) – Secure password hashing with bcrypt.

✅ User Login (/login/) – Returns a JWT authentication token.

✅ Protected Routes (/protected/) – Requires JWT authentication.

✅ MongoDB Integration – Stores user credentials securely.

✅ JWT Authentication – Ensures secure API access.



📌 Installation Guide

1️⃣ Clone the Repository

git clone https://github.com/yourusername/BaaS-Backend.git
cd BaaS-Backend

2️⃣ Create a Virtual Environment

python -m venv myenv
source myenv/Scripts/activate  # On Windows (Git Bash)
# OR
source myenv/bin/activate  # On macOS/Linux

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Set Up Environment Variables

Create a .env file in the project directory and add:

SECRET_KEY=your_generated_secret_key

⚠️ Do not share your SECRET_KEY! Generate one using:

python -c "import secrets; print(secrets.token_hex(32))"

5️⃣ Start the FastAPI Server

uvicorn main:app --reload

✅ Server running on: http://127.0.0.1:8000



📜 API Endpoints

🔹 User Signup (POST /signup/)

Registers a new user with a hashed password.

Example Request:

{
    "name": "John Doe",
    "email": "johndoe@example.com",
    "password": "securepassword"
}

Example Response:

{ "message": "User registered successfully" }

🔹 User Login (POST /login/)

Authenticates a user and returns a JWT token.

Example Response:

{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI...",
    "token_type": "bearer"
}

🔹 Protected Route (GET /protected/)

Requires authentication via JWT token.

If a valid token is provided, it returns:

{ "message": "Welcome, johndoe@example.com!" }

If no token is provided, it returns:
    { "detail": "Not authenticated" }


🔑 How to Use JWT Authentication

1️⃣ Get a JWT Token

Login using POST /login/.

Copy the access_token from the response.

2️⃣ Use Token to Access Protected Routes

In Swagger UI (http://127.0.0.1:8000/docs), click Authorize.

Paste the token in this format:

Bearer eyJhbGciOiJIUzI1NiIsInR5cCI...

Click Authorize and now you can access /protected/.



🎯 Project Structure

BaaS-Backend/
│── main.py            # Main FastAPI application
│── auth.py            # Authentication (JWT, password hashing)
│── database.py        # MongoDB connection
│── .env               # Secret keys (DO NOT SHARE)
│── requirements.txt   # Required dependencies
│── .gitignore         # Files to exclude from GitHub

🤝 Contributing

Fork the repository.

Create a new branch (feature-branch).

Commit your changes.

Push to your branch and create a Pull Request.