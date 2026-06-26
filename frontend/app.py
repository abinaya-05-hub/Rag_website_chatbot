import streamlit as st
import requests

# ---------------------------------------
# PAGE CONFIG
# ---------------------------------------

st.set_page_config(
    page_title="RAG Website Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------
# SESSION STATE
# ---------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "website_indexed" not in st.session_state:
    st.session_state.website_indexed = False

if "url" not in st.session_state:
    st.session_state.url = ""

# ---------------------------------------
# SIDEBAR
# ---------------------------------------

with st.sidebar:

    st.title("🌐 Website Indexer")

    url = st.text_input(
        "Enter Website URL",
        value=st.session_state.url,
        placeholder="https://python.org"
    )

    if st.button("📥 Index Website"):

        if url == "":
            st.warning("Please enter a website URL.")

        else:

            with st.spinner("Indexing website..."):

                response = requests.post(
                    "http://127.0.0.1:8000/index",
                    params={
                        "url": url
                    }
                )

            if response.status_code == 200:

                result = response.json()

                st.session_state.website_indexed = True
                st.session_state.url = url

                st.success("✅ Website Indexed")

                st.write(f"📄 Pages : {result['pages']}")
                st.write(f"🧩 Chunks : {result['chunks']}")

            else:

                st.error("Indexing Failed")
                st.write(response.text)

# ---------------------------------------
# MAIN PAGE
# ---------------------------------------

st.title("🤖 RAG Website Chatbot")

st.write(
    "Ask questions about any indexed website using Retrieval-Augmented Generation (RAG)."
)

st.divider()

# ---------------------------------------
# SHOW CHAT HISTORY
# ---------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------------------------
# CHAT INPUT
# ---------------------------------------

question = st.chat_input("Ask anything about the indexed website...")

if question:

    if not st.session_state.website_indexed:

        st.warning("⚠ Please index a website first.")

    else:

        # Show user message

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        # Ask backend

        with st.spinner("Thinking..."):

            response = requests.get(
                "http://127.0.0.1:8000/ask",
                params={
                    "url": st.session_state.url,
                    "question": question
                }
            )

        if response.status_code == 200:

            answer = response.json()["answer"]

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            with st.chat_message("assistant"):
                st.markdown(answer)

        else:

            st.error("Backend Error")

            st.code(response.text)