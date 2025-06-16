# 🛍️ EcommerceApp – Django-based Ecommerce Platform

A simple ecommerce web application built using **Django** that allows users to browse products, add items to their cart, and place orders. This project showcases core functionality of an online store, including product listing, cart management, and user authentication.

---

## 🚀 Features

- 🔐 User Authentication (Sign up, Login, Logout)
- 🛒 Add to Cart & View Cart
- 📦 Product Listing and Details View
- 💳 Checkout Process Simulation
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
├── Ecommerce/               # Main Django project folder
│   ├── settings.py
│   └── urls.py
│
├── ecommerceapp/            # Core app handling ecommerce logic
│   ├── views.py             # View functions for pages
│   ├── models.py            # Database models for products and orders
│   ├── templates/           # HTML templates
│   └── static/              # CSS & images
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
   pip install -r requirements.txt  # (if not present, install django manually)
   ```

4. **Run the server**
   ```bash
   python manage.py runserver
   ```

5. **Visit** `http://127.0.0.1:8000/` in your browser

---

## 📸 Screenshots  
*(Add screenshots of the home page, product page, cart, and admin panel here if possible)*

---

## 🤝 Contributions

If you'd like to contribute to this project, feel free to fork the repo and raise a pull request!

---

## 📃 License

This project is for educational purposes and doesn't include a license yet.
