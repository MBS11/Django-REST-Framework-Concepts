from rest_framework.permissions import BasePermission

class MyPermission(BaseException):
    def has_permission(self,request,view):
        if request.method=='POST':
            return True
        return False