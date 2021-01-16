from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Model Object - Single Student Data
def student_detail(request,id):
    stu=Student.objects.get(id=id)
    serializer=StudentSerializer(stu)
    #json_data=JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data)



# Quesry Set - All Student Data
def student_list(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu, many=True)
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data, safe=False)