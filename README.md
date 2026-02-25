<img width="1440" height="900" alt="Screenshot 2026-02-25 at 10 12 02 PM" src="https://github.com/user-attachments/assets/f55c3fdf-fe93-4fc0-b5eb-d47b5f615295" /><img width="1440" height="900" alt="Screenshot 2026-02-25 at 10 10 48 PM" src="https://github.com/user-attachments/assets/c2c91fd4-0fda-4905-82dd-41c6f6dacfaa" /># 🐦 SocialNest - Twitter Clone

<div align="center">

![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<h3>A fully functional Twitter clone built with Django</h3>

⭐ Internship-ready Django backend project

</div>

---

## 📌 Overview

**SocialNest** is a feature-rich Twitter clone built using Django.  
It includes authentication, social interactions, profile management, and a personalized timeline system.

This project demonstrates strong understanding of:
- Django models & relationships
- Authentication system
- Database constraints
- Social graph logic (follow system)
- Like & Retweet system
- Clean UI implementation

---

## ✨ Features

### 👤 User Authentication
- User registration with email
- Secure login & logout
- Profile management
- Login protection for actions

### 📝 Tweets
- Create tweets (max 240 characters)
- Upload images with tweets
- Edit & delete your own tweets
- View all tweets on homepage

### ❤️ Interactions
- Like / Unlike tweets
- Retweet / Unretweet
- Real-time like & retweet counts
- Unique constraint to prevent duplicate actions

### 👥 Social Features
- Follow / Unfollow users
- Follower & following counts
- View other users' profiles
- Personalized timeline (tweets from followed users)

### 🎨 Profile System
- Custom profile photos
- User bios
- Public profile pages
- Clickable avatars in navbar

### 🌙 UI/UX
- Beautiful dark theme
- Fully responsive design
- Smooth hover animations
- Full-screen image modals
- Toast notifications

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Django 6.0 | Backend framework |
| SQLite | Database |
| Bootstrap 5 | Frontend styling |
| Font Awesome | Icons |
| Python 3.13 | Programming language |

---

## 📸 Screenshots

> Replace placeholder images with real screenshots after deployment.

| Home Page | Tweet Modal | Profile Page |
|:---------:|:-----------:|:------------:|
| ![Home](<img width="1440" height="900" alt="Screenshot 2026-02-25 at 10 10 48 PM" src="https://github.com/user-attachments/assets/609adeb3-fb7e-4c72-ba21-68ecfec20204" />
) | ![Modal](<img width="1440" height="900" alt="Screenshot 2026-02-25 at 10 12 24 PM" src="https://github.com/user-attachments/assets/fb738036-b830-42bc-8cb1-69a1ae45d5d6" />
) | ![Profile](<img width="1440" height="900" alt="Screenshot 2026-02-25 at 10 12 02 PM" src="https://github.com/user-attachments/assets/9a5f6ea8-dbc7-422b-ae47-7c9d18cb1fc3" />
) |

---

## 🚀 Installation Guide

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/SahilP2321/socialnest.git
cd socialnest
```

---

### 🔹 2. Create Virtual Environment

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 🔹 3. Install Dependencies

```bash
pip install django pillow
```

---

### 🔹 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 🔹 5. Create Superuser

```bash
python manage.py createsuperuser
```

---

### 🔹 6. Run Development Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## 📖 Usage Guide

### 👤 Getting Started
1. Register a new account
2. Login
3. Upload profile photo & bio
4. Start tweeting 🚀

### 📝 Creating Tweets
- Click **Create Tweet**
- Write text (max 240 characters)
- Optionally upload image
- Click **Tweet**

### ❤️ Interacting with Tweets
- Click ❤️ to like/unlike
- Click 🔄 to retweet/unretweet
- Click images for full-screen preview

### 👥 Following Users
- Visit any user's profile
- Click **Follow**
- Their tweets appear in your timeline

---

## 🗂️ Project Structure

```
socialnest/
├── tweet/
│   ├── migrations/
│   ├── templates/
│   │   ├── layout.html
│   │   ├── tweet_list.html
│   │   ├── user_profile.html
│   │   ├── profile.html
│   │   └── tweet_form.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── media/
│   ├── photos/
│   └── profile/
├── SocialNest/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

---

## 🔒 Environment Variables

Create a `.env` file:

```
DEBUG=True
SECRET_KEY=your-secret-key-here
```

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 🚢 Deployment

You can deploy on:

- PythonAnywhere
- Render
- Railway
- DigitalOcean

### Basic Deployment Steps:
1. Upload code
2. Configure environment variables
3. Run migrations
4. Collect static files
5. Launch app 🚀

---

## 🧠 What This Project Demonstrates

- Database design with ForeignKey & OneToOne relationships
- Unique constraints for likes & retweets
- Clean MVC architecture
- Authentication & access control
- Social graph logic
- Production-ready structure

---

## 🤝 Contributing

1. Fork the repository  
2. Create feature branch  
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit changes  
   ```bash
   git commit -m "Add AmazingFeature"
   ```
4. Push to branch  
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open Pull Request  

---

## 👨‍💻 Author

**Sahil Patil**

GitHub: https://github.com/SahilP2321

---

<div align="center">

⭐ Star this repository if you found it useful!

</div>
