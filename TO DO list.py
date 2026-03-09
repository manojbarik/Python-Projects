# To-Do List Manager with Categories
# Add tasks, set deadlines, assign priority, and filter by project or tag.

tasks = []
def add_task():
    name = input("Enter task: ")
    category = input("Enter category: ")
    priority = input("Enter priority (High/Medium/Low): ")
    
    task = {"name": name, "category": category, "priority": priority}
    tasks.append(task)
    print("Task added")

def show_tasks():
    for t in tasks:
        print(t)

def filter_category():
    cat = input("Enter category: ")
    for t in tasks:
        if t["category"] == cat:
            print(t)

while True:
    print("\n1.Add Task 2.Show Tasks 3.Filter Category 4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        add_task()
    elif ch == 2:
        show_tasks()
    elif ch == 3:
        filter_category()
    else:
        break