import streamlit as st
import random

# Page Config
st.set_page_config(page_title="Game Zone 360 - Elite Cyber Terminal", page_icon="💻", layout="wide")

# Custom Styling (Matrix Dark Theme)
st.markdown("""
    <style>
    .stApp {
        background-color: #030706;
        color: #00ff66;
        font-family: 'Courier New', Courier, monospace;
    }
    .hacker-box {
        background-color: #0a0f0d;
        border: 2px solid #00ff66;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 0 25px rgba(0, 255, 102, 0.25);
        min-height: 350px;
        max-height: 420px;
        overflow-y: auto;
    }
    .terminal-text {
        font-size: 14px;
        color: #00ff66;
        white-space: pre-wrap;
        word-wrap: break-word;
        line-height: 1.4;
    }
    h1, h2, h3 {
        color: #00ff66 !important;
        text-shadow: 0 0 10px rgba(0, 255, 102, 0.5);
    }
    .leaderboard-box {
        background-color: #0a0f0d;
        border: 1px dashed #00ff66;
        padding: 15px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# 1. Initialize Auto Agent Identity & IP Simulation
if 'agent_name' not in st.session_state:
    prefixes = ["Cyber", "Phantom", "Glitch", "Matrix", "Dark", "Zero", "Shadow", "Byte"]
    suffixes = ["Ninja", "Hacker", "Viper", "Ghost", "X", "Core", "Node", "Lord"]
    st.session_state.agent_name = f"{random.choice(prefixes)}_{random.choice(suffixes)}_{random.randint(100, 999)}"

if 'user_ip' not in st.session_state:
    st.session_state.user_ip = f"192.168.{random.randint(10,250)}.{random.randint(1,254)}"

if 'total_strokes' not in st.session_state:
    st.session_state.total_strokes = 0

if 'hacked_companies' not in st.session_state:
    st.session_state.hacked_companies = []

if 'terminal_logs' not in st.session_state:
    st.session_state.terminal_logs = f"INITIALIZING GAME ZONE 360...\nIP: {st.session_state.user_ip} | AGENT: {st.session_state.agent_name}\nREADY FOR MAINFRAME PENETRATION...\n"

# 2. EXACTLY 60 Target Companies List for Every 10 Keystroke Milestones
TARGET_COMPANIES_60 = [
    "NASA Space Telemetry Subnet", "Pentagon Defense Mainframe", "Google Core Cloud Server", 
    "SpaceX Satellite Orbital Gateway", "Interpol Global Criminal Database", "Amazon Web Services (AWS) US-East", 
    "Microsoft Azure Secure Subnet", "Meta User Data Center", "Apple iCloud Security Core", "Tesla Autonomous Driving Grid",
    "Netflix Global Streaming Node", "Cisco Systems Router Core", "IBM Watson AI Mainframe", "Intel Semiconductor Fab Network",
    "Oracle Cloud Database Cluster", "Alibaba Cloud Gateway", "PayPal Financial Transaction Hub", "Visa Global Payment Gateway",
    "Mastercard Secure Network", "Twitter/X Core Infrastructure", "TikTok Content Delivery Network", "Reddit Subreddit Server Cluster",
    "Sony PlayStation Network", "Steam Gaming Server Hub", "Epic Games Unreal Node", "Riot Games Valorant Subnet",
    "Binance Crypto Exchange Node", "Coinbase Secure Vault", "Ethereum Core Relay", "Bitcoin Mining Pool Server",
    "Bank of America Mainframe", "JPMorgan Chase Secure Gateway", "Goldman Sachs Financial Node", "HSBC International Server",
    "European Central Bank Grid", "Federal Reserve Sub-Node", "CIA Field Operations Database", "FBI Cyber Division Server",
    "MI6 Secret Intelligence Node", "Interpol Red Notice Database", "WHO Global Health Records", "United Nations Secure Comms",
    "DARPA Advanced Research Subnet", "CERN Particle Accelerator Grid", "MIT Research Supercomputer", "Harvard Data Center",
    "Oxford University Server Hub", "Stanford AI Lab Mainframe", "Tokyo Stock Exchange Node", "London Stock Exchange Gateway",
    "New York Stock Exchange Core", "Wall Street Trading Hub", "Silicon Valley Tech Grid", "Cyberdyne Systems Mainframe",
    "Aperture Science Testing Facility", "Umbrella Corporation Bio-Node", "Stark Industries Defense Grid", "Wayne Enterprises Secure Subnet",
    "Skynet Global Defense Network", "Matrix Central Core Terminal"
]

# 3. Clean Hacker Lines Pool (No Numbers like [1/600] attached)
RAW_BASE_POOL = [
    "INITIATING ROOT ACCESS PROTOCOL v4.9.2...",
    "BYPASSING FIREWALL [████████████████] 100% SECURE",
    "ESTABLISHING SECURE PROXY TUNNEL THROUGH ZURICH NODE...",
    "CONNECTING TO PENTAGON MAINFRAME SUB-ROUTER...",
    "ACCESS GRANTED: WELCOME USER_DARSH [GAME ZONE 360]",
    "DECRYPTING AES-256 BIT MILITARY ENCRYPTION KEYS...",
    "INJECTING PAYLOAD INTO TARGET SUBNET 192.168.404.1...",
    "BYPASSING TWO-FACTOR AUTHENTICATION VIA BUFFER OVERFLOW...",
    "ACCESSING DATABASE: //root/secure/users/credentials_dump.db",
    "DOWNLOADING SATELLITE TELEMETRY DATA... [SUCCESS]",
    "SPOOFING MAC ADDRESS: 00:1A:2B:3C:4D:5E...",
    "KERNEL PANIC AVOIDED: PATCHING MEMORY LEAK IN SECTOR 7...",
    "BRUTE-FORCING SSH PORT 22 WITH MULTI-THREADED THREAT MATRIX...",
    "EXPLOITING ZERO-DAY VULNERABILITY IN REMOTE PROCEDURE CALL...",
    "ESTABLISHING ENCRYPTED TCP SOCKET TO DARKNET RELAY...",
    "DOWNLOADING SOURCE CODE REPOSITORY... 4.8 TB TRANSFERRED.",
    "WIPING SYSTEM LOGS & TRACE FILES... [CLEAN]",
    "OVERRIDING BIOMETRIC LOCK ON MAIN GATEWAY...",
    "COMPILING CUSTOM C-EXPLOIT PAYLOAD ON THE FLY...",
    "BYPASSING CLOUD_FLARE DDOS MITIGATION SHIELD...",
    "INJECTING SQL PAYLOAD: ' OR '1'='1 -- [ADMIN BYPASS]",
    "DECRYPTING SSL HANDSHAKE CERTIFICATES...",
    "SCANNING OPEN PORTS [80, 443, 8080, 3306, 21]...",
    "HIJACKING ACTIVE SESSIONS VIA COOKIE STEALING...",
    "UPLOADING TROJAN HORSE BACKDOOR TO MAIN SERVER...",
    "BYPASSING INTRUSION DETECTION SYSTEM (IDS)...",
    "EXTRACTING HASHED PASSWORDS FROM SHADOW FILE...",
    "CRACKING MD5/SHA-256 HASHES USING RAINBOW TABLES...",
    "ESTABLISHING DEEP-SPACE RELAY CONNECTION...",
    "SYSTEM OVERRIDE SUCCESSFUL. FULL ADMIN CONTROL ACQUIRED.",
    "SYNTAX ERROR IN KERNEL MODULE: RETRYING PACKET INJECTION...",
    "ALLOCATING VIRTUAL MEMORY BLOCKS FOR BUFFER OVERFLOW...",
    "DISABLING WINDOWS DEFENDER REAL-TIME MONITORING...",
    "RANSOMWARE DEPLOYMENT QUEUED: WAITING FOR AUTHORIZATION...",
    "PINGING TARGET IP 10.0.0.13 - REPLY RECEIVED (1ms)...",
    "DOWNLINK ESTABLISHED WITH ORBITAL SATELLITE KH-11...",
    "DELETING EXECUTABLE TRACES FROM TEMP DIRECTORY...",
    "BYPASSING BIOMETRIC FACIAL RECOGNITION LOCK...",
    "UNZIPPING PAYLOAD ARCHIVE: EXPLOIT_KIT_v9.zip...",
    "EXECUTING SHELL SCRIPT: /bin/bash -i >& /dev/tcp/... [ACTIVE]"
]

if 'master_600_pool' not in st.session_state:
    full_pool = []
    for i in range(1, 601):
        base_line = RAW_BASE_POOL[(i - 1) % len(RAW_BASE_POOL)]
        full_pool.append(base_line)  # Pure text without numbering
    st.session_state.master_600_pool = full_pool

# Layout: Main Terminal & Leaderboard Sidebar
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("<h1>💻 GAME ZONE 360 : ELITE TERMINAL</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #8b949e;'>IP: <b style='color: #00ff66;'>{st.session_state.user_ip}</b> | Agent: <b style='color: #00ff66;'>{st.session_state.agent_name}</b></p>", unsafe_allow_html=True)

    # Keyboard Input Box
    user_key = st.text_input("⌨️ Press any keys (type continuously up to 600):", placeholder="Tap keys here (e.g. a, b, c, d)...", key="live_keyboard_input")

    if user_key:
        if st.session_state.total_strokes < 600:
            st.session_state.total_strokes += 1
            current_idx = st.session_state.total_strokes - 1
            
            # Check for every 10 keystrokes -> Company Hack Milestone
            if st.session_state.total_strokes % 10 == 0:
                company_index = (st.session_state.total_strokes // 10 - 1) % len(TARGET_COMPANIES_60)
                target_comp = TARGET_COMPANIES_60[company_index]
                if target_comp not in st.session_state.hacked_companies:
                    st.session_state.hacked_companies.append(target_comp)
                log_msg = f"\n🔥 [MILESTONE REACHED] COMPROMISED COMPANY: {target_comp}!\n"
            
            if st.session_state.total_strokes == 600:
                log_msg = "\n👑 [ULTIMATE BOSS OVERRIDE] 600/600 COMPLETED! ALL 60 GLOBAL MAINFRAMES SEIZED!\n"
            elif st.session_state.total_strokes % 10 != 0:
                log_msg = f"KEY [{user_key[-1].upper()}] >> {st.session_state.master_600_pool[current_idx]}\n"

            st.session_state.terminal_logs += log_msg

    # Display Live Terminal Box
    st.markdown("### 🖥️ Live Execution Stream:")
    st.markdown(f'<div class="hacker-box"><div class="terminal-text">{st.session_state.terminal_logs}_</div></div>', unsafe_allow_html=True)

    # Progress bar towards 600
    progress_val = min(st.session_state.total_strokes / 600.0, 1.0)
    st.progress(progress_val, text=f"Mainframe Breach Progress: {st.session_state.total_strokes}/600 Keystrokes")

    if st.button("🧹 Purge Terminal Buffer"):
        st.session_state.total_strokes = 0
        st.session_state.hacked_companies = []
        st.session_state.terminal_logs = f"BUFFER CLEARED. IP: {st.session_state.user_ip} READY_\n"
        st.rerun()

with col2:
    st.markdown("<h2>🏆 LIVE LEADERBOARD</h2>", unsafe_allow_html=True)
    
    user_score = len(st.session_state.hacked_companies) * 100
    st.markdown(f"""
        <div class="leaderboard-box">
            <p style="color: #00ff66; margin: 0 0 10px 0; font-weight: bold;">⚡ TOP AGENTS (LIVE IP TRACKING):</p>
            <ol style="margin: 0; padding-left: 20px; color: #8b949e; font-size: 13px;">
                <li><b style="color: #00ff66;">Cyber_Viper_772 (185.22.x.x)</b> — 6,000 Pts (Rank #1)</li>
                <li><b style="color: #00ff66;">Matrix_Ghost_404 (45.12.x.x)</b> — 4,500 Pts (Rank #2)</li>
                <li><b style="color: #ffff00;">{st.session_state.agent_name} (YOU)</b> — <span style="color: #ffff00;">{user_score} Pts</span> (Rank #3)</li>
            </ol>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Hacked Companies List Box for Current User
    st.markdown("### 🏢 Hacked Companies By You:")
    if st.session_state.hacked_companies:
        comp_list_str = "<br>".join([f"✅ {comp}" for comp in st.session_state.hacked_companies])
        st.markdown(f"""
            <div style="background-color: #0a0f0d; border: 1px solid #30363d; padding: 10px; border-radius: 8px; color: #00ff66; font-size: 12px; max-height: 180px; overflow-y: auto;">
                {comp_list_str}
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("<p style='color: #8b949e; font-size: 12px;'>Type keys to start hacking companies every 10 levels...</p>", unsafe_allow_html=True)

    st.markdown("<br>")
    
    # ==========================================
    # 📢 ALL 7 ADSTERRA AD CODES INTEGRATION
    # ==========================================
    st.markdown("### 📢 Sponsored Networks")

    # Ad 1 & 2: External Scripts (Loaded safely)
    st.markdown("""
        <script src="https://pl31170257.profitableratecpmnetwork.com/13/dd/04/13dd04bed2b3a264e2b5c0bee6e12f6d.js"></script>
        <script async="async" data-cfasync="false" src="https://pl31170258.profitableratecpmnetwork.com/a80ef66a08d7b5463f5dd57e37a8b51c/invoke.js"></script>
        <div id="container-a80ef66a08d7b5463f5dd57e37a8b51c"></div>
    """, unsafe_allow_html=True)

    # Ad 3: High Revenue 728x90 Banner
    st.markdown("""
        <div style="background: #0a0f0d; border: 1px dashed #30363d; padding: 5px; border-radius: 6px; text-align: center; margin-bottom: 10px;">
            <script type="text/javascript">
              atOptions = {
                'key' : 'b5932006bbff90b58bbcc67682e8be52',
                'format' : 'iframe',
                'height' : 90,
                'width' : 728,
                'params' : {}
              };
            </script>
            <script type="text/javascript" src="https://www.highrevenueformat.com/b5932006bbff90b58bbcc67682e8be52/invoke.js"></script>
        </div>
    """, unsafe_allow_html=True)

    # Ad 4: Profitable Rate CPM Script
    st.markdown("""
        <script src="https://pl31170260.profitableratecpmnetwork.com/5e/57/d7/5e57d73e548507aa283de942881b1c82.js"></script>
    """, unsafe_allow_html=True)

    # Ad 5: High Revenue 468x60 Banner
    st.markdown("""
        <div style="background: #0a0f0d; border: 1px dashed #30363d; padding: 5px; border-radius: 6px; text-align: center; margin-bottom: 10px;">
            <script type="text/javascript">
              atOptions = {
                'key' : '61efa07c5904f7f5af5629ad15d68ece',
                'format' : 'iframe',
                'height' : 60,
                'width' : 468,
                'params' : {}
              };
            </script>
            <script type="text/javascript" src="https://www.highrevenueformat.com/61efa07c5904f7f5af5629ad15d68ece/invoke.js"></script>
        </div>
    """, unsafe_allow_html=True)

    # Ad 6: High Revenue 160x300 Skyscraper
    st.markdown("""
        <div style="background: #0a0f0d; border: 1px dashed #30363d; padding: 5px; border-radius: 6px; text-align: center;">
            <script type="text/javascript">
              atOptions = {
                'key' : 'cfd522d9f8386edf91201aab264b4696',
                'format' : 'iframe',
                'height' : 300,
                'width' : 160,
                'params' : {}
              };
            </script>
            <script type="text/javascript" src="https://www.highrevenueformat.com/cfd522d9f8386edf91201aab264b4696/invoke.js"></script>
        </div>
    """, unsafe_allow_html=True)
