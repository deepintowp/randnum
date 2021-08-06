from django.shortcuts import render
from rest_framework.serializers import Serializer
from main_apis import serializers
from rest_framework.generics import RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
import random



# Create your views here.
class GenerateNumView(RetrieveAPIView):
    serializer_class = serializers.GenerateNumber
    def get(self, request, *args, **kwargs):
        req_data = request.data.copy()
        serializered_obj = self.serializer_class(data=req_data)
        if serializered_obj.is_valid():
            start_no = serializered_obj.validated_data.get('start_no')
            end_no = serializered_obj.validated_data.get('end_no')
            generate_no = random.randint(start_no, end_no)
            return Response({"generate_no":generate_no}, status=status.HTTP_200_OK)
        else:
            return  Response(serializered_obj.errors, status=status.HTTP_400_BAD_REQUEST)
