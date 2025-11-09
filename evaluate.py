from openai import OpenAI
import os, json
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def evaluate_response(response_text):
    with open("prompts/teach_ai_prompt.txt") as f:
        system_prompt = f.read()

    prompt = system_prompt.replace("{{response_text}}", response_text)

    result = client.responses.create(
    model="gpt-3.5-turbo",
    input=prompt
)


    try:
        scores = json.loads(result.output_text)
    except Exception:
        scores = {"error": "Could not parse LLM output as JSON."}

    return scores
