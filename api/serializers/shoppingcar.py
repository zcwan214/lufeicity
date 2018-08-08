from rest_framework import serializers
from api import models

class CarSerializer(serializers.ModelSerializer):
    jiage = serializers.SerializerMethodField()

    def get_jiage(self,row):
        jiage_list = row.price.price_set.all()
        return [{'price':item.price} for item in jiage_list]

    class Meta:
        model = models.PricePolicy
        fields = ['price']