import streamlit as st
import time

# Page Config
st.set_page_config(page_title="Elite Hacker Typer 360", page_icon="💻", layout="wide")

# Custom Styling (Matrix Hacker Theme)
st.markdown("""
    <style>
    .stApp {
        background-color: #050505;
        color: #00ff66;
        font-family: 'Courier New', Courier, monospace;
    }
    .hacker-box {
        background-color: #0a0f0d;
        border: 2px solid #00ff66;
        border-radius: 10px;
        padding: 25px;
        box-shadow: 0 0 20px rgba(0, 255, 102, 0.3);
    }
    .terminal-text {
        font-size: 16px;
        color: #00ff66;
        white-space: pre-wrap;
        word-wrap: break-word;
    }
    h1, h2, h3 {
        color: #00ff66 !important;
        text-shadow: 0 0 10px rgba(0, 255, 102, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("<h1>💻 ELITE HACKER TERMINAL</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #8b949e;'>Type anything on your keyboard below to bypass mainframe security...</p>", unsafe_allow_html=True)

    # Fake Hacker Code Database to spit out
    hacker_code_block = """
    INITIATING ROOT ACCESS... 
    BYPASSING FIREWALL [████████████] 100%
    CONNECTING TO PENTAGON MAINSERVER...
    ACCESS GRANTED: WELCOME USER_DARSH
    DECRYPTING AES-256 BIT ENCRYPTION KEYS...
    injecting payload into target subnet...
    BYPASSING TWO-FACTOR AUTHENTICATION...
    ACCESSING DATABASE: //root/secure/users/credits...
    DOWNLOAD COMPLETE. SYSTEM SECURED.
    """

    # User Input for Typing Simulator
    user_input = st.text_area("⌨️ Type here like a hacker:", height=150, placeholder="Start typing random keys rapidly...")

    if user_input:
        # Generate simulated code based on input length
        display_length = min(len(user_input) * 5, len(hacker_code_block))
        current_output = hacker_code_block[:display_length]
        
        st.markdown("### 🖥️ Live Mainframe Output:")
        st.markdown(f'<div class="hacker-box"><div class="terminal-text">{current_output}_</div></div>', unsafe_allow_html=True)
    else:
        st.markdown("### 🖥️ Live Mainframe Output:")
        st.markdown('<div class="hacker-box"><div class="terminal-text">WAITING FOR KEYBOARD INPUT..._</div></div>', unsafe_allow_html=True)

with col2:
    st.markdown("<h2>👤 AGENT PROFILE</h2>", unsafe_allow_html=True)
    
    # Hacker Face / Avatar Box (Visual Vibe)
    st.markdown("""
        <div style="background-color: #0a0f0d; border: 2px dashed #00ff66; padding: 20px; border-radius: 10px; text-align: center;">
            <h1 style="font-size: 60px; margin: 0;">🥷</h1>
            <h3 style="color: #00ff66; margin-top: 10px;">STATUS: ACTIVE</h3>
            <p style="color: #00ff66; font-size: 14px;">IP: 192.168.404.0 [SECURE]</p>
            <p style="color: #8b949e; font-size: 12px;">Anonymous Proxy Connected</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔥 TRIGGER SYSTEM OVERRIDE"):
        with st.spinner("Breaching firewall..."):
            time.sleep(1.5)
        st.success("MAINFRAME BYPASSED SUCCESSFULLY!")
