from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Gives most control over the application logic',
            'Works as traditional django view',
            'Is mapped manually to urls',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
