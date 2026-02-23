# SocialNest 🪹

A modern Twitter-like social media platform built with Django. Users can create tweets, upload images, like posts, and interact in a beautiful dark-themed interface.

## ✨ Features

### Current Features ✅
- **User Authentication** - Register, login, and logout functionality
- **Tweet Management** - Create, edit, and delete your own tweets
- **Image Uploads** - Add images to your tweets
- **Like/Unlike System** - Like and unlike tweets from other users
- **Full-Screen View** - Click any tweet to open in immersive full-screen mode
- **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- **Dark Mode** - Easy on the eyes with a modern dark theme

### Coming Soon 🚀
- User profiles with avatars
- Comment on tweets
- Follow other users
- Real-time notifications

## 🛠️ Tech Stack

### Backend
- **Django 4.2** - Python web framework
- **SQLite** - Database (development)
- **Django Authentication** - User management

### Frontend
- **Bootstrap 5** - Responsive UI framework
- **JavaScript** - Interactive features (modal, like buttons)
- **Font Awesome 6** - Icons
- **CSS3** - Custom styling with dark mode

### Tools & Libraries
- **Pillow** - Image processing

## 📁 Project Structure

SocialNest/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── README.md
├── tweet/
│ ├── migrations/
│ ├── templates/
│ │ └── tweet/
│ │ ├── tweet_list.html
│ │ ├── tweet_form.html
│ │ └── tweet_confirm_delete.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
├── templates/
│ └── layout.html
├── media/
└── SocialNest/
├── init.py
├── settings.py
├── urls.py
└── wsgi.py



## 🚀 Live Demo


## 📸 Screenshots


## 🏗️ Installation

### Prerequisites
- Python 3.8+
- Git

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/socialnest.git
   cd socialnest
Create virtual environment

bash
# macOS/Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
Install dependencies

bash
pip install -r requirements.txt
Run migrations

bash
python manage.py migrate
Create superuser (optional)

bash
python manage.py createsuperuser
Start server

bash
python manage.py runserver
Open browser

App: http://127.0.0.1:8000/tweet/

Admin: http://127.0.0.1:8000/admin/

📝 Usage Guide
Register/Login to create an account
Create tweets using the + button
Like tweets by clicking the heart icon
Edit/Delete only your own tweets
Click any tweet for full-screen view
Use arrow keys to navigate in full-screen
🚢 Deployment (Render)
Push code to GitHub
Create Web Service on Render
Connect GitHub repository
Add environment variables:
DEBUG=False
SECRET_KEY (generate new)
Deploy!

🤝 Contributing
Fork the repository
Create feature branch (git checkout -b feature/AmazingFeature)
Commit changes (git commit -m 'Add feature')
Push to branch (git push origin feature/AmazingFeature)
Open Pull Request


👨‍💻 Author
Sahil 

GitHub: @SahilP2321

LinkedIn: www.linkedin.com/in/sahil-patil-15273a289


