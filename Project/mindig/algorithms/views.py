from django.shortcuts import render
from django.core.management import call_command
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView

from algorithms.serializers import AlgoSerializer


class Algorithm(APIView):
    serializer_class = AlgoSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
            alg = serializer.data['algo']
            fichier = serializer.data['fichier']
    if alg = 'spade':
      call_command('custom_command_spade fichier res')
      return Response({'result': res},status=status.HTTP_200_OK)

    if alg = 'gsp':
      call_command('custom_command_GSP fichier' )
      return Response({'result': res},status=status.HTTP_200_OK)
            






