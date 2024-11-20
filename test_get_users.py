'''
curl -X 'GET' \
  'https://reqres.in/api/users?page=1&per_page=15' \
  -H 'accept: application/json'
'''
import requests
# FILE: test_get_users.py
import requests

def test_get_users():
    base_url = 'https://reqres.in/api/users'
    params = {'page': 1, 'per_page': 15}
    response = requests.get(base_url, params=params)
    
    assert response.status_code == 200
    json_response = response.json()
    
    assert json_response['page'] == 1
    assert json_response['per_page'] == 15
    assert len(json_response['data']) == 12
    assert json_response['total_pages'] == 1
    assert json_response['total'] == 12
    
    first_user = json_response['data'][0]
    assert first_user['id'] == 1
    assert first_user['email'] == 'george.bluth@reqres.in'
    assert first_user['first_name'] == 'George'
    assert first_user['last_name'] == 'Bluth'
    assert first_user['avatar'] == 'https://reqres.in/img/faces/1-image.jpg'