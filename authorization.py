import os
import requests

api_address = '34.245.184.17'
api_port = 8000

params = [
    {
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'hello world'
    },
    {
        'username': 'bob',
        'password': 'builder',
        'sentence': 'hello world'
    }
]

for param in params:
    # Test for v1 endpoint
    r_v1 = requests.get(
        url=f'http://{api_address}:{api_port}/v1/sentiment',
        params=param
    )
    test_result_v1 = "✅ Test Passed" if r_v1.status_code == 200 else "❌ Test Failed"

    # Test for v2 endpoint
    r_v2 = requests.get(
        url=f'http://{api_address}:{api_port}/v2/sentiment',
        params=param
    )
    test_result_v2 = "✅ Test Passed" if (r_v2.status_code == 200 and param['username'] == 'alice') or (
        r_v2.status_code == 403 and param['username'] == 'bob') else "❌ Test Failed"

    output = f'''
============================
🔒 Authorization test 🤖
============================

============================
TEST username {param['username']}, password {param['password']} and sentence {param['sentence']}
============================

Test v1 result = {test_result_v1}
v1 status code = {r_v1.status_code}

Test v2 result = {test_result_v2}
v2 status code = {r_v2.status_code}

'''

    print(output)
    # impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output)
