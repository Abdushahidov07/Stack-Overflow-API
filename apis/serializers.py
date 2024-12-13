from rest_framework import serializers
from .models import Answer, Questions


# class QuestionsSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Questions
#         fields = ['title','question','created_at', 'user']



class AnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question','answer','created_at','user']


class QuestionsSerializers(serializers.ModelSerializer): 
    answers = AnswerSerializers(many=True, read_only=True) 

    class Meta: 
        model = Questions 
        fields = ['id','user', 'title', 'question','is_active','created_at','answers']