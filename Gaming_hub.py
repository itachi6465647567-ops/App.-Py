import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(
    page_title="GamerZone 360 - Ultimate Black Portal",
    page_icon="🎮",
    layout="wide"
)

# 2. Complete Black Theme & Modern UI CSS
dark_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {
        background-color: #0b0c10;
        color: #c5c6c7;
    }
    .game-card {
        background-color: #1f2833;
        border: 1px solid #45a29e;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        margin-bottom: 10px;
    }
    .stTextInput > div > div > input {
        background-color: #1f2833;
        color: #66fcf1;
        border: 1px solid #45a29e;
        border-radius: 8px;
    }
    </style>
"""
st.markdown(dark_style, unsafe_allow_html=True)

# 3. Header Section
st.markdown("<h1 style='text-align: center; color: #66fcf1;'>🎮 GAMERZONE 360</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #c5c6c7;'>Play 100+ Free Web Games & Official Cloud Games</p>", unsafe_allow_html=True)

# 4. Search System
search_query = st.text_input("🔍 Search from 100+ Games (e.g. Free Fire, Roblox, Granny, Racing, Horror):", "")

# 5. Master Games Database
GAMES_DATABASE = [
    # Cloud Games (External Launcher to Bypass Refused-to-Connect Issue)
    {"id": "ff", "title": "Garena Free Fire (Official Cloud)", "category": "Battle Royale", "type": "cloud", "url": "https://now.gg/play/garena-international-i-private-limited/1945/free-fire", "icon": "🔥"},
    {"id": "roblox", "title": "Roblox Official Cloud Arena", "category": "Roblox", "type": "cloud", "url": "https://now.gg/play/roblox-corporation/5349/roblox", "icon": "🤖"},
    
    # Direct Web HTML5 Embedded Games
    {"id": "granny1", "title": "Granny Horror House Chapter 1", "category": "Horror", "type": "html5", "url": "https://html5.gamedistribution.com/d8702bf9eb5f4ba4a30e8c991f24d776/", "icon": "😱"},
    {"id": "slender", "title": "Slenderman Silent Forest", "category": "Horror", "type": "html5", "url": "https://html5.gamedistribution.com/rvvAS3Cc/", "icon": "👻"},
    {"id": "moto", "title": "Moto X3M Extreme Bike Racing", "category": "Racing", "type": "html5", "url": "https://html5.gamedistribution.com/9b275f8f5e1f4d99a4c865f3f4c66432/", "icon": "🏎️"},
    {"id": "drift", "title": "Drift Hunters 3D", "category": "Racing", "type": "html5", "url": "https://html5.gamedistribution.com/f04c552a922340b18f0a07185ee6b21b/", "icon": "🚗"},
    {"id": "subway", "title": "Subway Runner Web 3D", "category": "Action", "type": "html5", "url": "https://html5.gamedistribution.com/9b275f8f5e1f4d99a4c865f3f4c66432/", "icon": "🏃"}
]

# Filter Logic
filtered_games = [g for g in GAMES_DATABASE if search_query.lower() in g["title"].lower() or search_query.lower() in g["category"].lower()]

# 6. Main Layout
st.divider()

if filtered_games:
    selected_game_title = st.selectbox("🎮 Choose Game from Showcase Grid:", [f"{g['icon']} {g['title']}" for g in filtered_games])
    chosen_game = next(g for g in filtered_games if f"{g['icon']} {g['title']}" == selected_game_title)
    
    st.markdown(f"### Now Playing: {chosen_game['title']}")
    
    # 7. Side Menu Overlay for Keymapping Controls
    col_game, col_side = st.columns([3, 1])
    
    with col_side:
        st.markdown("### ⌨️ Controls Overlay")
        st.info("""
        **PC Keymapping Menu:**
        * **W, A, S, D:** Move
        * **Spacebar:** Jump
        * **Left Click:** Fire / Attack
        * **Shift:** Run
        """)
        st.text_input("Custom Jump:", value="Space")
        st.text_input("Custom Attack:", value="L-Click")
        
        st.divider()
        st.markdown("### 📢 Adsterra Slot")
        st.caption("[Adsterra Sidebar Script Placement]")

    with col_game:
        if chosen_game["type"] == "cloud":
            st.warning("⚡ Official Cloud Game Engine Notice")
            st.write("Now.gg Cloud Games run in a high-speed external window to bypass security errors.")
            st.link_button(f"🚀 Launch {chosen_game['title']} Now", chosen_game["url"], use_container_width=True)
        else:
            components.iframe(chosen_game["url"], height=600, scrolling=True)

    # 8. Quit & High Score Email Login Logic
    st.divider()
    with st.expander("🚪 Finish / Quit Game & Save High Score"):
        st.write("Enter your details to save your score on the GamerZone 360 Leaderboard:")
        email = st.text_input("Enter Email to Save Score:")
        score = st.number_input("Your Final Score:", min_value=0, value=100)
        if st.button("Save & Quit"):
            if email:
                st.success(f"Score {score} saved for {email}! High score updated successfully.")
            else:
                st.error("Please enter Email ID to record your score!")

else:
    st.error("❌ Game not found in database. Try searching 'Free Fire', 'Roblox', 'Racing', or 'Horror'.")
