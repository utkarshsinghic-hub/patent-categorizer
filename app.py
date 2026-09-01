import streamlit as st

st.title("Patent Categorization Tool")

st.write(
    "My patent AI tool is working!"
)

text = st.text_area(
    "Paste patent claim"
)

if st.button("Translate"):

    st.write(
        "Translation will come here"
    )
