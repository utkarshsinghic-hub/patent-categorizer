import streamlit as st
from google import genai


st.set_page_config(
    page_title="Patent Categorization Tool",
    layout="wide"
)


# Gemini connection
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)


st.title("Patent Categorization Tool")

st.write(
    "AI-powered patent translation and analysis"
)


claim_text = st.text_area(
    "Paste patent claim",
    height=300
)


if st.button("Translate Claim"):

    if claim_text.strip():

        with st.spinner("Translating using Gemini..."):

            prompt = f"""
You are an expert patent translator.

Translate the following patent claim into professional English.

Rules:
- Preserve claim numbering.
- Preserve legal patent language.
- Keep technical meaning unchanged.
- Do not summarize.
- Do not add explanations.

Patent claim:

{claim_text}
"""


            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )


        st.subheader("English Translation")

        st.write(
            response.text
        )

    else:

        st.warning(
            "Please paste a patent claim first."
        )
