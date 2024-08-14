#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import json
import requests
import sys


def fetch_employee_data(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_todo_list(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def create_task_dictionary(employee_id, tasks, username):
    return {
        employee_id: [
            {"task": task.get('title'), "completed": task.get('completed'), "username": username}
            for task in tasks
        ]
    }


def save_to_json_file(employee_id, data):
    filename = f"{employee_id}.json"
    with open(filename, 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: {} <employeeId>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    employee_data = fetch_employee_data(employee_id)
    username = employee_data.get('username')

    tasks = fetch_todo_list(employee_id)

    task_dictionary = create_task_dictionary(employee_id, tasks, username)
    save_to_json_file(employee_id, task_dictionary)
