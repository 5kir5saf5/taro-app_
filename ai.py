import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

def interpret(question, cards):
    prompt = f"""
Ты таролог. Сделай расклад.

Вопрос: {question}

Карты:
{cards}

Дай:
- краткий смысл
- объяснение
- совет
"""

    response = model.generate_content(prompt)
    return response.text