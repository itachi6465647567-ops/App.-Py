import streamlit as st
import feedparser

# Page Configuration
st.set_page_config(page_title="Ultimate Gaming & Tech Hub", page_icon="🎮", layout="wide")

st.title("🚀 Gaming, Tech & Study Portal")
st.write("Welcome! Get the best PC optimization tips, trending news, and study guides all in one place.")

# Sidebar for Navigation
st.sidebar.title("📌 Menu")
choice = st.sidebar.radio("Go to:", ["🎮 PC Gaming & Optimization Tips", "🔥 Live Trending Gaming News", "📚 9th & 10th Study Formulas"])

# ---------------- SECTION 1: GAMING & OPTIMIZATION ----------------
if choice == "🎮 PC Gaming & Optimization Tips":
    st.header("🎮 Low-End PC Gaming & Optimization Guide")
    
    col1, col2 = st.col_row() if hasattr(st, 'col_row') else st.columns(2)
    
    with col1:
        st.subheader("🔥 Free Fire Lag Fix (2GB / 4GB RAM)")
        st.write("""
        * **Graphics Setting:** Always set Display to **Smooth** and High FPS to **Normal**.
        * **Clear Cache:** Open Free Fire Settings -> Others -> Clear Cache before playing.
        * **Background Apps:** Close Chrome and background apps before starting the game.
        """)
        
    with col2:
        st.subheader("🤖 Roblox Best Performance Settings")
        st.write("""
        * **Graphics Mode:** Change Graphics Mode from Automatic to **Manual**.
        * **Graphics Quality:** Lower graphics quality slider to **1-2 bars**.
        * **Task Manager:** Set Roblox process priority to **High** in Task Manager.
        """)

    st.markdown("---")
    st.subheader("💻 General PC Speed Up Tips")
    st.info("Press `Windows + R`, type `temp`, `%temp%`, and `prefetch` to delete junk files and free up RAM!")

# ---------------- SECTION 2: AUTOMATIC TRENDING NEWS ----------------
elif choice == "🔥 Live Trending Gaming News":
    st.header("🔥 Daily Auto-Updated Gaming & Tech News")
    st.caption("Updated automatically via Google News RSS Feed (No API Key Required!)")
    
    category = st.selectbox("Select Topic:", ["Gaming News", "Free Fire Updates", "Roblox Trends", "Tech News"])
    
    # Mapping search keywords to Google News RSS URLs
    rss_urls = {
        "Gaming News": "https://news.google.com/rss/search?q=gaming+news&hl=en-IN&gl=IN&ceid=IN:en",
        "Free Fire Updates": "https://news.google.com/rss/search?q=free+fire+game&hl=en-IN&gl=IN&ceid=IN:en",
        "Roblox Trends": "https://news.google.com/rss/search?q=roblox&hl=en-IN&gl=IN&ceid=IN:en",
        "Tech News": "https://news.google.com/rss/search?q=technology+news&hl=en-IN&gl=IN&ceid=IN:en"
    }
    
    with st.spinner("Fetching latest updates..."):
        feed = feedparser.parse(rss_urls[category])
        
        if feed.entries:
            for entry in feed.entries[:8]:  # Shows top 8 trending articles
                with st.container():
                    st.markdown(f"### 📰 [{entry.title}]({entry.link})")
                    st.caption(f"🗓️ Published: {entry.published}")
                    st.markdown("---")
        else:
            st.warning("Unable to fetch news right now. Please try again later.")

# ---------------- SECTION 3: STUDY FORMULAS ----------------
elif choice == "📚 9th & 10th Study Formulas":
    st.header("📚 Quick Study Reference Formulas")
    
    st.subheader("📐 Mathematics Formulas")
    st.write("""
    * **Algebra:** $(a + b)^2 = a^2 + 2ab + b^2$
    * **Algebra:** $(a - b)^2 = a^2 - 2ab + b^2$
    * **Algebra:** $a^2 - b^2 = (a + b)(a - b)$
    * **Area of Circle:** $\pi r^2$
    """)
    
    st.subheader("⚛️ Physics Basic Formulas")
    st.write("""
    * **Speed:** $\text{Speed} = \\frac{\text{Distance}}{\text{Time}}$
    * **Force (Newton's 2nd Law):** $F = m \\times a$
    * **Ohm's Law:** $V = I \\times R$
    """)
