from rest_framework.pagination import CursorPagination

class MyCursor(CursorPagination):
    page_size=3
    ordering='name'
    cursor_query_param='cu'