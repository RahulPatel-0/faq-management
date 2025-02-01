from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    question_translated = serializers.SerializerMethodField()
    answer_translated = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'question_translated', 'answer_translated']

    def get_question_translated(self, obj):
        lang = self.context.get('lang', 'en')  # Default to 'en' if no lang param is passed
        return obj.get_translated_question(lang)

    def get_answer_translated(self, obj):
        lang = self.context.get('lang', 'en')  # Default to 'en' if no lang param is passed
        return obj.get_translated_answer(lang)
