# Social Media API

## Overview
This project is a Social Media API built with Django and Django REST Framework.
It includes custom user authentication with token-based authentication.

## Features
- Custom User Model
- User Registration
- User Login
- Token Authentication
- User Profile View & Update
- Followers System

## Setup Instructions

1. Clone repository
2. Install dependencies:
   pip install -r requirements.txt
3. Run migrations:
   python manage.py makemigrations
   python manage.py migrate
4. Run server:
   python manage.py runserver

## Authentication

After registering or logging in, you will receive a token.

Use this token in request headers:

Authorization: Token your_token_here

## Endpoints
```bash
POST /api/register/  
POST /api/login/  
GET/PUT /api/profile/
```
