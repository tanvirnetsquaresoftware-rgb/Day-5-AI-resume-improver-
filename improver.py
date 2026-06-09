from google import genai
from google.genai import types
from dotenv import load_dotenv
import json
import os

load_dotenv(r"C:\Users\Tanul\OneDrive\Desktop\intern\DAY5\api.env")

apikey=os.getenv("gemini_api_key")

if apikey is None:
    raise ValueError("api key is missing")

client=genai.Client(api_key=apikey)

config=types.GenerateContentConfig(
    temperature=0.6,
    max_output_tokens=3000,
    response_mime_type="application/json",
    system_instruction="""
    You are an expert resume improvement specialist.

    Your job is to improve resumes using the analysis
    provided by the resume analyzer.

    Rules:
    - Do not add fake skills
    - Do not add fake experience
    - Do not add fake companies
    - Do not add fake achievements

    Improve:
    - wording
    - grammar
    - ATS keywords
    - project explanations
    - professional quality

    Return ONLY JSON.

    Format:
    {
        "improved_resume":"",
        "changes_made":[],
        "skills_improved":[],
        "sections_modified":[]
    }
    """
)

def improve_resume(resume_text,analysis):
    prompt=f"""
    Original Resume:
    {resume_text}

    Analyzer Report:
    {analysis}

    Improve the resume based on the analyzer report.
    """

    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=config
    )

    raw=response.text

    print("\nRAW IMPROVER OUTPUT:")
    print(raw)

    try:
        result=json.loads(raw)

    except json.JSONDecodeError:
        print("Improver JSON conversion failed")
        return None

    with open("improved_resume.json","w",encoding="utf-8") as file:
        json.dump(
            result,
            file,
            indent=4,
            ensure_ascii=False
        )

    return result