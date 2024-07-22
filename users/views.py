from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import UserEmailSerializer
from rest_framework import status
import json

@api_view(['POST'])
@permission_classes([AllowAny])
def verify_user(request):
    serializer = UserEmailSerializer(data=request.data)
    if serializer.is_valid():
        return Response(
            {
                'status': 'success',
                'message': 'The user is authorized to use the application'
            },
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {
                'status': 'error',
                'message': json.dumps(serializer.errors)
            },
            status=status.HTTP_400_BAD_REQUEST
       )
    