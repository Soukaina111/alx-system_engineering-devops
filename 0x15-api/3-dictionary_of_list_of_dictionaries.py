#!/usr/bin/python3

"""
This script exports json infos .
"""

import json
import requests


def fetch_todos_and_users():
    """Fetch todos and users data from the JSONPlaceholder API."""
    todos_url = "https://jsonplaceholder.typicode.com/todos/"
    users_url = "https://jsonplaceholder.typicode.com/users"

    todos_response = requests.get(todos_url)
    users_response = requests.get(users_url)

    if todos_response.status_code != 200 or users_response.status_code != 200:
        print("Error fetching data from API.")
        return None, None

    return todos_response.json(), users_response.json()


def prepare_data_for_export(todos, users):
    """ Prepare the data for export to JSON format."""
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
    """ Export the prepared data to a JSON file."""
    file_name = "todo_all_employees.json"

    try:
        with open(file_name, "w") as f:
            json.dump(data_for_export, f, indent=4)
        print(f"Data exported to {file_name}")
    except Exception as e:
        print(f"Error writing to file: {e}")

def main():
    todos, users = fetch_todos_and_users()
    if todos and users:
        data_for_export = prepare_data_for_export(todos, users)
        export_to_json(data_for_export)
    else:
        print("Failed to fetch data from API.")


if __name__ == "__main__":
    main()

