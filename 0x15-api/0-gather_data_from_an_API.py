#!/usr/bin/python3
"""
Accessing a RestAPI for todo lists of employees
"""

import requests
import sys

if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl = "/" + employeeId

    response = request.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todo"
    response = request.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        done_task.append(task)
        done += 1

    print("Employee {} is done with tasks({}/{}):"
            .format(employeeName, done, len(task)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
