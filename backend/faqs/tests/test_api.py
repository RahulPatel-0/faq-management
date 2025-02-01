import pytest
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_faq_api():
    client = APIClient()
    response = client.get(reverse("faq-list"))  # Use API URL name
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure response is a list
