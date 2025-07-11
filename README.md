
# 📝 Blog Website (Django)

A full-featured Blog Website built with **Django**, where users can register, log in, write blog posts, edit or delete them, and browse content written by others.

## 🚀 Features

- 🔐 **User Authentication**  
  - Register / Login / Logout  
  - Only authors can edit or delete their own posts
  - Profile pictures

- 📝 **Blog Functionality**  
  - Create new blog posts  
  - Edit existing posts  
  - Delete posts  
  - View all posts

- 📋 **User Dashboard**  
  - View all your posts  
  - Manage your account and posts easily
  - Pagination 

## 🧑‍💻 Getting Started

### Prerequisites

Make sure you have Python and pip installed. Then install Django:

```
pip install django
````

### Installation

```
git clone https://github.com/Yamii07/blog-website.git
cd Blog-website
python manage.py migrate
python manage.py createsuperuser  # to create admin account
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/` to explore the site.

## 🗂️ Project Structure

```
blog-website/
├── blog/             # Main app
├── users/            # User management (auth, profiles)
├── templates/        # HTML templates
├── static/           # Static files (CSS, JS)
├── db.sqlite3        # SQLite Database
├── manage.py
└── README.md
```

## 🔒 Security Features

* Passwords stored using Django’s built-in hashing
* Only logged-in users can create/edit/delete their own blogs
* CSRF protection enabled by default

## ✅ Future Improvements

* Add categories/tags for posts
* Commenting system


## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss.

## 📄 License

This project is licensed under the MIT License.




