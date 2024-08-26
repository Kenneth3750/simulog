from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import InternationalFreightSerializer
from .functions import international_freight_calculator

@api_view(['POST'])
@permission_classes([AllowAny])
def international_freight(request):
    serializer = InternationalFreightSerializer(data=request.data)
    if serializer.is_valid():
        fee = serializer.validated_data['fee']
        amount = serializer.validated_data['amount']
        baf = serializer.validated_data['baf']
        caf = serializer.validated_data['caf']
        ams = serializer.validated_data['ams']
        bl = serializer.validated_data['bl']
        cs = serializer.validated_data['cs']
        others = serializer.validated_data['others']
        
        total_basic_fee, total = international_freight_calculator(fee, amount, baf, caf, ams, bl, cs, others)
        return Response(
            {
                'status': 'success',
                'total_basic_fee': total_basic_fee,
                'total': total
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