import pytest
from typing import List
from  app import schemas

def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")
    
    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200

def test_noauth_get_all_posts(client ,test_posts):
    res = client.get("/posts/")

    assert res.status_code == 401

def test_noauth_get_a_post(client ,test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")

    assert res.status_code == 401

def test_get_noexistant_post(authorized_client, test_posts):
    res = authorized_client.get("/posts/8888")

    assert res.status_code == 404

def test_get_noexistant_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")

    post = schemas.PostVote(**res.json())
    
    assert res.status_code == 200
    assert post.Post.id == test_posts[0].id
    assert post.Post.title == test_posts[0].title
    assert post.Post.content == test_posts[0].content

@pytest.mark.parametrize("title, content, published", [("first post","yeet", True), ("pizza for cats","with kibbles", False)])
def test_create_post(authorized_client, test_user, test_posts, title, content, published):
    
    res = authorized_client.post("/posts/", json={"title": title, "content": content, "published": published})

    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published

def test_create_published_true(authorized_client):
    res = authorized_client.post("/posts/", json={"title": "test title", "content": "test_content"})
    created_post = schemas.Post(**res.json())
    
    assert res.status_code == 201
    assert created_post.published == True      

def test_noauth_create_post(client ,test_posts):
    res = client.post("/posts/", json={"title": "test title", "content": "test_content"})

    assert res.status_code == 401

def test_noauth_delete(client, test_posts):
    res = client.delete(f"/posts/{test_posts[0].id}")

    assert res.status_code == 401

def test_delete_success(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[0].id}")

    assert res.status_code == 204

def test_delete_non_exist_post(authorized_client, test_user, test_posts):
    res = authorized_client.delete("/posts/8888")

    assert res.status_code == 404

def test_delete_other_user_post(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[3].id}")

    assert res.status_code == 403

def test_update_post(authorized_client, test_user, test_posts):
    data = {"title": "updated", "content": "updated", "id": test_posts[0].id}
    res = authorized_client.put(f"/posts/{test_posts[0].id}", json=data)

    updated_post = schemas.Post(**res.json())
    assert updated_post.content == data["content"]
    assert updated_post.title == data["title"]
    assert res.status_code == 200

def test_update_other_user_post(authorized_client, test_user, test_user_other, test_posts):
    data = {"title": "updated", "content": "updated", "id": test_posts[3].id}
    res = authorized_client.put(f"/posts/{test_posts[3].id}", json=data)

    assert res.status_code == 403

# A few tests extra can be defined.