def test_state_mutation_is_applied_within_test(client):
    # Arrange
    activity_name = "Chess Club"
    email = "isolation-check@mergington.edu"

    # Act
    client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )
    activities_response = client.get("/activities")

    # Assert
    assert email in activities_response.json()[activity_name]["participants"]


def test_state_is_reset_between_tests(client):
    # Arrange
    activity_name = "Chess Club"
    email = "isolation-check@mergington.edu"

    # Act
    activities_response = client.get("/activities")

    # Assert
    assert email not in activities_response.json()[activity_name]["participants"]
