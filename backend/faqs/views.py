from django.http import JsonResponse
from .models import FAQ

def faq_list(request):
    lang = request.GET.get("lang", "en")  # Default to English
    faqs = FAQ.objects.all()
    
    faq_data = []
    for faq in faqs:
        translated = faq.get_translated_text(lang)
        faq_data.append({
            "id": faq.id,
            "question": translated["question"],
            "answer": translated["answer"],
        })
    
    return JsonResponse(faq_data, safe=False)
