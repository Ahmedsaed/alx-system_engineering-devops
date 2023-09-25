#!/usr/bin/python3
"""Exports a csv with a to-do list information for a given employee ID."""
import csv
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

    with open(f"{id}.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([id,
                             user.get("username"),
                             todo.get("completed"),
                             todo.get("title")])
