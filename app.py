import streamlit as st
import tempfile
import os

from resume_reader import extracting_resume
from resume_analyser import analyse
from improver import improve_resume


st.title("AI Resume Improver")


uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf","txt"]
)


if uploaded_file:


    st.success(
        "Resume uploaded successfully"
    )


    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=uploaded_file.name
    ) as temp:


        temp.write(
            uploaded_file.read()
        )


        file_path=temp.name



    if st.button("Analyze Resume"):


        with st.spinner(
            "Extracting resume..."
        ):


            resume_text=extracting_resume(
                file_path
            )



        st.subheader(
            "Extracted Resume"
        )


        st.text_area(
            "Resume Text",
            resume_text,
            height=200
        )



        with st.spinner(
            "Analyzing resume..."
        ):


            analysis=analyse(
                resume_text
            )



        st.subheader(
            "Resume Analysis"
        )


        st.json(
            analysis
        )



        with st.spinner(
            "Improving resume..."
        ):


            improved=improve_resume(
                resume_text,
                analysis
            )



        st.subheader(
            "Improved Resume"
        )


        st.json(
            improved
        )



        os.remove(
            file_path
        )