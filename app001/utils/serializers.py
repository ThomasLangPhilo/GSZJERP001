from rest_framework import serializers

from app001.models import rawstock, product, industry, stockbase


class RawstockSerializers(serializers.Serializer):

    id = serializers.IntegerField()

    name = serializers.CharField(max_length=32)


class IndustrySerializers(serializers.Serializer):
    id = serializers.IntegerField()
    industryname = serializers.CharField(max_length=64)


class stockbaseSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    stockbasename = serializers.CharField(max_length=64)


class ProductSerializers(serializers.Serializer):


    id = serializers.IntegerField()
    product = serializers.CharField(max_length=32)
    rawstock = RawstockSerializers(many=True)
    industry = IndustrySerializers(many=True)
    stockbase = stockbaseSerializers(many=True)
