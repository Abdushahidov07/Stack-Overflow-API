from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .serializers import *
from .models import *
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from urllib.parse import urlencode, urljoin
import requests
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from secret import *
from django.shortcuts import render, redirect
from django.views import View
from .permision import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


def google_login(request):
    google_callback_uri = GOOGLE_OAUTH_CALLBACK_URL  
    google_client_id = GOOGLE_OAUTH_CLIENT_ID

    params = {
        'redirect_uri': google_callback_uri,
        'prompt': 'consent',
        'response_type': 'code',
        'client_id': google_client_id,
        'scope': 'openid email profile',
        'access_type': 'offline',
    }

    google_auth_url = f"https://accounts.google.com/o/oauth2/v2/auth?redirect_uri={google_callback_uri}&prompt=consent&response_type=code&client_id={google_client_id}&scope=openid%20email%20profile&access_type=offline"
    print(google_auth_url)
    return redirect(google_auth_url)


class GoogleLoginCallback(APIView):
    def get(self, request, *args, **kwargs):
        code = request.GET.get("code")
        if code is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        token_endpoint_url = urljoin("http://localhost:8000", reverse("google_login"))
        response = requests.post(url=token_endpoint_url, data={"code": code})

        return Response(response.json(), status=status.HTTP_200_OK)


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://127.0.0.1:8000/api/v1/auth/google/callback/"
    client_class = OAuth2Client


class QuestionsCresteListAPIView(ListCreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializers
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_active', 'user'] 
    search_fields = ['title', 'question']
    ordering_fields = ['id', 'created_at']
    # def get_queryset(self):
    #     return Questions.objects.prefetch_related('answers').all()


class QuestionsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializers
    permission_classes = [permissions.IsAuthenticated, Isowner]
    def get_queryset(self):
        return Questions.objects.prefetch_related('answers').all()




class AnswerCresteListAPIView(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializers
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_active', 'user'] 
    search_fields = ['answer']
    ordering_fields = ['id', 'created_at']
    

class AnswerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializers
    permission_classes = [permissions.IsAuthenticated, Isowner]
    