import streamlit as st
import feedparser

# Page Configuration
st.set_page_config(page_title="Ultimate Gaming & Tech Hub", page_icon="🎮", layout="wide")

st.title("🚀 Gaming, Tech & Study Portal")
st.write("Welcome! Get the best PC optimization tips, trending news, and study guides all in one place.")

# Sidebar for Navigation
st.sidebar.title("📌 Menu")
choice = st.sidebar.radio("Go to:", ["🎮 PC Gaming & Optimization Tips", "🔥 Live Trending Gaming News", "📚 9th & 10th Study Formulas"])

# 1. GAMING & OPTIMIZATION
if choice == "🎮 PC Gaming & Optimization Tips":
    st.header("🎮 Low-End PC Gaming & Optimization Guide")
    
    col1, col2 = st.columns(2)
    
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

# 2. AUTOMATIC TRENDING NEWS
elif choice == "🔥 Live Trending Gaming News":
    st.header("🔥 Daily Auto-Updated Gaming & Tech News")
    st.caption("Updated automatically via Google News RSS Feed (No API Key Required!)")
    
    category = st.selectbox("Select Topic:", ["Gaming News", "Free Fire Updates", "Roblox Trends", "Tech News"])
    
    keywords = {
        "Gaming News": "gaming",
        "Free Fire Updates": "free fire game",
        "Roblox Trends": "roblox",
        "Tech News": "technology"
    }
    
    query = keywords[category]
    rss_url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"
    
    with st.spinner("Fetching latest updates from Google..."):
        try:
            feed = feedparser.parse(rss_url)
            
            if feed.entries:
                st.success(f"Total {len(feed.entries[:10])} Latest News Found!")
                for entry in feed.entries[:10]:
                    st.markdown(f"### 📰 [{entry.title}]({entry.link})")
                    st.caption(f"🗓️ Published: {entry.published}")
                    st.markdown("---")
            else:
                st.error("No news found. Please refresh or try another topic.")
        except Exception as e:
            st.error(f"Error loading news: {e}")

# 3. STUDY FORMULAS
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
