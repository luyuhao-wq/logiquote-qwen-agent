# LogiQuote: Qwen-powered Logistics Quotation Agent

LogiQuote is a Qwen-powered AI agent that converts messy cross-border logistics inquiries into structured quotation briefs, detects missing fields, generates follow-up questions, and supports human-in-the-loop review for logistics customer service teams.

## Problem

Cross-border logistics customer service teams often receive incomplete and unstructured quotation inquiries from customers. A customer may mention the origin, destination, cargo type, weight, volume, delivery deadline, or preferred shipping option in different formats, while important information such as pickup address, destination type, customs clearance, cargo value, packaging details, and insurance requirements may be missing.

This creates repetitive manual work for logistics staff. Before preparing a quotation, they often need to read the message carefully, extract key information, identify missing fields, and send follow-up questions to the customer. This process is time-consuming and can easily lead to inconsistent communication.

## Solution

LogiQuote helps logistics customer service teams transform unstructured customer inquiries into a structured and reviewable workflow.

The agent can:

1. Extract key shipping fields from messy customer inquiries.
2. Detect missing or unclear information required for quotation.
3. Generate follow-up questions that customer service staff can directly review and edit.
4. Produce an internal quotation preparation brief.
5. Support human-in-the-loop review before any response is sent to the customer.

## Key Features

- **Inquiry Summary**: Summarizes the customer's logistics request.
- **Structured Quotation Form**: Extracts origin, destination, cargo type, weight, volume, shipping preference, and delivery requirement.
- **Missing Field Detection**: Identifies missing information needed for quotation.
- **Risk and Clarification Notes**: Flags potential issues such as unclear destination type, battery-related goods, DDP requirements, or incomplete cargo details.
- **Customer Reply Draft**: Generates a professional follow-up message for customer service staff.
- **Human Review**: Keeps the logistics staff in control before sending any message.

## Track

This project is submitted to the **Autopilot Agent** track.

The reason is that LogiQuote is designed as an AI workflow that helps users complete a real business task: turning unclear logistics inquiries into structured quotation preparation materials.

## Tech Stack

- Qwen Cloud
- Alibaba Cloud
- Python
- Streamlit
- JSON
- Prompt Engineering
- GitHub

## Project Status

The original LogiQuote concept existed as an early AI workflow demo. During the Qwen Cloud Hackathon submission period, the project is being rebuilt and improved as a Qwen-powered AI agent.

Current improvements include:

- Rebuilding the workflow with Qwen Cloud API
- Creating structured field extraction prompts
- Adding missing-field detection
- Generating customer follow-up replies
- Preparing evaluation test cases
- Creating project documentation
- Planning Alibaba Cloud deployment

## Example Use Case

Customer inquiry:

> Hi, I need to ship 20 cartons of home decor products from Ningbo to Los Angeles. Total weight is around 480 kg and volume is 3.2 CBM. Could you quote me the cheapest option within 25 days?

LogiQuote will extract:

- Origin: Ningbo
- Destination: Los Angeles
- Cargo type: Home decor products
- Weight: 480 kg
- Volume: 3.2 CBM
- Preferred option: Cheapest
- Delivery requirement: Within 25 days

It will also detect missing information such as:

- Exact pickup address
- Delivery address type
- Incoterm
- Cargo value
- Insurance requirement
- Customs clearance requirement

Then it generates follow-up questions for customer service staff to review.

## Future Improvements

- Add customer history and preference memory
- Connect with real logistics quotation databases
- Support more shipping modes and destination rules
- Add multilingual inquiry handling
- Improve evaluation with more real-world test cases
- Add dashboard-style quotation preparation view
