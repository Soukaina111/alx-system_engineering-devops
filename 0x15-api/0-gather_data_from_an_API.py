#!/usr/bin/python3

"""
This is a python script that lists data of employees
using a REST API.
"""

import requests

def get_employee_todo_progress(employee_id):
    
    url = f"YOUR_API_ENDPOINT/employees/{employee_id}/todo"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        employee_name = data['employee_name']
        done_tasks = data['done_tasks']
        total_tasks = data['total_tasks']

        print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t {task['title']}")
    else:
        print(f"Error fetching data: {response.status_code}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

