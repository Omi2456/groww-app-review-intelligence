"""
Optional Gemini layer. No key is stored in this repository.
Install: pip install google-genai
Set: GEMINI_API_KEY
"""
import os, json, re
PROMPT="""You are a product-review intelligence analyst for Groww.
Using only supplied reviews: group into <=5 themes; return exactly top 3 themes;
select exactly 3 short verbatim quote excerpts; return exactly 3 evidence-grounded
actions; write a <=250-word weekly pulse; remove PII; no investment advice.
Return JSON: themes, quotes, actions, weekly_note."""
def analyze_with_gemini(reviews):
    from google import genai
    client=genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    payload=[{"rating":int(r["rating"]),"date":str(r["date"]),"text":r["review_text"],"platform":r["platform"]} for r in reviews]
    response=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=PROMPT+"\n\nREVIEWS:\n"+json.dumps(payload,ensure_ascii=False)
    )
    text=re.sub(r"^```json\s*|\s*```$","",response.text.strip())
    result=json.loads(text)
    source=[r["review_text"] for r in reviews]
    if len(result["themes"])>5 or len(result["themes"])!=3: raise ValueError("Theme constraint failed")
    if len(result["quotes"])!=3 or len(result["actions"])!=3: raise ValueError("Count constraint failed")
    if len(result["weekly_note"].split())>250: raise ValueError("Word limit failed")
    if not all(any(q in s for s in source) for q in result["quotes"]):
        raise ValueError("Quote validation failed")
    return result
