# Import
import sqlite3
import os
import csv
from basic_functions import get_valid_input


# Create tables
def create_tables(c):
    try:
        c.execute('''
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGE RPRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                year NUMERIC,
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS stars (
                movie_id INTEGER NOT NULL,
                person_id INTEGER NOT NULL,
                FOREIGN KEY(movie_id) REFERENCES movies(id),
                FOREIGN KEY(person_id) REFERENCES people(id))
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS directors (
                movie_id INTEGER NOT NULL,
                person_id INTEGER NOT NULL,
                FOREIGN KEY(movie_id) REFERENCES movies(id),
                FOREIGN KEY(person_id) REFERENCES people(id))
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS ratings (
                movie_id INTEGER NOT NULL,
                rating REAL NOT NULL,
                votes INTEGER NOT NULL,
                FOREIGN KEY(movie_id) REFERENCES movies(id))
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS people (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                birth NUMERIC,
        ''')
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Load data from csv
def load_from_csv(c):
    with open('movies.csv', 'r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            c.execute("INSERT INTO movies (id, title, year) VALUES (?, ?, ?)", (row['id'], row['title'], row['year']))
            c.execute("INSERT INTO ratings (movie_id, rating, votes) VALUES (?, ?, ?)", (row['id'], row['rating'], row['votes']))
            c.execute("INSERT INTO stars (movie_id, person_id) VALUES (?, ?)", (row['id'], row['stars']))
            c.execute("INSERT INTO directors (movie_id, person_id) VALUES (?, ?)", (row['id'], row['directors']))
            c.execute("INSERT INTO people (id, name, birth) VALUES (?, ?, ?)", (row['id'], row['name'], row['birth']))


# Print menu
def print_menu():
    options = [
        "Display Movie Details",
        "Display Movie Ratings",
        "Display Movies",
        "Display Movie Actors",
        "Display Movie Directors",
        "Display Top Rated Movies of All Time",
        "Display Top Rated Movies of a Given Year",
        "Display All Movies of a Given Actor",
        "Display All Movies of a Given Director",
        "Clear Screen",
    ]

    print("\nWhat operation do you want to perform? Select Option number. Enter 0 to quit.\n")
    for i, option in enumerate(options, start=1):
        print(f"\t{i}. {option}")


# Display movie details along with its stars, directors, ratings and votes from database
def display_movie_details(c, movie_title):
    try:
        c.execute("""
            SELECT movies.id, movies.title, movies.year, people.name, people2.name, ratings.rating, ratings.votes
            FROM movies
            LEFT JOIN stars ON movies.id = stars.movie_id
            LEFT JOIN people ON people.id = stars.person_id
            LEFT JOIN directors ON movies.id = directors.movie_id
            LEFT JOIN people as people2 ON people2.id = directors.person_id
            LEFT JOIN ratings ON movies.id = ratings.movie_id
            WHERE LOWER(movies.title) LIKE LOWER(?)
        """, (f"%{movie_title.lower()}%",))
        result = c.fetchall()
        if not result:
            print(f"No details found for movie '{movie_title}'.")
            return

        print(f"{'ID':<5} {'Title':<50} {'Year':<10} {'Stars':<20} {'Directors':<20} {'Ratings':<10} {'Votes':<10}")
        print("-"*125)
        for row in result:
            print(f"{row[0]:<5} {row[1]:<50} {row[2]:<10} {row[3]:<20} {row[4]:<20} {row[5]:<10} {row[6]:<10}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Display movie ratings from database with optional limit
def display_movie_ratings(c, limit=None):
    query = """
        SELECT movies.title, ratings.rating, ratings.votes
        FROM movies
        JOIN ratings ON movies.id = ratings.movie_id
    """
    if limit is not None:
        query += f" LIMIT {limit}"

    try:
        c.execute(query)
        result = c.fetchall()
        if not result:
            print(f"No ratings found.")
            return

        print(f"{'Title':<30} {'Rating':<10} {'Votes':<10}")
        print("-"*60)
        for row in result:
            print(f"{row[0]:<30} {row[1]:<10} {row[2]:<10}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Display movie directors from database with optional limit
def display_movie_directors(c, limit=None):
    query = """
        SELECT movies.title, people.name
        FROM movies
        JOIN directors ON movies.id = directors.movie_id
        JOIN people ON people.id = directors.person_id
    """
    if limit is not None:
        query += f" LIMIT {limit}"

    try:
        c.execute(query)
        result = c.fetchall()
        if not result:
            print(f"No directors found.")
            return

        print(f"{'Title':<30} {'Director':<20}")
        print("-"*60)
        for row in result:
            print(f"{row[0]:<30} {row[1]:<20}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Display all movies from database with optional limit
def display_all_movies(c, limit=None):
    query = "SELECT id, title, year FROM movies"
    if limit is not None:
        query += f" LIMIT {limit}"

    try:
        c.execute(query)
        result = c.fetchall()
        if not result:
            print(f"No movies found.")
            return

        print(f"{'ID':<5} {'Title':<50} {'Year':<10}")
        print("-"*65)
        for row in result:
            print(f"{row[0]:<5} {row[1]:<50} {row[2]:<10}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Display all actors from database with optional limit
def display_all_actors(c, limit=None):
    query = "SELECT id, name, birth FROM people"
    if limit is not None:
        query += f" LIMIT {limit}"

    try:
        c.execute(query)
        result = c.fetchall()
        if not result:
            print(f"No actors found.")
            return

        print(f"{'ID':<5} {'Name':<30} {'Birth Year':<10}")
        print("-"*45)
        for row in result:
            print(f"{row[0]:<5} {row[1]:<30} {row[2]:<10}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Display top rated movies of all time
def display_top_rated_movies(c, limit=10):
    try:
        c.execute("""
            SELECT movies.title, ratings.rating
            FROM movies
            JOIN ratings ON movies.id = ratings.movie_id
            ORDER BY ratings.rating DESC
            LIMIT ?
            """, (limit,))
        result = c.fetchall()
        if not result:
            print(f"No movie ratings found.")
            return

        print(f"{'Title':<50} {'Rating':<10}")
        print("-"*60)
        for row in result:
            print(f"{row[0]:<50} {row[1]:<10}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Display top rated movies of a given year
def display_top_rated_movies_of_year(c, year, limit=10):
    try:
        c.execute("""
            SELECT movies.title, ratings.rating
            FROM movies
            JOIN ratings ON movies.id = ratings.movie_id
            WHERE movies.year=?
            ORDER BY ratings.rating DESC
            LIMIT ?
            """, (year, limit))
        result = c.fetchall()
        if not result:
            print(f"No movie ratings found for year {year}.")
            return

        print(f"{'Title':<50} {'Rating':<10}")
        print("-"*60)
        for row in result:
            print(f"{row[0]:<50} {row[1]:<10}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Display all movies of a given actor
def display_movies_of_actor(c, actor_name):
    try:
        c.execute("""
            SELECT movies.title
            FROM movies
            JOIN stars ON movies.id = stars.movie_id
            JOIN people ON people.id = stars.person_id
            WHERE LOWER(people.name) LIKE LOWER(?)
            """, (f"%{actor_name.lower()}%",))
        result = c.fetchall()
        if not result:
            print(f"No movies found for the actor '{actor_name}'.")
            return

        print(f"Movies of '{actor_name}':")
        print("-"*60)
        for row in result:
            print(row[0])
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Display all movies of a given director
def display_movies_of_director(c, director_name):
    try:
        c.execute("""
            SELECT movies.title
            FROM movies
            JOIN directors ON movies.id = directors.movie_id
            JOIN people ON people.id = directors.person_id
            WHERE LOWER(people.name) LIKE LOWER(?)
            """, (f"%{director_name.lower()}%",))
        result = c.fetchall()
        if not result:
            print(f"No movies found for the director '{director_name}'.")
            return

        print(f"Movies of '{director_name}':")
        print("-"*60)
        for row in result:
            print(row[0])
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Main
def main():
    try:
        db_exists = os.path.isfile('DATA/movie_data.db')
        conn = sqlite3.connect('DATA/movie_data.db')
        c = conn.cursor()

        if not db_exists:
            create_tables(c)
            load_from_csv(c)

        while True:
            print_menu()
            case = get_valid_input(str,"\n\tEnter choice: ")
            if case == "1":
                movie_title = get_valid_input(str,"Enter movie title: ")
                display_movie_details(c, movie_title)
            elif case == "2":
                limit = get_valid_input(int, "Enter limit (or press enter for all results): ", optional=True)
                display_movie_ratings(c, limit)
            elif case == "3":
                limit = get_valid_input(int, "Enter limit (or press enter for all results): ", optional=True)
                display_all_movies(c, limit)
            elif case == "4":
                limit = get_valid_input(int, "Enter limit (or press enter for all results): ", optional=True)
                display_all_actors(c, limit)
            elif case == "5":
                limit = get_valid_input(int, "Enter limit (or press enter for all results): ", optional=True)
                display_movie_directors(c, limit)
            elif case == "6":
                limit = get_valid_input(int, "Enter limit (or press enter for TOP 10): ", optional=True)
                display_top_rated_movies(c, limit)
            elif case == "7":
                year = get_valid_input(int, "Enter the year: ")
                limit = get_valid_input(int, "Enter limit (or press enter TOP 10): ", optional=True)
                display_top_rated_movies_of_year(c, year, limit)
            elif case == "8":
                actor_name = get_valid_input(str, "Enter the actor's name: ")
                limit = get_valid_input(int, "Enter limit (or press enter for all results): ", optional=True)
                display_movies_of_actor(c, actor_name, limit)
            elif case == "9":
                director_name = get_valid_input(str, "Enter the director's name: ")
                limit = get_valid_input(int, "Enter limit (or press enter for all results): ", optional=True)
                display_movies_of_director(c, director_name, limit)
            elif case == "10":
                os.system("cls" if os.name == "nt" else "clear")
            elif case == "0":
                break
            else:
                print("\n\tInvalid choice.")
            input("\n\t\tPress Enter to continue...")
            conn.commit()

        conn.close()

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return


# Start
if __name__ == "__main__":
    main()
