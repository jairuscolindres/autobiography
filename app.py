from pathlib import Path
import base64
import numpy as np
import pandas as pd
import streamlit as st

# ---------------------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Jairus Colindres | Archive & Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# Authentic Frutiger Aero Archive Assets (Zero External Dependencies)
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets_fa"

def get_b64(path: Path) -> str:
    if path.exists():
        return base64.b64encode(path.read_bytes()).decode("utf-8")
    return ""

B64_LOGO = get_b64(ASSETS_DIR / "logo.png")
B64_INTRO = get_b64(ASSETS_DIR / "introduction.png")
B64_HISTORY = get_b64(ASSETS_DIR / "history.png")
B64_RESOURCES = get_b64(ASSETS_DIR / "resources.png")
B64_WALLPAPERS = get_b64(ASSETS_DIR / "wallpapers.png")
B64_BLOG = get_b64(ASSETS_DIR / "blog.png")
B64_LINKS = get_b64(ASSETS_DIR / "download_links.png")
B64_ICONS = get_b64(ASSETS_DIR / "icons.png")
B64_PROFILE = get_b64(BASE_DIR / "profile.jpg")

# Wallpaper: Windows Longhorn wallpaper from Frutiger Aero Archive
LONGHORN_PATH = ASSETS_DIR / "longhorn.jpg"
if not LONGHORN_PATH.exists():
    LONGHORN_PATH = BASE_DIR / "aero_bubbles_grass.jpg"
B64_BG = get_b64(LONGHORN_PATH)
BG_DATA_URL = f"data:image/jpeg;base64,{B64_BG}" if B64_BG else ""

# ---------------------------------------------------------------------------
# Session & Navigation State
# ---------------------------------------------------------------------------
PAGES = ["Introduction", "Autobiography", "Skills", "Projects", "Contact"]

# Synchronize query parameters with session state
query_page = st.query_params.get("page")
if query_page and query_page in PAGES:
    st.session_state.current_page = query_page
elif "current_page" not in st.session_state:
    st.session_state.current_page = "Introduction"

current_page = st.session_state.current_page

if "messages" not in st.session_state:
    st.session_state.messages = []
if "show_dream" not in st.session_state:
    st.session_state.show_dream = False

# ---------------------------------------------------------------------------
# Frutiger Aero Archive Design System (Direct replica of frutigeraeroarchive.org)
# ---------------------------------------------------------------------------
AERO_STYLE = f"""
<style>
/* Typography: Classic Segoe UI & Tahoma */
*, body, h1, h2, h3, h4, p, span, div, label, input, button {{
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif, Arial, Helvetica, sans-serif !important;
}}

/* Hide standard modern Streamlit sidebar, modern header bar, and default footer */
[data-testid="stSidebar"], 
section[data-testid="stSidebar"], 
[data-testid="collapsedControl"],
header[data-testid="stHeader"],
footer {{
    display: none !important;
}}

/* Desktop fixed wallpaper & background styling */
.stApp {{
    background-color: #121915 !important;
    background-image: url('{BG_DATA_URL}') !important;
    background-size: cover !important;
    background-position: center center !important;
    background-attachment: fixed !important;
    color: #dadada !important;
}}

/* Bounded centered container matching #websiteContainer */
.block-container {{
    max-width: 960px !important;
    margin: 18px auto 40px auto !important;
    padding: 0 10px !important;
}}

/* Top Semicircle Chrome Header (#mainHeader) */
#mainHeader {{
    background: linear-gradient(180deg, rgba(172,172,172,.92) 0, rgba(71,71,71,.92) 20%, rgba(19,19,19,.92) 40%, rgba(7,7,7,.95) 100%);
    border-right: 1px solid #4e4e4e;
    border-left: 1px solid #4e4e4e;
    border-top: 2px solid #5a5a5a;
    border-bottom: 2px solid #111111;
    border-radius: 40px 40px 0 0;
    padding: 10px 18px 10px 20px;
    box-shadow: rgba(0,0,0,.5) 0 14px 28px, rgba(0,0,0,.4) 0 10px 10px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    position: relative;
    z-index: 10;
    margin-bottom: 0px;
}}

.header-left {{
    display: flex;
    align-items: center;
    gap: 12px;
}}

#logo {{
    height: 38px;
    width: auto;
    filter: drop-shadow(0 2px 4px rgba(0,0,0,0.6));
    transition: filter 0.3s ease;
}}
#logo:hover {{
    filter: brightness(1.2) drop-shadow(0 0 8px rgba(60,218,86,0.8));
}}

.header-title-text {{
    font-size: 19px;
    font-weight: 700;
    color: #ffffff !important;
    letter-spacing: 0.4px;
    text-shadow: 0 1px 4px #000000, 0 0 10px rgba(0,0,0,0.8);
    line-height: 1.2;
}}

.header-subtitle-text {{
    font-size: 12px;
    color: #9eccaa !important;
    letter-spacing: 0.2px;
    text-shadow: 0 1px 2px #000000;
    margin-top: 2px;
}}


/* Two-column container styling */
div[data-testid="stHorizontalBlock"] {{
    gap: 0px !important;
}}

/* Navigation column (#navigationMenu) */
div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-child {{
    background: linear-gradient(to bottom, rgba(26,26,26,.90), rgba(20,20,20,.92) 95%) !important;
    border-left: 1px solid #4b4b4b !important;
    border-right: 1px solid #4b4b4b !important;
    border-bottom: 1px solid #4b4b4b !important;
    border-bottom-left-radius: 35px !important;
    padding: 12px 10px 18px 10px !important;
    box-shadow: rgba(0,0,0,.5) 0 14px 28px, rgba(0,0,0,.4) 0 10px 10px !important;
}}

/* Main Content column (#mainContent) */
div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:last-child {{
    background: rgba(28, 28, 28, 0.85) !important;
    border-right: 1px solid #3b3b3b !important;
    border-bottom: 1px solid #3b3b3b !important;
    border-left: 1px solid #222222 !important;
    border-bottom-right-radius: 35px !important;
    padding: 14px 18px 22px 18px !important;
    box-shadow: rgba(0,0,0,.5) 0 14px 28px, rgba(0,0,0,.4) 0 10px 10px !important;
    color: #dadada !important;
}}

/* Frutiger Aero Navigation Boxes & Titles */
.nav-categories {{
    outline: rgba(28,49,39,.5) solid 1px;
    background: linear-gradient(to bottom, rgba(80,80,80,.2), rgba(39,39,39,.1));
    border: 1px solid rgba(236,242,249,.2);
    border-radius: 4px;
    box-shadow: 2px 2px 3px rgba(0,0,0,.8);
    display: flex;
    flex-direction: column;
    padding: 2px 2px 4px 2px;
    margin-bottom: 8px;
}}

.navbar-titles {{
    background: linear-gradient(to bottom, #fff 0, rgba(129,129,129,.75) 3%, rgba(56,56,56,.75) 50%, rgba(27,27,27,.75) 50%);
    border: 1px solid #000;
    border-radius: 3px;
    color: #f7f4f4 !important;
    padding: 1px 4px;
    margin: 1px 1px 3px;
    font-size: 11.5px;
    height: 18px;
    font-weight: 600;
    text-align: center;
    text-shadow: 0 1px 2px #000;
    display: block;
}}

.nav-icons {{
    height: 18px;
    width: 18px;
    margin: 1px 6px 1px 4px;
    z-index: 1;
    object-fit: contain;
}}

/* Nav active / inactive links */
.nav-active, .nav-inactive {{
    border: 1px solid #0f0f0f;
    border-radius: 3px;
    color: #dadada !important;
    display: flex;
    align-items: center;
    margin: 1px auto;
    width: 95%;
    font-size: 12px;
    padding: 4px 6px;
    text-decoration: none !important;
    position: relative;
    box-sizing: border-box;
    transition: all 0.15s ease;
}}

.nav-active {{
    background: linear-gradient(to bottom, rgba(255,255,255,.25) 0, rgba(117,117,117,.2) 20%, rgba(92,92,92,.2) 40%, rgba(29,73,23,.3) 40%, rgba(43,240,36,.7) 100%) !important;
    color: #57fa6f !important;
    font-weight: 700;
    border-color: #148d28 !important;
    box-shadow: 0 0 6px rgba(60,218,86,0.4);
}}

.nav-inactive {{
    background: linear-gradient(to bottom, rgba(255,255,255,.25) 0, rgba(117,117,117,.15) 20%, rgba(92,92,92,.15) 60%, rgba(0,0,0,.3) 60%, rgba(41,41,41,.3) 100%);
}}

.nav-inactive:hover {{
    background: linear-gradient(to bottom, rgba(255,255,255,.25) 0, rgba(117,117,117,.2) 20%, rgba(92,92,92,.2) 50%, rgba(43,43,43,.3) 50%, rgba(161,161,161,.3) 100%);
    color: #ffffff !important;
    border-color: #555555;
}}

/* Profile box inside left navigation */
.profile-box {{
    text-align: center;
    padding: 8px 6px;
    margin-bottom: 8px;
    border: 1px solid rgba(236,242,249,.15);
    background: rgba(18, 18, 18, 0.65);
    border-radius: 4px;
    box-shadow: inset 0 0 4px rgba(0,0,0,0.8);
}}

.profile-avatar-frame {{
    width: 90px;
    height: 90px;
    margin: 0 auto 6px auto;
    border: 2px solid #4b4b4b;
    border-radius: 3px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.8), inset 0 0 3px rgba(255,255,255,0.2);
    overflow: hidden;
    background: #000;
}}

.profile-avatar-frame img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
}}

.profile-name {{
    font-size: 13px;
    font-weight: 700;
    color: #ffffff !important;
    text-shadow: 0 1px 2px #000;
}}

.profile-meta {{
    font-size: 11px;
    color: #9eccaa !important;
    line-height: 1.35;
    margin-top: 2px;
}}

/* Metallic Chrome Bar Headers (h1, h2, h3) */
h1, h2, h3, [data-testid="stHeadingWithActionElements"] h1, [data-testid="stHeadingWithActionElements"] h2, [data-testid="stHeadingWithActionElements"] h3 {{
    background: linear-gradient(to bottom, #bebebe 0, #777 3%, #232323 55%, #000 55%, #161616 98%, #000 100%) !important;
    box-shadow: rgba(0,0,0,.4) 0 3px 8px !important;
    border: 1px solid #000000 !important;
    border-top: 1px solid #707070 !important;
    border-radius: 3px 3px 0 0 !important;
    color: #f7f4f4 !important;
    padding: 4px 10px !important;
    display: flex !important;
    align-items: center !important;
    font-weight: 600 !important;
    font-size: 14.5px !important;
    text-shadow: 0 0 3px #000000 !important;
    margin-top: 8px !important;
    margin-bottom: 0px !important;
    letter-spacing: 0.3px !important;
}}

/* Skeuomorphic Glass Container (.styled-containers) */
.styled-containers {{
    background: rgba(27, 27, 27, 0.85);
    border: 1px solid rgba(236,242,249,.2);
    border-top: none;
    border-radius: 0 0 3px 3px;
    box-shadow: rgba(0,0,0,.4) 0 3px 8px;
    padding: 10px 12px;
    margin-bottom: 12px;
    color: #dadada !important;
    font-size: 13.5px;
    line-height: 1.6;
}}

/* Full borders when not directly under a header */
.styled-containers-full {{
    border-top: 1px solid rgba(236,242,249,.2);
    border-radius: 3px;
}}

/* Authentic Windows Longhorn Green Skeuomorphic Buttons */
div.stButton > button,
div[data-testid="stFormSubmitButton"] > button,
div[data-testid="stDownloadButton"] > button {{
    background: linear-gradient(to bottom, #fff 0, #82f577 3%, #32912a 40%, #185815 55%, #0b3112 55%, #1a5c1e 100%) !important;
    border: 1px solid #000000 !important;
    border-radius: 3px !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 12.5px !important;
    text-shadow: 0 1px 2px rgba(0,0,0,0.85) !important;
    box-shadow: 1px 1px 5px rgba(0,0,0,.4), inset 0 1px 0 rgba(255,255,255,0.4) !important;
    padding: 4px 12px !important;
    transition: all 0.15s ease !important;
    cursor: pointer !important;
}}

div.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover,
div[data-testid="stDownloadButton"] > button:hover {{
    background: linear-gradient(to bottom, #fff 0, #9efd96 3%, #32912a 40%, #185815 55%, #0b3112 55%, #47e951 100%) !important;
    box-shadow: 0 0 8px rgba(60,218,86,0.6), inset 0 1px 0 rgba(255,255,255,0.5) !important;
    color: #ffffff !important;
    transform: scale(1.01);
}}

div.stButton > button:active,
div[data-testid="stFormSubmitButton"] > button:active,
div[data-testid="stDownloadButton"] > button:active {{
    background: linear-gradient(to bottom, #0b3112 0%, #185815 50%, #32912a 100%) !important;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.7) !important;
    transform: scale(0.99);
}}

/* High-Contrast Skeuomorphic Metric Panels (NO TRUNCATION) */
div[data-testid="stMetric"] {{
    background: rgba(20, 20, 20, 0.90) !important;
    border: 1px solid rgba(236,242,249,.25) !important;
    border-top: 2px solid #3cda56 !important;
    border-radius: 3px !important;
    padding: 8px 12px !important;
    box-shadow: 2px 2px 4px rgba(0,0,0,0.6), inset 0 1px 0 rgba(255,255,255,0.08) !important;
}}
div[data-testid="stMetricValue"] {{
    white-space: normal !important;
    word-break: normal !important;
    overflow: visible !important;
    text-overflow: clip !important;
    font-size: 1.15rem !important;
    line-height: 1.25 !important;
    color: #57fa6f !important;
    font-weight: 700 !important;
    text-shadow: 0 0 4px rgba(0,0,0,0.9) !important;
}}
div[data-testid="stMetricLabel"] {{
    white-space: normal !important;
    word-break: normal !important;
    overflow: visible !important;
    text-overflow: clip !important;
    color: #a0cfa7 !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    font-size: 0.72rem !important;
    letter-spacing: 0.05em !important;
}}

/* Form Controls & Inputs */
div[data-testid="stTextInput"] input, 
div[data-testid="stTextArea"] textarea, 
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {{
    background: rgba(18, 18, 18, 0.92) !important;
    border: 1px solid #4b4b4b !important;
    border-radius: 3px !important;
    color: #eeeeee !important;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.7) !important;
    font-size: 13px !important;
}}

div[data-testid="stTextInput"] input:focus, 
div[data-testid="stTextArea"] textarea:focus {{
    border-color: #3cda56 !important;
    box-shadow: 0 0 6px rgba(60, 218, 86, 0.5), inset 0 1px 2px rgba(0,0,0,0.8) !important;
    outline: none !important;
}}

/* Tables with Chrome Header */
table {{
    border-collapse: collapse !important;
    width: 100% !important;
    border: 1px solid #4b4b4b !important;
    margin: 6px 0 !important;
    box-shadow: 2px 2px 4px rgba(0,0,0,0.6) !important;
}}
th {{
    background: linear-gradient(to bottom, #bebebe 0, #777 3%, #232323 55%, #000 55%, #161616 98%, #000 100%) !important;
    color: #ffffff !important;
    font-weight: 600 !important;
    padding: 6px 10px !important;
    border: 1px solid #4b4b4b !important;
    font-size: 12.5px !important;
    text-shadow: 0 0 3px #000 !important;
}}
td {{
    background: rgba(22, 22, 22, 0.88) !important;
    color: #dadada !important;
    padding: 6px 10px !important;
    border: 1px solid #383838 !important;
    font-size: 12.5px !important;
}}
tr:hover td {{
    background: rgba(35, 60, 35, 0.88) !important;
    color: #ffffff !important;
}}

/* Links */
a {{
    color: #3cda56 !important;
    text-decoration: none !important;
}}
a:hover {{
    color: #57fa6f !important;
    text-decoration: underline !important;
}}

/* Tags / Stack Pills */
.aero-tag {{
    background: rgba(20, 35, 25, 0.85);
    color: #bdf7c5;
    padding: 2px 7px;
    border-radius: 3px;
    font-size: 11.5px;
    font-weight: 600;
    border: 1px solid #2d7a3a;
    display: inline-block;
    margin-right: 4px;
    margin-bottom: 4px;
    box-shadow: 1px 1px 3px rgba(0,0,0,0.5);
}}

/* Bottom Semicircle Chrome Footer (#pageNav) */
#pageNav {{
    background: linear-gradient(to bottom, #1a1a1a 50%, #242424 70%, #313131 85%, #3d3d3d 100%);
    box-shadow: 1px 5px 1px #3d3d3d, rgba(0,0,0,.5) 0 14px 28px;
    border-right: 1px solid #4e4e4e;
    border-left: 1px solid #4e4e4e;
    border-bottom: 2px solid #5a5a5a;
    border-top: 1px solid #222222;
    border-radius: 0 0 40px 40px;
    padding: 10px 18px;
    margin-top: 0px;
    text-align: center;
    position: relative;
    z-index: 10;
}}

.footer-text {{
    font-size: 12px;
    color: #a0a0a0 !important;
    margin: 0;
    text-shadow: 0 1px 2px #000;
}}
</style>
"""

st.markdown(AERO_STYLE, unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Data Definitions
# ---------------------------------------------------------------------------
NAME = "Jairus Jasper Colindres"
PROGRAM = "BS Computer Science"
YEAR = "3rd year"
SECTION = "F2"
SCHOOL = "Cebu Institute of Technology - University (CIT-U)"
TAGLINE = "Computer Science student, CTF player, and future solarpunk farmer"
EMAIL = "colindresjairus@gmail.com"
GITHUB = "https://github.com/jairuscolindres"

SKILLS = pd.DataFrame(
    {
        "Skill": [
            "Capture the Flag (CTF)",
            "Problem Solving",
            "Cybersecurity",
            "Web Security",
            "C++",
            "Python",
            "Linux",
            "Data Structures & Algorithms",
            "Java",
            "Networking",
            "Self-Directed Learning",
        ],
        "Level": [75, 75, 70, 65, 60, 55, 65, 55, 50, 45, 80],
    }
)

PROJECTS = [
    {
        "title": "CITU Intramurals Website (TTSP)",
        "role": "Project Manager",
        "tools": ["Next.js", "Prisma", "Supabase", "Git", "GitHub"],
        "outcome": (
            "I was still a probationary member (probee) at the time. We had a ticketing "
            "system, and I was the one fixing logical and visual bugs during production."
        ),
    },
    {
        "title": "CSS Acquaintance Party Registration System",
        "role": "Initial Developer",
        "tools": ["SharePoint", "Microsoft Forms", "Power Automate"],
        "outcome": (
            "Built for the Computer Student Society (CSS). We reduced overall check-in "
            "time by 50% compared to last year."
        ),
    },
    {
        "title": "Table Monitoring System",
        "role": "Developer",
        "tools": ["Arduino", "ESP32", "WebSockets", "IR Sensors"],
        "outcome": "My first introduction to coding an actual project as a solution.",
    },
]

MILESTONES = pd.DataFrame(
    {
        "Year": ["2026", "2025", "2024", "Senior high", "Elementary"],
        "Milestone": [
            "Our team won champion in the Hack4Gov Region 7 CTF, representing our school",
            "My first hackathon, with random people I didn't know. We communicated in Tagalog",
            "First serious coding project: the Table Monitoring System",
            "Took the STEM track and became much more open-minded about ideas and principles",
            "Competed in MTAP year after year; our school won champion across all grade levels",
        ],
    }
)

INTERESTS = {
    "Arts and entertainment": [
        "Drawing and painting",
        "Learning piano and guitar",
        "Reading sci-fi and fantasy",
        "Writing stories and worldbuilding",
    ],
    "Fitness and health": [
        "Strength training and calisthenics",
        "Walking at least 10k steps a day",
    ],
    "Career-related": [
        "Building coding projects from scratch",
        "Hardware hacking (my old router)",
    ],
}

BACKGROUND = (
    "I was born on January 20, 2006, in the City of Naga, Cebu, and that's where I grew up. "
    "For most of my childhood, my father worked overseas as an electrician and my mother was "
    "a science teacher. Today my parents serve as pastors in Antique, and I live in Cebu City "
    "with my sister, whom I respect most for her grit. I also have an older brother who works "
    "as an electrical engineer on a ship and a younger brother who is also still in school."
)

EDUCATION = (
    "<strong>Elementary:</strong> At Langtad Elementary School, I joined the MTAP competitions year after "
    "year. My proudest moment was when our school won champion across all grade levels.<br><br>"
    "<strong>Junior high:</strong> I went to CIT-U and met some really smart people.<br><br>"
    "<strong>Senior high:</strong> I stayed at CIT-U and took the STEM track. This is when my eyes opened, "
    "and I became much more open-minded about ideas, opinions, philosophies, and principles.<br><br>"
    "<strong>College:</strong> I'm a Computer Science student at CIT-U, now in my 3rd year, doing my best "
    "to survive the curriculum."
)

BEYOND_CLASS = (
    "• Website manager, <strong>The Technologian Student Press</strong><br>"
    "• Member, Committee on Innovation and Research, <strong>Computer Student Society</strong><br>"
    "• Official player, <strong>CTF club</strong>"
)

BELIEF = (
    "I have a lot of values, but the one I hold above all the others is <strong>honesty to myself</strong>. "
    "It comes down to how much I value my own existence. If there's something I'm not being "
    "honest with myself about, then I'm confused about who I really am. That means I don't "
    "actually know who I am. If my idea of me isn't who I really am, then my sense of myself "
    "is wrong, and I have to ask: who has been existing in my body this whole time?"
)

DREAM = (
    "My biggest dream is to build a scientific community where people help each other, a "
    "solarpunk community for science and for the arts, with my own library, music studio, "
    "farm, homelab, and more. I know that's a big one, so my smaller dream is to live the "
    "solarpunk life myself, with a self-sufficient farm, a solar grid, and a bunch of other "
    "good things."
)

# ---------------------------------------------------------------------------
# Top Header Bar (#mainHeader)
# ---------------------------------------------------------------------------
logo_html = f'<img src="data:image/png;base64,{B64_LOGO}" id="logo" alt="Logo">' if B64_LOGO else ''

header_html = f"""
<div id="mainHeader">
    <div class="header-left">
        {logo_html}
        <div>
            <div class="header-title-text">{NAME}</div>
            <div class="header-subtitle-text">{PROGRAM} · {YEAR} · {SCHOOL}</div>
        </div>
    </div>
</div>
"""
st.markdown(header_html, unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Main 2-Column Layout
# ---------------------------------------------------------------------------
left_col, right_col = st.columns([1, 2.75], gap="small")

# ---------------------------------------------------------------------------
# Left Column: Navigation & Identity (Direct frutigeraeroarchive.org design)
# ---------------------------------------------------------------------------
with left_col:
    # Profile Card
    avatar_img = f'<img src="data:image/jpeg;base64,{B64_PROFILE}" alt="Profile">' if B64_PROFILE else ''
    profile_html = f"""
    <div class="profile-box">
        <div class="profile-avatar-frame">
            {avatar_img}
        </div>
        <div class="profile-name">{NAME}</div>
        <div class="profile-meta">{PROGRAM} · {YEAR}</div>
        <div class="profile-meta">Section {SECTION} · CIT-U</div>
    </div>
    """
    st.markdown(profile_html, unsafe_allow_html=True)

    # Navigation Links Box
    def nav_link(page_name: str, icon_b64: str, label: str) -> str:
        is_active = (current_page == page_name)
        cls_name = "nav-active" if is_active else "nav-inactive"
        icon_tag = f'<img src="data:image/png;base64,{icon_b64}" class="nav-icons" alt="{label}">' if icon_b64 else ''
        return f'<a href="?page={page_name}" class="{cls_name}" target="_self">{icon_tag}{label}</a>'

    nav_menu_html = f"""
    <nav class="nav-categories" aria-label="Navigation Category: Main Content">
        <span class="navbar-titles">Main Content</span>
        {nav_link("Introduction", B64_INTRO, "Introduction")}
        {nav_link("Autobiography", B64_HISTORY, "Autobiography")}
        {nav_link("Skills", B64_RESOURCES, "Skills & Stack")}
        {nav_link("Projects", B64_WALLPAPERS, "Projects")}
        {nav_link("Contact", B64_BLOG, "Contact")}
    </nav>
    """
    st.markdown(nav_menu_html, unsafe_allow_html=True)

    # Links Box
    ext_icon = f'<img src="data:image/png;base64,{B64_LINKS}" class="nav-icons" alt="Link">' if B64_LINKS else ''
    links_html = f"""
    <nav class="nav-categories" aria-label="Navigation Category: Links">
        <span class="navbar-titles">Connect</span>
        <a href="{GITHUB}" target="_blank" class="nav-inactive">
            {ext_icon}GitHub Profile
        </a>
        <a href="mailto:{EMAIL}" class="nav-inactive">
            {ext_icon}Email Me
        </a>
    </nav>
    """
    st.markdown(links_html, unsafe_allow_html=True)


    # Motto Card
    st.markdown(
        """
        <div class="styled-containers styled-containers-full" style="font-size: 11.5px; font-style: italic; color: #a4cfa8 !important; text-align: center; margin-top: 8px;">
            "Building open technology in service of ecology, community, and human curiosity."
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------------------------
# Right Column: Main Content Area
# ---------------------------------------------------------------------------
with right_col:
    # -----------------------------------------------------------------------
    # PAGE 1: Introduction
    # -----------------------------------------------------------------------
    if current_page == "Introduction":
        st.markdown("<h1>Introduction</h1>", unsafe_allow_html=True)
        st.markdown(
            f"""
            <div class="styled-containers">
                <p style="margin-bottom: 8px;">
                    Hi, I'm <strong>Jairus</strong>. {TAGLINE}.
                </p>
                <p>
                    Welcome to my personal archive and portfolio. I enjoy building things from scratch, 
                    competing in cybersecurity CTFs, exploring network hardware, and working toward 
                    sustainable, community-focused technology. Explore my autobiography, technical skills, 
                    and completed projects using the menu on the left.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<h2>Academic & Competition Highlights</h2>", unsafe_allow_html=True)
        # Using [1, 1, 1.45] ensures Team Champion NEVER truncates
        m1, m2, m3 = st.columns([1, 1, 1.45])
        with m1:
            st.metric("Academic Year", YEAR)
        with m2:
            st.metric("Projects Built", f"{len(PROJECTS)} Completed")
        with m3:
            st.metric("Regional CTF", "Team Champion")

        st.markdown("<h2>Quick Overview</h2>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class="styled-containers">
                <p><strong>Background:</strong> Born and raised in Naga, Cebu; currently surviving 3rd-year CS at CIT-U.</p>
                <p style="margin-top: 6px;"><strong>Core Principle:</strong> Honesty to myself above all other values.</p>
                <p style="margin-top: 6px;"><strong>Key Affiliations:</strong> The Technologian Student Press, Computer Student Society, and CIT-U CTF Club.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # -----------------------------------------------------------------------
    # PAGE 2: Autobiography
    # -----------------------------------------------------------------------
    elif current_page == "Autobiography":
        st.markdown("<h1>Autobiography & History</h1>", unsafe_allow_html=True)
        
        st.markdown("<h2>Background</h2>", unsafe_allow_html=True)
        st.markdown(f'<div class="styled-containers"><p>{BACKGROUND}</p></div>', unsafe_allow_html=True)

        st.markdown("<h2>Education</h2>", unsafe_allow_html=True)
        st.markdown(f'<div class="styled-containers"><p>{EDUCATION}</p></div>', unsafe_allow_html=True)

        st.markdown("<h2>Beyond Class</h2>", unsafe_allow_html=True)
        st.markdown(f'<div class="styled-containers"><p>{BEYOND_CLASS}</p></div>', unsafe_allow_html=True)

        st.markdown("<h2>Core Philosophy</h2>", unsafe_allow_html=True)
        st.markdown(f'<div class="styled-containers"><p>{BELIEF}</p></div>', unsafe_allow_html=True)

        st.markdown("<h2>Interests & Pursuits</h2>", unsafe_allow_html=True)
        with st.container():
            picked = st.multiselect(
                "Filter interest categories:",
                options=list(INTERESTS.keys()),
                default=list(INTERESTS.keys()),
            )
            interests_html = '<div class="styled-containers">'
            for cat in picked:
                interests_html += f'<div style="font-weight:700; color:#57fa6f; margin-top:4px;">{cat}</div><ul style="margin:2px 0 8px 18px; padding:0;">'
                for item in INTERESTS[cat]:
                    interests_html += f'<li style="color:#dadada;">{item}</li>'
                interests_html += '</ul>'
            interests_html += '</div>'
            st.markdown(interests_html, unsafe_allow_html=True)

        st.markdown("<h2>Milestones</h2>", unsafe_allow_html=True)
        st.table(MILESTONES.set_index("Year"))

        st.markdown("<h2>Where I'm Headed</h2>", unsafe_allow_html=True)
        st.markdown(
            '<div class="styled-containers">'
            '<p>I have both a long-term grand vision and a personal day-to-day commitment to technology and self-reliance.</p>'
            '</div>',
            unsafe_allow_html=True,
        )

        col_d1, col_d2 = st.columns([1, 1])
        with col_d1:
            if st.button("Reveal Big Dream", use_container_width=True):
                st.session_state.show_dream = not st.session_state.show_dream
        with col_d2:
            autobio_txt = (
                f"{NAME}\n{PROGRAM}, {YEAR}, Section {SECTION}\n{SCHOOL}\n\n"
                f"BACKGROUND\n{BACKGROUND}\n\n"
                f"EDUCATION\n{EDUCATION.replace('<strong>', '').replace('</strong>', '').replace('<br>', chr(10))}\n\n"
                f"CORE PHILOSOPHY\n{BELIEF.replace('<strong>', '').replace('</strong>', '')}\n\n"
                f"WHERE I'M HEADED\n{DREAM}\n"
            )
            st.download_button(
                "Download Autobiography (.txt)",
                data=autobio_txt,
                file_name="jairus_colindres_autobiography.txt",
                mime="text/plain",
                use_container_width=True,
            )

        if st.session_state.show_dream:
            st.markdown(
                f"""
                <div class="styled-containers styled-containers-full" style="border-left: 3px solid #3cda56; margin-top: 10px; background: rgba(20, 35, 20, 0.85);">
                    <div style="font-weight: 700; color: #57fa6f; margin-bottom: 4px;">Vision & Community Horizon</div>
                    <p style="margin: 0;">{DREAM}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # -----------------------------------------------------------------------
    # PAGE 3: Skills & Stack
    # -----------------------------------------------------------------------
    elif current_page == "Skills":
        st.markdown("<h1>Skills & Stack</h1>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class="styled-containers">
                <p>
                    Python and web development are my strongest skills, followed by capture the flag (CTF). 
                    Hardware hacking is the domain I'm currently exploring. The values below reflect self-ratings out of 100.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        ctrl_col, chart_col = st.columns([1, 2], gap="medium")
        with ctrl_col:
            st.markdown("<h2>Filters</h2>", unsafe_allow_html=True)
            min_lvl = st.slider("Min Proficiency", 0, 100, 0, step=10)
            sort_choice = st.selectbox("Sort Order", ["Highest first", "Lowest first", "Alphabetical"])
            chart_kind = st.radio("Chart Type", ["Bar Chart", "Area Chart"], horizontal=True)
            show_tbl = st.checkbox("Show Data Table", value=True)

        with chart_col:
            st.markdown("<h2>Visualization</h2>", unsafe_allow_html=True)
            filtered = SKILLS[SKILLS["Level"] >= min_lvl].copy()
            if sort_choice == "Highest first":
                filtered = filtered.sort_values("Level", ascending=False)
            elif sort_choice == "Lowest first":
                filtered = filtered.sort_values("Level")
            else:
                filtered = filtered.sort_values("Skill")

            if filtered.empty:
                st.warning("No skills match the specified threshold.")
            else:
                st.metric("Average Proficiency", f"{np.mean(filtered['Level']):.0f} / 100")
                series_data = filtered.set_index("Skill")["Level"]
                if chart_kind == "Bar Chart":
                    st.bar_chart(series_data, color="#3cda56")
                else:
                    st.area_chart(series_data, color="#3cda56")
                if show_tbl:
                    st.dataframe(
                        filtered,
                        hide_index=True,
                        use_container_width=True,
                        column_config={
                            "Level": st.column_config.ProgressColumn(
                                "Proficiency", min_value=0, max_value=100, format="%d%%"
                            )
                        },
                    )

    # -----------------------------------------------------------------------
    # PAGE 4: Projects
    # -----------------------------------------------------------------------
    elif current_page == "Projects":
        st.markdown("<h1>Projects & Works</h1>", unsafe_allow_html=True)
        search_kw = st.text_input(
            "Search projects by tool, keyword, or role:",
            placeholder="Try: Next.js, Arduino, Manager, Developer",
        ).strip().lower()

        matched = [
            p for p in PROJECTS
            if not search_kw
            or search_kw in p["title"].lower()
            or search_kw in p["role"].lower()
            or any(search_kw in t.lower() for t in p["tools"])
        ]

        if not matched:
            st.warning("No projects matched your criteria.")
        else:
            for prj in matched:
                st.markdown(f"<h2>{prj['title']}</h2>", unsafe_allow_html=True)
                tag_spans = " ".join(f'<span class="aero-tag">{t}</span>' for t in prj["tools"])
                st.markdown(
                    f"""
                    <div class="styled-containers">
                        <div style="margin-bottom: 6px;">
                            <strong>Role:</strong> <span style="color:#57fa6f;">{prj['role']}</span>
                        </div>
                        <div style="margin-bottom: 8px;">
                            <strong>Stack:</strong> {tag_spans}
                        </div>
                        <div>
                            <strong>Outcome:</strong>
                            <p style="margin-top: 4px;">{prj['outcome']}</p>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    # -----------------------------------------------------------------------
    # PAGE 5: Contact
    # -----------------------------------------------------------------------
    elif current_page == "Contact":
        st.markdown("<h1>Contact & Guestbook</h1>", unsafe_allow_html=True)
        f_col, i_col = st.columns([1.8, 1.2], gap="medium")

        with f_col:
            st.markdown("<h2>Send a Message</h2>", unsafe_allow_html=True)
            with st.form("contact_archive_form", clear_on_submit=True):
                c_name = st.text_input("Your Name")
                c_email = st.text_input("Your Email (optional)")
                c_topic = st.selectbox("Topic", ["General Inquiries", "Project Collaboration", "Feedback"])
                c_msg = st.text_area("Message", height=110)
                c_rating = st.slider("Rating", 1, 5, 5)
                c_reply = st.checkbox("I would like a reply")
                c_submit = st.form_submit_button("Send Message")

            if c_submit:
                if not c_name.strip() or not c_msg.strip():
                    st.error("Please enter both your name and message.")
                elif c_reply and "@" not in c_email:
                    st.error("Please provide a valid email address so I can reply.")
                else:
                    st.session_state.messages.append(
                        {"From": c_name.strip(), "Topic": c_topic, "Rating": f"{c_rating}/5"}
                    )
                    st.success(f"Message received! Thank you, {c_name.strip()}.")

        with i_col:
            st.markdown("<h2>Direct Details</h2>", unsafe_allow_html=True)
            st.markdown(
                f"""
                <div class="styled-containers">
                    <p><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></p>
                    <p style="margin-top: 6px;"><strong>GitHub:</strong> <a href="{GITHUB}" target="_blank">{GITHUB}</a></p>
                    <p style="margin-top: 6px; font-size: 11.5px; color: #a0a0a0;">
                        Messages submitted via the guestbook form are recorded during your session. 
                        For professional inquiries, reach out via email.
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if st.session_state.messages:
                st.markdown("<h2>Messages Received</h2>", unsafe_allow_html=True)
                st.dataframe(pd.DataFrame(st.session_state.messages), hide_index=True, use_container_width=True)

# ---------------------------------------------------------------------------
# Semicircle Bottom Footer Bar (#pageNav)
# ---------------------------------------------------------------------------
footer_html = f"""
<div id="pageNav">
    <p class="footer-text">
        {NAME} · {PROGRAM} · {YEAR} · Section {SECTION} · {SCHOOL}
    </p>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
