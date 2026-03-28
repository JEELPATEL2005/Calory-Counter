# Calory-Counter

![Python](https://img.shields.io/badge/-Python-blue?logo=python&logoColor=white)

## 📝 Description

Calory-Counter is a streamlined Python-based application designed to help health-conscious individuals monitor their daily nutritional intake with ease. This project provides a robust framework for logging meals, calculating total caloric consumption, and tracking progress toward fitness objectives. Built with Python, it focuses on delivering a simple yet effective interface for users to stay accountable for their dietary habits and achieve a healthier lifestyle through data-driven tracking.

# Admin Module

## Overview
This module provides role-based administrative access for managing the web application. It is designed with a strict hierarchy to ensure security and controlled access.

---

## Roles & Permissions

### Super Admin
- There is **only one Super Admin** in the system.
- The Super Admin has full control over the platform.
- Responsibilities:
  - Create new admins
  - Manage existing admins
  - Oversee the entire system

#### Default Credentials

Username: SUPER
Password: Calorie

### Admin
- Admins are created by the Super Admin.
- Each Admin is responsible for managing the web application.
- Permissions:
  - Access and manage assigned features of the web system
- Restrictions:
  - ❌ Cannot view other admins
  - ❌ Cannot manage or modify other admin accounts
  - ❌ No access to Super Admin controls

---

## Security Design
- Strict role-based access control (RBAC)
- Single Super Admin authority
- Isolation between Admin accounts to ensure privacy and security

---

## Usage Flow
1. Login using Super Admin credentials
2. Create Admin accounts
3. Admins log in and manage the web system independently
4. Admins operate without visibility of other admins

---

## Notes
- Ensure proper authentication and authorization checks are implemented.
- Always store passwords securely (hashed & salted).
- Limit access to Super Admin credentials.

---

## Future Improvements
- Add role expansion (e.g., Editor, Moderator)
- Implement activity logs for Admin actions
- Enable password reset & multi-factor authentication (MFA)

---

## 🛠️ Tech Stack

- 🐍 Python


## 📦 Key Dependencies

```
asgiref: 3.11.1
audioop-lts: 0.2.1
blinker: 1.9.0
certifi: 2026.1.4
charset-normalizer: 3.4.4
click: 8.1.8
colorama: 0.4.6
comtypes: 1.4.10
Django: 6.0.2
Faker: 40.4.0
Flask: 3.1.0
idna: 3.11
itsdangerous: 2.2.0
Jinja2: 3.1.6
MarkupSafe: 3.0.2
```

## 📁 Project Structure

```
.
├── Calory_Counter
│   ├── Admin
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_user_created_at.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── Admin
│   │   │       ├── dashboard.html
│   │   │       ├── edit_admin.html
│   │   │       ├── edit_food.html
│   │   │       ├── manage_admins.html
│   │   │       ├── manage_foods.html
│   │   │       └── manage_users.html
│   │   ├── urls.py
│   │   └── views.py
│   ├── Calory
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── management
│   │   │   └── commands
│   │   │       └── import_food.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── templates
│   │   │   └── Calory
│   │   │       ├── add_meal.html
│   │   │       ├── bot.html
│   │   │       ├── dashboard.html
│   │   │       ├── edit_meal.html
│   │   │       ├── login.html
│   │   │       ├── meals.html
│   │   │       ├── profile.html
│   │   │       ├── register.html
│   │   │       ├── report_30.html
│   │   │       ├── report_7.html
│   │   │       ├── summary.html
│   │   │       └── update_profile.html
│   │   ├── urls.py
│   │   ├── utils.py
│   │   └── views.py
│   ├── Calory_Counter
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── wsgi.py
│   ├── calories.csv
│   ├── db.sqlite3
│   ├── generate_food_csv.py
│   ├── manage.py
│   ├── requirements.txt
│   ├── static
│   │   └── css
│   │       ├── admin_style.css
│   │       └── user_style.css
│   └── templates
│       ├── admin_layout.html
│       ├── layout.html
│       └── user_layout.html
└── requirements.txt
```

## 🛠️ Development Setup

### Python Setup
1. Install Python (v3.8+ recommended)
2. Install dependencies: `pip install -r requirements.txt`

## 👥 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Clone** your fork: `git clone  https://github.com/JEELPATEL2005/Calory-Counter.git`
3. **Create** a new branch: `git checkout -b feature/your-feature`
4. **Commit** your changes: `git commit -am 'Add some feature'`
5. **Push** to your branch: `git push origin feature/your-feature`
6. **Open** a pull request

Please ensure your code follows the project's style guidelines and includes tests where applicable.

---
