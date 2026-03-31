import streamlit as st

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="MindEase AI",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #f9f6ff, #eef3ff, #fff6fb);
        color: black !important;
    }

    html, body, [class*="css"] {
        color: black !important;
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #5b57f0;
        margin-bottom: 6px;
    }

    .sub-title {
        font-size: 19px;
        color: black !important;
        margin-bottom: 20px;
    }

    .hero-box {
        background: linear-gradient(135deg, #6c63ff, #8f7cff, #ff8cc8);
        padding: 32px;
        border-radius: 26px;
        color: white !important;
        box-shadow: 0 14px 28px rgba(108,99,255,0.22);
        margin-bottom: 24px;
    }

    .hero-box h2, .hero-box p {
        color: white !important;
    }

    .safe-box {
        background: linear-gradient(135deg, #ffffff, #f8f3ff);
        padding: 24px;
        border-radius: 22px;
        border-left: 8px solid #7c5cff;
        box-shadow: 0 8px 20px rgba(0,0,0,0.05);
        margin-bottom: 22px;
        color: black !important;
    }

    .card {
        background: rgba(255,255,255,0.97);
        padding: 22px;
        border-radius: 22px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.06);
        margin-bottom: 20px;
        color: black !important;
    }

    .feature-card {
    background: rgba(255,255,255,0.98);
    padding: 24px;
    border-radius: 20px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.05);
    text-align: center;
    min-height: 220px;
    color: black !important;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.feature-card h3 {
    font-size: 20px !important;
    line-height: 1.4 !important;
    margin-top: 12px;
    margin-bottom: 10px;
    word-break: normal !important;
    white-space: normal !important;
}

.feature-card p {
    font-size: 16px !important;
    line-height: 1.6 !important;
    word-break: normal !important;
    white-space: normal !important;
}

    .stat-card {
    background: linear-gradient(135deg, #ffffff, #f5efff);
    padding: 24px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 6px 18px rgba(0,0,0,0.05);
    color: black !important;
    min-height: 170px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.stat-card p {
    font-size: 18px !important;
    line-height: 1.4 !important;
    margin-top: 10px;
    word-break: normal !important;
    white-space: normal !important;
}

    .stat-number {
        font-size: 30px;
        font-weight: 800;
        color: #6c63ff;
    }

    .chat-user {
        background: #ede9fe;
        padding: 14px 16px;
        border-radius: 16px;
        margin-bottom: 12px;
        border-left: 5px solid #8f7cff;
        color: black !important;
    }

    .chat-bot {
        background: #ffe4ef;
        padding: 14px 16px;
        border-radius: 16px;
        margin-bottom: 12px;
        border-left: 5px solid #ff8cc8;
        color: black !important;
    }

    .small-text {
        color: black !important;
        font-size: 14px;
    }

    .breathing-box {
        background: linear-gradient(135deg, #f5f0ff, #fff0f7);
        padding: 26px;
        border-radius: 22px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        color: black !important;
    }

    .wellness-check {
        background: linear-gradient(135deg, #fff, #f8f2ff);
        padding: 24px;
        border-radius: 24px;
        border: 2px dashed #b79cff;
        box-shadow: 0 8px 18px rgba(0,0,0,0.04);
        margin-bottom: 24px;
    }

    /* Purple buttons */
    .stButton > button {
        background-color: #7c5cff !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.55rem 1rem !important;
        font-weight: 600 !important;
    }

    .stButton > button:hover {
        background-color: #6847f5 !important;
        color: white !important;
    }

    .stButton > button:focus {
        outline: none !important;
        box-shadow: 0 0 0 0.2rem rgba(124, 92, 255, 0.35) !important;
    }

    /* Journal text area */
    textarea {
        background-color: white !important;
        color: black !important;
        border: 1px solid #d8d8d8 !important;
        border-radius: 12px !important;
    }

    textarea::placeholder {
        color: #666 !important;
    }

    div[data-baseweb="textarea"] textarea {
        background-color: white !important;
        color: black !important;
        border-radius: 12px !important;
    }

    div[data-baseweb="textarea"] {
        background-color: white !important;
        border-radius: 12px !important;
    }

    section[data-testid="stSidebar"] {
        background: #ffffff !important;
    }

    section[data-testid="stSidebar"] * {
        color: black !important;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# BACKEND FUNCTIONS
# -----------------------------------
def detect_mood(user_input):
    text = user_input.lower()

    if any(word in text for word in ["anxious", "anxiety", "panic"]):
        return "Anxious"
    elif any(word in text for word in ["stress", "stressed", "overthinking"]):
        return "Stressed"
    elif any(word in text for word in ["sad", "depressed", "low", "cry", "crying"]):
        return "Sad"
    elif any(word in text for word in ["happy", "good", "fine", "better"]):
        return "Happy"
    elif any(word in text for word in ["tired", "drained", "exhausted"]):
        return "Tired"
    elif any(word in text for word in ["angry", "frustrated", "anger"]):
        return "Angry"
    elif any(word in text for word in ["lonely", "alone"]):
        return "Lonely"
    else:
        return "Neutral"


def get_bot_response(user_input):
    text = user_input.lower()

    if any(word in text for word in ["suicide", "kill myself", "want to die", "end my life", "hurt myself", "self harm"]):
        return "I'm really sorry you're feeling this way. Please contact a trusted person, local emergency service, or a mental health helpline immediately. You deserve support right now."

    elif "anxious" in text or "anxiety" in text:
        return "I'm sorry you're feeling anxious. Try slow breathing: inhale for 4 seconds, hold for 4, and exhale for 6."

    elif "stress" in text or "stressed" in text:
        return "Stress can feel heavy. Try taking a short break, drinking water, and focusing on one small step at a time."

    elif "sad" in text or "depressed" in text or "low" in text:
        return "I'm here with you. It may help to talk to someone you trust or do one small comforting activity today."

    elif "lonely" in text:
        return "Feeling lonely can be painful. Reaching out to a friend, family member, or writing your thoughts may help."

    elif "happy" in text or "good" in text or "fine" in text:
        return "I'm glad to hear that. Keep noticing what helped you feel this way."

    elif "hello" in text or "hi" in text or "hey" in text:
        return "Hello 💜 How are you feeling today?"

    elif "overthinking" in text or "thinking too much" in text:
        return "Overthinking can be exhausting. Try writing down your thoughts and focusing on what you can control right now."

    elif "tired" in text or "exhausted" in text or "drained" in text:
        return "It sounds like you may be emotionally or physically tired. Rest, hydration, and gentle self-care can help."

    elif "angry" in text or "frustrated" in text:
        return "Anger is a valid emotion. Try stepping away for a moment and taking a few slow breaths."

    elif "sleep" in text or "insomnia" in text or "can't sleep" in text:
        return "Sleep issues can affect mental health a lot. Try reducing screen time and doing slow breathing before bed."

    elif "panic" in text or "panic attack" in text:
        return "Panic can feel intense, but it will pass. Try grounding yourself: name 5 things you see, 4 you can touch, 3 you hear."

    elif "motivation" in text or "unmotivated" in text or "lazy" in text:
        return "It's okay to have low motivation sometimes. Start with one very small task."

    elif "cry" in text or "crying" in text:
        return "Crying is a natural emotional release. Be gentle with yourself right now."

    else:
        return "Thank you for sharing that with me. Your feelings matter. Would you like to talk more about it?"


def get_support_message():
    return "You’re safe here. Take your time, breathe slowly, and remember that your feelings matter."

# -----------------------------------
# SESSION STATE
# -----------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "saved_moods" not in st.session_state:
    st.session_state.saved_moods = []

if "journal_entries" not in st.session_state:
    st.session_state.journal_entries = []

if "wellness_started" not in st.session_state:
    st.session_state.wellness_started = False

# -----------------------------------
# SIDEBAR
# -----------------------------------
st.sidebar.title("💜 MindEase AI")
menu = st.sidebar.radio(
    "Navigation",
    ["🏠 Dashboard", "💬 Chat Assistant", "😊 Mood Tracker", "🌿 Guided Breathing", "📔 Journal", "ℹ️ About"]
)

st.sidebar.markdown("---")
st.sidebar.write("Emotional support and wellness tools.")

# -----------------------------------
# HEADER
# -----------------------------------
st.markdown('<div class="main-title">MindEase AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">AI-Powered Mental Health Chatbot for Emotional Support and Wellness</div>', unsafe_allow_html=True)

# -----------------------------------
# DASHBOARD
# -----------------------------------
if menu == "🏠 Dashboard":
    st.markdown("""
    <div class="hero-box">
        <h2>Welcome to Your Wellness Space 💜</h2>
        <p>
            MindEase AI is designed to support emotional wellbeing through guided conversation,
            mood awareness, breathing support, journaling, and self-reflection.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="safe-box">
        <h3>🌸 Emotional Support Message</h3>
        <p style="font-size:17px;">{get_support_message()}</p>
    </div>
    """, unsafe_allow_html=True)

    # -----------------------------------
    # START YOUR WELLNESS CHECK
    # -----------------------------------
    st.markdown("""
    <div class="wellness-check">
        <h2 style="color:#5b57f0; margin-bottom:10px;">✨ Start Your Wellness Check</h2>
        <p style="font-size:17px; color:black;">
            A simple guided flow to help users begin their emotional wellness journey.
        </p>
    </div>
    """, unsafe_allow_html=True)

    step1, step2, step3 = st.columns(3, gap="large")

    with step1:
        st.markdown("""
        <div class="feature-card" style="text-align:left;">
            <h3>① Check Your Mood</h3>
            <p>Start by identifying how you feel right now.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Mood Tracker"):
            st.session_state.selected_page = "😊 Mood Tracker"
            st.rerun()

    with step2:
        st.markdown("""
        <div class="feature-card" style="text-align:left;">
            <h3>② Talk to MindEase AI</h3>
            <p>Share your emotions and receive supportive responses.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Chat Assistant"):
            st.session_state.selected_page = "💬 Chat Assistant"
            st.rerun()

    with step3:
        st.markdown("""
        <div class="feature-card" style="text-align:left;">
            <h3>③ Use a Wellness Tool</h3>
            <p>Try breathing, journaling, and calming support tools.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Wellness Tool"):
            st.session_state.selected_page = "🌿 Guided Breathing"
            st.rerun()

    # -----------------------------------
    # STATISTICS
    # -----------------------------------
    total_chats = len([m for m in st.session_state.messages if m["role"] == "user"])
    total_moods = len(st.session_state.saved_moods)
    total_journals = len(st.session_state.journal_entries)

    st.markdown("## 📊 Mood & Wellness Statistics")

    stat1, stat2, stat3 = st.columns(3, gap="large")

    with stat1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{total_chats}</div>
            <p>Chat Check-ins</p>
        </div>
        """, unsafe_allow_html=True)

    with stat2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{total_moods}</div>
            <p>Mood Entries</p>
        </div>
        """, unsafe_allow_html=True)

    with stat3:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{total_journals}</div>
            <p>Journal Notes</p>
        </div>
        """, unsafe_allow_html=True)

    # -----------------------------------
    # WELLNESS FEATURES
    # -----------------------------------
    st.markdown("## 🌼 Wellness Features")

    feat1, feat2, feat3 = st.columns(3, gap="large")

    with feat1:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size:42px;">💬</div>
            <h3>Chat Support</h3>
            <p>Talk with the AI chatbot and receive supportive emotional responses.</p>
        </div>
        """, unsafe_allow_html=True)

    with feat2:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size:42px;">😊</div>
            <h3>Mood Tracking</h3>
            <p>Track how you feel daily and build emotional awareness over time.</p>
        </div>
        """, unsafe_allow_html=True)

    with feat3:
        st.markdown("""
        <div class="feature-card">
            <div style="font-size:42px;">🌿</div>
            <h3>Guided Breathing</h3>
            <p>Use calming breathing exercises to regulate stress and anxiety.</p>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------
# CHAT PAGE
# -----------------------------------
if menu == "💬 Chat Assistant":
    st.markdown("""
    <div class="card">
        <h3>Chat with MindEase AI</h3>
        <p>Share how you’re feeling, and the chatbot will detect your mood and respond supportively.</p>
    </div>
    """, unsafe_allow_html=True)

    if len(st.session_state.messages) == 0:
        st.info("Start by typing a message below, such as 'I feel stressed' or 'I feel lonely'.")

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(
                f'<div class="chat-user"><b>You:</b><br>{msg["content"]}</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="chat-bot"><b>MindEase AI:</b><br><span class="small-text"><b>Detected Mood:</b> {msg["mood"]}</span><br><br>{msg["content"]}</div>',
                unsafe_allow_html=True
            )

    user_input = st.chat_input("Type your message here...")

    if user_input:
        mood = detect_mood(user_input)
        bot_reply = get_bot_response(user_input)

        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        st.session_state.messages.append({
            "role": "assistant",
            "content": bot_reply,
            "mood": mood
        })

        st.rerun()

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -----------------------------------
# MOOD TRACKER
# -----------------------------------
if menu == "😊 Mood Tracker":
    st.markdown("""
    <div class="card">
        <h3>Mood Tracker</h3>
        <p>Select your current mood and save it for self-reflection.</p>
    </div>
    """, unsafe_allow_html=True)

    mood = st.selectbox(
        "How are you feeling today?",
        ["😊 Happy", "😐 Neutral", "😟 Anxious", "😢 Sad", "😣 Stressed", "😴 Tired", "😠 Angry", "💔 Lonely"]
    )

    if st.button("Save Mood"):
        st.session_state.saved_moods.append(mood)
        st.success(f"Saved mood: {mood}")

    if st.session_state.saved_moods:
        st.subheader("Saved Mood Entries")
        for i, m in enumerate(st.session_state.saved_moods, start=1):
            st.write(f"{i}. {m}")

# -----------------------------------
# GUIDED BREATHING
# -----------------------------------
if menu == "🌿 Guided Breathing":
    st.markdown("""
    <div class="breathing-box">
        <h2>🌿 Guided Breathing Space</h2>
        <p>Use this simple breathing exercise whenever you feel anxious, overwhelmed, or stressed.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>💜 4 - 4 - 6 Calming Breath</h3>
        <p><b>Step 1:</b> Inhale slowly through your nose for <b>4 seconds</b>.</p>
        <p><b>Step 2:</b> Hold your breath gently for <b>4 seconds</b>.</p>
        <p><b>Step 3:</b> Exhale slowly through your mouth for <b>6 seconds</b>.</p>
        <p><b>Repeat this cycle 5 times.</b></p>
    </div>
    """, unsafe_allow_html=True)

    st.info("Try following the rhythm slowly: Inhale → Hold → Exhale")

    breath_col1, breath_col2, breath_col3 = st.columns(3)

    with breath_col1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">4</div>
            <p>Inhale</p>
        </div>
        """, unsafe_allow_html=True)

    with breath_col2:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">4</div>
            <p>Hold</p>
        </div>
        """, unsafe_allow_html=True)

    with breath_col3:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-number">6</div>
            <p>Exhale</p>
        </div>
        """, unsafe_allow_html=True)

    st.success("Breathing slowly can help reduce physical stress and calm your mind.")

# -----------------------------------
# JOURNAL
# -----------------------------------
if menu == "📔 Journal":
    st.markdown("""
    <div class="card">
        <h3>Daily Journal</h3>
        <p>Write your thoughts, feelings, or reflections privately.</p>
    </div>
    """, unsafe_allow_html=True)

    journal_text = st.text_area("Write here...", height=200)

    if st.button("Save Journal Entry"):
        if journal_text.strip():
            st.session_state.journal_entries.append(journal_text)
            st.success("Journal entry saved!")

    if st.session_state.journal_entries:
        st.subheader("Previous Entries")
        for i, entry in enumerate(st.session_state.journal_entries, start=1):
            st.markdown(f"**Entry {i}:** {entry}")

# -----------------------------------
# ABOUT
# -----------------------------------
if menu == "ℹ️ About":
    st.markdown("""
    <div class="card">
        <h3>About MindEase AI</h3>
        <p>
            MindEase AI is an AI-powered mental health chatbot developed to provide
            emotional support, mood awareness, guided breathing, journaling support,
            and wellness-focused self-care interaction.
        </p>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------
# FOOTER
# -----------------------------------
st.markdown("---")
st.markdown("""
<div style="
    background-color: #fff4cc;
    color: black;
    padding: 15px;
    border-radius: 12px;
    font-weight: 500;
    border-left: 6px solid #f4b400;
">
⚠️ This chatbot is for emotional support only and is not a replacement for professional medical or mental health care.
</div>
""", unsafe_allow_html=True)