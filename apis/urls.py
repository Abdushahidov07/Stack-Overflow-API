from django.urls import path
from .views import *

urlpatterns = [
    path("questions/", QuestionsCresteListAPIView.as_view(), name='questions'),
    path('questions/<int:pk>/', QuestionsRetrieveUpdateDestroyAPIView.as_view(), name='question-detail'),
    path("answer/", AnswerCresteListAPIView.as_view(), name='answer'),
    path("answer/<int:pk>/", AnswerRetrieveUpdateDestroyAPIView.as_view(), name='answer'),
]
