# NAME : VINAY PARMAR
# En. NO. : 0103AL231226
# BATCH : 5
# BRANCH : AIML

#quiz
# login
# attempt quiz
#    category(dsa, dbms python)
#         display atleast 5-10 questions randomly (shuffle)
#        at a time 1 q. with options
# score
    
# logout
# update show_profile
# show_profile



import json
import os
import sys
import random
import datetime

DATA_FILE = "students.json"

students = {}       # dictionary: username -> profile dict
logged_user = ""    # empty string means no one is logged in

def load_students():
    """Load students from DATA_FILE into the students dict.
       If file doesn't exist, start with empty dictionary."""
    global students
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            text = f.read()
            if text.strip() == "":
                students = {}
            else:
                students = json.loads(text)
    else:
        students = {}

def save_students():
    """Save the students dictionary to DATA_FILE as JSON text."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        text = json.dumps(students, indent=2)  # convert dict to nice JSON text
        f.write(text)

def wait():
    """Pause so user can read messages."""
    input("\nPress Enter to continue...")

def register():
    """Register a new student. Collect at least 10 fields."""
    global students
    print("\n--- REGISTER ---")
    # choose username
    while True:
        username = input("Enter username (no spaces): ").strip()
        if username == "":
            print("Username cannot be empty.")
            continue
        if " " in username:
            print("Please do not use spaces.")
            continue
        if username in students:
            print("This username already exists. Pick another.")
            continue
        break
    # password
    while True:
        password = input("Enter password: ")
        password2 = input("Confirm password: ")
        if password != password2:
            print("Passwords do not match.")
            continue
        if len(password) < 4:
            print("Password too short (min 4).")
            continue
        break

    print("\nEnter the student details (press Enter to leave a field blank):")
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    dob = input("Date of birth (YYYY-MM-DD): ").strip()
    gender = input("Gender(M/F/O): ").strip()
    email = input("Email: ").strip()
    phone = input("Phone: ").strip()
    address = input("Address: ").strip()
    course = input("Course (e.g. B.Tech CS): ").strip()
    year = input("Semester: ").strip()
    roll_no = input("Enrollment  ID: ").strip()
    guardian = input("Guardian name: ").strip()
    extra = input("Any extra info: ").strip()

    profile = {
        "username": username,
        "password": password, 
        "first_name": first_name,
        "last_name": last_name,
        "dob": dob,
        "gender(M/F/O)": gender,
        "email": email,
        "phone": phone,
        "address": address,
        "course": course,
        "year": year,
        "roll_no": roll_no,
        "guardian": guardian,
        "extra": extra
    }

    students[username] = profile
    save_students()
    print("\nRegistration complete. You can now login with your username.")
    wait()

def login():
    """Login by username and password."""
    global logged_user
    print("\n--- LOGIN ---")
    username = input("Username: ").strip()
    if username == "":
        print("Please enter a username.")
        wait()
        return
    if username not in students:
        print("No such user. Register first.")
        wait()
        return
    password = input("Password: ")
    if password == students[username]["password"]:
        logged_user = username
        print("Login successful. Welcome,", students[username].get("first_name", username))
    else:
        print("Wrong password.")
    wait()

def show_profile():
    """Display the profile of the logged-in user."""
    print("\n--- SHOW PROFILE ---")
    if logged_user == "":
        print("You must login first to view profile.")
        wait()
        return
    profile = students.get(logged_user)
    if profile is None:
        print("Profile not found.")
        wait()
        return

    # Print each field except the password
    print("Username :", profile.get("username", ""))
    print("First name:", profile.get("first_name", ""))
    print("Last name :", profile.get("last_name", ""))
    print("DOB       :", profile.get("dob", ""))
    print("Gender    :", profile.get("gender", ""))
    print("Email     :", profile.get("email", ""))
    print("Phone     :", profile.get("phone", ""))
    print("Address   :", profile.get("address", ""))
    print("Course    :", profile.get("course", ""))
    print("Year      :", profile.get("year", ""))
    print("Roll No   :", profile.get("roll_no", ""))
    print("Guardian  :", profile.get("guardian", ""))
    print("Extra     :", profile.get("extra", ""))

    wait()


def update_profile():
    """Update profile fields for the logged-in user (or change password)."""
    global students
    print("\n--- UPDATE PROFILE ---")
    if logged_user == "":
        print("You must login first to update profile.")
        wait()
        return
    profile = students.get(logged_user)
    if profile is None:
        print("Profile missing.")
        wait()
        return

    while True:
        print("\nUpdate options:")
        print("1 - Update fields (name, email, phone, address, etc.)")
        print("2 - Change password")
        print("3 - Back to main menu")
        choice = input("Choose 1/2/3: ").strip()
        if choice == "1":
            nf = input("First name (leave blank to keep): ").strip()
            if nf != "":
                profile["first_name"] = nf
            nl = input("Last name (leave blank to keep): ").strip()
            if nl != "":
                profile["last_name"] = nl
            ne = input("Email (leave blank to keep): ").strip()
            if ne != "":
                profile["email"] = ne
            np = input("Phone (leave blank to keep): ").strip()
            if np != "":
                profile["phone"] = np
            na = input("Address (leave blank to keep): ").strip()
            if na != "":
                profile["address"] = na
            nc = input("Course (leave blank to keep): ").strip()
            if nc != "":
                profile["course"] = nc
            ny = input("Year (leave blank to keep): ").strip()
            if ny != "":
                profile["year"] = ny
            ng = input("Guardian (leave blank to keep): ").strip()
            if ng != "":
                profile["guardian"] = ng
            ne2 = input("Extra info (leave blank to keep): ").strip()
            if ne2 != "":
                profile["extra"] = ne2

            students[logged_user] = profile
            save_students()
            print("Profile updated.")
            wait()
        elif choice == "2":
            old = input("Enter current password: ")
            if old != profile["password"]:
                print("Current password is wrong.")
                wait()
            else:
                new1 = input("Enter new password: ")
                new2 = input("Confirm new password: ")
                if new1 != new2:
                    print("Passwords do not match.")
                elif len(new1) < 4:
                    print("New password is too short.")
                else:
                    profile["password"] = new1
                    students[logged_user] = profile
                    save_students()
                    print("Password changed.")
                wait()
        elif choice == "3":
            break
        else:
            print("Please choose 1, 2, or 3.")



def load_questions(filename):
    """Reads questions from file and returns a list of dicts"""
    questions = []
    if not os.path.exists(filename):
        print(f"File {filename} not found!")
        return questions

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read().strip().split("\n\n")
        for block in content:
            lines = block.strip().split("\n")
            if len(lines) >= 6:
                q = {
                    "question": lines[0],
                    "A": lines[1],
                    "B": lines[2],
                    "C": lines[3],
                    "D": lines[4],
                    "ANSWER": lines[5].split(":")[1].strip().upper()
                }
                questions.append(q)
    return questions




def attempt_quiz(category):
   
        """Attempt quiz for given category"""
        filename = f"{category.lower()}.txt"
        questions = load_questions(filename)

        if not questions:
            print("No questions available for this category.")
            wait()
            return

        random.shuffle(questions)
        score = 0
        total = min(len(questions), 10)

        print(f"\nStarting {category.upper()} Quiz ({total} Questions)\n")

        for i, q in enumerate(questions[:total], start=1):
            print(f"Q{i}. {q['question']}")
            print(q['A'])
            print(q['B'])
            print(q['C'])
            print(q['D'])
            ans = input("Your answer (A/B/C/D): ").strip().upper()
            if ans == q['ANSWER']:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['ANSWER']}\n")

        percent = (score / total) * 100
        print(f"Quiz finished! Your Score: {score}/{total} ({percent:.2f}%)")

        # Save result to student's data
        # if logged_user != "":
        #     attempt = {
        #         "category": category.upper(),
        #         "marks": f"{score}/{total}",
        #         "datetime": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        #     }
        #     students[logged_user]["quiz_scores"].append(attempt)
        #     save_students()
        if logged_user != "":
            attempt = {
                "category": category.upper(),
                "marks": f"{score}/{total}",
                "datetime": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            }
            
            if "quiz_scores" not in students[logged_user]:
                students[logged_user]["quiz_scores"] = []

            students[logged_user]["quiz_scores"].append(attempt)
            save_students()


        wait()


def show_quiz_scores():
    """Show quiz history for logged user"""
    if logged_user == "":
        print("You must log in first.")
        wait()
        return
    user = students[logged_user]
    scores = user.get("quiz_scores", [])
    if not scores:
        print("No quiz attempts yet.")
    else:
        print("\n--- Quiz History ---")
        for s in scores:
            print(f"Category: {s['category']}\tMarks: {s['marks']}\tDate: {s['datetime']}")
    wait()


def quiz_menu():
    global students
    print("\n--- QUIZ MANU ---")
    if logged_user == "":
        print("You must login first to start quiz.")
        wait()
        return
    profile = students.get(logged_user)
    if profile is None:
        print("Profile missing.")
        wait()
        return
    
    """Quiz Menu visible after login"""
    while True:
        print("\n=== QUIZ MENU ===")
        print("1. Attempt Quiz")
        print("2. View Quiz Scores")
        print("3. Show Profile")
        print("4. Update Profile")
        print("5.  Return to Main Menu")
        print("6.  Logout")


        choice = input("Choose option (1-5): ").strip()

        if choice == "1":
            print("\nSelect Category:")
            print("1. DSA")
            print("2. DBMS")
            print("3. PYTHON")
            cat = input("Choose (1/2/3): ").strip()
            if cat == "1":
                attempt_quiz("DSA")
            elif cat == "2":
                attempt_quiz("DBMS")
            elif cat == "3":
                attempt_quiz("PYTHON")
            else:
                print("Invalid category.")
                wait()
        elif choice == "2":
            show_quiz_scores()
        elif choice == "3":
            show_profile()
        elif choice == "4":
            update_profile()
        elif choice == "5":
            main()
            
        elif choice == "6":
            logout()
            break
        else:
            print("Invalid option.")
            wait()







def logout():
    """Logout the current logged-in user."""
    global logged_user
    print("\n--- LOGOUT ---")
    if logged_user == "":
        print("No user is logged in.")
    else:
        print("User", logged_user, "has been logged out.")
        logged_user = ""
    wait()

def terminate():
    """Exit the program."""
    print("\nExiting. Goodbye!")
    sys.exit(0)

def main():
    load_students()   
    while True:
        print("\n=== LNCT Student System (Very Simple) ===")
        print("1. Registration")
        print("2. Login")
        print("3. Show Profile")
        print("4. Update Profile")
        print("5. Quiz manu")
        print("6. Logout")
        print("7. Main Menu (show again)")
        print("8. Exit")
        choice = input("Select option 1-8: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            show_profile()
        elif choice == "4":
            update_profile()
        elif choice == "5":
            quiz_menu()   
        elif choice == "6":
            logout()
        elif choice == "7":
            continue  # loop will reprint menu
        elif choice == "8":
            terminate()
        else:
            print("Invalid choice, please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
