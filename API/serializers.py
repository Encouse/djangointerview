from rest_framework import serializers
from .models import Interview, Question, Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
    def save(self):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        answer_set = AnswerSerializer(many = True)
        model = Question
        fields = ['interview', 'text', 'type','answer_set']



class InterviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        question_set = QuestionSerializer(many = True)
        model = Interview
        fields = ('name','description','start_date','end_date','question_set')
