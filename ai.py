from dotenv import load_dotenv
load_dotenv()
import os
import json
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
)

def analyze_resume(resume_text, user_goal):
    prompt = f"""
You are a senior recruiter and career coach.

User goal: "{user_goal}"

STRICT RULES:
- Extract only relevant skills for this goal
- REMOVE irrelevant tools (excel for backend, etc)
- Identify real gaps
- Generate roadmap only for missing fields
- Make output DIFFERENT based on goal

Return only JSON:
{{
"skills": [],
"missing_skills": [],
"roadmap": [],
"interview_questions": []
}}

Resume:
{resume_text}
"""
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        return {"error": str(e)}