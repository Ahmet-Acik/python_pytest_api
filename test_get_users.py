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
    
    # Extract and Print All User Emails:
    """
    User Emails: ['george.bluth@reqres.in', 'janet.weaver@reqres.in', 'emma.wong@reqres.in', 'eve.holt@reqres.in', 'charles.morris@reqres.in', 'tracey.ramos@reqres.in', 'michael.lawson@reqres.in', 'lindsay.ferguson@reqres.in', 'tobias.funke@reqres.in', 'byron.fields@reqres.in', 'george.edwards@reqres.in', 'rachel.howell@reqres.in']
    """
    emails = [user['email'] for user in json_response['data']]
    print("User Emails:", emails) 
    assert 'george.bluth@reqres.in' in emails
    
    
    # Count the Number of Users with a Specific Last Name:
    '''
    Number of users with last name 'Bluth': 1
    Number of users with first name 'George': 2
    '''
    last_name_count = sum(1 for user in json_response['data'] if user['last_name'] == 'Bluth')
    print("Number of users with last name 'Bluth':", last_name_count)
    assert last_name_count == 1
    
    first_name_count = sum(1 for user in json_response['data'] if user['first_name'] == 'George')
    print("Number of users with first name 'George':", first_name_count)
    assert first_name_count == 2
    
    # Create a Dictionary Mapping User IDs to Their Full Names:
    """
    User ID to Full Name Mapping: {1: 'George Bluth', 2: 'Janet Weaver', 3: 'Emma Wong', 4: 'Eve Holt', 5: 'Charles Morris', 6: 'Tracey Ramos', 7: 'Michael Lawson', 8: 'Lindsay Ferguson', 9: 'Tobias Funke', 10: 'Byron Fields', 11: 'George Edwards', 12: 'Rachel Howell'}
    User ID to Email Mapping: {1: 'george.bluth@reqres.in', 2: 'janet.weaver@reqres.in', 3: 'emma.wong@reqres.in', 4: 'eve.holt@reqres.in', 5: 'charles.morris@reqres.in', 6: 'tracey.ramos@reqres.in', 7: 'michael.lawson@reqres.in', 8: 'lindsay.ferguson@reqres.in', 9: 'tobias.funke@reqres.in', 10: 'byron.fields@reqres.in', 11: 'george.edwards@reqres.in', 12: 'rachel.howell@reqres.in'}
    """
    user_id_to_name = {user['id']: f"{user['first_name']} {user['last_name']}" for user in json_response['data']}
    print("User ID to Full Name Mapping:", user_id_to_name)
    assert user_id_to_name[1] == 'George Bluth'
    assert user_id_to_name[2] == 'Janet Weaver'
    assert user_id_to_name[3] == 'Emma Wong'
    
    user_id_to_email = {user['id']: user['email'] for user in json_response['data']}
    print("User ID to Email Mapping:", user_id_to_email)
    assert user_id_to_email[1] == 'george.bluth@reqres.in'
    assert user_id_to_email[2] == 'janet.weaver@reqres.in'
    assert user_id_to_email[3] == 'emma.wong@reqres.in'
    
    # Find the User with the Longest First Name:
    """
    User with the longest first name: {'id': 5, 'email': 'charles.morris@reqres.in', 'first_name': 'Charles', 'last_name': 'Morris', 'avatar': 'https://reqres.in/img/faces/5-image.jpg'}
    User with the shortest last name: {'id': 3, 'email': 'emma.wong@reqres.in', 'first_name': 'Emma', 'last_name': 'Wong', 'avatar': 'https://reqres.in/img/faces/3-image.jpg'}
    User with the longest email: {'id': 8, 'email': 'lindsay.ferguson@reqres.in', 'first_name': 'Lindsay', 'last_name': 'Ferguson', 'avatar': 'https://reqres.in/img/faces/8-image.jpg'}
    User with the shortest email: {'id': 4, 'email': 'eve.holt@reqres.in', 'first_name': 'Eve', 'last_name': 'Holt', 'avatar': 'https://reqres.in/img/faces/4-image.jpg'}
    """
    longest_first_name_user = max(json_response['data'], key=lambda user: len(user['first_name']))
    print("User with the longest first name:", longest_first_name_user)
    assert longest_first_name_user['first_name'] == 'Charles'
    assert longest_first_name_user['last_name'] == 'Morris'
    assert longest_first_name_user['email'] == 'charles.morris@reqres.in'
    assert longest_first_name_user['avatar'] == 'https://reqres.in/img/faces/5-image.jpg'
    
    shortest_last_name_user = min(json_response['data'], key=lambda user: len(user['last_name']))
    print("User with the shortest last name:", shortest_last_name_user)
    assert shortest_last_name_user['first_name'] == 'Emma'
    assert shortest_last_name_user['last_name'] == 'Wong'
    assert shortest_last_name_user['email'] == 'emma.wong@reqres.in'
    assert shortest_last_name_user['avatar'] == 'https://reqres.in/img/faces/3-image.jpg'
    
    user_with_longest_email = max(json_response['data'], key=lambda user: len(user['email']))
    print("User with the longest email:", user_with_longest_email)
    assert user_with_longest_email['first_name'] == 'Lindsay'
    assert user_with_longest_email['last_name'] == 'Ferguson'
    assert user_with_longest_email['email'] == 'lindsay.ferguson@reqres.in'
    assert user_with_longest_email['avatar'] == 'https://reqres.in/img/faces/8-image.jpg'
    
    
    user_with_shortest_email = min(json_response['data'], key=lambda user: len(user['email']))
    print("User with the shortest email:", user_with_shortest_email)
    assert user_with_shortest_email['first_name'] == 'Eve'
    assert user_with_shortest_email['last_name'] == 'Holt'
    assert user_with_shortest_email['email'] == 'eve.holt@reqres.in'
    assert user_with_shortest_email['avatar'] == 'https://reqres.in/img/faces/4-image.jpg'
    
    """
    
    """
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