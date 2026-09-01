import streamlit as st
from google import genai


st.set_page_config(
    page_title="Patent Categorization Tool",
    layout="wide"
)


client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)


st.title("Patent Categorization Tool")

st.subheader("Patent Translation")


claims = st.text_area(
    "Paste Patent Claims",
    height=300
)


if st.button("Translate Claims"):

    if claims.strip():

        with st.spinner("Translating patent claims..."):

            prompt = f"""
You are an expert patent translator.

Translate the following patent claims into professional English.

Rules:
- Preserve claim numbering.
- Preserve patent legal terminology.
- Maintain "comprising", "wherein", "configured to" style.
- Do not summarize.
- Do not add explanations.
- Keep technical meaning unchanged.

Patent Claims:

{claims}
"""


            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )


        st.subheader(
            "English Translation"
        )

        st.write(
            response.text
        )


    else:

        st.warning(
            "Please paste patent claims."
        )
