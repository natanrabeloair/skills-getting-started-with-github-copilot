from fastapi.testclient import TestClient

from src.app import activities, app


client = TestClient(app)


def test_unregister_existing_participant():
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    response = client.delete(
        f"/activities/{activity_name}/participants/{email}"
    )

    assert response.status_code == 200
    assert email not in activities[activity_name]["participants"]
    assert response.json()["message"] == (
        f"Unregistered {email} from {activity_name}"
    )


def test_unregister_missing_participant_returns_error():
    response = client.delete(
        "/activities/Chess Club/participants/not-registered@mergington.edu"
    )

    assert response.status_code == 400
    assert "not registered" in response.json()["detail"].lower()
