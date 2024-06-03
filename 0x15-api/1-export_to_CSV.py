#!/usr/bin/python3
"""
Accessing a RestAPI for todo list employees and export in CSV format
"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.arg[1]
    baseUrl = "https://jsonplacholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = request.get(url)
    username = response.json(todoUrl)
    tasks = response.json()

    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                    .format(employeeId, username, task.get('completed'),
                        task.get('title')))
