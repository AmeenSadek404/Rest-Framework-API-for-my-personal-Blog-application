from rest_framework.pagination import (LimitOffsetPagination, PageNumberPagination)


class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 5

class PostPageNumberPagination(PageNumberPagination):
    page_size = 5