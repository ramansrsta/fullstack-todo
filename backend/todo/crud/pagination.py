from rest_framework.pagination import PageNumberPagination

class Pagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10
    last_page_strings = 'end'

class PaginationLimitOffset(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    last_page_strings = 'end'