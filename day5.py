from resume_reader import extracting_resume
from resume_analyser import analyse
from improver import improve_resume
from evaluator import evaluate_resume

resume_text=extracting_resume(r"C:\Users\Tanul\OneDrive\Desktop\Manan Resume  (1).pdf")

analysis=analyse(resume_text)

improved=improve_resume(resume_text,analysis)

comparison=evaluate_resume(
    analysis,
    improved
)


print(comparison)
