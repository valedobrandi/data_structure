import time
from models.db import db


def test_status_response_existant_task(client, seed_project):
    task = db["projects"].find_one({"idProject": 1})
    response = client.get(f"/task/{task['_id']}")
    assert response.status_code == 200


def test_status_response_non_existant_task(client, seed_project):
    response = client.get("/task/qualquer_id")
    assert response.status_code == 404


def test_title_of_task(client, seed_project):
    task = db["projects"].find_one({"idProject": 1})
    response = client.get(f"/task/{task['_id']}")
    assert task["task"] in response.text


def test_save_new_task(client, seed_project):
    response = client.post(
        "/task/1/form",
        data=dict(
            task="Task 3",
            status="To Do",
            completionPercentage="90",
            descriptionTask="Description Task 3",
            deadline="2025-01-01",
            responsible="Responsible 3",
        ),
        follow_redirects=True,
    )

    time.sleep(5)
    task_1 = "<p>Task 1</p>"
    assert task_1 in response.text
