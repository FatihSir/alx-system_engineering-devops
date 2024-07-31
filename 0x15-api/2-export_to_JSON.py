#!/usr/bin/python3
""" Gather data from an API """
import csv
import json
import sys
import urllib.request


def get_name(users, user_id):
    """
    Get the name of a user

    Arguments:
        users (list of dictionaries): Json format of the users information
        user_id (int): The user id needed to be fetched

    Return:
        name (str): The name of the user
    """

    for user in users:
        if user['id'] == user_id:
            name = user['name'].strip()
            return name
    return None


def get_user_name(users, user_id):
    """
       Get the user_name of a user

       Arguments:
           users (list of dictionaries): Json format of the users information
           user_id (int): The user id needed to be fetched

       Return:
           user_name (str): The name of the user
       """
    for user in users:
        if user['id'] == user_id:
            user_name = user['username'].strip()
            return user_name
    return None


def calculate_tasks(to_do, user_id):
    """
    A function to calculate the number of tasks, number of completed tasks,
    completed tasks of the specified user

    Arguments:
        to_do (list of dictionaries): Json format of the tasks information
        user_id (int): The user id needed to be fetched

    Return:
        tasks (int): The number of tasks
        completed_tasks_count (int): The number of completed tasks
        completed_tasks (list): The list of completed tasks
    """
    tasks = 0
    completed_tasks_count = 0
    completed_tasks = []
    if not isinstance(user_id, int):
        raise TypeError('user_id must be an integer')
    for user in to_do:
        if user['userId'] == user_id and user['title'] is not None:
            tasks += 1
            if user['completed']:
                completed_tasks_count += 1
                completed_tasks.append(user['title'])

    return tasks, completed_tasks_count, completed_tasks


def print_info(tasks, completed_tasks_count, completed_tasks, user_name):
    """
    A function to print information about the tasks

    Arguments:
        tasks (int): The number of tasks
        completed_tasks_count (int): The number of completed tasks
        completed_tasks (list): The list of completed tasks
        user_name (str): The name of the user
    """
    if not isinstance(tasks, int):
        raise TypeError('tasks must be an integer')
    if not isinstance(completed_tasks_count, int):
        raise TypeError('tasks count must be an integer')
    if not isinstance(completed_tasks, list):
        raise TypeError('tasks count must be list')

    print("Employee {} is done with tasks({}/{}):".format(
        user_name, completed_tasks_count, tasks))
    for task in completed_tasks:
        print("\t {}".format(task))


def record_to_csv(to_do, users, user_id):
    """
    A function to record data to a csv file

    Arguments:
        to_do (list of dictionaries): Json format of the tasks information
        users (list of dictionaries): Json format of the users information
        user_id (int): The user id needed to be fetched
    """
    all_records = []
    user_name = get_user_name(users, user_id)
    for user in to_do:
        if user['userId'] == user_id and user['title'] is not None:
            record = [user_id, user_name, user['completed'], user['title']]
            all_records.append(record)

    with open(f'{user_id}.csv', mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for row in all_records:
            csv_writer.writerow(row)


def record_to_json(to_do, users, user_id):
    record = {}
    all_records = []
    file = {}
    user_name = get_user_name(users, user_id)
    record["username"] = user_name
    for user in to_do:
        if user["userId"] == user_id and user["title"] is not None:
            record["task"] = user["title"]
            record["completed"] = user["completed"]
        all_records.append(record)
    file[f"{user_id}"] = all_records

    with open(f"{user_id}.json", 'w', newline='') as json_file:
        json.dump(file, json_file)


if __name__ == '__main__':
    response_to_do = urllib.request.urlopen(
        'https://jsonplaceholder.typicode.com/todos')

    if response_to_do.getcode() == 200:
        response_users = urllib.request.urlopen(
            'https://jsonplaceholder.typicode.com/users')
        if response_users.getcode() == 200:
            to_do = json.loads(response_to_do.read().decode('utf-8'))
            users = json.loads(response_users.read().decode('utf-8'))
            record_to_json(to_do, users, int(sys.argv[1]))
