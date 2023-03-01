from rest_framework import serializers
from .models import TableTwo, TableOne


class TableTwoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TableTwo
        fields = ('class_name','weight','other_details')

