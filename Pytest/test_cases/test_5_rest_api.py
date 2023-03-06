import requests
# import uuid
import pytest

""" Link to the youtube video : https://www.youtube.com/watch?v=7dgQRVqF1N0. The endpoint we are using in this section
is https://todo.pixegami.io , to see the documentation of this endpoint add the /Docs at the end of the url."""

url = "https://todo.pixegami.io"


def task_payload():
    # user_id = f'test_user_{uuid.uuid4().hex}'
    # print(f"\n {user_id}")
    user_id = 'svm69006'
    return {"content": "My test content",
            "user_id": user_id,
            "is_done": False}


def create_task(json_data):
    return requests.put(url + "/create-task", json=json_data)


def get_task(requested_task_id):
    return requests.get(url + f'/get-task/{requested_task_id}')


def update_task(json_data):
    return requests.put(url + "/update-task", json=json_data)


def list_tasks(user_id):
    return requests.get(url + f"/list-tasks/{user_id}")


def delete_task(task_id):
    return requests.delete(url + f"/delete-task/{task_id}")


def test_can_call_endpoint():
    response = requests.get(url)
    assert response.status_code == 200, 'Test failed, cannot connect to url'


def test_can_create_task():
    payload = task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200, 'Test task is not created'
    created_task_data = create_task_response.json()
    content = created_task_data['task']['content']
    assert content == payload['content'], 'Test is not created with given content'


def test_can_get_task_by_task_id():
    task_id = input("Enter the task_id:")
    get_task_response = get_task(task_id)
    get_task_data = get_task_response.json()
    assert get_task_data['task_id'] == task_id, 'The given task id task does not exist.'
    print(get_task_data)


def test_can_update_task():
    payload = task_payload()
    create_task_response = create_task(payload)
    data = create_task_response.json()
    assert create_task_response.status_code == 200, 'Task is not created'
    new_payload = {
        'user_id': data['task']['user_id'],
        'task_id': data['task']['task_id'],
        'content': 'Updated content',
        'is_done': True
    }
    update_task_response = update_task(new_payload)
    get_task_response = get_task(data['task']['task_id'])
    get_task_data = get_task_response.json()
    assert update_task_response.status_code == 200, 'Requested task is not updated'
    assert get_task_data['content'] == new_payload['content'], 'Requested task is not updated'
    assert get_task_data['is_done'] == new_payload['is_done'], 'Requested task is not updated'


def test_can_list_tasks():
    """create n tasks with one user_id"""
    # payload = task_payload()
    # for _ in range(3):
    #     create_task_response = create_task(payload)
    #     assert create_task_response.status_code == 200, "Task not created"

    """ List the tasks, and checks that there are n items """
    user_id = input("Enter the user_id you want to list the tasks:")
    list_tasks_response = list_tasks(f"{user_id}")
    data = list_tasks_response.json()
    for item in data['tasks']:
        for key, values in item.items():
            if key == 'user_id':
                assert item[key] == user_id, "All tasks of given user are not returned"
                assert list_tasks_response.status_code == 200, "All tasks of given user_id are not returned"
    for items in list_tasks_response.json().values():
        for item in items:
            print(item, sep='\n')


task_ids = [
    "task_4853e3a339564210ba9035edaac32dbd",
    "task_051c51104e004e598aa8004c2f080bc4",
    "task_0ece6633af9448f48bde3fc6e73ebdcb",
    "task_e1bf69910eeb480fb41f6de5179a8bff",
    "task_b71fb9097aae4fecb5e81bc5677d1263",
    "task_6a1277d833444d7f81c92267bc1f1207",
    "task_970d27f21ad34aa9847152181bd86c34",
    "task_970d27f21ad34aa9847152181bd86c34",
    "task_2f5590ded6c644e38a97ec09d49594ab",
    "task_7445ec442c80458baac4586b7116d88d"]


@pytest.mark.parametrize("task_id", task_ids)
def test_can_delete_task(task_id):
    # payload = task_payload()
    # create_task_response = create_task(payload)
    # data = create_task_response.json()
    # task_id = data['task']['task_id']
    # assert create_task_response.status_code == 200, "Task is not created"
    # task_id = input("Enter the task_id you want to delete:")
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200, 'Task is not deleted'

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404, 'Task is not deleted'
