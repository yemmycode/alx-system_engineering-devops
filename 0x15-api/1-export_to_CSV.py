#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


def fetch_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(f"{base_url}/{employee_id}")
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()


def fetch_todo_list(employee_id):
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todo_url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()


def write_tasks_to_csv(employee_id, username, tasks):
    filename = f"{employee_id}.csv"
    with open(filename, 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employee_id, username, task.get('completed'), task.get('title')))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: {} <employeeId>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    employee_data = fetch_employee_data(employee_id)
    username = employee_data.get('username')

    tasks = fetch_todo_list(employee_id)

    write_tasks_to_csv(employee_id, username, tasks)
