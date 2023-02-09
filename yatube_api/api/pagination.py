from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class CustomPagination(LimitOffsetPagination):
    def get_paginated_response(self, data):
        return Response(data)


# {'count': 2,
#  'next': None,
#  'previous': None,
#  'results': [{'author': 'TestUser', 'group': 31, 'id': 23, 'image': None},
#              {'author': 'TestUserAnother', 'group': 32, 'id': 24, 'image': None}]
#  }