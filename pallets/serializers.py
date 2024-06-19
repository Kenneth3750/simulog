from rest_framework import serializers
from .models import Pallet

class PalletsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    width = serializers.FloatField()
    height = serializers.FloatField()
    length = serializers.FloatField()
    weight = serializers.FloatField()
    volume = serializers.FloatField()

    class Meta:
        model = Pallet
        fields = '__all__'


    