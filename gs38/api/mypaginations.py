from rest_framework.pagination import PageNumberPagination

class MyPageNo(PageNumberPagination):
    page_size=5
    page_query_param='p' #use instead of keyword page
    page_size_query_param='records' #user specific page size
    max_page_size=10
    last_page_strings='end'