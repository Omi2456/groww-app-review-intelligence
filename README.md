# Pulse — Groww Review Intelligence

An original Streamlit prototype for NextLeap Learn In Public — Challenge 5: App Review Insights Analyser.

## What it does

**Import → Group → Generate Note → Draft Email**

- Accepts one or multiple public review CSVs (Google Play, App Store, or both).
- Supports rating, title, review text and date; common column-name variants are normalized automatically.
- Uses the latest 12-week window anchored to the newest review in the uploaded data.
- Groups reviews into a maximum of 5 product themes.
- Shows the top 3 themes, 3 theme-aligned real-user quote excerpts and 3 action ideas.
- Scrubs obvious email addresses, phone numbers and long numeric IDs from analysis artifacts.
- Produces a scannable weekly Markdown note under the 250-word limit.
- Produces a draft email containing the weekly note.
- Provides a review explorer and downloadable analyzed CSV.

## Theme legend

1. **Features & UX** — navigation, watchlists, interface and feature requests.
2. **Trading & Order Execution** — orders, execution, stop-loss, positions and trading flows.
3. **App Performance & Reliability** — crashes, lag, loading, charts and stability.
4. **Customer Support** — support, tickets, response and help experience.
5. **Fees, Charges & Transactions** — brokerage, charges, deposits, withdrawals and payments.

## Re-run for a new week

1. Prepare a fresh public review CSV export with rating, title (optional), text and date.
2. Run `streamlit run app.py`.
3. Upload one CSV or both store CSVs.
4. Click **Analyze reviews**.
5. Download the generated weekly Markdown note, email draft and analyzed CSV.

The 12-week window automatically moves with the newest review date in the uploaded data.

## Data / privacy guardrails

- Public review exports only; no login or private data access.
- No usernames, emails, phone numbers or account IDs are required.
- No investment advice or return calculations.
- Quotes are excerpts from supplied reviews and are not presented as representative of all users.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

## Submission artifacts

- Working Streamlit prototype
- Latest weekly note: `weekly_note.md` / downloadable from the app
- Email draft: downloadable from the app
- Reviews CSV: `reviews_dataset.csv`
- README: this file

## Note on LLM usage

The prototype is deliberately deterministic by default so the same public CSV produces reproducible theme counts and quotes without requiring a paid API key. `gemini_adapter.py` and `llm_prompt.md` are retained as optional LLM-extension artifacts for W2 experimentation.
