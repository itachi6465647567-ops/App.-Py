# ---------------- SECTION 2: AUTOMATIC TRENDING NEWS ----------------
elif choice == "🔥 Live Trending Gaming News":
    st.header("🔥 Daily Auto-Updated Gaming & Tech News")
    st.caption("Updated automatically via Google News RSS Feed (No API Key Required!)")
    
    category = st.selectbox("Select Topic:", ["Gaming News", "Free Fire Updates", "Roblox Trends", "Tech News"])
    
    # Direct RSS Search URLs
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
                for entry in feed.entries[:10]: # Top 10 articles
                    st.markdown(f"### 📰 [{entry.title}]({entry.link})")
                    st.caption(f"🗓️ Published: {entry.published}")
                    st.markdown("---")
            else:
                st.error("No news found. Please refresh or try another topic.")
        except Exception as e:
            st.error(f"Error loading news: {e}")
