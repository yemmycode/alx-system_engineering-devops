#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import json
import requests


def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_user_todos(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def create_tasks_dict(users):
    tasks_dict = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        tasks = fetch_user_todos(user_id)
        tasks_dict[user_id] = [
            {"task": task.get('title'), "completed": task.get('completed'), "username": username}
            for task in tasks
        ]
    return tasks_dict


def save_to_json_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    users = fetch_users()
    tasks_dict = create_tasks_dict(users)
    save_to_json_file('todo_all_employees.json', tasks_dict)
