#!/usr/bin/python3

"""
This script exports data and convert it to json
"""

import json
import requests
import sys


def fetch_employee_data(employee_id):
    todos_url = "https://jsonplaceholder.typicode.com/todos/"
    users_url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(todos_url)
    if response.status_code != 200:
        print("Error fetching todos:", response.status_code)
        return None, None
    todos = response.json()

    response = requests.get(users_url)
    if response.status_code != 200:
        print("Error fetching users:", response.status_code)
        return None, None
    users = response.json()

    employee = None
    for user in users:
        if user['id'] == employee_id:
            employee = user['username']
            break

    if not employee:
        print("Employee not found.")
        return None, None

    return todos, employee

def export_to_json(employee_id, todos, employee):
    final_dict = {}
    final_dict[employee_id] = []

    for todo in todos:
        if todo['userId'] == employee_id:
            task_info = {
                'username': employee,
                'task': todo['title'],
                'completed': todo['completed']
            }
            final_dict[employee_id].append(task_info)

    json_obj = json.dumps(final_dict)

    file_name = f"{employee_id}.json"

    with open(file_name, "w") as f:
        f.write(json_obj)

    print(f"Data exported to {file_name}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    todos, employee = fetch_employee_data(employee_id)
    if todos and employee:
        export_to_json(employee_id, todos, employee)

if __name__ == "__main__":
    main()

