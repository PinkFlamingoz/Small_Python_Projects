# Import
import sqlite3
import os
from collections import defaultdict
from basic_functions import get_valid_input


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

        movies = defaultdict(lambda: {"title": None, "year": None, "directors": None, "ratings": None, "votes": None, "stars": []})
        for row in result:
            id = row[0]
            movies[id]["title"] = row[1] if row[1] is not None else 'N/A'
            movies[id]["year"] = row[2] if row[2] is not None else 'N/A'
            movies[id]["directors"] = row[4] if row[4] is not None else 'N/A'
            movies[id]["ratings"] = row[5] if row[5] is not None else 'N/A'
            movies[id]["votes"] = row[6] if row[6] is not None else 'N/A'
            if row[3]:
                movies[id]["stars"].append(row[3])

        print(f"{'ID':<10} {'Title':<70} {'Year':<10} {'Stars':<70} {'Directors':<50} {'Ratings':<10} {'Votes':<10}")
        print("-"*200)

        for id, movie in movies.items():
            stars = ', '.join(movie["stars"])
            # Slice the strings so they don't exceed the maximum length
            title = (movie['title'][:67] + '..') if len(movie['title']) > 70 else movie['title']
            stars = (stars[:67] + '..') if len(stars) > 70 else stars
            print(f"{id:<10} {title:<70} {movie['year']:<10} {stars:<70} {movie['directors']:<50} {movie['ratings']:<10} {movie['votes']:<10}")

        movie_id = get_valid_input(int,"\nEnter the ID of the movie you want to see details for: ")
        if movie_id in movies:
            movie = movies[movie_id]
            stars = ', '.join(movie["stars"])
            print(f"\nID: {movie_id}")
            print(f"Title: {movie['title']}")
            print(f"Year: {movie['year']}")
            print(f"Stars: {stars}")
            print(f"Directors: {movie['directors']}")
            print(f"Ratings: {movie['ratings']}")
            print(f"Votes: {movie['votes']}")
        else:
            print("Invalid movie ID entered.")
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

        print(f"{'Title':<70} {'Rating':<10} {'Votes':<10}")
        print("-"*100)
        for row in result:
            title = (row[0][:67] + '...') if row[0] and len(row[0]) > 70 else (row[0] if row[0] else 'N/A')
            rating = row[1] if row[1] else 'N/A'
            votes = row[2] if row[2] else 'N/A'
            print(f"{title:<70} {rating:<10} {votes:<10}")
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

        print(f"{'ID':<10} {'Title':<70} {'Year':<10}")
        print("-"*100)
        for row in result:
            id = row[0] if row[0] else 'N/A'
            title = (row[1][:67] + '...') if row[1] and len(row[1]) > 70 else (row[1] if row[1] else 'N/A')
            year = row[2] if row[2] else 'N/A'
            print(f"{id:<10} {title:<70} {year:<10}")
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

        print(f"{'ID':<10} {'Name':<50} {'Birth Year':<10}")
        print("-"*100)
        for row in result:
            id = row[0] if row[0] else 'N/A'
            name = row[1] if row[1] else 'N/A'
            birth_year = row[2] if row[2] else 'N/A'
            print(f"{id:<10} {name:<50} {birth_year:<10}")
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

        movies = defaultdict(list)
        for row in result:
            title = (row[0][:67] + '...') if row[0] and len(row[0]) > 70 else (row[0] if row[0] else 'N/A')
            director = row[1] if row[1] else 'N/A'
            movies[title].append(director)

        print(f"{'Title':<70} {'Director(s)':<50}")
        print("-"*100)
        for title, directors in movies.items():
            directors_str = ', '.join(directors)
            print(f"{title:<70} {directors_str:<50}")
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

        print(f"{'Title':<70} {'Rating':<10}")
        print("-"*100)
        for row in result:
            title = (row[0][:67] + '...') if row[0] and len(row[0]) > 70 else (row[0] if row[0] else 'N/A')
            rating = row[1] if row[1] else 'N/A'
            print(f"{title:<70} {rating:<10}")
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

        print(f"{'Title':<70} {'Rating':<10}")
        print("-"*100)
        for row in result:
            title = (row[0][:67] + '...') if row[0] and len(row[0]) > 70 else (row[0] if row[0] else 'N/A')
            rating = row[1] if row[1] else 'N/A'
            print(f"{title:<70} {rating:<10}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Display all movies of a given actor
def display_movies_of_actor(c, actor_name):
    try:
        c.execute("""
            SELECT movies.title, people.name
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
        print("-"*100)
        for row in result:
            title = (row[0][:67] + '...') if row[0] and len(row[0]) > 70 else (row[0] if row[0] else 'N/A')
            actor = row[1] if row[1] else 'N/A'
            print(f"Actor: {actor:<50} Movie: {title:<70}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Display all movies of a given director
def display_movies_of_director(c, director_name):
    try:
        c.execute("""
            SELECT movies.title, people.name
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
        print("-"*100)
        for row in result:
            title = (row[0][:67] + '...') if row[0] and len(row[0]) > 70 else (row[0] if row[0] else 'N/A')
            director = row[1] if row[1] else 'N/A'
            print(f"Director: {director:<50} Movie: {title:<70}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Main
def main():
    try:
        database = "DATA/movies.db"
        db_exists = os.path.isfile(database)
        conn = None

        # Exit if database not found
        if not db_exists:
             print(f"File {db_exists} does not exist.")
             return
        # Connect to database if it exists
        else:
            conn = sqlite3.connect(database)
            c = conn.cursor()

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
                display_movies_of_actor(c, actor_name)
            elif case == "9":
                director_name = get_valid_input(str, "Enter the director's name: ")
                display_movies_of_director(c, director_name)
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
