#!/usr/bin/python3

"""
This script exports json infos .
"""


from requests import get
import json

if __name__ == "__main__":
    todos_response = get('https://jsonplaceholder.typicode.com/todos/')
    todos_data = todos_response.json()

    user_response = get('https://jsonplaceholder.typicode.com/users')
    users_data = user_response.json()

    employee_tasks = {}

    for user in users_data:
        user_tasks = []
        for todo in todos_data:
            task_info = {}

            if user['id'] == todo['userId']:
                task_info['employee_name'] = user['username']
                task_info['task_title'] = todo['title']
                task_info['task_completed'] = todo['completed']
                user_tasks.append(task_info)

        employee_tasks[user['id']] = user_tasks

    with open("todo_all_employees.json", "w") as file:
        json_data = json.dumps(employee_tasks)
        file.write(json_data)

