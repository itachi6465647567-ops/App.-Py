import streamlit as st
import urllib.parse
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="Universal Resource Station", page_icon="🚀", layout="wide")

st.title("🚀 Smart Direct Version & Resource Hub")
st.write("குறிப்பிட்ட வெர்ஷன்கள் (e.g., Rufus 3.22, PrimeOS 0.4.5) டைப் செய்தவுடன் நேரடியாக டவுன்லோட் பக்கத்திற்கு அழைத்துச் செல்லும்!")

st.markdown("---")

# ---------------- SECTION 1: AUTO DIRECT REDIRECT SEARCH ----------------
st.subheader("🔍 Instant Direct Version Download Search")

user_input = st.text_input("Enter Software / Specific Version Name (e.g., 'Rufus 3.22', 'PrimeOS 0.4.5', 'Anaconda Windows 7'):")

if user_input.strip():
    encoded_query = urllib.parse.quote(user_input.strip())
    
    st.success(f"Redirecting directly to the exact version page for: **{user_input}**...")
    
    # Direct Official Version URL (DuckDuckGo 'I'm Feeling Lucky')
    direct_version_url = f"https://duckduckgo.com/?q=!ducky+{encoded_query}+official+download"
    
    # 1. Automatic JavaScript Redirect (Opens Direct Link Automatically)
    js_code = f"""
    <script>
        setTimeout(function() {{
            window.location.href = "{direct_version_url}";
        }}, 1000);
    </script>
    """
    components.html(js_code, height=0)
    
    # 2. Backup Direct Button (If Browser Blocks Popup/Auto-Redirect)
    st.markdown("### ⚡ Click below if auto-redirect doesn't open automatically:")
    st.link_button(f"🚀 Open Exact Version Page for '{user_input}' Directly", direct_version_url, use_container_width=True)

st.markdown("---")

# ---------------- SECTION 2: ALL WORLD IMPORTANT LINKS ----------------
st.subheader("📚 World Resource Directory")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💿 Operating Systems (OS)", 
    "🎮 Gaming & Emulators", 
    "🎬 Movies & Streaming (Official)", 
    "🛠️ Must-Have Utilities",
    "📚 Education & Study"
])

# OS TAB
with tab1:
    st.markdown("### 💿 Android OS for PC & Desktop OS")
    col_os1, col_os2 = st.columns(2)
    with col_os1:
        st.link_button("🌐 PrimeOS Official (Android for PC)", "https://www.primeos.in/")
        st.link_button("🌐 Bliss OS (Android OS for PC)", "https://blissos.org/")
        st.link_button("🌐 Phoenix OS Official", "http://www.phoenixos.com/")
        st.link_button("🪟 Windows 10 Official ISO", "https://www.microsoft.com/en-in/software-download/windows10")
    with col_os2:
        st.link_button("🪟 Windows 11 Official ISO", "https://www.microsoft.com/software-download/windows11")
        st.link_button("🐧 Ubuntu Desktop Linux", "https://ubuntu.com/download/desktop")
        st.link_button("🐧 Linux Mint OS", "https://linuxmint.com/")
        st.link_button("💻 ChromeOS Flex (Google)", "https://chromeenterprise.google/os/chromeosflex/")

# GAMING TAB
with tab2:
    st.markdown("### 🎮 Game Stores, Web Games & Emulators")
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.link_button("🕹️ BlueStacks Android Emulator", "https://www.bluestacks.com/")
        st.link_button("🕹️ LDPlayer Android Emulator", "https://www.ldplayer.net/")
        st.link_button("🕹️ MEmu Play Emulator", "https://www.memuplay.com/")
        st.link_button("🌐 Roblox Official", "https://www.roblox.com/")
        st.link_button("🌐 Garena Free Fire Official", "https://ff.garena.com/")
    with col_g2:
        st.link_button("🚀 Steam Store", "https://store.steampowered.com/")
        st.link_button("🚀 Epic Games Store", "https://store.epicgames.com/")
        st.link_button("👾 Armor Games", "https://armorgames.com/")
        st.link_button("👾 CrazyGames Portal", "https://www.crazygames.com/")
        st.link_button("👾 itch.io (Free Indie Games)", "https://itch.io/")

# MOVIES & MEDIA TAB
with tab3:
    st.markdown("### 🎬 Official Streaming & Movie Platforms")
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.link_button("🍿 YouTube Movies Official", "https://www.youtube.com/feed/storefront")
        st.link_button("🍿 Amazon Prime Video", "https://www.primevideo.com/")
        st.link_button("🍿 Disney+ Hotstar", "https://www.hotstar.com/")
    with col_m2:
        st.link_button("🍿 Netflix", "https://www.netflix.com/")
        st.link_button("🍿 Aha Tamil & Telugu", "https://www.aha.video/")
        st.link_button("🍿 Zee5 Platform", "https://www.zee5.com/")

# UTILITIES TAB
with tab4:
    st.markdown("### 🛠️ PC Software, Drivers & Tools")
    col_u1, col_u2 = st.columns(2)
    with col_u1:
        st.link_button("🎥 VLC Media Player", "https://www.videolan.org/vlc/")
        st.link_button("📦 WinRAR Archiver", "https://www.win-rar.com/download.html")
        st.link_button("📦 7-Zip Archiver", "https://www.7-zip.org/")
        st.link_button("🛠️ CPU-Z Hardware Tool", "https://www.cpuid.com/softwares/cpu-z.html")
    with col_u2:
        st.link_button("⚙️ DirectX Runtime", "https://www.microsoft.com/en-in/download/details.aspx?id=35")
        st.link_button("🌐 Google Chrome Browser", "https://www.google.com/chrome/")
        st.link_button("🖌️ OBS Studio (Recording/Streaming)", "https://obsproject.com/")
        st.link_button("🛡️ Malwarebytes Free Anti-Malware", "https://www.malwarebytes.com/")

# EDUCATION TAB
with tab5:
    st.markdown("### 📚 Study & Educational Platforms")
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.link_button("📘 TN School Textbooks Portal", "https://www.textbooksonline.tn.nic.in/")
        st.link_button("🎓 Khan Academy (Free Learning)", "https://www.khanacademy.org/")
    with col_e2:
        st.link_button("🌐 Wikipedia Encyclopedia", "https://www.wikipedia.org/")
        st.link_button("📄 National Digital Library of India", "https://ndl.iitkgp.ac.in/")
