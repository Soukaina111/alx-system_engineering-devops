#!/usr/bin/python3

"""
This  script exports data in  CSV format(comma separated values)
"""
import csv
import requests
import sys


def fetch_user_and_todos(userId):
    """Fetch user and todos data from the JSONPlaceholder API."""
    user_url = f"https://jsonplaceholder.typicode.com/users/{userId}"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error fetching data from API.")
        return None, None

    return user_response.json(), todos_response.json()


def export_to_csv(userId, user_name, todos):
    """Export user's todos to a CSV file."""
    filename = f"{userId}.csv"

    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos:
            if task.get('userId') == int(userId):
                writer.writerow([userId, user_name, str(task.get('completed')), task.get('title')])


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <userId>")
        sys.exit(1)

    userId = sys.argv[1]
    user_data, todos_data = fetch_user_and_todos(userId)

    if user_data and todos_data:
        user_name = user_data.get('username')
        export_to_csv(userId, user_name, todos_data)
        print(f"Data exported to {userId}.csv")
    else:
        print("Failed to fetch data from API.")


if __name__ == "__main__":
    main()

