from django.shortcuts import render
from rest_framework.response import Response
from .models import Student 
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView


class StudentAPI(APIView):
    def get(self,request,id=None,format=None):
        id=id
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data) 
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,id,format=None):
        id=id
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors)
    
    def patch(self,request,id,format=None):
        id=id
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self,request,id,format=None):
        id=id
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})













