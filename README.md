# 🛍️ EcommerceApp – Django-based Ecommerce Platform

A simple ecommerce web application built using **Django** that allows users to browse products, add items to their cart, and place orders. This project showcases core functionality of an online store, including product listing, cart management, and user authentication.

---

## 🚀 Features

- 🔐 User Authentication (Sign up, Login, Logout)
- 🛒 Add to Cart & View Cart
- 📦 Product Listing and Details View
- 🧑‍💻 Admin Interface for Product Management

---

## 🛠️ Tech Stack

- **Backend:** Django, Python  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite (Default Django DB)  

---

## 📁 Project Structure

```
EcommerceApp/
│
├── EcommerceApp/               # Main Django project folder
│   ├── admin.py
│   └── urls.py
│
├── cart/               # app to handle cart logic
│   ├── views.py             # View functions for cart
│   ├── models.py           # Database models for cart
│   ├── templates/           # HTML templates
│   ├── serializers.py/      # serializer for cart
│   └── urls.py
│
├── order/            # app to handle orders logic
│   ├── views.py             # View functions for order
│   ├── models.py         # Database models for orders
│   ├── templates/           # HTML templates
│   ├── serializers.py/    # serializer for orders
│   └── urls.py
│
├── user_registration/            # app to handle user registration and login
│   ├── views.py             # View functions for user login and registration
│   ├── models.py         # Database models for user
│   ├── templates/           # HTML templates
│   ├── serializers.py/    # serializer for user data
│   └── urls.py
│
├── media/product_images/            # to store images
│   ├── images            # image storage
│
├── product_view/            # app to handle product logic
│   ├── views.py             # View functions for product
│   ├── models.py         # Database models for product
│   ├── templates/           # HTML templates
│   ├── serializers.py/    # serializer for product
│   └── urls.py
│
└── manage.py                # Django's CLI manager
```

---

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/vedantsalvi10/Django.git
   cd Django/EcommerceApp
   ```

2. **Set up the virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```
4. **Install  djangorestframework**
   ```bash
   pip install djangorestframework
   ```
5. **Run the server**
   ```bash
   python manage.py runserver
   ```

5. **Visit** `http://127.0.0.1:8000/` in your browser

---

## 🤝 Contributions

If you'd like to contribute to this project, feel free to fork the repo and raise a pull request!

---

## 📃 License

This project is for educational purposes and doesn't include a license yet.
