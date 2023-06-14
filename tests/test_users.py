import pytest
from jose import jwt
from app import schemas, config

def test_create_user(client):
    res = client.post("/users/", json={"email": "dogfan@catreek.net", 
                                       "password": "fruityloops"})
    
    new_user = schemas.UserResponse(**res.json())
    assert new_user.email == "dogfan@catreek.net"
    assert res.status_code == 201


def test_login_user(client, test_user):
    
    res = client.post("/login", data={"username": test_user['email'], 
                                    "password": test_user['password']})

    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, 
                         key=config.settings.secret_key, 
                         algorithms=[config.settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
    ('wrong@email.com', 'fruityloops', 403),
    ('catfan@catreek.net', 'wrongpassword', 403),
    (None, 'fruityloops', 422),
    ('catfan@catreek.net', None, 422)])
def test_bad_login(email, password, status_code, test_user, client):
    res = client.post("/login", data={"username": email,
                                      "password": password})
    assert res.status_code == status_code
