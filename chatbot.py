import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are an AI governance expert assistant specialising in:
- The EU AI Act and its risk tiers
- GDPR and data subject rights
- ISO 42001 AI management systems
- NIST AI Risk Management Framework
- Responsible AI principles

When answering questions:
- Always cite the relevant article, clause, or section
- Give clear plain-English explanations
- Keep answers concise but accurate
- If something falls outside AI governance, politely redirect the user
- Always add a disclaimer that your answers are for guidance only and not legal advice"""

def ask_chatbot(question: str) -> dict:
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question}
            ]
        )
        return {
            "question": question,
            "answer": response.choices[0].message.content,
            "disclaimer": "This response is for guidance and portfolio demonstration only. It does not constitute legal advice."
        }
    except Exception as e:
        return {
            "question": question,
            "answer": f"Error: {str(e)}",
            "disclaimer": ""
        }