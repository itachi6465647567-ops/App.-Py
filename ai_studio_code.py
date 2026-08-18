import streamlit as st
from google import genai
from gtts import gTTS
import os

# 1. Setup and API Configuration
# Note: Using the specific model name and API key provided in the requirements
API_KEY = "AQ.Ab8RN6IpqRKjfpIMs03OzZeTf-ze6xWsgoSTEzw7Y3znd2CCjw"
MODEL_ID = "gemini-1.5-flash"


# Initialize the Gemini Client
client = genai.Client(api_key=API_KEY)

# 2. User Interface (Streamlit)
st.set_page_config(page_title="🎙️ AI Voice Wiki Assistant", layout="centered")

st.title("🎙️ AI Voice Wiki Assistant")
st.write("""
Welcome, Student! Type any topic you want to learn about below. 
The AI will give you a simple 3-point summary and read it out loud for you!
""")

# Input field for the student
user_query = st.text_input("What would you like to learn about?", placeholder="e.g., Explain Photosynthesis")

# 3. App Logic & Integration
if st.button("Get Answer & Voice"):
    if user_query.strip() == "":
        st.warning("Please enter a question first!")
    else:
        with st.spinner("Gemini is thinking and preparing your audio..."):
            try:
                # Gemini AI Integration
                # We prompt the AI specifically for 3 bullet points as requested
                prompt = f"Explain the following topic for a student in exactly 3 short, simple bullet points: {user_query}"
                
                response = client.models.generate_content(
                    model=MODEL_ID,
                    contents=prompt
                )
                
                answer_text = response.text

                # Display the text answer
                st.subheader("Summary")
                st.write(answer_text)

                # 4. Text-to-Speech (gTTS Integration)
                # We clean the text slightly (removing asterisks) for better voice clarity
                audio_text = answer_text.replace("*", "") 
                
                tts = gTTS(text=audio_text, lang='en', slow=False)
                audio_file = "response.mp3"
                tts.save(audio_file)

                # Embed and play the audio
                st.audio(audio_file, format="audio/mp3")
                
                # Success message
                st.success("Audio generated successfully!")

            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.info("Note: If the model name 'gemini-2.5-flash' is not yet released in your region, try changing it to 'gemini-1.5-flash' in the code.")

# Footer
st.markdown("---")
st.caption("Powered by Google Gemini AI & gTTS")
