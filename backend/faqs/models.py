from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  # WYSIWYG support
    question_hi = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        translator = Translator()
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest="hi").text
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, dest="hi").text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest="bn").text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, dest="bn").text

        super().save(*args, **kwargs)

    def get_translated_text(self, lang="en"):
        if lang == "hi":
            return {"question": self.question_hi or self.question, "answer": self.answer_hi or self.answer}
        elif lang == "bn":
            return {"question": self.question_bn or self.question, "answer": self.answer_bn or self.answer}
        return {"question": self.question, "answer": self.answer}  # Fallback to English

    def __str__(self):
        return self.question
