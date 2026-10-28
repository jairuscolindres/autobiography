from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

# ---------------------------------------------------------------------------
# Page setup
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Jairus Colindres | Portfolio",
    page_icon="🌱",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Content (edit everything here)
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
            "Won the Hack4Gov Region 7 (Regional) CTF Championship, representing my school",
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
# Sidebar
# ---------------------------------------------------------------------------
with st.sidebar:
    st.header("Jairus Colindres")
    st.write(f"**{PROGRAM}**")
    st.write(f"{YEAR} · Section **{SECTION}**")
    st.caption(SCHOOL)
    st.divider()
    st.link_button("GitHub profile", GITHUB, use_container_width=True)
    st.link_button("Email me", f"mailto:{EMAIL}", use_container_width=True)
    st.divider()
    if st.button("Send kudos 🌻", use_container_width=True):
        st.session_state.kudos += 1
    st.caption(f"Kudos this visit: {st.session_state.kudos}")
    if st.session_state.kudos >= 3:
        st.success("Thank you, that means a lot!")

# ---------------------------------------------------------------------------
# Header and about
# ---------------------------------------------------------------------------
st.title(NAME)
st.caption(f"{PROGRAM} · {YEAR} · Section {SECTION} · {SCHOOL}")

photo_col, about_col = st.columns([1, 2], gap="large")

with photo_col:
    if PHOTO.exists():
        st.image(str(PHOTO), caption=NAME)
    else:
        st.info(
            "📷 **Photo placeholder.** Add a file named `profile.jpg` next to "
            "`app.py` and your picture will appear here."
        )

with about_col:
    st.header("About me")
    st.write(
        f"Hi, I'm Jairus. {TAGLINE}. I like building things from scratch, from coding "
        "projects to hacking my old router. This page is my autobiography and a small "
        "portfolio of what I've built so far."
    )
    m1, m2, m3 = st.columns(3)
    m1.metric("Year level", YEAR)
    m2.metric("Projects", len(PROJECTS))
    m3.metric("Regional CTF", "Champion")

st.divider()

# ---------------------------------------------------------------------------
# Main sections
# ---------------------------------------------------------------------------
tab_bio, tab_skills, tab_projects, tab_contact = st.tabs(
    ["📖 Autobiography", "🛠️ Skills", "🚀 Projects", "✉️ Contact"]
)

# ---- Autobiography --------------------------------------------------------
with tab_bio:
    st.header("Autobiography")
    left, right = st.columns(2, gap="large")

    with left:
        st.subheader("Background")
        st.write(BACKGROUND)
        st.subheader("Education")
        st.markdown(EDUCATION)
        st.subheader("Beyond class")
        st.markdown(BEYOND_CLASS)

    with right:
        st.subheader("What I love")
        picked = st.multiselect(
            "Choose categories to show",
            options=list(INTERESTS.keys()),
            default=list(INTERESTS.keys()),
        )
        for category in picked:
            st.markdown(f"**{category}**")
            for item in INTERESTS[category]:
                st.markdown(f"- {item}")
        if not picked:
            st.caption("Pick at least one category to see my interests.")
        st.caption("Workload limits most of these for now.")

        st.subheader("What I believe")
        st.write(BELIEF)

    st.subheader("Milestones")
    st.table(MILESTONES.set_index("Year"))

    st.subheader("Where I'm headed")
    if st.button("Reveal my big dream"):
        st.session_state.show_dream = not st.session_state.show_dream
    if st.session_state.show_dream:
        st.write(DREAM)

    autobio_text = (
        f"{NAME}\n{PROGRAM}, {YEAR}, Section {SECTION}\n\n"
        f"BACKGROUND\n{BACKGROUND}\n\n"
        f"EDUCATION\n{EDUCATION.replace('**', '')}\n\n"
        f"WHAT I BELIEVE\n{BELIEF.replace('**', '')}\n\n"
        f"WHERE I'M HEADED\n{DREAM}\n"
    )
    st.download_button(
        "Download my autobiography (.txt)",
        data=autobio_text,
        file_name="jairus_colindres_autobiography.txt",
        mime="text/plain",
    )

# ---- Skills ---------------------------------------------------------------
with tab_skills:
    st.header("Skills")
    st.write(
        "Python and web development are my strongest skills, followed by capture the "
        "flag. Hardware hacking is the one I'm still just starting out in. The numbers "
        "below are my own self-ratings out of 100."
    )

    controls, display = st.columns([1, 2], gap="large")

    with controls:
        st.subheader("Explore")
        min_level = st.slider("Minimum skill level", 0, 100, 0, step=10)
        sort_by = st.selectbox(
            "Sort by", ["Highest first", "Lowest first", "Alphabetical"]
        )
        chart_type = st.radio("Chart style", ["Bar", "Area"], horizontal=True)
        show_table = st.checkbox("Show table", value=True)

    with display:
        shown = SKILLS[SKILLS["Level"] >= min_level].copy()
        if sort_by == "Highest first":
            shown = shown.sort_values("Level", ascending=False)
        elif sort_by == "Lowest first":
            shown = shown.sort_values("Level")
        else:
            shown = shown.sort_values("Skill")

        if shown.empty:
            st.warning("No skills at that level. Lower the slider to see more.")
        else:
            st.metric("Average of shown skills", f"{np.mean(shown['Level']):.0f} / 100")
            chart_data = shown.set_index("Skill")["Level"]
            if chart_type == "Bar":
                st.bar_chart(chart_data)
            else:
                st.area_chart(chart_data)
            if show_table:
                st.dataframe(
                    shown,
                    hide_index=True,
                    column_config={
                        "Level": st.column_config.ProgressColumn(
                            "Level", min_value=0, max_value=100, format="%d"
                        )
                    },
                )

# ---- Projects -------------------------------------------------------------
with tab_projects:
    st.header("Projects")
    query = st.text_input(
        "Search my projects",
        placeholder="Try: Arduino, Next.js, Developer",
    ).strip().lower()

    matches = [
        p
        for p in PROJECTS
        if not query
        or query in p["title"].lower()
        or query in p["role"].lower()
        or any(query in t.lower() for t in p["tools"])
    ]

    if not matches:
        st.warning("No projects match that search. Try a tool or role name.")
    else:
        cols = st.columns(len(matches), gap="medium")
        for col, project in zip(cols, matches):
            with col:
                with st.container(border=True):
                    st.subheader(project["title"])
                    st.markdown(f"**Role:** {project['role']}")
                    st.markdown(
                        "**Tools:** " + " ".join(f"`{t}`" for t in project["tools"])
                    )
                    st.markdown("**Outcome:**")
                    st.write(project["outcome"])

# ---- Contact --------------------------------------------------------------
with tab_contact:
    st.header("Contact and feedback")
    form_col, info_col = st.columns([2, 1], gap="large")

    with form_col:
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your name")
            email = st.text_input("Your email (optional)")
            topic = st.selectbox(
                "Topic", ["Feedback on this page", "Project question", "Say hi"]
            )
            message = st.text_area("Message", height=120)
            rating = st.slider("How did you like this page?", 1, 5, 4)
            wants_reply = st.checkbox("I'd like a reply")
            submitted = st.form_submit_button("Send message")

        if submitted:
            if not name.strip() or not message.strip():
                st.error("Please enter your name and a message.")
            elif wants_reply and "@" not in email:
                st.error("Add a valid email so I can reply.")
            else:
                st.session_state.messages.append(
                    {"From": name.strip(), "Topic": topic, "Rating": rating}
                )
                st.success(
                    f"Thanks, {name.strip()}! Your {rating}-star feedback was received."
                )
                st.balloons()

    with info_col:
        st.subheader("Reach me directly")
        st.write(f"📧 {EMAIL}")
        st.write(f"💻 [github.com/jairuscolindres]({GITHUB})")
        st.caption(
            "This form only records messages for your current visit and doesn't "
            "send email. Use the links above to contact me directly."
        )
        if st.session_state.messages:
            with st.expander("Your messages this visit", expanded=True):
                st.dataframe(
                    pd.DataFrame(st.session_state.messages), hide_index=True
                )

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.divider()
st.caption(
    f"{NAME} · {PROGRAM} · {YEAR} · Section {SECTION} · CSIT 349 Applied AI"
)
