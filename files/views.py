
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
import requests, os

"""
def get_acc (request):
    form = AccountForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        token = obj.token
        url= 'http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/'
        r = requests.get(url, headers={'X-Auth-Token': token}).text
        obj_arr = r.split("\n")
        obj_arr.pop()
        return render (request, 'files/display_cont.html', {"obj_arr": obj_arr, "token":token})
    context = {
        "form": form,
    }
    return render(request, 'files/input.html', context)
	
def search_object (request):
    form = FilesForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        container = obj.container
        object_name = obj.object
        token = obj.token
        location = obj.location
        url= 'http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/' + container + '/'+ object_name
        r = requests.get(url, headers={'X-Auth-Token': token})
        #return r
        with open(location, "wb") as code:
         code.write(r.content)
        return render (request, 'files/success.html')
    context = {
        "form": form,
    }
    return render(request, 'files/input.html', context)

def get_cont (request, container, token):
     url= 'http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/' + container
     r = requests.get(url, headers={'X-Auth-Token': token}).text
     #r = r.decode ("utf-8")
     obj_arr = r.split("\n")
     obj_arr.pop()
     return render (request, 'files/display_objects.html', {"obj_arr": obj_arr, "container":container, "token":token})


def get_obj(request, container,object, token):
    url = 'http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/' + container + '/'+ object
    r = requests.get(url, headers={'X-Auth-Token': token})
    with open(object, "wb") as code:
      code.write(r.content)
    return render (request, 'files/success.html')

"""

@api_view(['GET', 'DELETE'])
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
    if request.method =='DELETE':
        r = requests.delete('http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/' + container + '/' + object, headers={'X-Auth-Token': token}).text
        return Response (r)


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
        return Response (obj_arr)
    if request.method =='PUT':
        new_cont = request.data
        r = requests.put ('http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/' + new_cont, headers={'X-Auth-Token': token}).text
        return Response (r)


@api_view(['GET', 'PUT', 'DELETE'])
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
        return Response (obj_arr)
    if request.method =='PUT':
        url = request.data
        obj = os.path.basename(url)
        r = requests.put ('http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/'+container + '/' + obj , headers={'X-Auth-Token': token}, data = open (url, "rb")).text
        return Response (r)
    if request.method =='DELETE':
        r = requests.delete('http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/' + container, headers={'X-Auth-Token': token}).text
        return Response (r)





    


