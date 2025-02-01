from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "question_hi", "question_bn")
    search_fields = ("question", "question_hi", "question_bn")
    list_filter = ("question",)
    fieldsets = (
        ("English", {"fields": ("question", "answer")}),
        ("Hindi", {"fields": ("question_hi", "answer_hi")}),
        ("Bengali", {"fields": ("question_bn", "answer_bn")}),
    )
