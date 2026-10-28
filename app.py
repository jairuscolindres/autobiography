from pathlib import Path
import base64

import numpy as np
import pandas as pd
import streamlit as st

# ---------------------------------------------------------------------------
# Page setup
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Jairus Colindres | Aero Portfolio",
    page_icon="🫧",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Background wallpaper resolution (Iconic Frutiger Aero Bubbles & Grass)
# ---------------------------------------------------------------------------
WALLPAPER_LOCAL = Path(__file__).parent / "aero_bubbles_grass.jpg"
if not WALLPAPER_LOCAL.exists():
    WALLPAPER_LOCAL = Path(__file__).parent / "aero_wallpaper.png"

if WALLPAPER_LOCAL.exists():
    b64_wallpaper = base64.b64encode(WALLPAPER_LOCAL.read_bytes()).decode("utf-8")
    BG_URL = f"data:image/jpeg;base64,{b64_wallpaper}"
else:
    BG_URL = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Frutiger_Aero_Bubbles_And_Grass.jpg/1280px-Frutiger_Aero_Bubbles_And_Grass.jpg"

# ---------------------------------------------------------------------------
# Authentic 2000s Frutiger Aero Design System (Windows Vista / 7 & Aqua Skeuomorphism)
# ---------------------------------------------------------------------------
AERO_CSS = """
<style>
/* True Frutiger Aero Typography: Segoe UI, Frutiger, Lucida Grande, Tahoma */
* {
    font-family: 'Segoe UI', 'Frutiger', 'Lucida Grande', Tahoma, Verdana, Arial, sans-serif !important;
}

/* Frutiger Aero Vibrant Desktop Canvas */
.stApp {
    background-color: #2980b9;
    background-image: 
        radial-gradient(ellipse at 50% 15%, rgba(255, 255, 255, 0.45) 0%, rgba(135, 206, 250, 0.25) 40%, transparent 75%),
        url('__BG_URL__');
    background-size: cover;
    background-position: center center;
    background-attachment: fixed;
    color: #0c2b45;
}

/* Windows Vista Acrylic Frosted Glass Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(135deg, rgba(230, 245, 255, 0.82) 0%, rgba(200, 235, 255, 0.72) 50%, rgba(175, 220, 250, 0.82) 100%) !important;
    backdrop-filter: blur(24px) saturate(190%) !important;
    -webkit-backdrop-filter: blur(24px) saturate(190%) !important;
    border-right: 2px solid rgba(255, 255, 255, 0.9) !important;
    box-shadow: 4px 0 25px rgba(0, 70, 140, 0.3), inset -1px 0 2px rgba(255, 255, 255, 0.8) !important;
}

/* Aero Headings with classic Vista white halo glow */
h1, h2, h3, h4, h5 {
    color: #073a61 !important;
    font-weight: 700 !important;
    letter-spacing: -0.01em;
    text-shadow: 0 1px 0 #ffffff, 0 0 10px rgba(180, 230, 255, 0.9), 0 0 18px rgba(100, 200, 255, 0.6) !important;
}

/* Windows Vista / 7 Aero Glass Main Window Shell */
.aero-window {
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.92) 0%, rgba(240, 248, 255, 0.82) 48%, rgba(225, 242, 255, 0.78) 52%, rgba(235, 248, 255, 0.90) 100%);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border: 1px solid rgba(255, 255, 255, 0.95);
    border-top: 2px solid rgba(255, 255, 255, 1);
    border-radius: 10px;
    box-shadow: 
        0 12px 35px rgba(0, 60, 120, 0.35),
        inset 0 1px 2px #ffffff,
        inset 0 -1px 3px rgba(0, 120, 215, 0.3);
    margin-bottom: 1.5rem;
    overflow: hidden;
}

/* Authentic Aero Titlebar */
.aero-titlebar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: linear-gradient(180deg, 
        rgba(255, 255, 255, 0.95) 0%, 
        rgba(215, 238, 252, 0.85) 45%, 
        rgba(152, 212, 248, 0.80) 50%, 
        rgba(195, 232, 252, 0.90) 100%);
    border-bottom: 1px solid rgba(135, 195, 235, 0.8);
    box-shadow: inset 0 1px 1px #ffffff, 0 1px 4px rgba(0, 70, 140, 0.15);
    padding: 0.45rem 0.85rem;
    font-size: 0.86rem;
    font-weight: 700;
    color: #0b3d63;
    text-shadow: 0 1px 0 #ffffff;
}
.aero-titlebar-left {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.aero-window-controls {
    display: flex;
    gap: 4px;
    align-items: center;
}
.win-ctrl-btn {
    display: inline-flex;
    justify-content: center;
    align-items: center;
    width: 26px;
    height: 18px;
    border-radius: 3px;
    font-size: 10px;
    font-weight: bold;
    cursor: default;
    border: 1px solid rgba(120, 170, 210, 0.7);
    background: linear-gradient(180deg, #ffffff 0%, #d8ecf8 50%, #b8def4 100%);
    box-shadow: inset 0 1px 0 #ffffff, 0 1px 2px rgba(0, 0, 0, 0.15);
    color: #2b5470;
}
.win-ctrl-btn.close {
    background: linear-gradient(180deg, #fca29a 0%, #e65245 50%, #cc2b1d 100%);
    border-color: #a82015;
    color: #ffffff;
    text-shadow: 0 1px 1px #590f0a;
}

/* Windows Vista Explorer Breadcrumb Toolbar */
.aero-toolbar {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    background: linear-gradient(180deg, #fdfefe 0%, #eaf3f9 50%, #d5e7f3 100%);
    border-bottom: 1px solid #a8cde5;
    padding: 0.4rem 0.85rem;
    font-size: 0.82rem;
    color: #19466b;
    box-shadow: inset 0 1px 0 #ffffff;
}
.aero-nav-circle {
    display: inline-flex;
    justify-content: center;
    align-items: center;
    width: 26px;
    height: 26px;
    border-radius: 50%;
    background: linear-gradient(180deg, #ffffff 0%, #bde1f7 48%, #67bbf0 52%, #85cdf5 100%);
    border: 1px solid #4a9fd5;
    box-shadow: inset 0 1px 1px #ffffff, 0 2px 5px rgba(0, 90, 180, 0.25);
    color: #0b3d63;
    font-size: 0.85rem;
    font-weight: bold;
}
.aero-address-box {
    flex-grow: 1;
    background: #ffffff;
    border: 1px solid #89b8dc;
    border-radius: 4px;
    padding: 0.25rem 0.65rem;
    box-shadow: inset 0 1px 2px rgba(0, 60, 120, 0.15);
    display: flex;
    align-items: center;
    gap: 0.4rem;
    font-size: 0.82rem;
    color: #0d3858;
}

/* Vista Sidebar Gadget Container */
.vista-gadget {
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.9) 0%, rgba(225, 245, 255, 0.75) 50%, rgba(200, 235, 255, 0.85) 100%);
    border: 1px solid rgba(255, 255, 255, 0.95);
    border-radius: 12px;
    padding: 0.85rem 1rem;
    margin-bottom: 1rem;
    box-shadow: 
        0 4px 15px rgba(0, 70, 140, 0.15),
        inset 0 1px 2px #ffffff,
        inset 0 -1px 2px rgba(0, 130, 220, 0.2);
}
.vista-gadget-title {
    font-size: 0.84rem;
    font-weight: 700;
    color: #02538c;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 0.5rem;
    border-bottom: 1px solid rgba(90, 170, 230, 0.35);
    padding-bottom: 0.25rem;
    text-shadow: 0 1px 0 #ffffff;
}

/* Vista Yellow Sticky Note Gadget */
.vista-note {
    background: linear-gradient(180deg, #fffbc7 0%, #fff7a1 100%);
    border: 1px solid #edd96a;
    border-radius: 4px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15), inset 0 1px 1px #fff;
    padding: 0.75rem 0.9rem;
    font-size: 0.82rem;
    color: #5c4d15;
    line-height: 1.45;
    font-style: italic;
    position: relative;
    margin-bottom: 1rem;
}
.vista-note::before {
    content: "📌";
    position: absolute;
    top: -10px;
    left: 45%;
    font-size: 14px;
}

/* Vista Acrylic Glass Content Panel */
.aero-panel {
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.92) 0%, rgba(240, 248, 255, 0.80) 48%, rgba(225, 243, 255, 0.72) 52%, rgba(235, 249, 255, 0.88) 100%);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.95);
    border-radius: 12px;
    padding: 1.25rem;
    margin-bottom: 1.1rem;
    box-shadow: 
        0 8px 25px rgba(0, 70, 140, 0.12),
        inset 0 1px 2px #ffffff,
        inset 0 -1px 2px rgba(0, 140, 230, 0.15);
}

/* Streamlit Container border=True override for Aero glass */
div[data-testid="stVerticalBlock"] > div[data-testid="stContainer"] {
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.92) 0%, rgba(240, 248, 255, 0.80) 48%, rgba(225, 243, 255, 0.72) 52%, rgba(235, 249, 255, 0.88) 100%) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    border: 1px solid rgba(255, 255, 255, 0.95) !important;
    border-radius: 12px !important;
    padding: 1.1rem !important;
    box-shadow: 
        0 8px 25px rgba(0, 70, 140, 0.12),
        inset 0 1px 2px #ffffff,
        inset 0 -1px 2px rgba(0, 140, 230, 0.15) !important;
}

/* Windows Vista Performance Gadgets (Metrics) */
div[data-testid="stMetric"] {
    background: linear-gradient(180deg, 
        #ffffff 0%, 
        #ebf5fc 46%, 
        #cbe5f7 48%, 
        #aee0fb 52%, 
        #cde9fa 100%) !important;
    backdrop-filter: blur(12px) !important;
    border: 1px solid #7cbde6 !important;
    border-radius: 12px !important;
    padding: 0.75rem 1rem !important;
    box-shadow: 
        0 4px 14px rgba(0, 80, 160, 0.18),
        inset 0 1px 2px #ffffff,
        inset 0 -1px 2px rgba(0, 110, 210, 0.3) !important;
}
div[data-testid="stMetricValue"] {
    white-space: normal !important;
    word-break: break-word !important;
    overflow: visible !important;
    text-overflow: clip !important;
    font-size: 1.55rem !important;
    color: #015088 !important;
    font-weight: 800 !important;
    text-shadow: 0 1px 0 #ffffff, 0 0 8px rgba(110, 200, 255, 0.7) !important;
}
div[data-testid="stMetricLabel"] {
    white-space: normal !important;
    word-break: break-word !important;
    overflow: visible !important;
    text-overflow: clip !important;
    color: #0a4670 !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.05em !important;
    text-shadow: 0 1px 0 #ffffff !important;
}

/* Skeuomorphic Aqua / Vista 3D Glossy Pill Buttons */
div.stButton > button, div[data-testid="stLinkButton"] > a {
    background: linear-gradient(180deg, 
        #ffffff 0%, 
        #eaf6fd 45%, 
        #b8e2fa 46%, 
        #72c6f6 50%, 
        #90d5f8 80%, 
        #c4eafc 100%) !important;
    color: #06395b !important;
    border: 1px solid #52a8dc !important;
    border-radius: 22px !important;
    font-weight: 700 !important;
    box-shadow: 
        inset 0 1px 1px #ffffff, 
        inset 0 -1px 2px rgba(0, 70, 140, 0.25), 
        0 3px 8px rgba(0, 100, 180, 0.22) !important;
    transition: all 0.2s ease !important;
    text-shadow: 0 1px 0 rgba(255, 255, 255, 0.9) !important;
    padding: 0.5rem 1.35rem !important;
}
div.stButton > button:hover, div[data-testid="stLinkButton"] > a:hover {
    background: linear-gradient(180deg, 
        #ffffff 0%, 
        #dbf2fe 45%, 
        #9ad9f9 46%, 
        #41b5f4 50%, 
        #6bc8f7 80%, 
        #b0e4fc 100%) !important;
    border-color: #1e92d8 !important;
    color: #022c47 !important;
    box-shadow: 
        inset 0 1px 2px #ffffff, 
        0 0 14px rgba(0, 180, 255, 0.65),
        0 4px 10px rgba(0, 80, 160, 0.25) !important;
    transform: translateY(-1px);
}
div.stButton > button:active, div[data-testid="stLinkButton"] > a:active {
    background: linear-gradient(180deg, #62bef3 0%, #35a8eb 50%, #1f9ce7 100%) !important;
    box-shadow: inset 0 2px 5px rgba(0, 50, 100, 0.4) !important;
    transform: translateY(1px);
}

/* Windows Vista Property Page Navigation Tabs */
div[data-testid="stTabs"] {
    border-bottom: 2px solid #64b5f6 !important;
    margin-bottom: 1.25rem !important;
}
div[data-testid="stTabs"] button[role="tab"] {
    background: linear-gradient(180deg, #f7fafd 0%, #e1eef8 48%, #cbe3f5 50%, #d8ecf8 100%) !important;
    border: 1px solid #94b9d6 !important;
    border-bottom: none !important;
    border-radius: 8px 8px 0 0 !important;
    color: #1e4a6d !important;
    font-weight: 600 !important;
    font-size: 0.94rem !important;
    padding: 0.55rem 1.4rem !important;
    margin-right: 4px !important;
    box-shadow: inset 0 1px 0 #ffffff, 0 -1px 3px rgba(0, 60, 120, 0.08) !important;
    transition: all 0.2s ease !important;
}
div[data-testid="stTabs"] button[role="tab"]:hover {
    background: linear-gradient(180deg, #ffffff 0%, #e8f4fc 48%, #d6ebf9 50%, #e4f2fc 100%) !important;
    border-color: #5aa5d8 !important;
    color: #025087 !important;
    box-shadow: 0 0 10px rgba(0, 170, 255, 0.35) !important;
}
div[data-testid="stTabs"] button[aria-selected="true"] {
    background: linear-gradient(180deg, #ffffff 0%, #edf7ff 48%, #dcf0fd 50%, #ffffff 100%) !important;
    border: 1px solid #5aa5d8 !important;
    border-top: 3px solid #00a3e0 !important;
    border-bottom: 2px solid #ffffff !important;
    color: #014373 !important;
    font-weight: 700 !important;
    box-shadow: 0 -3px 10px rgba(0, 160, 240, 0.3) !important;
    transform: translateY(2px);
}

/* Windows 7 Green Liquid Progress Bar */
div[data-testid="stProgressBar"] > div {
    background-color: #e0f2fe !important;
    border: 1px solid #8ec8f0 !important;
    border-radius: 10px !important;
    overflow: hidden !important;
    height: 18px !important;
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.15) !important;
}
div[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(180deg, #e4fce0 0%, #7ee673 48%, #3bd22b 50%, #5fe052 100%) !important;
    border-radius: 8px !important;
    box-shadow: inset 0 1px 1px #ffffff, inset 0 -1px 2px rgba(0, 80, 0, 0.3) !important;
}

/* Glass Details Grid Table */
table {
    border-collapse: separate !important;
    border-spacing: 0 !important;
    border-radius: 8px !important;
    overflow: hidden !important;
    border: 1px solid #8ec5eb !important;
    box-shadow: 0 4px 14px rgba(0, 70, 140, 0.1), inset 0 1px 1px #ffffff !important;
    width: 100% !important;
}
th {
    background: linear-gradient(180deg, #ffffff 0%, #e6f3fc 50%, #cde5f7 100%) !important;
    color: #064069 !important;
    font-weight: 700 !important;
    padding: 0.65rem 0.85rem !important;
    border-bottom: 1px solid #7fbbe4 !important;
    text-shadow: 0 1px 0 #ffffff !important;
}
td {
    background: rgba(255, 255, 255, 0.88) !important;
    color: #0e2f4a !important;
    padding: 0.65rem 0.85rem !important;
    border-bottom: 1px solid #e1eff8 !important;
}
tr:hover td {
    background: linear-gradient(180deg, #f0f8ff 0%, #dcf0fd 100%) !important;
}

/* Beveled Glass Form Controls */
div[data-testid="stTextInput"] input, 
div[data-testid="stTextArea"] textarea, 
div[data-testid="stSelectbox"] div[data-baseweb="select"] {
    background: #ffffff !important;
    border: 1px solid #7fbce4 !important;
    border-radius: 6px !important;
    color: #0b2f4c !important;
    box-shadow: inset 0 1px 3px rgba(0, 60, 120, 0.15) !important;
    font-size: 0.9rem !important;
}
div[data-testid="stTextInput"] input:focus, 
div[data-testid="stTextArea"] textarea:focus {
    border-color: #0099e6 !important;
    box-shadow: 0 0 8px rgba(0, 170, 255, 0.5), inset 0 1px 2px rgba(0, 0, 0, 0.1) !important;
}

/* Vista Aurora Dreamscape Card */
.aurora-dream-card {
    background: linear-gradient(135deg, 
        rgba(255, 255, 255, 0.95) 0%, 
        rgba(215, 248, 235, 0.90) 35%, 
        rgba(185, 235, 255, 0.90) 70%, 
        rgba(225, 245, 255, 0.95) 100%);
    border: 1px solid #78d2b8;
    border-left: 5px solid #20c997;
    border-radius: 10px;
    padding: 1.25rem;
    box-shadow: 0 8px 24px rgba(32, 201, 151, 0.2), inset 0 1px 2px #ffffff;
    margin-top: 1rem;
}

/* Windows 7 Aero Taskbar / Status Footer */
.aero-taskbar-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: linear-gradient(180deg, 
        rgba(235, 247, 255, 0.90) 0%, 
        rgba(180, 222, 250, 0.80) 45%, 
        rgba(130, 198, 242, 0.85) 50%, 
        rgba(165, 218, 250, 0.92) 100%);
    backdrop-filter: blur(16px);
    border-top: 1px solid rgba(255, 255, 255, 0.95);
    border-radius: 6px;
    padding: 0.5rem 1rem;
    margin-top: 2rem;
    box-shadow: 0 -2px 10px rgba(0, 70, 140, 0.15), inset 0 1px 1px #ffffff;
    font-size: 0.82rem;
    font-weight: 600;
    color: #0b3d63;
}
.aero-start-orb {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    background: linear-gradient(180deg, #ffffff 0%, #c4e4f8 50%, #68bbf0 100%);
    border: 1px solid #3d9ed6;
    border-radius: 14px;
    padding: 0.18rem 0.65rem;
    font-size: 0.78rem;
    box-shadow: inset 0 1px 1px #ffffff, 0 1px 4px rgba(0, 0, 0, 0.15);
}
</style>
""".replace("__BG_URL__", BG_URL)

st.markdown(AERO_CSS, unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Content definitions
# ---------------------------------------------------------------------------
NAME = "Jairus Jasper Colindres"
PROGRAM = "BS Computer Science"
YEAR = "3rd year"
SECTION = "F2"
SCHOOL = "Cebu Institute of Technology - University (CIT-U)"
TAGLINE = "Computer Science student, CTF player, and future solarpunk farmer"
EMAIL = "colindresjairus@gmail.com"
GITHUB = "https://github.com/jairuscolindres"
PHOTO = Path(__file__).parent / "profile.jpg"

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
            "Data Structures and Algorithms",
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
    "**Elementary:** At Langtad Elementary School, I joined the MTAP competitions year after "
    "year. My proudest moment was when our school won champion across all grade levels.\n\n"
    "**Junior high:** I went to CIT-U and met some really smart people.\n\n"
    "**Senior high:** I stayed at CIT-U and took the STEM track. This is when my eyes opened, "
    "and I became much more open-minded about ideas, opinions, philosophies, and principles.\n\n"
    "**College:** I'm a Computer Science student at CIT-U, now in my 3rd year, doing my best "
    "to survive the curriculum."
)

BEYOND_CLASS = (
    "- Website manager, **The Technologian Student Press**\n"
    "- Member, Committee on Innovation and Research, **Computer Student Society**\n"
    "- Official player, **CTF club**"
)

BELIEF = (
    "I have a lot of values, but the one I hold above all the others is **honesty to myself**. "
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
# Session state
# ---------------------------------------------------------------------------
if "kudos" not in st.session_state:
    st.session_state.kudos = 0
if "messages" not in st.session_state:
    st.session_state.messages = []
if "show_dream" not in st.session_state:
    st.session_state.show_dream = False

# ---------------------------------------------------------------------------
# Windows Vista Sidebar (Gadget Deck)
# ---------------------------------------------------------------------------
with st.sidebar:
    st.markdown(
        """
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.6rem;">
            <span style="font-size: 0.76rem; font-weight: 700; color: #064b7c; text-transform: uppercase;">Windows Sidebar</span>
            <span style="font-size: 0.9rem;">➕ ⚙️</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Gadget 1: Identity Card
    st.markdown(
        f"""
        <div class="vista-gadget">
            <div class="vista-gadget-title">👤 User Profile</div>
            <div style="font-weight: 700; font-size: 1.05rem; color: #08406b;">{NAME}</div>
            <div style="color: #0077c8; font-weight: 600; font-size: 0.88rem;">{PROGRAM}</div>
            <div style="font-size: 0.82rem; color: #2e5978;">{YEAR} · Section <strong>{SECTION}</strong></div>
            <div style="font-size: 0.78rem; color: #537d99; margin-top: 0.25rem;">{SCHOOL}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Gadget 2: Quick Links
    st.markdown('<div class="vista-gadget"><div class="vista-gadget-title">🌐 Quick Launch</div>', unsafe_allow_html=True)
    st.link_button("GitHub Profile", GITHUB, use_container_width=True)
    st.link_button("Send Email", f"mailto:{EMAIL}", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Gadget 3: Interactive Kudos Meter
    st.markdown(
        f"""
        <div class="vista-gadget">
            <div class="vista-gadget-title">✨ Kudos Gauge</div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                <span style="font-size: 0.82rem; color: #1e5277;">Visits / Kudos:</span>
                <span style="background: linear-gradient(180deg, #00b4d8 0%, #0077b6 100%); color: #fff; padding: 0.15rem 0.55rem; border-radius: 12px; font-weight: bold; font-size: 0.85rem; box-shadow: inset 0 1px 1px #fff;">{st.session_state.kudos}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("🫧 Send Kudos", use_container_width=True):
        st.session_state.kudos += 1
    if st.session_state.kudos >= 3:
        st.success("🌟 Thank you! Kudos registered!")

    # Gadget 4: Vista Sticky Note
    st.markdown(
        """
        <div class="vista-note">
            "Building open technology in service of ecology, community, and human curiosity."
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------------------------
# Windows Aero Main Explorer Window
# ---------------------------------------------------------------------------
st.markdown(
    f"""
    <div class="aero-window">
        <div class="aero-titlebar">
            <div class="aero-titlebar-left">
                <span>🫧</span>
                <span>{NAME} - Windows Aero Explorer</span>
            </div>
            <div class="aero-window-controls">
                <span class="win-ctrl-btn">—</span>
                <span class="win-ctrl-btn">▢</span>
                <span class="win-ctrl-btn close">✕</span>
            </div>
        </div>
        <div class="aero-toolbar">
            <span class="aero-nav-circle">◀</span>
            <span class="aero-nav-circle" style="opacity: 0.5;">▶</span>
            <div class="aero-address-box">
                <span>💻</span>
                <span>Computer</span>
                <span>▶</span>
                <span>Local Disk (C:)</span>
                <span>▶</span>
                <span>Portfolio</span>
                <span>▶</span>
                <strong>{NAME}</strong>
            </div>
            <span style="color: #0b3d63; font-weight: bold;">🔍 Search</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Hero Profile Block
photo_col, about_col = st.columns([1, 2], gap="large")

with photo_col:
    with st.container(border=True):
        if PHOTO.exists():
            st.image(str(PHOTO), caption=NAME, use_container_width=True)
        else:
            st.info("📷 **Photo placeholder:** Place profile.jpg in workspace.")

with about_col:
    with st.container(border=True):
        st.markdown(f"<h2 style='margin-top:0;'>{NAME}</h2>", unsafe_allow_html=True)
        st.markdown(
            f"<p style='font-size: 1.05rem; line-height: 1.6; color: #0c3352;'>Hi, I'm <strong>Jairus</strong>. {TAGLINE}. "
            "I enjoy building things from scratch, from coding projects to exploring network hardware and designing sustainable systems. "
            "Welcome to my autobiography, values, and interactive project portfolio.</p>",
            unsafe_allow_html=True,
        )
        m1, m2, m3 = st.columns(3)
        m1.metric("Academic Year", YEAR)
        m2.metric("Featured Works", f"{len(PROJECTS)} Projects")
        m3.metric("Regional CTF", "Team Champion 🏆")

st.divider()

# ---------------------------------------------------------------------------
# Windows Property Page Tabs (4 Tabs)
# ---------------------------------------------------------------------------
tab_bio, tab_skills, tab_projects, tab_contact = st.tabs(
    ["📖 Autobiography", "🛠️ Skills Explorer", "🚀 Project Portfolio", "✉️ Contact & Feedback"]
)

# ---- Tab 1: Autobiography ------------------------------------------------
with tab_bio:
    col_bio_left, col_bio_right = st.columns(2, gap="large")

    with col_bio_left:
        with st.container(border=True):
            st.subheader("📁 Background & Origins")
            st.write(BACKGROUND)

        with st.container(border=True):
            st.subheader("🎓 Education Path")
            st.markdown(EDUCATION)

        with st.container(border=True):
            st.subheader("🌟 Beyond the Classroom")
            st.markdown(BEYOND_CLASS)

    with col_bio_right:
        with st.container(border=True):
            st.subheader("🎨 Passions & Creative Interests")
            picked = st.multiselect(
                "Filter categories to view:",
                options=list(INTERESTS.keys()),
                default=list(INTERESTS.keys()),
            )
            for category in picked:
                st.markdown(f"**{category}**")
                for item in INTERESTS[category]:
                    st.markdown(f"- {item}")
            if not picked:
                st.caption("Select a category above to view.")

        with st.container(border=True):
            st.subheader("💎 Core Values & Beliefs")
            st.write(BELIEF)

    with st.container(border=True):
        st.subheader("🏆 Key Milestones")
        st.table(MILESTONES.set_index("Year"))

    with st.container(border=True):
        st.subheader("🌅 Vision & Future Horizon")
        if st.button("Reveal My Big Dream ✨"):
            st.session_state.show_dream = not st.session_state.show_dream
        if st.session_state.show_dream:
            st.markdown(
                f"""
                <div class="aurora-dream-card">
                    <h4 style="margin-top: 0; color: #0d6b52;">Aurora Vision</h4>
                    <p style="margin-bottom: 0; line-height: 1.6; color: #093b2d;">{DREAM}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.write("")
        autobio_text = (
            f"{NAME}\n{PROGRAM}, {YEAR}, Section {SECTION}\n{SCHOOL}\n\n"
            f"BACKGROUND\n{BACKGROUND}\n\n"
            f"EDUCATION\n{EDUCATION.replace('**', '')}\n\n"
            f"WHAT I BELIEVE\n{BELIEF.replace('**', '')}\n\n"
            f"WHERE I'M HEADED\n{DREAM}\n"
        )
        st.download_button(
            "💾 Download Full Autobiography (.txt)",
            data=autobio_text,
            file_name="jairus_colindres_autobiography.txt",
            mime="text/plain",
        )

# ---- Tab 2: Skills Explorer ----------------------------------------------
with tab_skills:
    st.subheader("🛠️ Technical & Practical Competencies")
    st.write(
        "Python and web development are my strongest skills, followed by capture the flag. "
        "Hardware hacking is the one I'm still just starting out in. The numbers below are self-ratings out of 100."
    )

    controls_col, display_col = st.columns([1, 2], gap="large")

    with controls_col:
        with st.container(border=True):
            st.markdown("**🔧 Skill Query Filters**")
            min_level = st.slider("Minimum Proficiency Level", 0, 100, 0, step=10)
            sort_by = st.selectbox(
                "Sort Order", ["Highest first", "Lowest first", "Alphabetical"]
            )
            chart_type = st.radio("Visualization Style", ["Bar Chart", "Area Graph"], horizontal=True)
            show_table = st.checkbox("Display Detail Grid", value=True)

    with display_col:
        with st.container(border=True):
            shown = SKILLS[SKILLS["Level"] >= min_level].copy()
            if sort_by == "Highest first":
                shown = shown.sort_values("Level", ascending=False)
            elif sort_by == "Lowest first":
                shown = shown.sort_values("Level")
            else:
                shown = shown.sort_values("Skill")

            if shown.empty:
                st.warning("No skills match the specified threshold.")
            else:
                st.metric("Average Competency Score", f"{np.mean(shown['Level']):.0f} / 100")
                chart_data = shown.set_index("Skill")["Level"]
                if chart_type == "Bar Chart":
                    st.bar_chart(chart_data)
                else:
                    st.area_chart(chart_data)
                if show_table:
                    st.dataframe(
                        shown,
                        hide_index=True,
                        use_container_width=True,
                        column_config={
                            "Level": st.column_config.ProgressColumn(
                                "Proficiency Meter", min_value=0, max_value=100, format="%d%%"
                            )
                        },
                    )

# ---- Tab 3: Projects -----------------------------------------------------
with tab_projects:
    st.subheader("🚀 Software & Hardware Projects")

    search_query = st.text_input(
        "🔍 Search Projects by keyword, technology, or role:",
        placeholder="Try: Next.js, Arduino, Developer, Manager",
    ).strip().lower()

    matches = [
        p for p in PROJECTS
        if not search_query
        or search_query in p["title"].lower()
        or search_query in p["role"].lower()
        or any(search_query in t.lower() for t in p["tools"])
    ]

    if not matches:
        st.warning("No projects matched your search criteria.")
    else:
        project_cols = st.columns(len(matches), gap="medium")
        for col, project in zip(project_cols, matches):
            with col:
                with st.container(border=True):
                    st.markdown(f"<h4 style='margin-top:0; color: #026ca8;'>📂 {project['title']}</h4>", unsafe_allow_html=True)
                    st.markdown(f"**Role:** `{project['role']}`")
                    tools_tags = " ".join(
                        f"<span style='background: linear-gradient(180deg, #e1f5fe 0%, #b3e5fc 100%); color: #0277bd; padding: 0.18rem 0.5rem; border-radius: 12px; font-size: 0.78rem; font-weight: 700; border: 1px solid #81d4fa; box-shadow: inset 0 1px 1px #fff; display: inline-block; margin-right: 0.2rem; margin-bottom: 0.25rem;'>{t}</span>"
                        for t in project["tools"]
                    )
                    st.markdown(f"**Stack:** {tools_tags}", unsafe_allow_html=True)
                    st.markdown("**Key Outcome:**")
                    st.write(project["outcome"])

# ---- Tab 4: Contact & Feedback -------------------------------------------
with tab_contact:
    st.subheader("✉️ Get in Touch & Feedback")
    form_col, info_col = st.columns([2, 1], gap="large")

    with form_col:
        with st.form("aero_contact_form", clear_on_submit=True):
            st.markdown("<strong>Send a Direct Message</strong>", unsafe_allow_html=True)
            name = st.text_input("Your Name")
            email = st.text_input("Your Email Address (optional)")
            topic = st.selectbox(
                "Inquiry Subject", ["General Inquiries / Greetings", "Project Discussion", "Portfolio Feedback"]
            )
            message = st.text_area("Your Message", height=130)
            rating = st.slider("Experience Rating", 1, 5, 5)
            wants_reply = st.checkbox("I would like a response")
            submitted = st.form_submit_button("📨 Submit Message")

        if submitted:
            if not name.strip() or not message.strip():
                st.error("Please provide both your name and message content.")
            elif wants_reply and "@" not in email:
                st.error("Please provide a valid email address so I can reply.")
            else:
                st.session_state.messages.append(
                    {"From": name.strip(), "Topic": topic, "Rating": rating}
                )
                st.success(f"Message received! Thank you for the {rating}-star rating, {name.strip()}!")

    with info_col:
        with st.container(border=True):
            st.subheader("🌐 Network Links")
            st.markdown(f"**Email:** [{EMAIL}](mailto:{EMAIL})")
            st.markdown(f"**GitHub:** [{GITHUB}]({GITHUB})")
            st.caption(
                "Messages sent via this form are recorded for the current session. "
                "For direct contact, please reach out via email or GitHub."
            )

        if st.session_state.messages:
            with st.expander("📬 Session Message Log", expanded=True):
                st.dataframe(pd.DataFrame(st.session_state.messages), hide_index=True, use_container_width=True)

# ---------------------------------------------------------------------------
# Windows 7 Aero Taskbar / Status Bar Footer
# ---------------------------------------------------------------------------
st.markdown(
    f"""
    <div class="aero-taskbar-footer">
        <div style="display: flex; align-items: center; gap: 0.65rem;">
            <span class="aero-start-orb">🫧 Start</span>
            <span>● Status: All Systems Operational</span>
        </div>
        <div>
            {NAME} · {PROGRAM} · {YEAR} · Section {SECTION} · {SCHOOL}
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
