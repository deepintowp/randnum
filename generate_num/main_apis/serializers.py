from rest_framework import serializers

class GenerateNumber(serializers.Serializer):
    start_no = serializers.IntegerField(min_value=1, required=False, default=1)
    end_no = serializers.IntegerField(required=False, min_value=2, default=1000)