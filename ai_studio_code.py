import streamlit as st
import urllib.parse

# Page Configuration
st.set_page_config(page_title="Universal Resource Station", page_icon="🚀", layout="wide")

st.title("🚀 Smart Software & Resource Hub")
st.write("உங்களுக்குத் தேவையான சாஃப்ட்வேர், கேம்ஸ் அல்லது ISO பெயரைக் டைப் செய்யுங்கள். நேரடி **Official Direct Link** உருவாக்கப்படும்!")

st.markdown("---")

# ---------------- SECTION 1: SMART OFFICIAL SEARCH GENERATOR ----------------
st.subheader("🔍 Smart Download Link Generator")

user_input = st.text_input("Enter Software or OS Name (e.g., 'BlueStacks', 'VLC Player', 'Windows 11 ISO'):")

if user_input.strip():
    encoded_query = urllib.parse.quote(user_input.strip())
    
    st.success(f"Generated links for: **{user_input}**")
    
    # 1. Primary Official Link (Google Search for Official Website Only)
    st.markdown("### 🌐 Primary Official Download")
    official_search_url = f"https://www.google.com/search?q={encoded_query}+official+website+download"
    st.link_button(f"✨ Go to Official Site for '{user_input}'", official_search_url, use_container_width=True)
    
    st.markdown("---")
    
    # 2. Secondary Trusted Sources (If Official Site Not Available)
    st.markdown("### 🛡️ Secondary Trusted Repositories (Alternate)")
    col_s1, col_s2, col_s3 = st.columns(3)
    
    with col_s1:
        st.link_button(f"📥 Search on Uptodown", f"https://en.uptodown.com/search/{encoded_query}")
        st.link_button(f"📥 Search on FileHippo", f"https://filehippo.com/search/?q={encoded_query}")

    with col_s2:
        st.link_button(f"📥 Search on Softpedia", f"https://www.softpedia.com/hubs/search.php?q={encoded_query}")
        st.link_button(f"📥 Search on GitHub (Open Source)", f"https://github.com/search?q={encoded_query}")

    with col_s3:
        st.link_button(f"📥 Search on MajorGeeks", f"https://www.majorgeeks.com/files/search.html?q={encoded_query}")
        st.link_button(f"🔎 Direct Google Search", f"https://www.google.com/search?q={encoded_query}")

st.markdown("---")

# ---------------- SECTION 2: CATEGORY WISE STATION LINKS ----------------
st.subheader("📌 Categorized Resource Station")

tab1, tab2, tab3 = st.tabs(["🎮 Gaming Station", "🎬 Media & Tools", "💿 OS & Utilities"])

with tab1:
    st.markdown("### 🎮 Top Gaming Sites & Platforms")
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.link_button("🌐 Armor Games Official", "https://armorgames.com/")
        st.link_button("🌐 itch.io (Free Indie Games)", "https://itch.io/")
        st.link_button("🌐 CrazyGames Portal", "https://www.crazygames.com/")
    with col_g2:
        st.link_button("🌐 Roblox Official Portal", "https://www.roblox.com/")
        st.link_button("🌐 Steam Game Store", "https://store.steampowered.com/")
        st.link_button("🌐 Epic Games Store", "https://store.epicgames.com/")

with tab2:
    st.markdown("### 🎬 Media, Drivers & Useful Utilities")
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.link_button("🎥 VLC Media Player Official", "https://www.videolan.org/vlc/")
        st.link_button("🛠️ CPU-Z (Hardware Info)", "https://www.cpuid.com/softwares/cpu-z.html")
        st.link_button("🛠️ GPU-Z (Graphics Info)", "https://www.techpowerup.com/gpuz/")
    with col_m2:
        st.link_button("📦 WinRAR Official Download", "https://www.win-rar.com/download.html")
        st.link_button("📦 7-Zip Official Archiver", "https://www.7-zip.org/")
        st.link_button("⚙️ DirectX End-User Runtime", "https://www.microsoft.com/en-in/download/details.aspx?id=35")

with tab3:
    st.markdown("### 💿 Operating Systems (Official ISO)")
    col_o1, col_o2 = st.columns(2)
    with col_o1:
        st.link_button("🪟 Windows 10 Official ISO", "https://www.microsoft.com/en-in/software-download/windows10")
        st.link_button("🪟 Windows 11 Official ISO", "https://www.microsoft.com/software-download/windows11")
    with col_o2:
        st.link_button("🐧 Ubuntu Desktop OS", "https://ubuntu.com/download/desktop")
        st.link_button("🐧 Linux Mint OS", "https://linuxmint.com/download.php")
