import datetime
import json
import random
import time
import streamlit as st

# Page Config & Custom Styling
st.set_page_config(
    page_title="Pro Gaming Redeem Hub", page_icon="🎮", layout="centered"
)

st.markdown(
    """
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
        font-size: 26px;
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
""",
    unsafe_allow_html=True,
)

# Title Section
st.markdown(
    '<div class="title-box">🎮 ULTIMATE GAMING REDEEM CODES</div>',
    unsafe_allow_html=True,
)
st.caption("✨ 100% Working Daily Live Redeem Codes")

# 1 to 1000 Dynamic Winner Counter Logic (Increases with time of day)
now = datetime.datetime.now()
total_seconds_today = (
    now.hour * 3600 + now.minute * 60 + now.second
)  # 0 to 86400
calculated_winners = int((total_seconds_today / 86400) * 980) + random.randint(
    1, 20
)
calculated_winners = min(1000, max(1, calculated_winners))  # Cap between 1 and 1000

st.markdown(
    f"""
    <div class="winner-card">
        🔥 <b>Today's Claimed Rewards:</b> 
        <span class="winner-count">{calculated_winners} / 1000 Players</span>
        <br><small style="color: #4facfe;">⚡ Real working codes released today!</small>
    </div>
""",
    unsafe_allow_html=True,
)


# Function to load codes from JSON
def load_codes():
    try:
        with open("codes.json", "r") as f:
            return json.load(f)
    except Exception as e:
        return []


codes_data = load_codes()

# Header Controls: Info & Refresh
col1, col2 = st.columns([3, 1])
with col1:
    st.info(
        "💡 **Tip:** Click 'Unlock Code' & wait 10s to reveal your unique"
        " working code!"
    )
with col2:
    if st.button("🔄 Refresh", use_container_width=True):
        for k in list(st.session_state.keys()):
            if k.startswith("code_") or k.startswith("unlocked_"):
                del st.session_state[k]
        st.rerun()

st.markdown("---")

# Render Game Code Cards
if codes_data:
    for index, item in enumerate(codes_data):
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

        st.markdown('<div class="game-card">', unsafe_allow_html=True)
        c1, c2 = st.columns([3, 1.2])

        with c1:
            st.markdown(f"### 🎯 **{game_name}**")
            st.write(f"🎁 **Reward:** {reward_info}")

            if st.session_state[unlocked_key]:
                st.code(current_code, language="text")
                st.success(
                    "🎉 Code Unlocked! Copy and redeem in official site."
                )
            else:
                st.code("••••-••••-••••", language="text")

        with c2:
            st.write("")
            if status_info == "Active":
                st.success("🟢 Active")
            else:
                st.error("🔴 Expired")

            if not st.session_state[unlocked_key] and status_info == "Active":
                if st.button(
                    "🔓 Unlock Code",
                    key=f"btn_{game_name}_{index}",
                    use_container_width=True,
                ):
                    timer_placeholder = st.empty()
                    for seconds_left in range(10, 0, -1):
                        timer_placeholder.warning(
                            f"⏳ Unlocking in {seconds_left}s..."
                        )
                        time.sleep(1)

                    timer_placeholder.empty()
                    st.session_state[unlocked_key] = True
                    st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# Dynamic Mass Winners Feed
st.subheader("🔥 Live Today's Winners Feed")

mass_usernames = [
    "Mass_FreeFire_FF",
    "Gamer_King_FF",
    "Dharsh_FF_Pro",
    "Roblox_Mass_Gamer",
    "Headshot_King",
    "Tamil_Gamer_FF",
    "Killer_Boy_2026",
    "Pro_FreeFire_Player",
    "Roblox_Master_007",
    "Diamond_Hunter_FF",
    "FreeFire_Boss_Tamil",
    "Shadow_Gamer_FF",
]

# Pick 5 random users from mass_usernames list on every render
sample_winners = random.sample(mass_usernames, 5)

for user in sample_winners:
    mins = random.randint(1, 20)
    st.caption(f"✅ **{user}** just unlocked a code ({mins} mins ago)")
