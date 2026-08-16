import re
import pandas as pd

THEMES = {
    "App Performance & Reliability": ["lag", "slow", "loading", "crash", "glitch", "hang", "server", "chart", "stability", "error", "freeze", "buffer", "not working"],
    "Trading & Order Execution": ["order", "stop loss", "stop-loss", "execution", "execute", "trade", "trading", "f&o", "scalping", "market price", "position", "option", "slippage", "trigger", "intraday"],
    "Customer Support": ["customer support", "support", "customer care", "call centre", "call center", "ticket", "chatbot", "help section", "helpline", "response", "reply"],
    "Fees, Charges & Transactions": ["brokerage", "charge", "charges", "fee", "fees", "commission", "tax", "deduct", "withdrawal", "deposit", "upi", "payment", "refund", "balance", "negative"],
    "Features & UX": ["feature", "interface", "ui", "ux", "watchlist", "wishlist", "international", "dashboard", "layout", "add", "request", "easy", "beginner", "family account", "ai", "ipad"],
}

ALIASES = {
    "review_date": "date", "Date": "date", "Review Date": "date", "posted_at": "date", "created_at": "date",
    "body": "review_text", "review": "review_text", "text": "review_text", "content": "review_text",
    "Review": "review_text", "Review Text": "review_text",
    "Review Title": "title", "review_title": "title", "Title": "title",
    "stars": "rating", "Rating": "rating",
}

def scrub(s):
    s = str(s)
    s = re.sub(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}', '[REDACTED_EMAIL]', s)
    s = re.sub(r'(?<!\d)(?:\+91[\s-]?)?[6-9]\d{9}(?!\d)', '[REDACTED_PHONE]', s)
    s = re.sub(r'\b(?:ticket|case|complaint|reference|ref)\s*(?:number|no\.?|#)?\s*[:\-]?\s*\d{5,}\b', '[REDACTED_ID]', s, flags=re.I)
    s = re.sub(r'\b\d{7,}\b', '[REDACTED_ID]', s)
    return s.strip()

def classify(text):
    t = str(text).lower()
    scores = {theme: sum(t.count(k) for k in kws) for theme, kws in THEMES.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] else "Features & UX"

def prepare_frame(df, source_hint=""):
    df = df.copy()
    df.columns = [str(c).strip() for c in df.columns]
    df = df.rename(columns={k: v for k, v in ALIASES.items() if k in df.columns})
    required = ["rating", "review_text", "date"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required column(s): {', '.join(missing)}")
    if "title" not in df.columns:
        df["title"] = ""
    if "platform" not in df.columns:
        hint = str(source_hint).lower()
        df["platform"] = "App Store" if "app" in hint or "ios" in hint else "Google Play"
    if "source" not in df.columns:
        df["source"] = df["platform"]
    df["date"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=True)
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    df["review_text"] = df["review_text"].fillna("").map(scrub)
    df["title"] = df["title"].fillna("").map(scrub)
    df = df.dropna(subset=["date", "rating", "review_text"]).copy()
    df["review_text_for_analysis"] = (df["title"].astype(str) + " " + df["review_text"].astype(str)).str.strip()
    df["theme"] = df["review_text_for_analysis"].map(classify)
    return df

def run(csv_path, end_date=None, weeks=12):
    df = prepare_frame(pd.read_csv(csv_path))
    return filter_window(df, end_date=end_date, weeks=weeks)

def filter_window(df, end_date=None, weeks=12):
    df = df.copy()
    if df.empty:
        raise ValueError("No valid reviews remain after parsing the CSV.")
    anchor = pd.Timestamp(end_date) if end_date else df["date"].max()
    start = anchor - pd.Timedelta(weeks=weeks)
    df = df[(df["date"] >= start) & (df["date"] <= anchor)].copy()
    if df.empty:
        raise ValueError("No reviews fall inside the latest 12-week window.")
    df = df.sort_values("date", ascending=False).reset_index(drop=True)
    df["review_id"] = [f"review-{i+1:03d}" for i in range(len(df))]
    top3 = list(df["theme"].value_counts().head(3).items())
    return df, top3

def combine_frames(frames):
    combined = pd.concat(frames, ignore_index=True)
    # Keep the newest copy if an identical review is uploaded twice.
    combined["_dedupe_key"] = (
        combined["platform"].astype(str).str.lower().str.strip() + "|" +
        combined["rating"].astype(str) + "|" +
        combined["date"].astype(str) + "|" +
        combined["review_text"].astype(str).str.lower().str.strip()
    )
    combined = combined.drop_duplicates("_dedupe_key").drop(columns="_dedupe_key").reset_index(drop=True)
    return combined
