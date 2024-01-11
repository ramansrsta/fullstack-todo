from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

from .serializers import StudentSerializer
import io

from .models import Student

@method_decorator(csrf_exempt, name="dispatch")
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Student Added Successfull'}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)
    
    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Student Data Update Successfull'}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)
    
    def delete(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg' : 'Student Deleted Successfully'}
        return JsonResponse(res)