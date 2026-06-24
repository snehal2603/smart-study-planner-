import sqlite3

def add_task():

    conn = sqlite3.connect("study_planner.db")

    cursor = conn.cursor()

    task = input("Enter Task: ")

    cursor.execute(
        "INSERT INTO tasks(task_name,status) VALUES(?,?)",
        (task,"Pending")
    )

    conn.commit()

    conn.close()


    print("Task Added Successfully")
def view_tasks():

    conn = sqlite3.connect("study_planner.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()
def complete_task():

    conn = sqlite3.connect("study_planner.db")
    cursor = conn.cursor()

    task_id = int(input("Enter Task ID to Complete: "))

    cursor.execute(
        "UPDATE tasks SET status=? WHERE id=?",
        ("Completed", task_id)
    )

    conn.commit()

    conn.close()

    print("Task Completed Successfully")  
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
while True:

    print("\n===== STUDY PLANNER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task ")
    print("4. delete task ")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_task()
        print("Add Task Selected")

    elif choice == 2:
        view_tasks()
        print("View Tasks Selected")

    elif choice == 3:
        complete_task()
        print("complete task selected ")
    elif choice==4:
        delete_task()
        print("delete task ");
    elif choice==5:
        print("thank you ");
        break
    else:
        print("Invalid Choice")