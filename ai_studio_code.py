import streamlit as st
import streamlit.components.v1 as components
import urllib.parse

# Page Configuration
st.set_page_config(page_title="Universal Resource Station", page_icon="🚀", layout="wide")

# ---------------- MONETAG VERIFICATION CODE ----------------
monetag_meta_code = """
<script>
    var meta = document.createElement('meta');
    meta.name = "monetag";
    meta.content = "95c357e457206bc35e5824e28d5941da";
    document.getElementsByTagName('head')[0].appendChild(meta);
</script>
"""
components.html(monetag_meta_code, height=0, width=0)
# -----------------------------------------------------------

st.title("🚀 Smart Direct Download & Resource Hub")
st.write("சாஃப்ட்வேர் மற்றும் குறிப்பிட்ட வெர்ஷன்களின் (Exact Versions) நேரடி டவுன்லோட் லிங்க்குகள்!")

st.markdown("---")

# ---------------- SECTION 1: DIRECT DOWNLOAD FINDER ----------------
st.subheader("🔍 Exact Version Direct Download Finder")

user_input = st.text_input("Enter Software or OS Name (e.g., 'Anaconda3 2020.02', 'Rufus 3.22', 'PrimeOS Classic 0.4.5'):")

if user_input.strip():
    encoded_query = urllib.parse.quote(user_input.strip())
    
    st.success(f"Finding direct download links for: **{user_input}**")
    
    # Direct Download Engine
    direct_url = f"https://duckduckgo.com/?q=!ducky+{encoded_query}+direct+download+file"
    
    # SINGLE DIRECT BUTTON
    st.link_button(
        f"📥 Download '{user_input}' Directly", 
        direct_url, 
        use_container_width=True
    )

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
        st.link_button("🌐 PrimeOS Official", "https://www.primeos.in/")
        st.link_button("🌐 Bliss OS Official", "https://blissos.org/")
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
        st.link_button("📘 TN School Textbooks Portal","https://www.tntextbooks.in/p/school-books.html?m=1") 
        st.link_button("🎓 Khan Academy (Free Learning)", "https://www.khanacademy.org/")
    with col_e2:
        st.link_button("🌐 Wikipedia Encyclopedia", "https://www.wikipedia.org/")
        st.link_button("📄 National Digital Library of India", "https://ndl.iitkgp.ac.in/")
