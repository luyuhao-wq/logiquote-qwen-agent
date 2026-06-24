import json
from pathlib import Path

import streamlit as st

from agent_workflow import run_logiquote_agent


st.set_page_config(
    page_title="LogiQuote AI Agent",
    page_icon="🚢",
    layout="wide"
)

st.title("🚢 LogiQuote: Qwen-powered Logistics Quotation Agent")

st.markdown(
    """
LogiQuote helps cross-border logistics customer service teams convert messy customer inquiries into structured quotation briefs, missing-field checks, risk notes, and follow-up replies.

This demo follows a human-in-the-loop workflow. It supports both **Live Mode** with Qwen Cloud API and **Demo Mode** using saved sample outputs.
"""
)

st.divider()


def load_demo_result() -> dict:
    """
    Load one saved batch test result for demo mode.
    This allows reviewers to explore the app without setting up an API key.
    """
    demo_path = Path("data/batch_test_results.json")

    if not demo_path.exists():
        return {
            "original_inquiry": "Demo data is not available.",
            "extracted_fields": {},
            "missing_field_check": {
                "missing_required_fields": [],
                "unclear_fields": [],
                "risk_notes": [],
                "quotation_readiness": "demo_data_missing",
                "recommended_next_action": "Please run test_batch.py first to generate demo results."
            },
            "reply_generation": {
                "customer_reply_draft": "",
                "follow_up_questions": [],
                "internal_operation_notes": []
            }
        }

    results = json.loads(demo_path.read_text(encoding="utf-8"))

    if isinstance(results, list) and len(results) > 0:
        return results[0]

    return {
        "original_inquiry": "Demo data is empty.",
        "extracted_fields": {},
        "missing_field_check": {
            "missing_required_fields": [],
            "unclear_fields": [],
            "risk_notes": [],
            "quotation_readiness": "demo_data_empty",
            "recommended_next_action": "Please check data/batch_test_results.json."
        },
        "reply_generation": {
            "customer_reply_draft": "",
            "follow_up_questions": [],
            "internal_operation_notes": []
        }
    }


def display_result(result: dict):
    """
    Display LogiQuote workflow result in the Streamlit interface.
    """
    st.success("Analysis completed.")

    st.subheader("1. Original Inquiry")
    st.write(result.get("original_inquiry", ""))

    st.subheader("2. Extracted Logistics Fields")
    extracted_fields = result.get("extracted_fields", {})
    st.json(extracted_fields)

    st.subheader("3. Missing Field Check")
    missing_check = result.get("missing_field_check", {})
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Missing Required Fields**")
        st.write(missing_check.get("missing_required_fields", []))

        st.markdown("**Unclear Fields**")
        st.write(missing_check.get("unclear_fields", []))

        st.markdown("**Quotation Readiness**")
        st.info(missing_check.get("quotation_readiness", ""))

    with col2:
        st.markdown("**Risk Notes**")
        risk_notes = missing_check.get("risk_notes", [])
        if risk_notes:
            for note in risk_notes:
                st.write(f"- {note}")
        else:
            st.write("No major risk notes detected.")

        st.markdown("**Recommended Next Action**")
        st.write(missing_check.get("recommended_next_action", ""))

    st.subheader("4. Customer Reply Draft")
    reply_result = result.get("reply_generation", {})
    st.text_area(
        "AI-generated reply draft for customer service review:",
        value=reply_result.get("customer_reply_draft", ""),
        height=180
    )

    st.subheader("5. Follow-up Questions")
    follow_up_questions = reply_result.get("follow_up_questions", [])
    if follow_up_questions:
        for question in follow_up_questions:
            st.write(f"- {question}")
    else:
        st.write("No follow-up questions generated.")

    st.subheader("6. Internal Operation Notes")
    internal_notes = reply_result.get("internal_operation_notes", [])
    if internal_notes:
        for note in internal_notes:
            st.write(f"- {note}")
    else:
        st.write("No internal operation notes generated.")

    st.divider()

    st.warning(
        "Human-in-the-loop checkpoint: The generated reply should be reviewed and edited by logistics staff before being sent to the customer."
    )

    with st.expander("Full JSON Output"):
        st.json(result)


with st.sidebar:
    st.header("Demo Settings")

    mode = st.radio(
        "Select running mode:",
        ["Demo Mode", "Live Qwen API Mode"],
        index=0
    )

    st.markdown(
        """
**Demo Mode** uses saved sample outputs from `data/batch_test_results.json`.

**Live Qwen API Mode** calls Qwen Cloud API using your local `.env` file.
"""
    )

sample_inquiry = """Hi, I need to ship 20 cartons of home decor products from Ningbo to Los Angeles.
Total weight is around 480 kg and volume is 3.2 CBM.
Could you quote me the cheapest option within 25 days?"""

customer_inquiry = st.text_area(
    "Paste a customer logistics inquiry here:",
    value=sample_inquiry,
    height=180
)

analyze_button = st.button("Analyze Inquiry")

if analyze_button:
    if mode == "Demo Mode":
        with st.spinner("Loading saved demo result..."):
            result = load_demo_result()
        display_result(result)

    else:
        if not customer_inquiry.strip():
            st.warning("Please enter a customer inquiry.")
        else:
            try:
                with st.spinner("LogiQuote is analyzing the inquiry with Qwen Cloud..."):
                    result = run_logiquote_agent(customer_inquiry)

                display_result(result)

            except Exception as e:
                st.error("Live Qwen API Mode failed.")
                st.write(
                    "Please check whether your `.env` file is correctly configured with `DASHSCOPE_API_KEY`, `QWEN_BASE_URL`, and `QWEN_MODEL`."
                )
                st.code(str(e))
