from django.shortcuts import render
from rest_framework import status
from .serializers import PalletsSerializer
from rest_framework.generics import GenericAPIView
from .models import Pallet
from rest_framework.response import Response


class PalletsView(GenericAPIView):
    def get_queryset(self):
        return Pallet.objects.all()

    def get(self, request, id=None):
        if id:
            try:
                pallet = Pallet.objects.get(id=id)
                serializer = PalletsSerializer(pallet)
                return Response(
                    {'status': 'success', 
                    'data': serializer.data},
                    status=status.HTTP_200_OK )
            
            except Pallet.DoesNotExist:
                return Response(
                    {'status': 'error', 
                    'message': 'Pallet not found'},
                    status=status.HTTP_404_NOT_FOUND )
        
        else:
            pallets = Pallet.objects.all()
            serializer = PalletsSerializer(pallets, many=True)
            return Response(
                {'status': 'success', 
                 'data': serializer.data},
                status=status.HTTP_200_OK )
