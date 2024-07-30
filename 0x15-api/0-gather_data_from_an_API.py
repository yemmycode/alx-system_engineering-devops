#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: {} <employeeId>".format(sys.argv[0]))
        sys.exit(1)

    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = "{}/{}".format(baseUrl, employeeId)

    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching employee data:", response.text)
        sys.exit(1)

    employeeName = response.json().get('name')

    todoUrl = "{}/todos".format(url)
    response = requests.get(todoUrl)
    if response.status_code != 200:
        print("Error fetching employee's tasks:", response.text)
        sys.exit(1)

    tasks = response.json()
    done_tasks = [task for task in tasks if task.get('completed')]
    done = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(tasks)))

    for task in done_tasks:
        print("\t{}".format(task.get('title')))


if __name__ == '__main__':
    main()

