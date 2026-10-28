import os
import mysql.connector
from mysql.connector import Error
from flask import Flask, render_template, request

app = Flask(__name__)

def get_db_connection():
    """Create a connection using environment variables instead of hard-coded secrets."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "nps@123"),
        database=os.getenv("DB_NAME", "food_finder"),
    )

@app.route("/", methods=["GET", "POST"])
def index():
    # GET supports search links such as /?food=burger; POST supports the search form.
    food = (request.values.get("food") or "").strip()
    results = []
    searched = bool(food)
    error_message = None

    if searched:
        connection = None
        cursor = None
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)

            # Case-insensitive partial matching for both the food item and restaurant name.
            search_pattern = f"%{food}%"
            query = """
                SELECT DISTINCT Food, Foodchain
                FROM restaurants
                WHERE LOWER(Food) LIKE LOWER(%s)
                   OR LOWER(Foodchain) LIKE LOWER(%s)
                ORDER BY Foodchain, Food
                LIMIT 60
            """
            cursor.execute(query, (search_pattern, search_pattern))
            results = cursor.fetchall()

        except Error:
            app.logger.exception("Food Finder database query failed")
            error_message = (
                "We couldn't connect to the restaurant database. "
                "Please check the database settings and try again."
            )
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None and connection.is_connected():
                connection.close()

    return render_template(
        "index.html",
        food=food,
        results=results,
        searched=searched,
        error_message=error_message,
    )

if __name__ == "__main__":
    # Debug mode is for local development only. Use a production server when deploying.
    app.run(debug=True)
