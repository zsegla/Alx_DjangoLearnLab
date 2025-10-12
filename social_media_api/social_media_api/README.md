
# 🧩 Social Media API

## 📘 Project Overview
The **Social Media API** is a Django REST Framework-based backend that provides user authentication and profile management for a social media platform.  
This is the foundation for building a scalable social media system where users can register, log in, and manage their profiles.

---

Register
POST /api/accounts/register/

{
  "username": "mahid",
  "email": "mahid@example.com",
  "password": "12345"
}

➤ Login

POST /api/accounts/login/

{
  "username": "mahid",
  "password": "12345"
}


You’ll receive:

{
  "user": {
    "id": 1,
    "username": "mahid",
    "email": "mahid@example.com"
  },
  "token": "abc123..."
}

➤ Profile

GET /api/accounts/profile/ with header:

Authorization: Token abc123...
