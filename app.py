import streamlit as st
from content import SLIDES

st.set_page_config(
    page_title="Червона панда — Ailurus fulgens",
    page_icon="🐼",
    layout="centered",
)

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp { background: #1A0F08; }

.block-container {
    padding-top: 0.5rem !important;
    padding-bottom: 0.5rem !important;
    max-width: 1000px !important;
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}

.slide-card {
    background: #2B1810;
    border: 1px solid #4A2818;
    border-radius: 18px;
    padding: 1.5rem 1.8rem;
    text-align: center;
    margin: 0.5rem 0;
    animation: fadeInUp 0.6s ease-out;
    box-shadow: 0 10px 40px rgba(232, 93, 42, 0.15);
}
.slide-emoji { font-size: 3rem; margin-bottom: 0.5rem; }
.slide-title { font-size: 1.7rem; font-weight: 800; color: #F5E6D3; margin-bottom: 0.3rem; }
.slide-subtitle { font-size: 1rem; color: #E85D2A; margin-bottom: 1rem; font-weight: 600; }
.slide-text { font-size: 0.95rem; color: #D4B89C; line-height: 1.7; text-align: left; white-space: pre-line; }
.progress-text { text-align: center; color: #8B6F5A; font-size: 0.85rem; margin-bottom: 0.3rem; }

.element-container { margin-bottom: 0.3rem !important; }
.stProgress { margin-bottom: 0.4rem !important; }

div[data-testid="stProgress"] > div > div { background-color: #3A2218 !important; }
.stProgress > div > div { background-color: #3A2218 !important; }
div[role="progressbar"] { background-color: #3A2218 !important; }
div[data-testid="stProgress"] > div > div > div { background-color: #E85D2A !important; }
.stProgress > div > div > div { background-color: #E85D2A !important; }
div[role="progressbar"] > div { background-color: #E85D2A !important; }

.stButton > button,
div[data-testid="stButton"] > button {
    background-color: #E85D2A !important;
    color: #F5E6D3 !important;
    border: 1px solid #E85D2A !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: 0.4rem 1rem !important;
}
.stButton > button:hover,
div[data-testid="stButton"] > button:hover {
    background-color: #FF7A3D !important;
    border-color: #FF7A3D !important;
    color: #FFFFFF !important;
}
.stButton > button:focus,
div[data-testid="stButton"] > button:focus {
    box-shadow: none !important;
}

/* ===== ТОЧКИ НАВИГАЦИИ ===== */
.dots-container {
    display: flex;
    justify-content: center;
    gap: 0.5rem;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
}
.dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background-color: #4A2818;
    display: inline-block;
    transition: all 0.3s ease;
}
.dot.active {
    background-color: #E85D2A;
    transform: scale(1.3);
    box-shadow: 0 0 10px rgba(232, 93, 42, 0.6);
}
</style>
""", unsafe_allow_html=True)

if "slide" not in st.session_state:
    st.session_state.slide = 0

total = len(SLIDES)
current = st.session_state.slide
slide = SLIDES[current]

st.markdown(f'<p class="progress-text">Слайд {current + 1} з {total}</p>', unsafe_allow_html=True)
st.progress((current + 1) / total)

st.markdown(f'<div class="slide-card">'
            f'<div class="slide-emoji">{slide["emoji"]}</div>'
            f'<div class="slide-title">{slide["title"]}</div>'
            f'<div class="slide-subtitle">{slide["subtitle"]}</div>'
            f'<div class="slide-text">{slide["text"]}</div>'
            f'</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if current > 0:
        if st.button("← Назад", use_container_width=True):
            st.session_state.slide -= 1
            st.rerun()
with col3:
    if current < total - 1:
        if st.button("Далі →", use_container_width=True):
            st.session_state.slide += 1
            st.rerun()
    else:
        if st.button("🏁 На початок", use_container_width=True):
            st.session_state.slide = 0
            st.rerun()

# Точки навигации
dots_html = '<div class="dots-container">'
for i in range(total):
    active = "active" if i == current else ""
    dots_html += f'<span class="dot {active}"></span>'
dots_html += '</div>'
st.markdown(dots_html, unsafe_allow_html=True)