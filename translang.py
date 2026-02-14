import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Translation Function
def translate_text(text, source_language, target_language):
    prompt = (
        f"Translate the following text from {source_language} "
        f"to {target_language}. Only return the translated text:\n\n{text}"
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# Streamlit UI
st.set_page_config(page_title="TransLingua", page_icon="🌍")
st.title("🌍 TransLingua - AI Multi-Language Translator")

text = st.text_area("Enter text to translate")

languages = [
    "English",
    "Telugu",
    "Hindi",
    "Tamil",
    "Kannada",
    "Malayalam",
    "French",
    "German",
    "Spanish"
]

source = st.selectbox("Source Language", languages)
target = st.selectbox("Target Language", languages)

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    elif source == target:
        st.warning("Source and Target languages cannot be the same.")
    else:
        with st.spinner("Translating..."):
            result = translate_text(text, source, target)
            st.success("Translation Complete ✅")
            st.write(result)

st.markdown("---")
st.caption("Built using Gemini 2.5 Flash Model 🚀")
