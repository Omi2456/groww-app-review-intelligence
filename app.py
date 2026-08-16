
import streamlit as st
from pathlib import Path
import pandas as pd
import html

from process_reviews import prepare_frame, filter_window, combine_frames

# ---------------------------------------------------------
# Page setup
# ---------------------------------------------------------
st.set_page_config(
    page_title="Pulse — Groww Review Intelligence",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# Design system
# ---------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif; font-size: 16px;
}

.stApp {
    background:
        radial-gradient(circle at 8% 0%, rgba(124,92,255,.10), transparent 27%),
        radial-gradient(circle at 92% 7%, rgba(31,181,134,.09), transparent 24%),
        #f7f8fc;
}

.block-container {
    max-width: 1280px;
    padding-top: 2.1rem;
    padding-bottom: 4rem;
}

[data-testid="stSidebar"] {
    background: #111827;
    border-right: 0;
}

[data-testid="stSidebar"] * {
    color: #e5e7eb !important;
}

.brand {
    padding: 6px 0 24px 2px;
}

.brand-mark {
    display:inline-flex;
    width:42px;
    height:42px;
    border-radius:12px;
    align-items:center;
    justify-content:center;
    background:linear-gradient(135deg,#8b5cf6,#22c55e);
    color:white;
    font-weight:800;
    font-size:21px;
    margin-right:10px;
    vertical-align:middle;
}

.brand-name {
    font-family:'Space Grotesk',sans-serif;
    font-size:26px;
    font-weight:700;
    color:#fff;
    vertical-align:middle;
}

.sidebar-label {
    color:#9ca3af !important;
    font-size:12px;
    text-transform:uppercase;
    letter-spacing:.12em;
    margin:16px 0 7px;
}

.sidebar-note {
    color:#9ca3af !important;
    font-size:14px;
    line-height:1.65;
    padding:12px;
    border:1px solid rgba(255,255,255,.08);
    border-radius:12px;
    background:rgba(255,255,255,.035);
}

.hero {
    background:linear-gradient(135deg,#171c2c 0%,#20273a 52%,#182b2a 100%);
    border-radius:28px;
    padding:38px 40px;
    color:white;
    box-shadow:0 22px 60px rgba(17,24,39,.18); animation: heroIn .7s ease both;
    margin-bottom:22px;
    position:relative;
    overflow:hidden;
}

.hero:after {
    content:"";
    position:absolute;
    width:240px;
    height:240px;
    border-radius:50%;
    right:-80px;
    top:-110px;
    background:rgba(139,92,246,.22);
    filter:blur(4px);
}

.hero-eyebrow {
    color:#a7f3d0;
    font-size:13px;
    font-weight:700;
    text-transform:uppercase;
    letter-spacing:.13em;
    margin-bottom:9px;
}

.hero h1 {
    font-family:'Space Grotesk',sans-serif;
    font-size:50px;
    line-height:1.03;
    margin:0 0 10px;
    letter-spacing:-1.4px;
}

.hero p {
    color:#cbd5e1;
    max-width:700px;
    font-size:17px;
    margin:0;
}

.badge {
    display:inline-block;
    margin-top:17px;
    padding:7px 11px;
    border-radius:999px;
    background:rgba(255,255,255,.08);
    border:1px solid rgba(255,255,255,.11);
    color:#e2e8f0;
    font-size:12px;
}

.metric-card {
    background:#fff;
    border:1px solid #e8eaf0;
    border-radius:17px;
    padding:22px;
    min-height:128px;
    box-shadow:0 7px 22px rgba(17,24,39,.045);
}

.metric-label {
    color:#6b7280;
    font-size:12px;
    font-weight:600;
    text-transform:uppercase;
    letter-spacing:.06em;
}

.metric-value {
    font-family:'Space Grotesk',sans-serif;
    font-size:34px;
    font-weight:700;
    color:#111827;
    margin-top:7px;
}

.metric-sub {
    color:#8b93a3;
    font-size:14px;
    margin-top:4px;
}

.section-title {
    font-family:'Space Grotesk',sans-serif;
    font-size:26px;
    font-weight:700;
    color:#111827;
    margin:38px 0 16px;
}

.theme-card {
    background:#fff;
    border:1px solid #e8eaf0;
    border-radius:16px;
    padding:22px;
    min-height:165px;
    box-shadow:0 6px 20px rgba(17,24,39,.035);
}

.theme-rank {
    color:#8b5cf6;
    font-weight:800;
    font-size:12px;
}

.theme-name {
    color:#111827;
    font-size:18px;
    font-weight:700;
    margin:8px 0 5px;
}

.theme-count {
    color:#6b7280;
    font-size:14px;
}

.quote-card {
    background:#fff;
    border:1px solid #e8eaf0;
    border-radius:16px;
    padding:24px;
    min-height:190px;
    box-shadow:0 6px 20px rgba(17,24,39,.035);
}

.quote-mark {
    color:#8b5cf6;
    font-family:Georgia,serif;
    font-size:34px;
    line-height:.6;
}

.quote-text {
    color:#283142;
    font-size:16px;
    line-height:1.7;
    margin-top:10px;
}

.quote-theme {
    display:inline-block;
    margin-top:13px;
    color:#667085;
    background:#f2f3f7;
    border-radius:999px;
    padding:5px 9px;
    font-size:12px;
    font-weight:700;
}

.action-card {
    background:#fff;
    border-left:4px solid #8b5cf6;
    border-top:1px solid #e8eaf0;
    border-right:1px solid #e8eaf0;
    border-bottom:1px solid #e8eaf0;
    border-radius:13px;
    padding:19px 21px;
    margin-bottom:10px;
    box-shadow:0 5px 18px rgba(17,24,39,.03);
}

.action-number {
    color:#8b5cf6;
    font-weight:800;
    margin-right:8px;
}

.workflow {
    display:flex;
    gap:8px;
    flex-wrap:wrap;
    margin-top:20px;
}

.step {
    background:rgba(255,255,255,.07);
    border:1px solid rgba(255,255,255,.09);
    border-radius:999px;
    padding:7px 11px;
    color:#dbe4ef;
    font-size:11px;
}

div.stButton > button {
    border-radius:11px;
    font-weight:700;
    border:1px solid #e3e5eb;
    min-height:48px;
}

div.stButton > button[kind="primary"] {
    background:linear-gradient(135deg,#7c3aed,#8b5cf6);
    border:0;
}

[data-testid="stFileUploader"] {
    background:#fff;
    border:1px dashed #cfd3dc;
    border-radius:14px;
    padding:10px;
    font-size:14px;
}

div[data-testid="stExpander"] {
    border:1px solid #e5e7eb;
    border-radius:14px;
    background:#fff;
}

.footer {
    color:#98a0ae;
    text-align:center;
    font-size:11px;
    padding:30px 0 5px;
}

/* Pulse motion + interaction layer */
@keyframes heroIn { from { opacity:0; transform:translateY(12px) scale(.99); } to { opacity:1; transform:none; } }
@keyframes floatOrb { 0%,100% { transform:translate3d(0,0,0); } 50% { transform:translate3d(-18px,14px,0); } }
@keyframes fadeUp { from { opacity:0; transform:translateY(10px); } to { opacity:1; transform:none; } }
@keyframes shimmer { 0% { background-position:-500px 0; } 100% { background-position:500px 0; } }
.hero:before { content:""; position:absolute; width:180px; height:180px; left:45%; bottom:-120px; border-radius:50%; background:rgba(34,197,94,.13); filter:blur(3px); animation:floatOrb 6s ease-in-out infinite; }
.hero .workflow { animation:fadeUp .9s .15s ease both; }
.metric-card, .theme-card, .quote-card, .action-card { animation:fadeUp .55s ease both; transition:transform .2s ease, box-shadow .2s ease, border-color .2s ease; }
.metric-card:hover, .theme-card:hover, .quote-card:hover, .action-card:hover { transform:translateY(-4px); box-shadow:0 16px 34px rgba(17,24,39,.10); border-color:#d9d1ff; }
.theme-card { position:relative; overflow:hidden; }
.theme-card:after { content:""; position:absolute; inset:0; pointer-events:none; background:linear-gradient(110deg,transparent 30%,rgba(139,92,246,.07) 45%,transparent 60%); background-size:500px 100%; opacity:0; }
.theme-card:hover:after { opacity:1; animation:shimmer 1.1s ease; }
.metric-value { letter-spacing:-1px; }
.section-title { letter-spacing:-.4px; }
.stCaption, [data-testid="stCaptionContainer"] { font-size:14px !important; }
[data-testid="stFileUploaderDropzone"] { min-height:92px; }
[data-testid="stFileUploaderDropzoneInstructions"] { font-size:14px !important; }
div[data-baseweb="tab-list"] { gap:8px; }
button[data-baseweb="tab"] { font-size:15px !important; font-weight:700 !important; padding:10px 14px !important; }
div.stButton > button:hover { transform:translateY(-1px); box-shadow:0 8px 20px rgba(124,58,237,.12); }
@media (max-width: 900px) { .hero h1 { font-size:38px; } .hero { padding:28px; } .metric-value { font-size:28px; } .section-title { font-size:24px; } }
@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation:none !important; transition:none !important; } }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Data helpers
# ---------------------------------------------------------
BASE = Path(__file__).parent
DEFAULT_CSV = BASE / "reviews_dataset.csv"

def esc(value):
    return html.escape(str(value))

def load_analysis(path):
    df, top3 = run(path)
    return df, top3

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div class="brand">
        <span class="brand-mark">✦</span>
        <span class="brand-name">Pulse</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-label">Workspace</div>', unsafe_allow_html=True)
    st.markdown("**Groww · Review Intelligence**")

    st.markdown('<div class="sidebar-label">Workflow</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="sidebar-note">
    01 · Import public reviews<br>
    02 · Group into themes<br>
    03 · Surface user voice<br>
    04 · Turn evidence into actions<br>
    05 · Draft the weekly pulse
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-label">Guardrails</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="sidebar-note">
    Max 5 themes<br>
    No PII in outputs<br>
    Quotes come from source reviews<br>
    No investment advice
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-label">Data source</div>', unsafe_allow_html=True)
    st.caption("Public App Store + Google Play review exports")

# ---------------------------------------------------------
# Hero
# ---------------------------------------------------------
st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">✦ WEEKLY PRODUCT PULSE · CHALLENGE 5</div>
    <h1>Listen to the reviews.<br>See what matters next.</h1>
    <p>Turn public App Store and Google Play reviews into a compact product signal — themes, real user voice and practical actions for the team.</p>
    <div class="workflow">
        <span class="step">Import</span>
        <span class="step">Cluster</span>
        <span class="step">Prioritize</span>
        <span class="step">Recommend</span>
        <span class="step">Draft</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Import section
# ---------------------------------------------------------
st.markdown('<div class="section-title">01 · Bring in the latest reviews</div>', unsafe_allow_html=True)

uploaded = st.file_uploader(
    "Drop public review CSVs here",
    type=["csv"],
    accept_multiple_files=True,
    help="Upload one Play Store CSV, one App Store CSV, or both. Supported fields include rating, title, text and date.",
)

path = BASE / "reviews_dataset.csv"
source_label = "Bundled project dataset"
analyze = False

if uploaded:
    source_label = " + ".join(u.name for u in uploaded)
    st.caption("You can upload both stores. The analyzer merges them, removes exact duplicates, and keeps the latest 12 weeks.")
    analyze = st.button("Analyze reviews →", type="primary", width="stretch")
else:
    analyze = st.button("Analyze included sample →", type="primary", width="stretch")

if analyze:
    try:
        with st.spinner("Reading reviews, grouping themes and building the weekly signal…"):
            if uploaded:
                frames = []
                for u in uploaded:
                    frames.append(prepare_frame(pd.read_csv(u), source_hint=u.name))
                raw_df = combine_frames(frames)
            else:
                raw_df = prepare_frame(pd.read_csv(path), source_hint="Google Play")
            df, top3 = filter_window(raw_df, end_date=None, weeks=12)
        st.session_state.analysis = df
        st.session_state.top3 = top3
        st.session_state.source_label = source_label
        st.success(f"Analysis ready · {len(df):,} reviews in the latest 12-week window")
    except Exception as e:
        st.error(f"Could not analyze this CSV: {e}")
        st.stop()

# ---------------------------------------------------------
# Results
# ---------------------------------------------------------
if "analysis" not in st.session_state:
    st.info("Upload a CSV or use the included dataset, then click **Analyze reviews →**.")
    st.markdown('<div class="footer">Built as an original product-intelligence prototype for NextLeap · Challenge 5</div>', unsafe_allow_html=True)
    st.stop()

df = st.session_state.analysis
top3 = st.session_state.top3

# KPIs
st.markdown('<div class="section-title">02 · What changed in the review feed?</div>', unsafe_allow_html=True)

ratings = pd.to_numeric(df["rating"], errors="coerce").dropna()
avg_rating = ratings.mean() if not ratings.empty else 0
negative_share = (ratings <= 2).mean() * 100 if not ratings.empty else 0
date_min = pd.to_datetime(df["date"]).min()
date_max = pd.to_datetime(df["date"]).max()

metrics = [
    ("Reviews analyzed", f"{len(df):,}", "Public review sample"),
    ("Avg. rating", f"{avg_rating:.1f} / 5", "Across analyzed reviews"),
    ("Negative share", f"{negative_share:.0f}%", "Ratings ≤ 2"),
    ("Review window", f"{(date_max-date_min).days} days", f"{date_min:%d %b} → {date_max:%d %b}"),
]

cols = st.columns(4)
for col, (label, value, sub) in zip(cols, metrics):
    with col:
        st.markdown(
            f'<div class="metric-card"><div class="metric-label">{esc(label)}</div>'
            f'<div class="metric-value">{esc(value)}</div><div class="metric-sub">{esc(sub)}</div></div>',
            unsafe_allow_html=True
        )

# Themes
st.markdown('<div class="section-title">03 · The strongest signals</div>', unsafe_allow_html=True)

theme_cols = st.columns(3)
for i, (theme, count) in enumerate(top3):
    share = count / len(df) * 100 if len(df) else 0
    with theme_cols[i]:
        st.markdown(
            f'<div class="theme-card">'
            f'<div class="theme-rank">SIGNAL 0{i+1}</div>'
            f'<div class="theme-name">{esc(theme)}</div>'
            f'<div class="theme-count"><b>{count:,}</b> reviews · {share:.0f}% of analyzed feed</div>'
            f'</div>',
            unsafe_allow_html=True
        )

with st.expander("See all themes"):
    all_themes = df["theme"].value_counts().rename_axis("Theme").reset_index(name="Reviews")
    st.dataframe(all_themes, width="stretch", hide_index=True)

# User voice
st.markdown('<div class="section-title">04 · What users are actually saying</div>', unsafe_allow_html=True)

quote_keywords = {
    "Features & UX": ["feature", "interface", "watchlist", "layout", "dashboard", "navigation", "easy", "add", "request"],
    "Trading & Order Execution": ["order", "stop loss", "execution", "position", "trade", "option", "trigger", "intraday"],
    "App Performance & Reliability": ["lag", "slow", "crash", "glitch", "loading", "chart", "hang", "error"],
    "Customer Support": ["support", "ticket", "response", "reply", "customer care", "helpline"],
    "Fees, Charges & Transactions": ["brokerage", "charge", "fee", "withdrawal", "deposit", "payment", "refund"],
}

def choose_quote(frame, theme):
    c = frame[frame["theme"] == theme].copy()
    if c.empty:
        return "", ""
    kws = quote_keywords.get(theme, [])
    def score(row):
        txt = str(row["review_text"]).lower()
        title = str(row["title"]).lower()
        relevance = sum(txt.count(k) + title.count(k) for k in kws)
        length_penalty = 1 if len(txt.split()) >= 8 else 0
        return relevance * 10 + length_penalty
    c["_score"] = c.apply(score, axis=1)
    c = c.sort_values(["_score", "rating", "date"], ascending=[False, True, False])
    row = c.iloc[0]
    quote = " ".join(str(row["review_text"]).split())
    if len(quote.split()) > 25:
        quote = " ".join(quote.split()[:25]) + "…"
    return quote, row["platform"]

quotes = []
for theme, _ in top3:
    q, platform = choose_quote(df, theme)
    if q:
        quotes.append((theme, q, platform))

quote_cols = st.columns(3)
for col, (theme, quote, platform) in zip(quote_cols, quotes):
    with col:
        st.markdown(
            f'<div class="quote-card"><div class="quote-mark">“</div>'
            f'<div class="quote-text">{esc(quote)}</div>'
            f'<div class="quote-theme">{esc(theme)} · {esc(platform)}</div></div>',
            unsafe_allow_html=True
        )

# Actions
st.markdown('<div class="section-title">05 · From signal to action</div>', unsafe_allow_html=True)

action_map = {
    "App Performance & Reliability":
        "Prioritize market-hours stability and chart/loading reliability; instrument crash and latency rates by app version.",
    "Trading & Order Execution":
        "Audit order-state synchronization and execution UX during volatile periods; show clear order and position status.",
    "Customer Support":
        "Reduce unresolved-support loops with better first-response quality, escalation paths and issue-specific status updates.",
    "Fees, Charges & Transactions":
        "Make transaction-cost breakdowns clearer and improve visibility of withdrawal and payment status.",
    "Features & UX":
        "Prioritize recurring usability requests and test simpler navigation for watchlists, charts and portfolio views.",
}

for i, (theme, _) in enumerate(top3, 1):
    st.markdown(
        f'<div class="action-card"><span class="action-number">0{i}</span>'
        f'<b>{esc(theme)}</b><br><span style="color:#5f6878">{esc(action_map[theme])}</span></div>',
        unsafe_allow_html=True
    )

# Weekly note + email
st.markdown('<div class="section-title">06 · Weekly pulse & handoff</div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Weekly note", "Email draft", "Review explorer"])

def build_weekly_note(df, top3):
    date_min = pd.to_datetime(df["date"]).min()
    date_max = pd.to_datetime(df["date"]).max()
    stores = sorted(set(str(x) for x in df["platform"].dropna()))
    source_text = " + ".join(stores) if stores else "Public app-store review sample"
    lines = [
        "# Groww — Weekly App Review Pulse",
        f"**Review window:** {date_min:%d %b %Y} – {date_max:%d %b %Y}",
        f"**Reviews analyzed:** {len(df)} | **Source:** {source_text}",
        "",
        "## Top 3 themes",
    ]
    for i, (theme, count) in enumerate(top3, 1):
        lines.append(f"{i}. **{theme}** — {count} reviews")
    lines += ["", "## User voice"]
    for theme, _ in top3:
        quote, platform = choose_quote(df, theme)
        if quote:
            lines.append(f'- “{quote}” *(verbatim excerpt · {platform})*')
    action_map = {
        "App Performance & Reliability": "Prioritize market-hours stability and chart/loading reliability; instrument crash and latency rates by app version.",
        "Trading & Order Execution": "Audit order-state synchronization and execution UX during volatile periods; show clear order and position status.",
        "Customer Support": "Reduce unresolved-support loops with better first-response quality, escalation paths and issue-specific status updates.",
        "Fees, Charges & Transactions": "Make transaction-cost breakdowns clearer and improve visibility of withdrawal and payment status.",
        "Features & UX": "Prioritize recurring usability requests and test simpler navigation for watchlists, charts and portfolio views.",
    }
    lines += ["", "## 3 action ideas"]
    for i, (theme, _) in enumerate(top3, 1):
        lines.append(f"{i}. {action_map[theme]}")
    lines += ["", "*Theme legend: maximum 5 themes. PII is scrubbed from artifacts. Quotes are verbatim excerpts from supplied public reviews.*"]
    note = "\n".join(lines)
    # Enforce the assignment's <=250-word requirement.
    if len(note.split()) > 250:
        raise ValueError("Generated weekly note exceeds the 250-word assignment limit.")
    return note

note = build_weekly_note(df, top3)
email = f"""Subject: Groww Weekly Product Pulse — {pd.to_datetime(df['date']).max():%d %b %Y}\n\nHi Team,\n\nSharing this week's Groww app-review pulse.\n\n{note}\n\nBest,\nProduct Insights\n"""

with tab1:
    st.markdown(note)
    st.caption(f"Weekly note: {len(note.split())} words · {len(top3)} top themes · {len(quotes)} quotes")
    st.download_button(
        "Download weekly note",
        note,
        file_name="groww_weekly_pulse.md",
        mime="text/markdown",
    )

with tab2:
    st.text_area("Draft email", email, height=360)
    st.download_button(
        "Download email draft",
        email,
        file_name="groww_weekly_pulse_email.txt",
        mime="text/plain",
    )
    st.caption("The draft is ready to paste into Gmail/Outlook. The prototype does not access or store your mailbox.")

with tab3:
    display = df[["review_id","platform","rating","title","review_text","date","theme"]].copy()
    display["date"] = pd.to_datetime(display["date"]).dt.strftime("%Y-%m-%d")
    st.dataframe(display, width="stretch", hide_index=True)
    st.download_button(
        "Download analyzed CSV",
        display.to_csv(index=False),
        file_name="groww_review_analysis.csv",
        mime="text/csv",
    )

# Footer
st.markdown(
    '<div class="footer">Pulse · Groww Review Intelligence · Original interface built for this project · '
    'Public review data only · No PII · Facts from reviews, not investment advice</div>',
    unsafe_allow_html=True,
)
