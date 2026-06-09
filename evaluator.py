from google import genai
from google.genai import types
import os 
import json 
from  dotenv import load_dotenv

load_dotenv(r"C:\Users\Tanul\OneDrive\Desktop\intern\DAY5\api.env")
apikey=os.getenv("gemini_api_key")
client=genai.Client(api_key=apikey)

config=types.GenerateContentConfig(
    temprature=0.6,
    max_output_tokens=2000,
    response="application/json",

    system_instruction=""" You are a resume evaluator.

    Compare the original analysis
    with the improved resume.

    Check if weaknesses were fixed.

    Return JSON only.

    Format:

    {
        "fixed_problems":[],
        "remaining_problems":[],
        "improvement_summary":"",
        "old_score":0,
        "new_score":0
    }

    """
)
def evaluate_resume(
        analysis,
        improved
):

    prompt=f"""

    Original analysis:

    {analysis}


    Improved resume:

    {improved}


    Compare them.

    """


    response=client.models.generate_content(

        model="gemini-2.5-flash",

        contents=prompt,

        config=config
    )


    result=json.loads(
        response.text
    )


    with open(
        "comparison.json",
        "w"
    ) as file:


        json.dump(
            result,
            file,
            indent=4
        )


    return result


