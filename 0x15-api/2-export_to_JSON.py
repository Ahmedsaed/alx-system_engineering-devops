#!/usr/bin/python3
"""Exports a json file with a to-do
list information for a given employee ID."""
import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]

    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/?id={id}"
    ).json()[0]
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos/?userId={id}"
    ).json()

    with open(f"{id}.json", "w") as json_file:
        json.dump({id: [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            } for todo in todos]}, json_file)
