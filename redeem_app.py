import datetime
import json
import random
import time
import streamlit as st

# Page Config
st.set_page_config(
    page_title="Ultimate Redeem Code Hub", page_icon="🎁", layout="centered"
)

# Custom Styling
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
        border: 1px solid rgba(255, 215, 0, 0.4);
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
        margin-bottom: 20px;
    }
    .winner-count {
        font-size: 26px;
        font-weight: bold;
        color: #00f2fe;
    }
    .game-card {
        background: rgba(255, 255, 255, 0.05);
        border-left: 5px solid #ff8c00;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Title
st.markdown(
    '<div class="title-box">🎁 DAILY REAL REDEEM CODE HUB</div>',
    unsafe_allow_html=True,
)
st.caption(
    "🔥 Free Fire | Google Play | Roblox — Refreshes Automatically Daily!"
)

# Daily 1 Real Winner Logic State
if "last_reset_day" not in st.session_state:
    st.session_state["last_reset_day"] = datetime.datetime.now().day
    st.session_state["is_claimed_today"] = False

if st.session_state["last_reset_day"] != datetime.datetime.now().day:
    st.session_state["last_reset_day"] = datetime.datetime.now().day
    st.session_state["is_claimed_today"] = False

# Dynamic Winner Counter (Step Incrementing towards 1000)
now = datetime.datetime.now()
current_day = now.day
# Day-based base calculation + Step increments of 50 during the day
hour_step = (now.hour // 1) * 40
calculated_winners = min(
    1000, 120 + hour_step + ((current_day * 7) % 50) + random.randint(1, 15)
)

st.markdown(
    f"""
    <div class="winner-card">
        🎉 <b>Today's Total Claimed Rewards:</b> 
        <span class="winner-count">{calculated_winners} / 1000 Gamers</span>
        <br><small style="color: #00f2fe;">⚡ 1 Guaranteed Working Code Released Daily!</small>
    </div>
""",
    unsafe_allow_html=True,
)


# Load Codes
def load_codes():
    try:
        with open("codes.json", "r") as f:
            return json.load(f)
    except Exception as e:
        return []


codes_data = load_codes()

# Header Refresh Control
col1, col2 = st.columns([3, 1])
with col1:
    st.info(
        "💡 **Tip:** Click 'Unlock Code' & wait 10s to get your working code!"
    )
with col2:
    if st.button("🔄 Refresh", use_container_width=True):
        for k in list(st.session_state.keys()):
            if k.startswith("code_") or k.startswith("unlocked_"):
                del st.session_state[k]
        st.rerun()

st.markdown("---")

# Render all 3 categories (Free Fire, Google Play, Roblox)
if codes_data:
    for index, item in enumerate(codes_data):
        game_name = item.get("game", "Game")
        code_list = item.get("codes", ["N/A"])
        reward_info = item.get("reward", "Free Rewards")
        status_info = item.get("status", "Active")

        # Pick random code from list
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
            st.markdown(f"### 🎮 **{game_name} Redeem Code**")
            st.write(f"🎁 **Reward:** {reward_info}")

            if st.session_state[unlocked_key]:
                st.code(current_code, language="text")
            else:
                st.code("••••-••••-••••-••••", language="text")

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

                    # Daily 1 Lucky Winner Check
                    if not st.session_state["is_claimed_today"]:
                        st.session_state["is_claimed_today"] = True
                        st.balloons()
                        st.success(
                            "🎉 CONGRATULATIONS! You unlocked Today's REAL"
                            " Working Redeem Code!"
                        )

                    st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# Dynamic Mass Live Feed
st.subheader("🔥 Today's Live Winners Feed")

mass_usernames = [
    "Mass_FreeFire_FF",
    "Gamer_King_FF",
    "Dharsh_FF_Pro",
    "Roblox_Mass_Gamer",
    "GooglePlay_Winner_99",
    "Headshot_King_Tamil",
    "Killer_Boy_2026",
    "Pro_FreeFire_Player",
    "Roblox_Master_007",
    "Diamond_Hunter_FF",
    "FreeFire_Boss_Tamil",
    "Shadow_Gamer_FF",
    "PlayStore_King_100",
    "Tamil_Gamer_Official",
]

sample_winners = random.sample(mass_usernames, 6)

for user in sample_winners:
    mins = random.randint(1, 25)
    code_type = random.choice(["Free Fire Code", "Google Play ₹100", "Roblox Pet Code"])
    st.caption(f"✅ **{user}** successfully claimed **{code_type}** ({mins} mins ago)")
