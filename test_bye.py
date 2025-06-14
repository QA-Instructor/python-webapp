from application import app


def test_bye_page():
    with app.test_client() as test_client:
        response = test_client.get('/bye')
        assert response.status_code == 200
        assert b"Goodbye World" in response.data
        assert b"YOUR NAME" in response.data
        assert b"Version" in response.data


def test_bye_page2():
    with app.test_client() as test_client:
        response = test_client.get('/bye')
        assert response.status_code == 200
        assert b"Goodbye" in response.data
        assert b"YOUR NAME" in response.data
        assert b"Version" in response.data