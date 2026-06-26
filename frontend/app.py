import streamlit as st
import requests

st.set_page_config(
    page_title="RAG Website Chatbot",
    page_icon="🤖"
)

st.title("🤖 RAG Website Chatbot")
st.write("Chat with any website using RAG.")

# ----------------------------
# WEBSITE URL
# ----------------------------

url = st.text_input(
    "Enter Website URL",
    placeholder="https://example.com"
)

# ----------------------------
# INDEX WEBSITE
# ----------------------------

if st.button("Index Website"):

    if not url:
        st.warning("Please enter a website URL.")

    else:

        with st.spinner("Indexing Website..."):

            response = requests.post(
                "http://127.0.0.1:8000/index",
                params={
                    "url": url
                }
            )

        if response.status_code == 200:

            result = response.json()

            st.success(result["message"])
            st.write(f"Pages Indexed : {result['pages']}")
            st.write(f"Chunks Created : {result['chunks']}")

        else:

            st.error("Indexing Failed")
            st.write(response.text)

# ----------------------------
# ASK QUESTION
# ----------------------------

st.divider()

question = st.text_input(
    "Ask a Question"
)

if st.button("Ask"):

    if not url:

        st.warning("Please enter the website URL first.")

    elif not question:

        st.warning("Please enter a question.")

    else:

        with st.spinner("Generating Answer..."):

            response = requests.get(
                "http://127.0.0.1:8000/ask",
                params={
                    "url": url,
                    "question": question
                }
            )

        if response.status_code == 200:

            result = response.json()

            st.subheader("Answer")

            st.success(result["answer"])

        else:

            st.error("Failed to generate answer")
            st.write(response.text)