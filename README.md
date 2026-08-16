# Groww — Review Intelligence Pulse

A Streamlit-based product review intelligence tool built for **NextLeap Learn In Public — Challenge 5: App Review Insights Analyser**.

The project converts a public review dataset into a concise weekly product pulse that helps product, growth and support teams understand what users are experiencing and what should be investigated next.

## What the project does

The workflow is:

**Import Reviews → Analyze → Group Themes → Surface User Voice → Generate Actions → Weekly Pulse → Email Draft**

The application:

- Accepts a public review CSV through the UI.
- Normalizes common review-column names automatically.
- Uses review rating, title, text and date for analysis.
- Automatically identifies the latest 12-week review window from the uploaded dataset.
- Groups reviews into a maximum of 5 predefined product themes.
- Identifies the top 3 themes by review volume.
- Surfaces 3 real-user quote excerpts aligned with the strongest themes.
- Generates 3 practical product action ideas.
- Produces a concise weekly pulse of no more than 250 words.
- Generates a ready-to-use email draft containing the weekly pulse.
- Provides a review explorer for inspecting analyzed reviews.
- Allows the weekly note, email draft and analyzed review data to be downloaded.

## Product analyzed

**Product:** Groww  
**Review source:** Public Google Play reviews  
**Dataset used for the current submission:** 170 reviews

### Current review window

**29 May 2026 – 13 August 2026**

The application is not hard-coded to this date range. When a new dataset is uploaded, the analysis window moves automatically based on the newest review date in that dataset.

## Current analysis

The current Groww review dataset produced the following top signals:

1. **Features & UX** — 57 reviews
2. **Trading & Order Execution** — 47 reviews
3. **App Performance & Reliability** — 29 reviews

The weekly pulse also includes three verbatim review excerpts and three corresponding action ideas.

## Theme framework

The application currently uses a maximum of five product themes:

### 1. Features & UX
Navigation, watchlists, interface usability, charts and feature requests.

### 2. Trading & Order Execution
Orders, order execution, stop-loss, positions and trading workflows.

### 3. App Performance & Reliability
Crashes, lag, loading problems, charts and application stability.

### 4. Customer Support
Support requests, tickets, response quality and help experience.

### 5. Fees, Charges & Transactions
Brokerage, transaction charges, deposits, withdrawals and payment-related issues.

The application never displays more than five themes, while the weekly pulse highlights the top three.

## Weekly Product Pulse

The generated weekly note contains:

- Review window
- Number of reviews analyzed
- Top 3 themes
- 3 real user voice excerpts
- 3 product action ideas
- Theme legend and data/privacy note

The generated note is designed to remain **scannable and under 250 words**, as required by the challenge.

## Email Draft

The application generates an email draft from the same weekly analysis.

The draft contains:

- Subject
- Review window
- Review count
- Top 3 themes
- User voice
- 3 action ideas
- Short product-team sign-off

The prototype generates the draft without requiring access to a user's Gmail, Outlook or other mailbox.

## Data and privacy guardrails

The project is designed around the challenge constraints:

- Uses public review data only.
- Does not require login access to app-store accounts.
- Does not collect usernames, emails, phone numbers or account numbers.
- Obvious email addresses, phone numbers and long numeric identifiers are scrubbed from analysis outputs.
- No investment advice is generated.
- No return or performance calculations are performed.
- User quotes are excerpts from the supplied public review dataset.
- The tool does not claim that the selected quotes represent every user.

## Input CSV

The application accepts common review-data column variations and normalizes them automatically.

Typical fields include:

| Field | Required |
|---|---|
| Rating | Yes |
| Review text | Yes |
| Date | Yes |
| Title | Optional |
| Platform / Source | Optional |

Examples of supported date-column names include:

- `date`
- `review_date`
- `Review Date`
- `posted_at`
- `created_at`

The same normalization approach is used for common review-text and rating column names.

## Re-run the analysis for a new week

1. Prepare a fresh public review CSV.
2. Start the Streamlit application.
3. Upload the CSV through the interface.
4. Click **Analyze Reviews**.
5. Review the generated themes, user voice and action ideas.
6. Open the **Weekly Note** section.
7. Open the **Email Draft** section.
8. Download the required artifacts.

The application automatically determines the latest 12-week analysis window from the newest review date in the uploaded dataset.

## Run locally

Create a virtual environment:

```bash
python -m venv .venv

Activate it on Windows PowerShell:

.\.venv\Scripts\Activate.ps1
Install dependencies:

pip install -r requirements.txt
Start the application:

streamlit run app.py
The application will then be available at the local Streamlit URL shown in the terminal.

Project structure
groww-app-review-intelligence/
│
├── app.py                  # Streamlit application and UI
├── process_reviews.py      # Review processing and analysis logic
├── requirements.txt        # Python dependencies
├── reviews_dataset.csv     # Public review dataset used for the submission
├── weekly_note.md          # Generated weekly pulse
├── email_draft.txt         # Generated email draft
├── llm_prompt.md           # Prompting reference
├── gemini_adapter.py       # Optional LLM integration artifact
├── demo.html               # Supporting demo artifact
├── README.md               # Project documentation
└── .gitignore              # Files excluded from Git
Challenge deliverables
This repository contains the core artifacts required for Challenge 5:

Working Streamlit prototype

Weekly product pulse

Email draft

Public review CSV

README with rerun instructions

Theme legend

Design approach
The interface is designed as a lightweight product-intelligence workspace called Pulse.

The goal is to move from raw review noise to an actionable product signal:

Reviews → Signals → User Voice → Actions → Weekly Pulse

The UI intentionally keeps the workflow simple so that a product or growth team member can upload a new review dataset and quickly understand what users are saying.

LLM approach
The default analysis pipeline is deterministic so that the same public dataset produces reproducible results without requiring a paid API key.

The repository also contains:

llm_prompt.md — prompting reference for summarization and product-insight generation.

gemini_adapter.py — optional LLM integration artifact.

The current submission does not require an external LLM API key to run the core workflow.

Limitations
The current submission dataset contains public Google Play reviews for Groww.

Theme classification uses a lightweight deterministic classification approach rather than claiming fully autonomous LLM clustering.

The email component generates a draft; it does not require access to or automatically send from the user's personal mailbox.

Analysis quality depends on the quality and structure of the uploaded review CSV.

Disclaimer
This tool is intended for product review analysis and does not provide investment advice or recommendations.