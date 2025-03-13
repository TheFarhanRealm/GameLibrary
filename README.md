# GameLibrary
A web application built with Django, MySQL, Python, and HTML that allows users to manage a game collection using CRUD (Create, Read, Update, Delete) operations.

## GameLibrary Web Application

This is a simple **MySQL** and **Django** web application that allows you to manage a collection of games. You can add, view, edit, and delete games from the database.

---

### Features:
- Add new games
- View a list of games
- Edit and delete games

---

### Requirements:
- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Django**: Install with `pip install django`

---

### Setup:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/TheFarhanRealm/Gamelibrary.git
   ```

2. **Install dependencies**:

   Navigate to the project folder and install the required packages:

   ```bash
   cd Gamelibrary
   pip install -r requirements.txt
   ```

3. **Set up the database**:

   Apply migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

---

### Running the Project:

1. **Start the server**:

   Run this command to start the Django development server:

   ```bash
   python manage.py runserver
   ```

2. **Open the app in your browser**:

   Go to the following URL:

   [http://127.0.0.1:8000/games/](http://127.0.0.1:8000/games/)

---

### Project Structure:

```
Gamelibrary/
├── manage.py
├── db.sqlite3
└── games/
    ├── migrations/
    ├── templates/games/
    ├── admin.py
    ├── models.py
    └── views.py
```

- **`manage.py`**: Command-line tool to manage the project.
- **`db.sqlite3`**: SQLite database where game data is stored.
- **`games/`**: The Django app containing all models, views, templates, and static files related to games.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
