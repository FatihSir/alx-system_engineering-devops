#!/usr/bin/python3
""" Gather data from an API """


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
            return user['name']


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
        user_name, completed_tasks_count, tasks
    ))
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == '__main__':
    import json
    from urllib.request import urlopen
    from sys import argv

    response_to_do = urlopen(
        'https://jsonplaceholder.typicode.com/todos')

    if response_to_do.getcode() == 200:
        response_users = urlopen(
            'https://jsonplaceholder.typicode.com/users')
        if response_users.getcode() == 200:
            to_do = json.loads(response_to_do.read().decode('utf-8'))
            users = json.loads(response_users.read().decode('utf-8'))
            if to_do and users:
                tasks, completed_tasks_count, completed_tasks = (
                    calculate_tasks(to_do, int(argv[1])))
                user_name = get_name(users, int(argv[1]))

                print_info(tasks, completed_tasks_count,
                           completed_tasks, user_name)
        else:
            print("Users can not be retrieved : {}"
                  .format(response_users.getcode()))
    else:
        print("To do can not be retrieved : {}"
              .format(response_to_do.getcode()))
