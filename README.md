
# 🍽️ Django Restaurant Menu App

A dynamic, full-stack web application built with Python and Django. This project allows a restaurant to display its menu to customers, categorized logically by meal types (Starters, Salads, Main Dishes, Desserts), and provides a robust admin dashboard for staff to manage food items and availability.

## ✨ Features

* **Categorized Menu Display:** Customers can browse food items neatly organized by their respective categories.
* **Detailed Item Views:** Clicking on a menu item opens a dedicated page displaying its full description, price, and exact category.
* **Real-time Availability:** Menu items display their current status (Available or Unavailable).
* **Admin Management Dashboard:** A secure backend interface where administrators can seamlessly add new dishes, update prices, change descriptions, and toggle item availability.
* **Responsive Design:** The frontend is styled using Bootstrap 5, ensuring the application looks great on both desktop and mobile devices.

## 🛠️ Technologies Used

* **Backend:** Python, Django (Web Framework)
* **Frontend:** HTML5, Django/Jinja Templating, Bootstrap 5 (via CDN)
* **Database:** SQLite (Django's default, can be configured for PostgreSQL/MySQL)

## 🚀 Installation & Setup

Follow these steps to get the project up and running on your local machine.

### Prerequisites
* Python 3.x installed on your machine.
* Git installed.

### Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/Food-Ordering-menu-App18.git
    cd Food-Ordering-menu-App18
    ```

2.  **Create and activate a virtual environment:**
    * *On Windows:*
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    * *On macOS/Linux:*
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install django
    ```

4.  **Apply database migrations:**
    This creates the necessary database tables for the `Item` model.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Create a superuser (Admin):**
    You will need an admin account to access the dashboard and add menu items.
    ```bash
    python manage.py createsuperuser
    ```
    *(Follow the prompts to set a username, email, and password)*

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7.  **Access the application:**
    * **Main Website:** Open `http://127.0.0.1:8000/` in your web browser.
    * **Admin Dashboard:** Open `http://127.0.0.1:8000/admin/` and log in with the superuser credentials you created in Step 5.

## 📁 Project Structure

```text
Food-ordering-app18/
│
├── mysite/                 # Main Django project configuration directory
│   ├── settings.py         # Global project settings
│   └── urls.py             # Master URL routing
│
├── restaurant_menu/        # Main application directory
│   ├── models.py           # Database schemas (Item model)
│   ├── views.py            # Business logic (MenuList, MenuItemDetail)
│   ├── urls.py             # App-specific URL routing
│   └── admin.py            # Admin dashboard configuration
│
├── templates/              # HTML frontend files
│   ├── base.html           # Master layout with Bootstrap navbar
│   ├── index.html          # Homepage displaying the categorized menu
│   ├── menu_item_detail.html # Page for individual dish details
│   └── about.html          # About the restaurant page
│
└── manage.py               # Django command-line utility
