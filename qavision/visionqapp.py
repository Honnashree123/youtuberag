import os
import base64
import streamlit as st
from groq import Groq

MODEL="meta-llama/llama-4-scout-17b-16e-instruct"
MIME_MAP = {
    "image/jpeg": "image/jpeg",
    "image/png": "image/png",
    "image/webp": "image/webp",
    "image/gif": "image/gif",
}




def encode_image(uploaded_file) -> tuple[str, str]:
    mime_type = MIME_MAP.get(uploaded_file.type, "image/jpeg")
    encoded = base64.b64encode(uploaded_file.read()).decode("utf-8")
    return encoded, mime_type

def ask(client:Groq, image_b64:str, mime_type:str, question:str, history:list) -> str:
    messages = history + [
        {
            "role": "user",
            "content": [
                {
                    "type": "text", "text":question
                },
                {
                    "type": "image_url", "image_url":{"url":f"data:{mime_type};base64,{image_b64}"}
                },
            ],
        }
    ]
    response = client.chat.completions.create(model = MODEL, messages = messages)
    return response.choices[0].message.content
st.set_page_config(page_title="Vision QA")
st.title("Vision QA")

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Groq API Key", value=os.environ.get("GROQ_API_KEY", ""), type="password")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "webp", "gif"])
    if st.button("Clear chat"):
        st.session_state.messages = []
        st.rerun()
if "messages" not in st.session_state:
    st.session_state.messages = []
if "image_b64" not in st.session_state:
    st.session_state.image_b64 = None
if "mime_type" not in st.session_state:
    st.session_state.mime_type = None
if "last_file_name" not in st.session_state:
    st.session_state.last_file_name = None

if uploaded_file:
    if uploaded_file.name != st.session_state.last_file_name:
        image_b64, mime_type = encode_image(uploaded_file)
        st.session_state.image_b64 = image_b64
        st.session_state.mime_type = mime_type
        st.session_state.last_file_name = uploaded_file.name
        st.session_state.messages = []
    with st.sidebar:
        st.image(uploaded_file, caption=uploaded_file.name, use_container_width=True)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


if not uploaded_file:
    st.info("Upload an image in the sidebar to get started.")
elif not api_key:
    st.warning("Enter your Groq API key in the sidebar.")
else:
    if question := st.chat_input("Ask a question about the image…"):
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)


        with st.chat_message("assistant"):
            with st.spinner("Thinking…"):
                client = Groq(api_key=api_key)
                # Build history without image attachments (text only) for context
                history = [
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages[:-1]
                ]
                answer = ask(
                    client,
                    st.session_state.image_b64,
                    st.session_state.mime_type,
                    question,
                    history,
                )
            st.markdown(answer)


        st.session_state.messages.append({"role": "assistant", "content": answer})
