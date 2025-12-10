from rest_framework.pagination import PageNumberPagination


class CategoryPagination(PageNumberPagination):
    page_size = 8

class ProductPagination(PageNumberPagination):
    page_size = 5
