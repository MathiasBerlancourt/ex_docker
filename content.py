import os
import requests

api_address = '34.245.184.17'
api_port = 8000

params = [
    {
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'life is beautiful'
    }, {
        'username': 'alice',
        'password': 'wonderland',
        'sentence': 'that sucks'
    }
]

for param in params:
    # Test for v1 endpoint
    r_v1 = requests.get(
        url=f'http://{api_address}:{api_port}/v1/sentiment',
        params=param
    )
    res_v1 = r_v1.json()
    if (r_v1.status_code == 200 and param['sentence'] == 'life is beautiful' and res_v1['score'] > 0):
        test_result_v1 = "✅ Test Passed"
    elif (r_v1.status_code == 200 and param['sentence'] == 'that sucks' and res_v1['score'] < 0):
        test_result_v1 = "✅ Test Passed"
    else:
        test_result_v1 = "⛔ Test Failed"

    # Test for v2 endpoint
    r_v2 = requests.get(
        url=f'http://{api_address}:{api_port}/v2/sentiment',
        params=param
    )
    res_v2 = r_v2.json()
    if (r_v2.status_code == 200 and param['sentence'] == 'that sucks' and res_v2['score'] < 0):
        test_result_v2 = "✅ Test Passed"
    elif (r_v2.status_code == 200 and param['sentence'] == 'life is beautiful' and res_v2['score'] > 0):
        test_result_v2 = "✅ Test Passed"
    else:
        test_result_v2 = "⛔ Test Failed"

    output = f'''
============================
📄 Content test 🤖
============================

============================
TEST V1 with sentence: {param['sentence']}
============================
Test v1 result = {test_result_v1}
v1 status code = {r_v1.status_code}
============================
TEST V2 with sentence: {param['sentence']}
============================
Test v2 result = {test_result_v2}
v2 status code = {r_v2.status_code}

    '''
    print(output)

    # impression dans un fichier
    if os.environ.get('LOG') == 1:
        with open('api_test.log', 'a') as file:
            file.write(output)
