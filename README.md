# OAuth 2.0 API Security Lab

## Description
This project demonstrates OAuth 2.0 authentication using GitHub and Flask. It includes login, protected routes, and session-based authorization.

## Features
- GitHub OAuth Login
- Protected API endpoint
- Session authentication
- Logout functionality

## Tech Stack
- Python
- Flask
- Authlib
- GitHub OAuth

## Routes
- /login
- /callback
- /profile (protected)
- /logout
- /api/secure-data (protected)

## How to Run
1. Install dependencies:
   pip install flask authlib requests

2. Run the app:
   python app.py

3. Open:
   http://localhost:5000/login