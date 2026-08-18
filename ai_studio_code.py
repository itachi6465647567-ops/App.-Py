import streamlit as st
import urllib.parse

# Page Configuration
st.set_page_config(page_title="Universal Software Link Generator", page_icon="⚡", layout="wide")

st.title("⚡ Universal Software & ISO Link Generator")
st.write("உங்களுக்குத் தேவையான சாஃப்ட்வேர் அல்லது Windows ISO பெயரைக் கீழே டைப் செய்யுங்கள். ஆட்டோமேட்டிக்காக டவுன்லோட் லிங்க்குகள் உருவாக்கப்படும்!")

st.markdown("---")

# ---------------- SECTION 1: DYNAMIC LINK GENERATOR ----------------
st.subheader("🔍 Auto Link Generator (Search Any Software)")

user_input = st.text_input("Enter Software or OS Name (e.g., 'Windows 10 ISO', 'Photoshop Free Trial', 'OBS Studio'):")

if user_input.strip():
    encoded_query = urllib.parse.quote(user_input.strip())
    
    st.success(f"Generated official download sources for: **{user_input}**")
    
    col_g1, col_g2, col_g3 = st.columns(3)
    
    with col_g1:
        st.markdown("### 🌐 Official & Trusted Sources")
        st.link_button(f"📥 Download via FileHippo", f"https://filehippo.com/search/?q={encoded_query}")
        st.link_button(f"📥 Download via MajorGeeks", f"https://www.majorgeeks.com/files/search.html?q={encoded_query}")

    with col_g2:
        st.markdown("### 🛡️ Verified Repositories")
        st.link_button(f"📥 Search on Softpedia", f"https://www.softpedia.com/hubs/search.php?q={encoded_query}")
        st.link_button(f"📥 Search on GitHub (Open Source)", f"https://github.com/search?q={encoded_query}")

    with col_g3:
        st.markdown("### 🔍 Direct Search Option")
        st.link_button(f"🔎 Google Direct Download Search", f"https://www.google.com/search?q={encoded_query}+official+download")

st.markdown("---")

# ---------------- SECTION 2: POPULAR FREE SOFTWARE & OS ----------------
st.subheader("📌 Popular Free Software & Windows ISO Links")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 💿 Operating Systems (Free / Official)")
    st.link_button("🪟 Windows 10 Official ISO", "https://www.microsoft.com/en-in/software-download/windows10")
    st.link_button("🪟 Windows 11 Official ISO", "https://www.microsoft.com/software-download/windows11")
    st.link_button("🐧 Ubuntu Linux (Free OS)", "https://ubuntu.com/download/desktop")

with col2:
    st.markdown("### 🛠️ Utilities & Drivers")
    st.link_button("⚙️ DirectX End-User Runtime", "https://www.microsoft.com/en-in/download/details.aspx?id=35")
    st.link_button("📊 CPU-Z Hardware Info", "https://www.cpuid.com/softwares/cpu-z.html")
    st.link_button("📦 7-Zip File Archiver", "https://www.7-zip.org/")

with col3:
    st.markdown("### 🎮 Gaming & Media")
    st.link_button("🎥 VLC Media Player", "https://www.videolan.org/vlc/")
    st.link_button("🤖 Roblox Engine", "https://www.roblox.com/download")
    st.link_button("🚀 Steam Launcher", "https://store.steampowered.com/about/")
