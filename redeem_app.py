import streamlit as st
import json
import time
import datetime
import random
import requests
from bs4 import BeautifulSoup

# Streamlit Page Config
st.set_page_config(page_title="Free Fire & Roblox Redeem Code Tracker", page_icon="🎮", layout="centered")

# Custom CSS for Gaming UI & Background
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)), 
                    url('https://images.alphacoders.com/100/thumb-1920-1004586.jpg') no-repeat center center fixed;
        background-size: cover;
    }
    .title-text {
        font-size: 30px;
        font-weight: bold;
        color: #ffb703;
        text-align: center;
        margin-bottom: 5px;
    }
    .winner-box {
        background-color: rgba(255, 183, 3, 0.15);
        border: 1px solid #ffb703;
        border-radius: 10px;
        padding: 12px;
        text-align: center;
        margin-bottom: 15px;
    }
    .winner-count {
        font-size: 22px;
        font-weight: bold;
        color: #00ffcc;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-text">🎁 FREE FIRE & ROBLOX REDEEM CODES</div>', unsafe_allow_html=True)
st.caption("🔥 Live Daily Codes - Refreshes Automatically Every 10 Minutes!")

# Daily Reset Logic for 1 Real Winner
if "last_reset_day" not in st.session_state:
    st.session_state["last_reset_day"] = datetime.datetime.now().day
    st.session_state["is_claimed_today"] = False

if st.session_state["last_reset_day"] != datetime.datetime.now().day:
    st.session_state["last_reset_day"] = datetime.datetime.now().day
    st.session_state["is_claimed_today"] = False

# Dynamic Winner Counter Logic (Fake Auto-Incrementing Counter)
now = datetime.datetime.now()
# 30 பிளஸ் அன்றைய மணி நேரத்தை வச்சு ஒரு ஃபேக் கவுண்ட் கணக்கிடும் (நேரம் ஆக ஆக கூடும்)
base_winners = 25 + (now.hour * 3) + random.randint(1, 5)

st.markdown(f"""
    <div class="winner-box">
        🎉 <b>Today's Real Reward Claimed Users:</b> 
        <span class="winner-count">{base_winners} Players</span>
        <br><small style="color: #aaa;">(1 Guaranteed Working Code Released Every Day!)</small>
    </div>
""", unsafe_allow_html=True)

# Read Codes from JSON
def load_codes():
    try:
        with open("codes.json", "r") as f:
            return json.load(f)
    except:
        return [
            {"game": "Free Fire", "code": "FF9MJ3939615", "reward": "Exclusive Diamonds & Skins", "status": "Active"},
            {"game": "Roblox", "code": "SPIDERCOLA", "reward": "Spider Cola Pet", "status": "Active"}
        ]

codes_data = load_codes()

# Header Controls: Refresh & Info
col1, col2 = st.columns([3, 1])
with col1:
    st.info("💡 **Tip:** Click 'Unlock Code' to wait 10 seconds and get working codes!")
with col2:
    if st.button("🔄 Refresh", use_container_width=True):
        st.rerun()

st.markdown("---")

# Display Game Code Cards
if codes_data:
    for index, item in enumerate(codes_data):
        game_name = item.get("game", "Game")
        code_val = item.get("code", "N/A")
        reward_info = item.get("reward", "Free Rewards")
        status_info = item.get("status", "Active")

        unlocked_key = f"unlocked_{index}"
        if unlocked_key not in st.session_state:
            st.session_state[unlocked_key] = False

        with st.container():
            c1, c2 = st.columns([3, 1.2])
            
            with c1:
                st.markdown(f"### 🎮 **{game_name}**")
                st.write(f"🎁 **Reward:** {reward_info}")
                
                # Show Code if unlocked
                if st.session_state[unlocked_key]:
                    st.code(code_val, language="text")
                else:
                    st.code("••••••••••••", language="text")
                
            with c2:
                st.write("")
                if status_info == "Active":
                    st.success("🟢 Active")
                else:
                    st.error("🔴 Expired")
                
                # Unlock Button Logic with 10s Timer
                if not st.session_state[unlocked_key] and status_info == "Active":
                    if st.button("🔓 Unlock Code", key=f"btn_{index}", use_container_width=True):
                        timer_placeholder = st.empty()
                        for seconds_left in range(10, 0, -1):
                            timer_placeholder.warning(f"⏳ Please wait... {seconds_left} seconds")
                            time.sleep(1)
                        
                        timer_placeholder.empty()
                        st.session_state[unlocked_key] = True
                        
                        # Daily 1 Guaranteed Real Winner Logic
                        if not st.session_state["is_claimed_today"]:
                            st.session_state["is_claimed_today"] = True
                            st.balloons()
                            st.success("🎉 CONGRATULATIONS! You unlocked Today's REAL Working Redeem Code!")
                        
                        st.rerun()

        st.markdown("---")

# Recent Winners Ticker (Social Proof)
st.subheader("🔥 Recent Winners Feed")
fake_users = [
    "User_Tamil_**91", "FreeFire_Pro_**02", "Roblox_King_**45", 
    "Gamer_Tamil_**11", "FF_Lover_**88"
]
for user in fake_users:
    mins = random.randint(1, 15)
    st.caption(f"✅ **{user}** successfully claimed a code ({mins} mins ago)")
