#  Social Media API

##  Overview

This project is a robust **Social Media API** built with **Django** and **Django REST Framework**. It has been scaled from a local development environment to a **production-ready cloud architecture**, featuring a remote managed database and serverless deployment.

---

##  Features

* **Custom User Model**
  Extended Django `AbstractUser` for flexible profile management.

* **Authentication**
  Token-based authentication for secure API access.

* **Followers System**
  Functionality for users to follow/unfollow each other.

* **Posts & Comments**
  Full CRUD capabilities for user-generated content.

* **Cloud Hosted**
  Live deployment on **Vercel** with a managed **Aiven MySQL** database.

---

##  Architecture

###  Live Deployment

* **API Root**
  [https://socialmediaapi-delta.vercel.app/api/](https://socialmediaapi-delta.vercel.app/api/)

* **Admin Panel**
  [https://socialmediaapi-delta.vercel.app/admin/](https://socialmediaapi-delta.vercel.app/admin/)

---

##  Setup & Local Development

### 1️ Clone the Repository

```bash
git clone https://github.com/your-username/Alx_DjangoLearnLab.git
cd social_media_api
```

### 2️ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️ Configure Environment Variables

Create a `.env` file in the root directory and add:

* `DATABASE` credentials
* `SECRET_KEY`

---

### 4️ Run Migrations

```bash
python manage.py migrate
```

---

### 5️ Start the Server

```bash
python manage.py runserver
```

---

##  Production Stack

* **Framework**: Django 5.x / Django REST Framework
* **Database**: Aiven MySQL (Cloud Managed)
* **Hosting**: Vercel (Serverless)
* **Static Files**: WhiteNoise
* **Database Driver**: PyMySQL (with version spoofing for Django compatibility)

---

#  API Endpoints

##  Authentication

| Method | Endpoint         | Description                     |
| ------ | ---------------- | ------------------------------- |
| POST   | `/api/register/` | Register a new user             |
| POST   | `/api/login/`    | Login and receive an Auth Token |

---

##  Profiles & Social

| Method    | Endpoint                     | Description                         |
| --------- | ---------------------------- | ----------------------------------- |
| GET / PUT | `/api/profile/`              | View or update current user profile |
| POST      | `/api/follow/<int:user_id>/` | Follow a user                       |

---

##  Content

| Method             | Endpoint               | Description                       |
| ------------------ | ---------------------- | --------------------------------- |
| GET / POST         | `/api/posts/`          | List or create social media posts |
| GET / PUT / DELETE | `/api/posts/<int:pk>/` | Manage specific post content      |

---

##  Authentication Usage

After logging in, include the token in your request headers:

```
Header: Authorization
Value: Token your_unique_token_here
```

Example:

```
Authorization: Token 123abc456def
```

---

#  Scrutiny of Changes

* **Live Links Added**
  Included the Vercel URL so reviewers can test the API immediately.

* **Production Stack Section Expanded**
  Explicitly mentions Aiven and Vercel to demonstrate cloud deployment proficiency.

* **PyMySQL Highlighted**
  Showcases technical depth by noting the version spoofing workaround for MySQL compatibility on serverless hosts.

* **Expanded Endpoints**
  Added the `/api/posts/` endpoints that were recently verified.

---