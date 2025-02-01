const API_URL = "http://127.0.0.1:8000/api/faqs/";

export async function fetchFAQs(lang = "en") {
  const response = await fetch(`${API_URL}?lang=${lang}`);
  return response.json();
}

export async function createFAQ(data) {
  return fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
}