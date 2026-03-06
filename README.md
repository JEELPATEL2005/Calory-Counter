# My_Djanngo_Project

## Setup & Default Admin

A helper script is provided to create an initial administrator. Run it with:

```bash
python create_admin.py
```

The script will output credentials like:

```
Username: admin
Password: Admin@12345
Role: Super Admin
```

You can then log in using either the **user login page** (`/login/`) or the
**admin login page** (`/custom-admin/login/`). Both views accept the
default username or the email address. Once authenticated as an admin you'll
be redirected to the admin dashboard.
