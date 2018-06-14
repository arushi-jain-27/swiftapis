from django.shortcuts import render
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
import requests

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
@api_view(['GET'])
def download_object(request, container, object, format=None):
    if request.method == 'GET':
        r = requests.get('http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/' + container + '/' + object, headers={'X-Auth-Token': 'b5303fbd78134deab5671cbf4ee45155'})
        with open(object, "wb") as code:
            code.write(r.content)
        return render(request, 'files/success.html')


@api_view(['GET'])
def container_list(request, format=None):
    if request.method == 'GET':
        r = requests.get('http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/', headers={'X-Auth-Token': 'b5303fbd78134deab5671cbf4ee45155'}).text
        obj_arr = r.split ("\n")
        obj_arr.pop()
        return Response (obj_arr)


@api_view(['GET'])
def object_list(request, container, format=None):
    if request.method == 'GET':
        r = requests.get('http://10.129.103.86:8080/v1/AUTH_b3f70be8acad4ec197e2b5edf48d9e5a/'+container , headers={'X-Auth-Token': 'b5303fbd78134deab5671cbf4ee45155'}).text
        obj_arr = r.split ("\n")
        obj_arr.pop()
        return Response (obj_arr)





    


