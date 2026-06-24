# LogiQuote Portfolio Case Study

## 1. Project Overview

**LogiQuote** is an AI agent portfolio project designed for cross-border logistics quotation preparation.

The project focuses on a common business workflow in logistics customer service: converting messy customer inquiries into structured quotation preparation materials. Instead of directly generating final prices, LogiQuote helps customer service staff extract key shipment information, identify missing fields, detect quotation risks, and prepare customer follow-up reply drafts for human review.

The project was built as an independent AI Agent prototype to demonstrate practical AI product thinking, prompt design, structured output design, workflow automation, and human-in-the-loop system design.

## 2. Background

In cross-border logistics, customer inquiries are often incomplete, unstructured, and inconsistent.

A customer may send a message such as:

> Hi, I need to ship 20 cartons of home decor products from Ningbo to Los Angeles. Total weight is around 480 kg and volume is 3.2 CBM. Could you quote me the cheapest option within 25 days?

Although this inquiry contains useful information, it is not enough for accurate quotation preparation. Logistics staff still need to confirm missing details such as shipping mode, pickup address, destination address type, trade term, cargo value, insurance requirement, and customs clearance responsibility.

In real customer service work, this early-stage quotation preparation process is repetitive and time-consuming. Staff need to manually read each inquiry, extract shipment information, identify missing details, and write follow-up questions. LogiQuote was designed to make this process more structured and consistent.

## 3. User Pain Points

The target users are logistics customer service staff or quotation support staff.

Their main pain points include:

1. **Messy customer messages**
   Customers may describe shipment needs in free text, using incomplete or informal language.

2. **Missing quotation fields**
   Important fields such as trade term, pickup address, cargo value, insurance requirement, and customs clearance responsibility are often missing.

3. **Repetitive manual extraction**
   Staff need to repeatedly extract the same types of shipment information from different inquiries.

4. **Inconsistent follow-up questions**
   Different staff may ask different questions, leading to inconsistent customer communication.

5. **Risk of premature quotation**
   Preparing a quotation before confirming key details may lead to inaccurate cost estimation or operational misunderstanding.

6. **Need for human review**
   Logistics quotation decisions still require professional judgment, so AI output should support staff rather than replace them.

## 4. Product Goal

The goal of LogiQuote is to build an AI-assisted workflow that helps logistics staff prepare quotations more efficiently and consistently.

The product does not aim to automatically send quotations or replace human decision-making. Instead, it provides structured support before quotation preparation.

The core product goals are:

* Convert messy customer inquiries into structured quotation briefs.
* Identify missing or unclear information.
* Generate risk and clarification notes.
* Produce professional follow-up reply drafts.
* Keep human staff in control through a human-in-the-loop review process.
* Allow reviewers to explore the system without requiring an API key through Demo Mode.

## 5. Target Users

### Primary Users

* Cross-border logistics customer service staff
* Quotation support staff
* Operations coordinators

### Secondary Users

* Logistics sales assistants
* Freight forwarding interns
* AI product reviewers
* Portfolio reviewers interested in AI workflow design

## 6. User Flow

The main user flow is:

```text
Customer Inquiry
        ↓
Paste Inquiry into Streamlit Interface
        ↓
AI Field Extraction
        ↓
Missing Field and Risk Check
        ↓
Customer Reply Draft Generation
        ↓
Human Review
        ↓
Customer Follow-up
```

The workflow keeps human staff at the final decision point. AI-generated outputs are treated as preparation materials, not final business decisions.

## 7. Core Features

### 7.1 Structured Field Extraction

LogiQuote extracts key logistics fields from unstructured customer messages, including:

* Origin
* Destination
* Cargo type
* Weight
* Volume
* Package details
* Shipping mode
* Delivery requirement
* Preferred option
* Trade term
* Cargo value
* Pickup address
* Delivery address type
* Insurance requirement
* Customs clearance requirement
* Special cargo risk
* Confidence level

### 7.2 Missing Field Detection

The agent identifies fields that are missing or unclear before quotation preparation.

Examples of missing fields include:

* Shipping mode
* Trade term
* Pickup address
* Delivery address type
* Cargo value
* Insurance requirement
* Customs clearance requirement

This helps staff understand why an inquiry is not yet ready for quotation.

### 7.3 Risk and Clarification Notes

LogiQuote provides risk notes based on the extracted information.

For example:

* The customer requests the cheapest option, but shipping mode is not confirmed.
* Destination address type is missing, which may affect last-mile delivery cost.
* Cargo value is missing, which may affect insurance and customs valuation.
* Trade term is missing, so import/export responsibility is unclear.

These notes are designed to support operational awareness before quotation preparation.

### 7.4 Customer Reply Draft

The agent generates a professional follow-up reply draft that customer service staff can review and edit.

The draft usually includes:

* A short thank-you message
* Confirmation of understood shipment details
* Missing information questions
* A polite explanation that the quotation will be prepared after confirmation

### 7.5 Internal Operation Notes

The system also generates internal notes for logistics staff. These notes help staff understand which parts of the inquiry require further checking before proceeding.

### 7.6 Demo Mode Without API Key

A portfolio reviewer may not have a Qwen Cloud API key. To improve accessibility, LogiQuote includes Demo Mode.

Demo Mode loads saved outputs from:

```text
data/batch_test_results.json
```

This allows reviewers to explore the workflow without setting up API credentials.

### 7.7 Live Qwen API Mode

Users with a valid Qwen Cloud API key can switch to Live Qwen API Mode.

In this mode, the system calls Qwen Cloud API in real time and generates fresh responses based on the input inquiry.

## 8. System Design

LogiQuote uses a modular AI workflow.

The main components are:

```text
Streamlit Frontend
        ↓
LogiQuote Agent Workflow
        ↓
Field Extraction Module
        ↓
Missing Field Check Module
        ↓
Reply Generation Module
        ↓
Structured Output for Human Review
```

### 8.1 Streamlit Frontend

The Streamlit frontend provides a simple interface where users can paste logistics inquiries and select the running mode.

It supports:

* Demo Mode
* Live Qwen API Mode
* Inquiry input
* Structured result display
* Missing field display
* Risk notes
* Customer reply draft
* Full JSON output

### 8.2 Agent Workflow

The agent workflow is implemented in `agent_workflow.py`.

It coordinates three stages:

1. Field extraction
2. Missing field and risk check
3. Reply generation

Each stage has a specific prompt module and returns structured output.

### 8.3 Prompt Modules

The project uses separate prompt files:

```text
prompts/extraction_prompt.md
prompts/missing_fields_prompt.md
prompts/reply_generation_prompt.md
```

This structure makes the prompts easier to maintain, test, and improve.

### 8.4 Qwen Cloud API Layer

The Qwen API integration is handled in:

```text
qwen_client.py
```

The API key is stored locally in a `.env` file and is not uploaded to GitHub.

### 8.5 Data and Evaluation

Sample inquiries and batch test results are stored in the `data/` folder.

Key files include:

```text
data/sample_inquiries.json
data/field_schema.json
data/batch_test_results.json
```

These files support testing, evaluation, and Demo Mode.

## 9. Evaluation Design

The project includes batch testing with five sample logistics inquiries.

The evaluation is designed to test whether the agent can handle:

* English inquiries
* Chinese inquiries
* Complete shipment information
* Incomplete shipment information
* Trade term requirements
* Risk clarification
* Low-information customer messages

| Case   | Language | Scenario                                                  | Main Evaluation Focus                                              |
| ------ | -------- | --------------------------------------------------------- | ------------------------------------------------------------------ |
| Case 1 | English  | Standard shipment inquiry from Ningbo to Los Angeles      | Basic field extraction and missing field detection                 |
| Case 2 | Chinese  | Bluetooth speakers from Shenzhen to a US Amazon warehouse | Chinese input handling and destination type clarification          |
| Case 3 | English  | DDP quote for LED lights from Guangzhou to Toronto        | Trade term detection and risk clarification                        |
| Case 4 | English  | Furniture sea freight from Foshan to Sydney               | Shipping mode preference and cargo detail extraction               |
| Case 5 | Chinese  | Highly incomplete inquiry to Germany                      | Low-information inquiry handling and follow-up question generation |

The batch results are saved in:

```text
data/batch_test_results.json
```

A more detailed evaluation summary is available in:

```text
docs/evaluation_summary.md
```

## 10. Example Output

For a customer inquiry about shipping 20 cartons of home decor products from Ningbo to Los Angeles, LogiQuote can extract:

```json
{
  "origin": "Ningbo",
  "destination": "Los Angeles",
  "cargo_type": "home decor products",
  "weight": "480 kg",
  "volume": "3.2 CBM",
  "package_details": "20 cartons",
  "delivery_requirement": "within 25 days",
  "preferred_option": "cheapest",
  "shipping_mode": "missing",
  "trade_term": "missing",
  "cargo_value": "missing",
  "pickup_address": "missing",
  "delivery_address_type": "missing"
}
```

It then identifies that the quotation is not ready and recommends asking follow-up questions before preparing a quotation.

## 11. Human-in-the-loop Design

Human-in-the-loop review is a key design principle of this project.

LogiQuote does not automatically send messages to customers. It also does not generate final prices.

Instead, it supports human staff by preparing:

* Structured shipment information
* Missing field lists
* Risk notes
* Reply drafts
* Internal notes

The final review, editing, and customer communication remain under human control.

This is important because logistics quotation involves professional judgment, pricing rules, customs requirements, delivery feasibility, and customer-specific conditions.

## 12. My Role

This was an independent portfolio project.

My responsibilities included:

* Identifying the business problem
* Defining the target users and pain points
* Designing the AI-assisted workflow
* Creating the structured field schema
* Designing prompt modules
* Implementing the Qwen API integration
* Developing the Streamlit prototype
* Adding Demo Mode for reviewers without API keys
* Creating sample test cases
* Running batch evaluation
* Writing documentation and README content
* Preparing the project as an AI Agent portfolio case

## 13. Product Thinking Reflections

This project helped me practice AI product thinking beyond simply calling an LLM API.

Important product decisions included:

1. **Focusing on preparation, not automation**
   I avoided designing the system as an automatic quotation sender because logistics quotation requires human judgment.

2. **Using structured output**
   JSON output makes the AI results easier to inspect, evaluate, and integrate into future systems.

3. **Separating prompts by task**
   Dividing extraction, missing field checking, and reply generation into separate modules makes the workflow easier to debug and improve.

4. **Designing for reviewers**
   Demo Mode allows others to understand the project without setting up API credentials.

5. **Keeping human review visible**
   The interface clearly reminds users that AI-generated replies should be reviewed before being sent.

## 14. Technical Implementation

The project is implemented with:

* Python
* Streamlit
* Qwen Cloud API
* JSON output parsing
* Environment variable configuration
* Modular prompt files
* Batch testing script

Main files:

```text
app.py                  Streamlit frontend
agent_workflow.py        Main AI workflow logic
qwen_client.py           Qwen API client
test_workflow.py         Single workflow test
test_batch.py            Batch evaluation test
```

## 15. Limitations

LogiQuote is currently a prototype and has several limitations:

* It does not connect to a real carrier pricing database.
* It does not calculate final freight prices.
* It does not include real customs rule validation.
* It does not connect to a CRM system.
* It does not include customer account history.
* The evaluation dataset is small.
* AI-generated outputs still require human review.
* Risk detection is prompt-based and may be conservative.

These limitations are acceptable for the current portfolio prototype because the project focuses on quotation preparation support rather than full logistics automation.

## 16. Future Improvements

Future improvements may include:

1. **Mock quotation database**
   Add sample rate tables to simulate pricing support.

2. **CRM-style customer history**
   Store customer preferences and past inquiry records.

3. **PDF export**
   Export structured quotation preparation briefs as PDF files.

4. **Manual correction feedback loop**
   Allow staff to correct AI outputs and use corrections for future prompt improvement.

5. **Multilingual frontend**
   Add a Chinese-English interface for bilingual logistics teams.

6. **More evaluation cases**
   Expand test cases to include more cargo types, destinations, shipping modes, and risk scenarios.

7. **Carrier rule engine**
   Add rule-based checks for cargo type, restricted items, delivery address type, and service feasibility.

8. **Cloud deployment**
   Deploy the app using Streamlit Community Cloud, Render, Hugging Face Spaces, or another lightweight platform.

## 17. Portfolio Value

LogiQuote demonstrates the following abilities:

* AI product problem framing
* User pain point analysis
* AI agent workflow design
* Prompt engineering
* Structured JSON output design
* Human-in-the-loop system design
* Streamlit prototype development
* Evaluation using multilingual test cases
* Technical documentation
* Product case study writing

This project is especially relevant to AI product management, AI application design, business workflow automation, and applied AI agent development.

## 18. Conclusion

LogiQuote is a practical AI Agent prototype for logistics quotation preparation.

It addresses a real business workflow where staff need to transform messy customer messages into structured, reviewable quotation preparation materials. By combining structured extraction, missing field detection, risk notes, reply draft generation, and human review, the project demonstrates how AI can support professional service workflows without fully replacing human judgment.
