from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Account, Destination
from .serializers import AccountSerializer, DestinationSerializer
import requests

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

@api_view(['POST'])
def incoming_data(request):
    app_secret_token = request.headers.get('CL-X-TOKEN')
    if not app_secret_token:
        return Response({"error": "Un Authenticate"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        account = Account.objects.get(app_secret_token=app_secret_token)
    except Account.DoesNotExist:
        return Response({"error": "Invalid Token"}, status=status.HTTP_400_BAD_REQUEST)

    data = request.data

    for destination in account.destinations.all():
        headers = destination.headers
        method = destination.http_method.lower()
        url = destination.url

        if method == 'get':
            response = requests.get(url, params=data, headers=headers)
        else:
            response = getattr(requests, method)(url, json=data, headers=headers)

        if not response.ok:
            return Response({"error": f"Failed to send data to {url}"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "Data sent successfully"}, status=status.HTTP_200_OK)
