import streamlit as st
import json
import time
import requests
from bs4 import BeautifulSoup

# Page Layout Configuration
st.set_page_config(page_title="Live Game Redeem Codes", page_icon="🎁", layout="centered")

# Custom Title Header
st.title("🎁 Live Game Redeem Code Tracker")
st.caption("Free Fire & Roblox Daily Working Codes (Auto-Updated)")

# Top Refresh Button & Info
col_ref1, col_ref2 = st.columns([3, 1])
with col_ref1:
    st.info("💡 **Tip:** 'Unlock Code' பட்டனை அமுத்தி 10 செகண்ட் காத்திருந்தால் கோடு தெரியும்!")
with col_ref2:
    if st.button("🔄 Refresh Codes", use_container_width=True):
        st.rerun()

# Read Data from JSON
def load_codes():
    try:
        with open("codes.json", "r") as f:
            return json.load(f)
    except Exception as e:
        return [
            {
                "game": "Free Fire",
                "code": "FF9MJ3939615",
                "reward": "Exclusive Skin & Diamonds",
                "status": "Active"
            },
            {
                "game": "Roblox",
                "code": "SPIDERCOLA",
                "reward": "Spider Cola Shoulder Pet",
                "status": "Active"
            }
        ]

codes_data = load_codes()

st.markdown("---")

# Display Codes List
if codes_data:
    for index, item in enumerate(codes_data):
        game_name = item.get("game", "Game")
        code_val = item.get("code", "N/A")
        reward_info = item.get("reward", "Free Rewards")
        status_info = item.get("status", "Active")

        # Session state key for each code timer
        unlocked_key = f"unlocked_{index}"
        if unlocked_key not in st.session_state:
            st.session_state[unlocked_key] = False

        # Card Container
        with st.container():
            col1, col2 = st.columns([3, 1.2])
            
            with col1:
                st.markdown(f"### 🎮 **{game_name}**")
                st.write(f"🎁 **Reward:** {reward_info}")
                
                # Check if code is unlocked
                if st.session_state[unlocked_key]:
                    st.code(code_val, language="text")
                else:
                    st.code("••••••••••••", language="text")
                
            with col2:
                st.write("")
                if status_info == "Active":
                    st.success("🟢 Active")
                else:
                    st.error("🔴 Expired")
                
                # Unlock Button & 10-Second Timer Logic
                if not st.session_state[unlocked_key] and status_info == "Active":
                    if st.button("🔓 Unlock Code", key=f"btn_{index}", use_container_width=True):
                        # Countdown Timer
                        timer_placeholder = st.empty()
                        for seconds_left in range(10, 0, -1):
                            timer_placeholder.warning(f"⏳ {seconds_left} விநாடிகள்...")
                            time.sleep(1)
                        
                        timer_placeholder.empty()
                        st.session_state[unlocked_key] = True
                        st.rerun()

        st.markdown("---")
else:
    st.warning("தற்போது எந்தக் கோட்களும் கிடைக்கவில்லை. சிறிது நேரம் கழித்து மீண்டும் முயற்சிக்கவும்.")
