# Groww — Review Intelligence Pulse
## Email Draft

The application generates an email draft from the same weekly analysis.

The draft contains:

- Subject
- Review window
- Review count
- Top 3 themes
- User voice
- 3 action ideas
- Product-team sign-off

The prototype generates a ready-to-use draft without requiring access to a user's Gmail, Outlook or other personal mailbox.

**Note:** The current prototype generates the email draft but does not automatically send an email from the user's personal mailbox.

---

## Data & Privacy Guardrails

The project follows the data and privacy constraints of the challenge:

- Uses public review data only.
- Does not require login access to app-store accounts.
- Does not require usernames, emails, phone numbers or account numbers.
- Obvious email addresses, phone numbers and long numeric identifiers are scrubbed from analysis outputs.
- Does not provide investment advice.
- Does not calculate investment returns.
- User quotes are excerpts from the supplied public review dataset.
- Quotes are not presented as representative of every user.

---

## Input CSV

The application accepts common review-data column variations and normalizes them automatically.

### Supported Fields

| Field | Required |
|---|---|
| Rating | Yes |
| Review text | Yes |
| Date | Yes |
| Title | Optional |
| Platform / Source | Optional |

Common date-column variations include:

- `date`
- `review_date`
- `Review Date`
- `posted_at`
- `created_at`

The application similarly handles common variations in review-text, rating and title column names.

---

## Re-run the Analysis for a New Week

To analyze a new batch of reviews:

1. Prepare a fresh public review CSV.
2. Start the Streamlit application.
3. Upload the CSV through the interface.
4. Click **Analyze Reviews**.
5. Review the generated themes.
6. Review the three user-voice excerpts.
7. Review the three action ideas.
8. Open the **Weekly Note** section.
9. Open the **Email Draft** section.
10. Download the required artifacts.

The application automatically determines the latest 12-week analysis window from the newest review date in the uploaded dataset.

---

## Run Locally

### 1. Create a virtual environment

```bash
python -m venv .venv
2. Activate the virtual environment
On Windows PowerShell:

.\.venv\Scripts\Activate.ps1
3. Install dependencies
pip install -r requirements.txt
4. Start the application
streamlit run app.py
The application will then be available at the local Streamlit URL shown in the terminal, usually:

http://localhost:8501
Project Structure
groww-app-review-intelligence/
│
├── app.py                  # Streamlit application and UI
├── process_reviews.py      # Review processing and analysis logic
├── requirements.txt        # Python dependencies
├── reviews_dataset.csv     # Public review dataset used for submission
├── weekly_note.md          # Generated weekly product pulse
├── email_draft.txt         # Generated email draft
├── llm_prompt.md           # Prompting reference
├── gemini_adapter.py       # Optional LLM integration artifact
├── demo.html               # Supporting demo artifact
├── README.md               # Project documentation
└── .gitignore              # Files excluded from Git
Challenge 5 Deliverables
This repository contains the core artifacts required for NextLeap Learn In Public — Challenge 5: App Review Insights Analyser.

Deliverable	Status
Working Streamlit prototype	✅
Weekly product pulse	✅
Email draft	✅
Public review CSV	✅
README with rerun instructions	✅
Theme legend	✅
Review explorer	✅
Downloadable analyzed CSV	✅
Design Approach
The interface is designed as a lightweight product-intelligence workspace called Pulse.

The goal is to transform raw review noise into an actionable product signal:

Reviews → Signals → User Voice → Actions → Weekly Pulse → Email Draft

The UI keeps the workflow simple so that a product or growth team member can upload a new review dataset and quickly understand:

What users are talking about

Which themes appear most frequently

What users are actually saying

What product teams could investigate next

How to communicate the findings to the team

LLM Approach
The default analysis pipeline is deterministic so that the same public CSV produces reproducible results without requiring a paid API key.

The repository also contains optional LLM experimentation artifacts:

llm_prompt.md — prompting reference for summarization and product-insight generation.

gemini_adapter.py — optional Gemini integration artifact.

The core application does not require an external LLM API key to run.

This makes the prototype easier to run and avoids requiring users to configure or expose personal API credentials.

Project Workflow
PUBLIC REVIEW CSV
       │
       ▼
┌───────────────────┐
│ Import & Normalize│
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Review Analysis   │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Theme Grouping    │
└─────────┬─────────┘
          │
     ┌────┴────┐
     ▼         ▼
Top Themes   User Voice
     │         │
     └────┬────┘
          ▼
┌───────────────────┐
│ Action Ideas      │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Weekly Pulse      │
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│ Email Draft       │
└───────────────────┘
Limitations
The current submission dataset contains public Google Play reviews for Groww.

The prototype can process compatible review CSVs from different public review sources when their required fields are available.

Theme classification uses a lightweight deterministic classification approach rather than claiming fully autonomous LLM clustering.

The email component generates a draft and does not automatically access or send from a user's personal mailbox.

Analysis quality depends on the quality, completeness and structure of the uploaded review CSV.

The application is intended for product-review analysis and does not provide investment recommendations.

Disclaimer
This tool is intended for product review analysis and product intelligence.

It does not provide investment advice, financial recommendations or buy/sell recommendations.
