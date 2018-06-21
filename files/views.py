from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
import requests, os
from rest_framework.reverse import reverse



@api_view(['GET', 'PUT'])
def container_list(request, format=None):
    url = 'http://10.129.103.86:5000/v3/auth/tokens'
    headers = {'content-type': 'application/json'}
    data = '\n{ "auth": {\n    "identity": {\n      "methods": ["password"],\n      "password": {\n        "user": {\n          "name": "swift",\n          "domain": { "name": "default" },\n          "password": "swift"\n        }\n      }\n    },\n    "scope": {\n      "project": {\n        "name": "service",\n        "domain": { "name": "default" }\n      }\n    }\n  }\n}'
    r = requests.post(url, headers=headers, data=data)
    token = r.headers.get('X-Subject-Token')
    if request.method == 'GET':
        r = requests.get('http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/', headers={'X-Auth-Token': token}).text
        obj_arr = r.split ("\n")
        obj_arr.pop()
        rows = len(obj_arr)
        columns = 2
        Matrix = [[0 for x in range(columns)] for x in range(rows)]
        for i in range(rows):
            Matrix[i][0] = obj_arr[i]
            Matrix[i][1] = reverse('files:cont_info', kwargs={'container': obj_arr[i]}, request=request, format=format)
        return Response(Matrix)
    if request.method =='PUT':
        new_cont = request.data
        r = requests.put ('http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/' + new_cont, headers={'X-Auth-Token': token}).text
        return Response (r)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def object_list(request, container, format=None):
    url = 'http://10.129.103.86:5000/v3/auth/tokens'
    headers = {'content-type': 'application/json'}
    data = '\n{ "auth": {\n    "identity": {\n      "methods": ["password"],\n      "password": {\n        "user": {\n          "name": "swift",\n          "domain": { "name": "default" },\n          "password": "swift"\n        }\n      }\n    },\n    "scope": {\n      "project": {\n        "name": "service",\n        "domain": { "name": "default" }\n      }\n    }\n  }\n}'
    r = requests.post(url, headers=headers, data=data)
    token = r.headers.get('X-Subject-Token')
    if request.method == 'GET':
        r = requests.get('http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/'+container , headers={'X-Auth-Token': token}).text
        obj_arr = r.split ("\n")
        obj_arr.pop()
        rows = len(obj_arr)
        columns = 2
        Matrix = [[0 for x in range(columns)] for x in range(rows)]
        for i in range(rows):
            Matrix[i][0] = obj_arr[i]
            Matrix[i][1] = reverse('files:obj_info', kwargs={'container': container, 'object': obj_arr[i]},
                                   request=request, format=format)
        return Response(Matrix)
    if request.method =='PUT':
        url = request.data
        obj = os.path.basename(url)
        r = requests.put ('http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/'+container + '/' + obj , headers={'X-Auth-Token': token}, data = open (url, "rb")).text
        return Response (r)
    if request.method == 'POST':
        t = {'X-Auth-Token': token }
        data = JSONParser().parse(request)
        data.update (t)
        requests.post('http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/' + container,headers=data)
        r = requests.get('http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/' + container,
                         headers={'X-Auth-Token': token})
        return Response (r.headers)
    if request.method =='DELETE':
        r = requests.delete('http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/' + container, headers={'X-Auth-Token': token}).text
        return Response (r)


@api_view(['GET','POST', 'DELETE'])
def download_object(request, container, object, format=None):
    url = 'http://10.129.103.86:5000/v3/auth/tokens'
    headers = {'content-type': 'application/json'}
    data = '\n{ "auth": {\n    "identity": {\n      "methods": ["password"],\n      "password": {\n        "user": {\n          "name": "swift",\n          "domain": { "name": "default" },\n          "password": "swift"\n        }\n      }\n    },\n    "scope": {\n      "project": {\n        "name": "service",\n        "domain": { "name": "default" }\n      }\n    }\n  }\n}'
    r = requests.post(url, headers=headers, data=data)
    token = r.headers.get('X-Subject-Token')
    if request.method == 'GET':
        r = requests.get('http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/' + container + '/' + object, headers={'X-Auth-Token': token})
        with open(object, "wb") as code:
            code.write(r.content)
        return Response (r.headers)
    if request.method == 'POST':
        t = {'X-Auth-Token': token}
        data = JSONParser().parse(request)
        data.update(t)
        requests.post('http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/' + container, headers=data)
        r = requests.get('http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/' + container,
                         headers={'X-Auth-Token': token})
        return Response(r.headers)
    if request.method =='DELETE':
        r = requests.delete('http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/' + container + '/' + object, headers={'X-Auth-Token': token}).text
        return Response (r)


    


