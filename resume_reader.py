import os 
import fitz
def read_text(file):
    with open(file,"r",encoding="utf-8") as file:
        text=file.read()
    return text

# now that the content has been extracted now we have to clean the content such that i can
# be read and understood by the Ai properly

def clean_text(text):
    lines=text.split('\n')
    cleaned_lines=[]
    for line in lines:
        if line:
            cleaned_lines.append(line)
    final_text="\n".join(cleaned_lines)

    return final_text

def read_pdf(file):
    document=fitz.open(file)
    text=""
    for page in document:
        text+=page.get_text()
    document.close()
    return text

def extracting_resume(file):
    extension=os.path.splitext(file)[1]

    if extension==".txt":
        raw_text=read_text(file)
    
    elif extension==".pdf":
        raw_text=read_pdf(file)

    else:
        return "unsported file "
    
    cleaned=clean_text(raw_text)

    return cleaned
