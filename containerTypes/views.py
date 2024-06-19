from django.shortcuts import render
from .serializers import ContainerSerializer
from rest_framework.generics import GenericAPIView
from .models import Containers
from rest_framework.response import Response
from rest_framework import status


class ContainerView(GenericAPIView):
    def get_queryset(self):
        return Containers.objects.all()

    def get(self, request, id=None):
        if id:
            try:
                container = Containers.objects.get(id=id)
                serializer = ContainerSerializer(container)
                return Response(
                    {'status': 'success',
                    'data': serializer.data},
                    status=status.HTTP_200_OK)

            except Containers.DoesNotExist:
                return Response(
                    {'status': 'error',
                    'message': 'Container not found'},
                    status=status.HTTP_404_NOT_FOUND)
        else:
            containers = Containers.objects.all()
            serializer = ContainerSerializer(containers, many=True)
            return Response(
                {'status': 'success',
                 'data': serializer.data},
                status=status.HTTP_200_OK)
