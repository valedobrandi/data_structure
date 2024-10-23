def test_status_response(client):
    response = client.get("/")
    assert response.status_code == 200
