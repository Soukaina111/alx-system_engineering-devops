#!/usr/bin/python3

"""
This script exports json infos .
"""

import json
import requests


def fetch_employee_and_todo_data():
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

    return todos, users


def prepare_data_for_export(todos, users):
    data_for_export = {}

    for user in users:
        user_id = user['id']
        user_todos = [todo for todo in todos if todo['userId'] == user_id]
        user_data = []

        for todo in user_todos:
            task_info = {
                'username': user['username'],
                'task': todo['title'],
                'completed': todo['completed']
            }
            user_data.append(task_info)

        data_for_export[user_id] = user_data

    return data_for_export


def export_to_json(data_for_export):
    json_obj = json.dumps(data_for_export)

    file_name = "todo_all_employees.json"

    with open(file_name, "w") as f:
        f.write(json_obj)

    print(f"Data exported to {file_name}")


def main():
    todos, users = fetch_employee_and_todo_data()
    if todos and users:
        data_for_export = prepare_data_for_export(todos, users)
        export_to_json(data_for_export)


if __name__ == "__main__":
    main()

