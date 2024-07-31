#!/usr/bin/python3
""" Gather data from an API """
import json
import urllib.request


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


def get_all_records(to_do, users, user_id):
    all_records = []
    file = {}
    user_name = get_user_name(users, user_id)
    for user in to_do:
        if user["userId"] == user_id and user["title"] is not None:
            all_records.append({"username": user_name,
                                "task": user["title"],
                                "completed": user["completed"]})
    file[f"{user_id}"] = all_records
    return file


def all_records_to_json(to_do, users):
    """
    A function to export all records to a json file

    Arguments:
         to_do (list of dictionaries): Json format of the users information
         users (list of dictionaries): Json format of the users information
    """
    file = {}
    for user in users:
        all_records = get_all_records(to_do, users, user['id'])
        file[f"{user['id']}"] = all_records[f"{user['id']}"]

    with open("todo_all_employees.json", 'w', newline='') as json_file:
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
            all_records_to_json(to_do, users)
