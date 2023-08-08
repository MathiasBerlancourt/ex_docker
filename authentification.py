import os
import requests

api_address = '34.245.184.17'
api_port = 8000

params = [
    {
        'username': 'alice',
        'password': 'wonderland'
    },
    {
        'username': 'bob',
        'password': 'builder'
    },
    {
        'username': 'clementine',
        'password': 'mandarine'
    }
]

for param in params:
    r = requests.get(
        url=f'http://{api_address}:{api_port}/permissions',
        params=param
    )

    expected_status_code = 403 if param['username'] not in [
        'alice', 'bob'] else 200
    test_status = "✅ Test Passed" if r.status_code == expected_status_code else "❌ Test Failed"

    output = f'''
============================
👨‍💻 Authentication test 🤖
============================

============================
TEST username {param['username']} and password {param['password']}
============================

request done at "/permissions"
| username={param['username']}
| password={param['password']} 

expected result = {expected_status_code}
actual result = {r.status_code}

==>  {test_status}
'''
    print(output)

    # impression dans un fichier
    if os.environ.get('LOG') == 1:
        with open('api_test.log', 'a') as file:
            file.write(output)
