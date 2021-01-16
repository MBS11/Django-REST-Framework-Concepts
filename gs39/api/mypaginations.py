from rest_framework.pagination import LimitOffsetPagination

class MyLimit(LimitOffsetPagination):
    default_limit=5
    limit_query_param='mylimit' #to use this instead of keyword limit
    offset_query_param='myoffset'#to use this instead of keyword offset
    max_limit=7