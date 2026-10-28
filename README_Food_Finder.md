# Food Finder

Food Finder is a web application that helps users discover restaurants by searching for a food item or restaurant name. It is built with Python, Flask, MySQL, HTML, and CSS.

## Features

- Search for food items or restaurant names
- Case-insensitive, partial-match search
- Display matching restaurants and the food items they serve
- Responsive interface for desktop and mobile screens
- MySQL-backed results

## Technology Stack

- **Backend:** Python and Flask
- **Database:** MySQL
- **Frontend:** HTML and CSS
- **Database connector:** MySQL Connector/Python

## Project Structure

```text
Food_Finder_Improved/
├── app.py
├── requirements.txt
├── schema.sql
├── README.md
├── static/
│   └── style.css
└── templates/
    └── index.html
```

## Requirements

- Python 3.10 or newer
- MySQL Server
- pip

## Setup

1. Install and start MySQL Server.
2. Create the database and table using the SQL in `schema.sql`. For example, from a MySQL client, run the contents of that file.
3. Open a terminal in the project directory.
4. Install the Python dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Configure the database connection with environment variables:

   **Windows PowerShell**

   ```powershell
   $env:DB_HOST="localhost"
   $env:DB_USER="root"
   $env:DB_PASSWORD="your_mysql_password"
   $env:DB_NAME="food_finder"
   ```

   Replace `your_mysql_password` with your own MySQL password. Do not commit passwords or other secrets to GitHub.

6. Start the application:

   ```bash
   python app.py
   ```

7. Open `http://127.0.0.1:5000` in your browser.

## Database Structure

The application expects a table named `restaurants` with these columns:

- `Food` — the food item
- `Foodchain` — the restaurant or food-chain name

See `schema.sql` for the table definition.

## Deployment

For public hosting, deploy the Flask application to a Python-compatible hosting service and use a hosted MySQL database. Set `DB_HOST`, `DB_USER`, `DB_PASSWORD`, and `DB_NAME` in the host's private environment-variable settings. The start command for a typical Gunicorn deployment is:

```bash
gunicorn app:app
```

The deployed app cannot connect to a MySQL server running only on your own computer through `localhost`; it needs a database reachable from the hosting environment.

## Troubleshooting

- **Access denied:** Check the MySQL username and password.
- **Can't connect to MySQL:** Make sure MySQL is running and `DB_HOST` and port settings are correct.
- **No results found:** Confirm that the `restaurants` table contains records and that the food/restaurant search text matches the data.
- **Missing Python package:** Run `python -m pip install -r requirements.txt` again.
