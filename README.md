# 📰 News Portal (Django)

A modern **News Website** built with **Python and Django**.
This project allows users to read news articles, browse categories, search posts, and leave comments.

---

# 📌 Features

* 📰 News article management
* 🗂 Categories for organizing news
* 🔎 Search functionality
* 💬 Comment system
* 🏷 Tag system
* 📄 Pagination for posts
* 📤 Share news via email
* 🔥 Latest and most popular posts
* 👨‍💻 Admin panel for managing content

---

# 🛠 Technologies Used

Backend

* Python
* Django

Frontend

* HTML
* CSS
* JavaScript
* Bootstrap

Database

* SQLite / PostgreSQL

Other

* Django Taggit

---

# 📂 Project Structure

```
news_project/
│
├── news/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── news_project/
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py
│
├── manage.py
└── README.md
```

---

# ⚙️ Installation

### 1 Clone the repository

```
git clone https://github.com/yourusername/news-portal.git
```

### 2 Go to project folder

```
cd news-portal
```

### 3 Create virtual environment

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Linux / Mac

```
source venv/bin/activate
```

---

### 4 Install dependencies

```
pip install -r requirements.txt
```

---

### 5 Run migrations

```
python manage.py migrate
```

---

### 6 Create superuser

```
python manage.py createsuperuser
```

---

### 7 Run server

```
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000
```

---

# 👨‍💻 Admin Panel

Admin panel orqali:

* News qo‘shish
* News tahrirlash
* Kategoriyalar qo‘shish
* Kommentlarni boshqarish

Admin panel:

```
http://127.0.0.1:8000/admin
```

---

# 📊 Database Models

Main models:

* Post
* Category
* Comment
* User

---

# 🚀 Future Improvements

* REST API
* Like system
* Bookmark system
* User authentication
* Newsletter subscription
* Dark mode

---

# 🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss what you would like to change.

---

# 📄 License

This project is open-source and available under the **MIT License**.
