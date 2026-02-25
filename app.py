from dotenv import load_dotenv
import streamlit as st
import os
from google import genai
from PIL import Image

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, image, prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",  # ✅ correct model
        contents=[
            input_text if input_text else "",
            prompt,
            image
        ]
    )
    return response.text


st.set_page_config(page_title="Civil Engineering Insight Studio", page_icon="🏗️")

st.header("🏗️ Civil Engineering Insight Studio")

st.markdown("""
### Analyze Civil Engineering Structures with AI
Upload an image of any civil engineering structure to get detailed insights about:
- Structure type and purpose
- Materials used in construction
- Dimensions and scale
- Construction methods
- Notable features and engineering challenges
""")

input_text = st.text_input(
    "Input Prompt:",
    placeholder="e.g., Analyze this bridge structure..."
)

uploaded_file = st.file_uploader(
    "Choose an image...",
    type=["jpg", "jpeg", "png"]
)

image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("🔍 Describe Structure")

input_prompt = """
You are an expert civil engineer analyzing structures. Based on the provided image,
please provide a comprehensive description including:

1. Structure Type
2. Materials Used
3. Dimensions & Scale
4. Construction Methods
5. Notable Features
6. Engineering Challenges
7. Condition Assessment

Be detailed and technical in your analysis.
"""

if submit:
    if image is not None:
        try:
            with st.spinner("Analyzing structure... Please wait..."):
                response = get_gemini_response(
                    input_text,
                    image,  # ✅ Pass PIL image
                    input_prompt
                )

            st.subheader("📋 Analysis Results")
            st.write(response)
            st.success("✅ Analysis completed successfully!")

        except Exception as e:
            st.error(f"⚠️ An error occurred: {str(e)}")
    else:
        st.warning("⚠️ Please upload an image before submitting.")

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>Built with Streamlit & Google Gemini AI</div>",
    unsafe_allow_html=True
)