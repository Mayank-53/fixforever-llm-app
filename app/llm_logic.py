from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def predict_issue_reason(issue: str) -> str:
    prompt = (
    f"The user reports a laptop issue: \"{issue}\".\n"
    f"In 15 words or fewer, describe the most likely technical reason."
)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a technical support assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50,
            temperature=0.7
        )
        reason = response.choices[0].message.content.strip()
        return reason
    except Exception as e:
        return f"Error: {str(e)}"
