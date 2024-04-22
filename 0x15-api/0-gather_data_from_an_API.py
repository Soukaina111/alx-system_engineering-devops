#!/usr/bin/python3

"""
This is a python script that lists data of employees
using a REST API.
"""
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
                tasks.append(todo.get('title'))

    print(f"Employee {employee} is done with tasks({completed}/{total}):")
    for task in tasks:
        print(f"\t {task}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)


if __name__ == "__main__":
    main()
