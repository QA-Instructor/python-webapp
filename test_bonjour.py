from application import app


def test_bonjour_page():
    with app.test_client() as test_client:
        response = test_client.get('/bonjour')
        assert response.status_code == 200
        assert b"Bonjour le monde" in response.data
        assert b"Bienvenue" in response.data
        assert b"Version" in response.data