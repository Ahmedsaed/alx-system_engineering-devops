#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]

    user = requests.get(f"https://jsonplaceholder.typicode.com/users/?id={id}")
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos/?userId={id}"
    )

    user = json.loads(user.text)
    todos = json.loads(todos.text)

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = len(todos)

    for todo in todos:
        if todo.get("completed"):
            NUMBER_OF_DONE_TASKS += 1

    print(f"Employee {user[0].get('name')} is done "
          f"with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for todo in todos:
        if todo.get("completed"):
            print(f"\t {todo.get('title')}")
