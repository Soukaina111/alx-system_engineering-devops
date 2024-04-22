#!/usr/bin/python3

"""
Python script that exports data in the CSV format
"""

import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    todos_url = "https://jsonplaceholder.typicode.com/todos/"
    users_url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(todos_url)
    if response.status_code != 200:
        print("Error fetching todos:", response.status_code)
        return
    todos = response.json()

    response = requests.get(users_url)
    if response.status_code != 200:
        print("Error fetching users:", response.status_code)
        return
    users = response.json()

    employee = None
    for user in users:
        if user.get('id') == employee_id:
            employee = user.get('name')
            break

    if not employee:
        print("Employee not found.")
        return

    completed = 0
    total = 0
    tasks = []
    for todo in todos:
        if todo.get('userId') == employee_id:
            total += 1
            if todo.get('completed'):
                completed += 1
                tasks.append((employee_id, employee, True, todo.get('title')))
            else:
                tasks.append((employee_id, employee, False, todo.get('title')))

    print(f"Employee {employee} is done with tasks({completed}/{total}):")
    for task in tasks:
        print(f"\t {task[3]}")

    export_to_csv(employee_id, tasks)


def export_to_csv(employee_id, tasks):
    file_name = f"{employee_id}.csv"

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID",
                        "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            writer.writerow(task)

    print(f"Tasks exported to {file_name}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)


if __name__ == "__main__":
    main()
