import pytest
from faq_app.models import FAQ

@pytest.mark.django_db
def test_faq_model():
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework.",
    )
    assert faq.question == "What is Django?"
    assert faq.answer == "Django is a web framework."
    assert faq.get_translated_text("hi")["question"]  # Ensure translation method works
