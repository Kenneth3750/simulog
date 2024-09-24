from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import UserEmailSerializer, UsersListSerializer
from .functions import get_email_users, create_update_list
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
    
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def users_list(request):
    if request.method == 'GET':   
        users = get_email_users()
        serializer = UsersListSerializer(data={'users': users})
        if serializer.is_valid():
            return Response(
                {
                    'status': 'success',
                    'users': users
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
    elif request.method == 'POST':
        serializer = UsersListSerializer(data=request.data)
        if serializer.is_valid():
            users = serializer.validated_data['users']
            result = create_update_list(users)
            if 'message' in result:
                return Response(
                    {
                        'status': 'success',
                        'message': 'The list of users has been updated'
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        'status': 'error',
                        'message': result['Error']
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {
                    'status': 'error',
                    'message': json.dumps(serializer.errors)
                },
                status=status.HTTP_400_BAD_REQUEST
            )