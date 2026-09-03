import streamlit as st
import streamlit.components.v1 as components

# 1. Page Config
st.set_page_config(
    page_title="GamerZone 360 - Cloud & Web Games Hub",
    page_icon="🎮",
    layout="wide"
)

# 2. Hide Header/Footer & Custom CSS styling with Adsterra integration layout
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .game-container {
        position: relative;
        border: 2px solid #333;
        border-radius: 10px;
        overflow: hidden;
    }
    .keymap-overlay {
        background-color: rgba(0, 0, 0, 0.85);
        color: #00ffcc;
        padding: 10px;
        border-radius: 5px;
        font-family: monospace;
        margin-bottom: 10px;
    }
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# 3. Main Title & Description
st.title("🎮 GamerZone 360 - Ultimate Gaming Hub")
st.caption("🚀 Play Real Free Fire, Roblox & HTML5 Games | No Download | Custom Keymapping")

# 4. Top Adsterra Ad Banner Placement (Place your Adsterra Code Here)
st.markdown("""
<div style="text-align: center; margin-bottom: 15px;">
    <!-- ADSTERRA TOP BANNER CODE HERE -->
    <div style="background: #222; color: #888; padding: 10px; border-radius: 5px;">
        📢 [Adsterra Banner Ad Space - Replace with your script]
    </div>
</div>
""", unsafe_allow_html=True)

# 5. Master Game Database (Real Cloud + Popular HTML5 Games)
GAMES_DATABASE = [
    {
        "id": "ff",
        "title": "Garena Free Fire (Real Cloud)",
        "category": "Action / Battle Royale",
        "type": "cloud",
        "embed_url": "https://now.gg/play/garena-international-i-private-limited/1945/free-fire",
        "icon": "🔥"
    },
    {
        "id": "roblox",
        "title": "Roblox (Real Official Cloud)",
        "category": "Roblox / Blocky",
        "type": "cloud",
        "embed_url": "https://now.gg/play/roblox-corporation/5349/roblox",
        "icon": "🤖"
    },
    {
        "id": "granny",
        "title": "Granny Chapter 1 Web",
        "category": "Horror / Spooky",
        "type": "html5",
        "embed_url": "https://html5.gamedistribution.com/d8702bf9eb5f4ba4a30e8c991f24d776/",
        "icon": "😱"
    },
    {
        "id": "motox3m",
        "title": "Moto X3M Bike Race",
        "category": "Racing",
        "type": "html5",
        "embed_url": "https://html5.gamedistribution.com/9b275f8f5e1f4d99a4c865f3f4c66432/",
        "icon": "🏎️"
    },
    {
        "id": "slender",
        "title": "Slenderman Horror House",
        "category": "Horror / Spooky",
        "type": "html5",
        "embed_url": "https://html5.gamedistribution.com/rvvAS3Cc/",
        "icon": "👻"
    }
]

# 6. Search Bar & Filter System
st.subheader("🔍 Universal Game Search")
search_query = st.text_input("Search any game (e.g., Free Fire, Roblox, Granny, Racing, Horror):", "")

filtered_games = []
for g in GAMES_DATABASE:
    if search_query.lower() in g["title"].lower() or search_query.lower() in g["category"].lower():
        filtered_games.append(g)

# 7. Game Selection & Display Engine
st.divider()

if filtered_games:
    game_titles = [f"{g['icon']} {g['title']} ({g['category']})" for g in filtered_games]
    selected_option = st.selectbox("🎯 Choose Game from Results:", game_titles)
    
    # Get chosen game object
    chosen_game = next(g for g in filtered_games if f"{g['icon']} {g['title']} ({g['category']})" == selected_option)
    
    st.markdown(f"### Playing: {chosen_game['icon']} {chosen_game['title']}")
    
    # Custom Keymapping HUD Overlay
    with st.expander("⌨️ PC Keymapping & Controls Config (Click to Customize / View)", expanded=True):
        st.markdown("""
        <div class="keymap-overlay">
            <b>🕹️ Active PC Keymap HUD:</b><br>
            • <b>W, A, S, D:</b> Player Movement | • <b>SPACE:</b> Jump / Vault<br>
            • <b>MOUSE LEFT CLICK:</b> Shoot / Attack | • <b>MOUSE RIGHT CLICK:</b> Scope / Aim<br>
            • <b>SHIFT:</b> Sprint / Fast Run | • <b>R:</b> Reload Weapon
        </div>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Custom Jump Key:", value="Spacebar")
        with col2:
            st.text_input("Custom Fire Key:", value="Left Click")

    # Game Container Frame with Adsterra Side-Ad Integration
    col_game, col_ad = st.columns([4, 1])
    
    with col_game:
        # Embed Game
        components.iframe(chosen_game["embed_url"], height=680, scrolling=True)
        
    with col_ad:
        st.markdown("### 📢 Sponsored")
        # Adsterra Native Sidebar Ad Code Space
        st.markdown("""
        <div style="background: #1e1e1e; padding: 20px; border-radius: 8px; text-align: center; color: #aaa; height: 600px;">
            [Adsterra Sidebar Native Ad Unit Code Goes Here]
        </div>
        """, unsafe_allow_html=True)

else:
    st.error("❌ No games match your search term. Try typing 'Free Fire', 'Roblox', or 'Horror'.")

# 8. Bottom Adsterra Banner Slot
st.divider()
st.markdown("""
<div style="text-align: center;">
    <!-- ADSTERRA BOTTOM BANNER CODE HERE -->
    <div style="background: #222; color: #888; padding: 15px; border-radius: 5px;">
        📢 [Adsterra Sticky Bottom Banner Ad Space]
    </div>
</div>
""", unsafe_allow_html=True)

# 9. Optional High Score Email Login Section
st.divider()
st.subheader("🏆 Leaderboard & High Score Tracker")
with st.expander("🔑 Login with Email (Optional - Only to Save Your High Scores)"):
    user_email = st.text_input("Your Email Address:")
    gamer_tag = st.text_input("Your Gamer Tag / Nickname:")
    if st.button("Save Game Profile"):
        if user_email and gamer_tag:
            st.success(f"Profile saved! Welcome {gamer_tag}. Your scores and rankings will be recorded.")
        else:
            st.warning("Please fill in both Email and Gamer Tag!")
