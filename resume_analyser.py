from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import json

load_dotenv(r"C:\Users\Tanul\OneDrive\Desktop\intern\DAY5\api.env")

apikey=os.getenv("gemini_api_key")

if apikey is None:
    raise ValueError("API key missing")

client=genai.Client(api_key=apikey)

config=types.GenerateContentConfig(
    temperature=0.2,
    max_output_tokens=1500,
    response_mime_type="application/json",
    system_instruction="""
    You are an expert technical recruiter.

    Your job is to analyse resumes.

    Rules:
    - Do not improve the resume
    - Do not rewrite the resume
    - Extract information only

    Return ONLY valid JSON.

    JSON structure:

    {
        "skills":[],
        "projects":[],
        "experience":"",
        "strengths":[],
        "weaknesses":[],
        "missing_sections":[]
    }
    """
)

def analyse(resume_text):
    prompt=f"""
    Analyse the following resume:
    {resume_text}
    """

    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=config
    )

    raw=response.text

    print("\nRAW OUTPUT FROM GEMINI:")
    print(raw)

    try:
        result=json.loads(raw)

    except json.JSONDecodeError:
        print("JSON conversion failed")
        return None

    with open("analysis.json","w",encoding="utf-8") as file:
        json.dump(
            result,
            file,
            indent=4,
            ensure_ascii=False
        )

    return result