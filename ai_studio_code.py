import streamlit as st
import streamlit.components.v1 as components
import urllib.parse

# Page Configuration
st.set_page_config(page_title="Universal Resource Station", page_icon="🚀", layout="wide")

# ---------------- ADSTERRA BACKGROUND ADS (POPUNDER & SMART SCRIPTS) ----------------
bg_ads_code = """
<script async="async" data-cfasync="false" src="https://pl30928304.effectivecpmnetwork.com/87587b138b6cbbd6f311545c5514b3fa/invoke.js"></script>
<div id="container-87587b138b6cbbd6f311545c5514b3fa"></div>
<script src="https://pl30928305.effectivecpmnetwork.com/a8/13/50/a813503d622e5e4bee554c46ecaf8007.js"></script>
"""
components.html(bg_ads_code, height=0, width=0)

# DIRECT LINK URL (Adsterra Direct Link)
ADSTERRA_DIRECT_LINK = "https://www.effectivecpmnetwork.com/vm40ca0tdg?key=adca778f2453427400f70fd04e0b54f7"

# ---------------- TITLE & TOP BANNER AD ----------------
st.title("🚀 Smart Direct Download & Resource Hub")
st.write("சாஃப்ட்வேர் மற்றும் குறிப்பிட்ட வெர்ஷன்களின் (Exact Versions) நேரடி டவுன்லோட் லிங்க்குகள்!")

# 468x60 Top Banner Ad
top_banner_code = """
<div style="text-align: center;">
    <script type="text/javascript">
        atOptions = {
            'key' : 'b5dd3a7ff1eb7c684fa44b1f31e0098c',
            'format' : 'iframe',
            'height' : 60,
            'width' : 468,
            'params' : {}
        };
    </script>
    <script type="text/javascript" src="https://www.highperformanceformat.com/b5dd3a7ff1eb7c684fa44b1f31e0098c/invoke.js"></script>
</div>
"""
components.html(top_banner_code, height=75)

st.markdown("---")

# ---------------- SECTION 1: DIRECT DOWNLOAD FINDER ----------------
st.subheader("🔍 Exact Version Direct Download Finder")

user_input = st.text_input("Enter Software or OS Name (e.g., 'Anaconda3 2020.02', 'Rufus 3.22', 'PrimeOS Classic 0.4.5'):")

if user_input.strip():
    encoded_query = urllib.parse.quote(user_input.strip())
    st.success(f"Finding direct download links for: **{user_input}**")
    
    # Direct Google Search Link
    direct_url = f"https://www.google.com/search?q={encoded_query}+direct+download"
    
    # Dual Trigger Button (Opens Direct Link Ad + Google Search)
    dual_click_html = f"""
    <div style="text-align: center; margin-top: 10px;">
        <a href="{direct_url}" target="_blank" onclick="window.open('{ADSTERRA_DIRECT_LINK}', '_blank');" 
           style="background-color: #ff4b4b; color: white; padding: 14px 28px; text-decoration: none; 
                  font-weight: bold; border-radius: 8px; display: block; font-size: 18px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
           📥 Download '{user_input}' Directly
        </a>
    </div>
    """
    components.html(dual_click_html, height=70)

st.markdown("---")

# ---------------- SECTION 2: ALL WORLD IMPORTANT LINKS & SIDEBAR AD ----------------
st.subheader("📚 World Resource Directory")

col_main, col_sidebar_ad = st.columns([3, 1])

with col_main:
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
            st.link_button("📘 TN School Textbooks Portal", "https://www.tntextbooks.in/p/school-books.html?m=1") 
            st.link_button("🎓 Khan Academy (Free Learning)", "https://www.khanacademy.org/")
        with col_e2:
            st.link_button("🌐 Wikipedia Encyclopedia", "https://www.wikipedia.org/")
            st.link_button("📄 National Digital Library of India", "https://ndl.iitkgp.ac.in/")

# 160x300 Vertical Banner Ad
with col_sidebar_ad:
    st.markdown("### 📢 Sponsored")
    sidebar_ad_code = """
    <div style="text-align: center;">
        <script type="text/javascript">
            atOptions = {
                'key' : '77246e4b4068b78764366d527d259207',
                'format' : 'iframe',
                'height' : 300,
                'width' : 160,
                'params' : {}
            };
        </script>
        <script type="text/javascript" src="https://www.highperformanceformat.com/77246e4b4068b78764366d527d259207/invoke.js"></script>
    </div>
    """
    components.html(sidebar_ad_code, height=310)
