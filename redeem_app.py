import streamlit as st
import json
import requests
from bs4 import BeautifulSoup

# Page Layout Configuration
st.set_page_config(page_title="Live Game Redeem Codes", page_icon="🎁", layout="centered")

# Custom Title Header
st.title("🎁 Live Game Redeem Code Tracker")
st.caption("Free Fire & Roblox Daily Working Codes (Auto-Updated)")

st.info("💡 **Tip:** கீழே உள்ள கோட்களை நேரடியாக Copy செய்து கேமில் Redeem செய்து கொள்ளுங்கள்!")

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
                "status": "Active",
                "ad_link": "https://google.com"
            }
        ]

codes_data = load_codes()

st.markdown("---")

# Display Codes List
if codes_data:
    for item in codes_data:
        game_name = item.get("game", "Game")
        code_val = item.get("code", "N/A")
        reward_info = item.get("reward", "Free Rewards")
        status_info = item.get("status", "Active")
        ad_url = item.get("ad_link", "https://google.com")

        # Visual Card Design
        with st.container():
            col1, col2 = st.columns([3, 1.2])
            
            with col1:
                st.markdown(f"### 🎮 **{game_name}**")
                st.write(f"🎁 **Reward:** {reward_info}")
                # Click to Copy Box
                st.code(code_val, language="text")
                
            with col2:
                st.write("")
                if status_info == "Active":
                    st.success("🟢 Active")
                else:
                    st.error("🔴 Expired")
                
                # AdStar / Monetization Button
                st.link_button("🚀 Extra Rewards / Ads", ad_url, use_container_width=True)

        st.markdown("---")
else:
    st.warning("தற்போது எந்தக் கோட்களும் கிடைக்கவில்லை. சிறிது நேரம் கழித்து மீண்டும் முயற்சிக்கவும்.")
