#!/usr/bin/python3

"""
This  script exports data in  CSV format(comma separated values)
"""
import csv
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

def export_to_csv(employee_id, todos, employee):
    file_name = f"{employee_id}.csv"

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            if todo['userId'] == employee_id:
                writer.writerow([todo['userId'], employee, todo['completed'], todo['title']])

    print(f"Tasks exported to {file_name}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    todos, employee = fetch_employee_data(employee_id)
    if todos and employee:
        export_to_csv(employee_id, todos, employee)

if __name__ == "__main__":
    main()

