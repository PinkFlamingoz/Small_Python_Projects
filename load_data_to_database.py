# Import
import sqlite3
import os
from basic_functions import get_valid_input


# Create tables
def create_tables(c):
    try:
        c.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT NOT NULL)
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS houses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                house_name TEXT NOT NULL,
                head_name TEXT NOT NULL)
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS assignments (
                student_id INTEGER NOT NULL,
                house_id INTEGER NOT NULL,
                FOREIGN KEY(student_id) REFERENCES students(id),
                FOREIGN KEY(house_id) REFERENCES houses(id))
        ''')
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Print menu
def print_menu():
    options = [
        "Add House",
        "Add Student",
        "Delete Student",
        "Delete House",
        "Display House Head",
        "Display All Houses",
        "Display All Students",
        "Display Students in House",
        "Clear Screen",
    ]

    print("\nWhat operation do you want to perform? Select Option number. Enter 0 to quit.\n")
    for i, option in enumerate(options, start=1):
        print(f"\t{i}. {option}")


# Add house to database
def add_house(c, house_name, head_name):
    try:
        c.execute("INSERT INTO houses (house_name, head_name) VALUES (?, ?)", (house_name, head_name))
        print(f"House {house_name} has been successfully added.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Add student to database
def add_student(c, student_name, house_name):
    try:
        c.execute("SELECT id FROM houses WHERE house_name=?", (house_name,))
        result = c.fetchone()
        if result is None:
            print("House not found. Please add the house first.")
        else:
            house_id = result[0]
            c.execute("INSERT INTO students (student_name) VALUES (?)", (student_name,))
            student_id = c.lastrowid 
            c.execute("INSERT INTO assignments (student_id, house_id) VALUES (?, ?)", (student_id, house_id))
            print(f"Student {student_name} has been successfully added.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Delete house from database
def delete_house(c, house_name):
    try:
        c.execute("SELECT id FROM houses WHERE house_name=?", (house_name,))
        result = c.fetchone()
        if result is None:
            print("House not found.")
        else:
            c.execute("DELETE FROM assignments WHERE house_id=(SELECT id FROM houses WHERE house_name=?)", (house_name,))
            c.execute("DELETE FROM houses WHERE house_name=?", (house_name,))
            print(f"House {house_name} has been successfully deleted.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Delete student from database
def delete_student(c, student_name):
    try:
        c.execute("SELECT id FROM students WHERE student_name=?", (student_name,))
        result = c.fetchone()
        if result is None:
            print("Student not found.")
        else:
            c.execute("DELETE FROM assignments WHERE student_id=(SELECT id FROM students WHERE student_name=?)", (student_name,))
            c.execute("DELETE FROM students WHERE student_name=?", (student_name,))
            print(f"Student {student_name} has been successfully deleted.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Display head of house from database
def display_house_head(c, house_name):
    try:
        c.execute("SELECT * FROM houses WHERE house_name=?", (house_name,))
        result = c.fetchone()
        if result is None:
            print(f"The house '{house_name}' does not exist.")
            return

        c.execute("SELECT head_name FROM houses WHERE house_name=?", (house_name,))
        result = c.fetchone()
        print(f"Head: {result[0]}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Display students in house from database 
def display_students_in_house(c, house_name):
    try:
        c.execute("SELECT * FROM houses WHERE house_name=?", (house_name,))
        result = c.fetchone()
        if result is None:
            print(f"The house '{house_name}' does not exist.")
            return

        c.execute("""
        SELECT students.id, students.student_name
        FROM students
        JOIN assignments ON students.id = assignments.student_id
        JOIN houses ON houses.id = assignments.house_id
        WHERE houses.house_name=?
        """, (house_name,))
        result = c.fetchall()
        if not result:
            print(f"No students are assigned to house '{house_name}'.")
            return

        print(f"{'ID':<5} {'Student':<20}")
        print("-"*30)
        for row in result:
            print(f"{row[0]:<5} {row[1]:<20}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Display all houses from database
def display_all_houses(c):
    try:
        c.execute("SELECT * FROM houses")
        result = c.fetchall()
        print(f"{'House':<20} {'Head':<20}")
        print("-"*40)
        for row in result:
            print(f"{row[1]:<20} {row[2]:<20}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Display all students from database
def display_all_students(c):
    try:
        c.execute("SELECT students.id, students.student_name, houses.house_name FROM students JOIN assignments ON students.id = assignments.student_id JOIN houses ON houses.id = assignments.house_id")
        result = c.fetchall()
        print(f"{'ID':<5} {'Student':<33} {'House':<20}")
        print("-"*50)
        for row in result:
            print(f"{row[0]:<5} {row[1]:<33} {row[2]:<20}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Main
def main():
    try:
        conn = sqlite3.connect('DATA/student_data.db')
        c = conn.cursor()

        create_tables(c)

        while True:
            print_menu()
            case = get_valid_input(str,"\n\tEnter choice: ")
            if case == "1":
                house_name = get_valid_input(str,"Enter house name: ")
                head_name = get_valid_input(str,"Enter head name: ")
                add_house(c, house_name, head_name)
            elif case == "2":
                student_name = get_valid_input(str,"Enter student name: ")
                house_name = get_valid_input(str,"Enter house name: ")
                add_student(c, student_name, house_name)
            elif case == "3":
                student_name = get_valid_input(str,"Enter student name: ")
                delete_student(c, student_name)
            elif case == "4":
                house_name = get_valid_input(str,"Enter house name: ")
                delete_house(c, house_name)
            elif case == "5":
                house_name = get_valid_input(str,"\n\tEnter house name: ")
                display_house_head(c, house_name)
            elif case == "6":
                display_all_houses(c)
            elif case == "7":
                display_all_students(c)
            elif case == "8":
                house_name = get_valid_input(str,"\n\tEnter house name: ")
                display_students_in_house(c, house_name)
            elif case == "9":
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
