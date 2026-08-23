import streamlit as st
import json
import time
import datetime
import random

# Page Config & Custom Styling
st.set_page_config(page_title="Pro Gaming Redeem Hub", page_icon="🎮", layout="centered")

# Custom CSS for Beautiful UI
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #ffffff;
    }
    .title-box {
        background: linear-gradient(90deg, #ff8c00, #e52e71);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 32px;
        font-weight: 900;
        text-align: center;
        margin-bottom: 5px;
    }
    .winner-card {
        background: rgba(255, 255, 255, 0.07);
        border: 1px solid rgba(255, 215, 0, 0.3);
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }
    .winner-count {
        font-size: 24px;
        font-weight: bold;
        color: #00f2fe;
    }
    .game-card {
        background: rgba(255, 255, 255, 0.05);
        border-left: 4px solid #00f2fe;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Title Section
st.markdown('<div class="title-box">🎮 ULTIMATE GAMING REDEEM CODES</div>', unsafe_allow_html=True)
st.caption("✨ 100% Working Daily Live Redeem Codes")

# Dynamic Winner Counter
now = datetime.datetime.now()
base_winners = 42 + (now.hour * 2) + random.randint(1, 4)

st.markdown(f"""
    <div class="winner-card">
        🔥 <b>Today's Claimed Rewards:</b> 
        <span class="winner-count">{base_winners} Gamers</span>
        <br><small style="color: #4facfe;">⚡ Real codes available in database!</small>
    </div>
""", unsafe_allow_html=True)

# Function to load codes safely from JSON
@st.cache_data
def load_codes():
    try:
        with open("codes.json", "r") as f:
            return json.load(f)
    except Exception as e:
        return []

codes_data = load_codes()

# 🔍 SEARCH BAR COMPONENT
st.markdown("### 🔍 Search Your Game Codes")
search_query = st.text_input("Enter Game Name or Keyword (e.g., Free Fire, Roblox, Diamonds)", "").strip().lower()

col1, col2 = st.columns([3, 1])
with col1:
    st.info("💡 **Tip:** Click 'Unlock Code' & wait 10s to reveal your unique working code!")
with col2:
    if st.button("🔄 Refresh", use_container_width=True):
        for k in list(st.session_state.keys()):
            if k.startswith("code_") or k.startswith("unlocked_"):
                del st.session_state[k]
        st.rerun()

st.markdown("---")

# Filter codes based on Search Query
filtered_data = []
if codes_data:
    for item in codes_data:
        game_name = item.get("game", "")
        reward_info = item.get("reward", "")
        if search_query in game_name.lower() or search_query in reward_info.lower():
            filtered_data.append(item)

# Render Game Code Cards
if filtered_data:
    for index, item in enumerate(filtered_data):
        game_name = item.get("game", "Game")
        code_list = item.get("codes", ["N/A"])
        reward_info = item.get("reward", "Free Rewards")
        status_info = item.get("status", "Active")

        # Pick a randomized code from codes.json array
        code_key = f"code_{game_name}_{index}"
        if code_key not in st.session_state:
            st.session_state[code_key] = random.choice(code_list)

        current_code = st.session_state[code_key]

        unlocked_key = f"unlocked_{game_name}_{index}"
        if unlocked_key not in st.session_state:
            st.session_state[unlocked_key] = False

        st.markdown(f'<div class="game-card">', unsafe_allow_html=True)
        c1, c2 = st.columns([3, 1.2])
        
        with c1:
            st.markdown(f"### 🎯 **{game_name}**")
            st.write(f"🎁 **Reward:** {reward_info}")
            
            if st.session_state[unlocked_key]:
                st.code(current_code, language="text")
                st.success("🎉 Code Unlocked! Copy and redeem in official site.")
            else:
                st.code("••••-••••-••••", language="text")
            
        with c2:
            st.write("")
            if status_info == "Active":
                st.success("🟢 Active")
            else:
                st.error("🔴 Expired")
            
            if not st.session_state[unlocked_key] and status_info == "Active":
                if st.button("🔓 Unlock Code", key=f"btn_{game_name}_{index}", use_container_width=True):
                    timer_placeholder = st.empty()
                    for seconds_left in range(10, 0, -1):
                        timer_placeholder.warning(f"⏳ Unlocking in {seconds_left}s...")
                        time.sleep(1)
                    
                    timer_placeholder.empty()
                    st.session_state[unlocked_key] = True
                    st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.warning("❌ No matching codes found! Try searching for 'Free Fire' or 'Roblox'.")

st.markdown("---")

# Recent Live Feed
st.subheader("⚡ Live Winner Feed")
fake_users = ["Tamil_Gamer_**88", "Pro_FreeFire_**12", "Roblox_King_**99", "FF_Master_**07", "Dark_Ninja_**34"]
for user in fake_users:
    st.caption(f"✅ **{user}** just unlocked a code ({random.randint(1, 10)} mins ago)")
