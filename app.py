import streamlit as st
import time
import random

st.set_page_config(page_title="Bestie Surprise 💖", layout="centered")

# ---------- STATE ----------
if "step" not in st.session_state:
    st.session_state.step = 0
if "typing_done" not in st.session_state:
    st.session_state.typing_done = False
if "current_joke" not in st.session_state:
    st.session_state.current_joke = ""

# ---------- CSS ----------
st.markdown("""
<style>
/* Full background gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(120deg, #ff99cc, #ff66b3, #ff3399);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    overflow: hidden;
}
@keyframes gradientBG {
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}

/* Remove Streamlit padding */
.block-container { padding: 0 !important; margin: 0 !important; }

/* Lock screen */
html, body, [data-testid="stAppViewContainer"] {
    height: 100%;
    overflow: hidden;
    margin: 0;
    padding: 0;
}

/* Centered container */
.full-center {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 100%;
    max-width: 650px;
}

/* Typing text */
.typing {
    font-size: clamp(20px, 4.5vw, 28px);
    font-weight: 700;
    color: #fff;
    margin: 10px 0;
    white-space: pre-wrap;
    word-wrap: break-word;
    opacity: 0;
    animation: fadeIn 0.7s forwards;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Button styling */
.stButton { display: flex; justify-content: center; margin-top: 20px; }
.stButton button {
    font-size: clamp(14px, 3.5vw, 18px) !important;
    padding: 12px 26px !important;
    border-radius: 14px;
    background: linear-gradient(45deg, #ff4da6, #ff80bf);
    color: #fff;
    border: 0;
    font-weight: 700;
    width: min(260px, 80%);
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    transition: all 0.5s ease-in-out;
}
.stButton button:hover {
    transform: scale(1.05);
    background: linear-gradient(45deg, #ff3399, #ff66b2);
}

/* Smooth fade for container */
.fade-container {
    animation: fadeContainer 0.6s ease-in-out;
}
@keyframes fadeContainer {
    from {opacity: 0;}
    to {opacity: 1;}
}

/* Floating hearts for love step */
@keyframes floatHeart {
    0% { transform: translateY(0) rotate(0deg); opacity:1; }
    100% { transform: translateY(-600px) rotate(360deg); opacity:0; }
}
.heart {
    position: fixed;
    color: #ff66b2;
    font-size: 24px;
    animation: floatHeart 6s linear infinite;
    z-index: 9999;
}

/* Twinkling stars in background */
@keyframes twinkle {
    0%, 100% {opacity: 0.3;}
    50% {opacity: 1;}
}
.star {
    position: fixed;
    color: #fff;
    font-size: 12px;
    animation: twinkle 2s infinite;
    z-index: 1;
}
</style>
""", unsafe_allow_html=True)

# ---------- Typing ----------
def type_line(line: str, container, speed: float = 0.04):
    out = ""
    for ch in line:
        out += ch
        container.markdown(f"<div class='typing'>{out}</div>", unsafe_allow_html=True)
        time.sleep(speed)
    container.markdown(f"<div class='typing'>{line}</div>", unsafe_allow_html=True)
    time.sleep(0.25)

def type_lines(lines, box, speed: float = 0.04):
    for line in lines:
        line_spot = box.empty()
        type_line(line, line_spot, speed)

# ---------- Helpers ----------
def clear_and_go(next_step: int, root_placeholder):
    st.session_state.step = next_step
    st.session_state.typing_done = False
    root_placeholder.empty()
    st.rerun()

def new_joke():
    jokes = [
        "👩‍🏫 Teacher: Tum late kyu aaye?\n😅 Pappu: Sir, board pe likha tha 'School Ahead, Go Slow'...\n🤣 to main dheere aaya!",
        "😆 Why don’t scientists trust atoms?\nBecause they make up everything!",
        "😂 I told my computer I needed a break, and it said: 'No problem — I'll go to sleep.'",
        "😹 Why did the scarecrow win an award?\nBecause he was outstanding in his field!",
        "😅 I would tell you a joke about construction, but I'm still working on it.",
        "🤣 Why did the math book look sad?\nBecause it had too many problems.",
        "😂 Why can’t your nose be 12 inches long?\nBecause then it would be a foot!",
        "😆 Why did the coffee file a police report?\nIt got mugged.",
        "😹 Parallel lines have so much in common… it’s a shame they’ll never meet.",
        "😂 Why don’t programmers like nature?\nIt has too many bugs.",
        "🤣 How does a penguin build its house?\nIgloos it together.",
        "😅 What do you call fake spaghetti?\nAn impasta!",
        "😂 Why did the bicycle fall over?\nBecause it was two-tired.",
        "😆 What do you call cheese that isn't yours?\nNacho cheese!",
        "🤣 Why did the tomato turn red?\nBecause it saw the salad dressing!"
    ]
    st.session_state.current_joke = random.choice(jokes)

# ---------- Floating Hearts ----------
def floating_hearts(n=10):
    hearts_html = ""
    for i in range(n):
        left = random.randint(5, 95)
        delay = random.uniform(0, 5)
        hearts_html += f'<div class="heart" style="left:{left}%; animation-delay:{delay}s;">❤️</div>'
    st.markdown(hearts_html, unsafe_allow_html=True)

# ---------- Twinkling Stars ----------
def twinkling_stars(n=30):
    stars_html = ""
    for i in range(n):
        left = random.randint(0, 100)
        top = random.randint(0, 100)
        size = random.randint(8, 16)
        delay = random.uniform(0, 3)
        stars_html += f'<div class="star" style="left:{left}%; top:{top}%; font-size:{size}px; animation-delay:{delay}s;">✦</div>'
    st.markdown(stars_html, unsafe_allow_html=True)

# ---------- MAIN ----------
root = st.empty()
with root.container():
    twinkling_stars(30)  # Add stars in background
    st.markdown('<div class="full-center fade-container">', unsafe_allow_html=True)
    lines_box = st.container()

    # Step 0: Surprise Box
    if st.session_state.step == 0:
        
        lines = ["🎁 Surprise!"]
        if not st.session_state.typing_done:
            type_lines(lines, lines_box, speed=0.05)
            st.session_state.typing_done = True
        else:
            for l in lines:
                lines_box.markdown(f"<div class='typing'>{l}</div>", unsafe_allow_html=True)
        if st.session_state.typing_done and st.button("✨ Open Gift"):
            st.balloons()
            
            clear_and_go(1, root)

    # Step 1: Welcome
    elif st.session_state.step == 1:
        lines = ["💖 Welcome 💖", "💖 My dear Bestie 💖"]
        if not st.session_state.typing_done:
            type_lines(lines, lines_box, speed=0.04)
            st.session_state.typing_done = True
        else:
            for l in lines:
                lines_box.markdown(f"<div class='typing'>{l}</div>", unsafe_allow_html=True)
        if st.session_state.typing_done and st.button("😂 Tell me a Joke"):
            new_joke()
        
            clear_and_go(2, root)

    # Step 2: Random Joke
    elif st.session_state.step == 2:
        if st.session_state.current_joke == "":
            new_joke()
        lines = st.session_state.current_joke.split("\n")
        if not st.session_state.typing_done:
            type_lines(lines, lines_box, speed=0.035)
            st.session_state.typing_done = True
        else:
            for l in lines:
                lines_box.markdown(f"<div class='typing'>{l}</div>", unsafe_allow_html=True)

        col1, col2 = st.columns([1,1])
        with col1:
            if st.button("💖 Show Love"):
                clear_and_go(3, root)
        with col2:
            if st.button("🔄 Refresh Joke"):
                new_joke()
                st.session_state.typing_done = False
                st.rerun()

    # Step 3: Love Messages with hearts
    elif st.session_state.step == 3:
        floating_hearts(15)
        lines = [
            "💖 May your life always overflow with happiness & laughter!",
            "🌸 You deserve all the joy in the world, Bestie!",
            "⭐ Keep shining bright like the star you are!",
            "🤗 Stay happy, smiling, and forever amazing!"
        ]
        if not st.session_state.typing_done:
            st.balloons()
            type_lines(lines, lines_box, speed=0.035)
            st.session_state.typing_done = True
        else:
            for l in lines:
                lines_box.markdown(f"<div class='typing'>{l}</div>", unsafe_allow_html=True)

        if st.session_state.typing_done and st.button("🔄 Start Again"):
            clear_and_go(0, root)

    st.markdown('</div>', unsafe_allow_html=True)
