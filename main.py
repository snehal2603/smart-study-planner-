import sqlite3

def dashboard():

    conn = sqlite3.connect("study_planner.db")
    cursor = conn.cursor()

    # Total tasks
    cursor.execute("SELECT COUNT(*) FROM tasks")
    total = cursor.fetchone()[0]

    # Pending tasks
    cursor.execute("SELECT COUNT(*) FROM tasks WHERE status='Pending'")
    pending = cursor.fetchone()[0]

    # Completed tasks
    cursor.execute("SELECT COUNT(*) FROM tasks WHERE status='Completed'")
    completed = cursor.fetchone()[0]

    # Placement Readiness Score
    if total > 0:
        score = (completed / total) * 100
    else:
        score = 0

    print("\n===== SMART DASHBOARD =====")
    print("Total Tasks:", total)
    print("Pending Tasks:", pending)
    print("Completed Tasks:", completed)
    print("Placement Readiness Score:", round(score, 2), "%")

    conn.close()
# ---------------- ADD TASK ----------------
def add_task():

    conn = sqlite3.connect("study_planner.db")
    cursor = conn.cursor()

    task = input("Enter Task: ")

    cursor.execute(
        "INSERT INTO tasks(task_name, status) VALUES(?, ?)",
        (task, "Pending")
    )

    conn.commit()
    conn.close()

    print("Task Added Successfully")


# ---------------- VIEW TASKS ----------------
def view_tasks():

    conn = sqlite3.connect("study_planner.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


# ---------------- COMPLETE TASK ----------------
def complete_task():

    conn = sqlite3.connect("study_planner.db")
    cursor = conn.cursor()

    task_id = int(input("Enter Task ID to Mark Completed: "))

    cursor.execute(
        "UPDATE tasks SET status=? WHERE id=?",
        ("Completed", task_id)
    )

    conn.commit()
    conn.close()

    print("Task Completed Successfully")


# ---------------- DELETE TASK ----------------
def delete_task():

    conn = sqlite3.connect("study_planner.db")
    cursor = conn.cursor()

    task_id = int(input("Enter Task ID to Delete: "))

    cursor.execute(
        "DELETE FROM tasks WHERE id=?",
        (task_id,)
    )

    conn.commit()
    conn.close()

    print("Task Deleted Successfully")


# ---------------- MENU ----------------
while True:

    print("\n===== STUDY PLANNER =====")
    print("0. dashboard ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 0:
        dashboard()

    elif choice == 1:
        add_task()

    elif choice == 2:
        view_tasks()

    elif choice == 3:
        complete_task()

    elif choice == 4:
        delete_task()

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid Choice")
