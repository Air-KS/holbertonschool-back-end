#!/usr/bin/python3
import requests
import sys


def print_todo_progress(employee_id):
    BASE_URL = "https://jsonplaceholder.typicode.com/"

    # Récupère le nom de l'employée
    user_data = requests.get("{}users/{}".format
                             (BASE_URL, employee_id)).json()

    # Récupère les TODOs pour cet employé
    todos_data = requests.get("{}todos?userId={}".format
                              (BASE_URL, employee_id)).json()

    # Filtre les tâches terminées
    done_tasks = [task for task in todos_data if task["completed"]]

    # Afficher les informations
    print("Employee {} is done with tasks {}/{}".format
          (user_data["name"], len(done_tasks), len(todos_data)))
    for task in done_tasks:
        print("\t {}".format(task["title"]))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ID employed")
    else:
        print_todo_progress(int(sys.argv[1]))
