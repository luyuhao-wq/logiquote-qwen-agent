# Project Story

## Inspiration

Cross-border logistics customer service teams often receive quotation inquiries in messy and incomplete formats. Customers may send short messages with only part of the required shipping information, such as origin, destination, cargo type, weight, volume, or delivery time. However, key quotation details such as pickup address, delivery address type, trade term, customs clearance requirements, cargo value, package details, and insurance needs are often missing.

This creates repetitive manual work for logistics staff. Before preparing a quotation, they need to read the inquiry carefully, extract useful information, identify missing fields, check possible risks, and write follow-up questions. This process is time-consuming and may lead to inconsistent communication.

LogiQuote was created to explore how an AI agent can support this workflow by transforming unstructured logistics inquiries into structured, human-reviewable quotation preparation materials.

## What it does

LogiQuote is designed as an AI agent for cross-border logistics quotation preparation.

It helps logistics customer service teams:

1. Summarize a messy customer inquiry.
2. Extract key shipping fields into a structured quotation form.
3. Detect missing or unclear information.
4. Identify potential risk and clarification points, such as DDP requirements, battery-related goods, Amazon warehouse delivery, missing cargo value, or incomplete address details.
5. Generate professional follow-up questions.
6. Produce a customer reply draft for human review.
7. Keep customer service staff in control before any response is sent.

The goal is not to replace logistics staff or automatically generate final prices. Instead, LogiQuote focuses on the earlier stage of the quotation workflow: turning messy customer messages into structured, reviewable information.

## Why it matters

In cross-border logistics, a quotation depends on many details. If the inquiry is incomplete, the quotation may be inaccurate or delayed. A small missing field, such as cargo value, delivery address type, or customs clearance requirement, can affect cost, service scope, compliance risk, and customer communication.

LogiQuote aims to reduce repetitive manual work, improve communication consistency, and help customer service teams prepare quotation-related information more efficiently.

## How it works

The project is designed as an AI workflow for the Autopilot Agent track.

The planned workflow includes:

1. **Input Layer**
   A logistics customer service user enters or pastes a customer inquiry in English or Chinese.

2. **Field Extraction Layer**
   The agent extracts structured fields such as origin, destination, cargo type, weight, volume, package details, shipping mode, delivery requirement, preferred option, trade term, cargo value, pickup address, delivery address type, insurance requirement, customs clearance requirement, and special cargo risk.

3. **Missing Field Detection Layer**
   The agent checks which required fields are missing or unclear before a quotation can be prepared.

4. **Risk and Clarification Layer**
   The agent identifies possible operational or compliance risks, such as battery-related goods, DDP requirements, missing cargo value, Amazon warehouse delivery, or unclear delivery address type.

5. **Reply Generation Layer**
   The agent generates a polite customer follow-up reply and internal operation notes.

6. **Human Review Layer**
   The final output is designed for customer service staff to review, edit, and confirm before sending any response to the customer.

## Current progress

The current version of the project includes:

* A clear product concept and workflow design.
* A structured logistics quotation field schema.
* English and Chinese sample inquiry test cases.
* Prompt modules for field extraction, missing-field detection, and reply generation.
* A human-in-the-loop workflow design.
* A GitHub repository organized for hackathon development.
* Documentation for project story, evaluation, architecture, and deployment planning.

During the hackathon submission period, this project is being upgraded into a Qwen-powered AI agent. The next development steps include Qwen Cloud API integration, a simple Streamlit interface, Alibaba Cloud deployment, demo video production, and final Devpost submission.

## Built with

Planned and current technologies include:

* Qwen Cloud
* Alibaba Cloud
* Python
* Streamlit
* JSON
* Prompt Engineering
* GitHub

## Challenges

One key challenge is preventing the AI agent from inventing missing logistics information. In quotation preparation, details such as address, cargo value, shipping mode, and trade term must be accurate. Therefore, the prompt rules require the model to mark unknown information as `"missing"` or `"unclear"` instead of guessing.

Another challenge is balancing completeness and usability. If the agent asks too many follow-up questions at once, the customer experience may become poor. To address this, the reply generation prompt prioritizes the most important missing fields and groups related questions together.

A third challenge is designing the project as an agent workflow rather than a simple chatbot. LogiQuote is structured around a business process: inquiry understanding, field extraction, missing information check, risk detection, reply drafting, and human review.

## Accomplishments so far

The project currently has:

* A focused real-world logistics use case.
* A clear AI agent workflow.
* Structured prompt design.
* Sample test cases in both English and Chinese.
* A quotation field schema for consistent output.
* A repository structure suitable for further development.
* A product direction that connects AI agents, business operations, logistics customer service, and information systems.

## What I learned

Through this project, I learned that building an AI agent for a real business workflow is different from simply building a chatbot. A useful AI agent needs clear input and output structure, domain-specific rules, risk control, test cases, and human review.

I also learned that prompt design should be connected to product logic. In logistics quotation preparation, the agent should not only generate text, but also support structured decision-making by identifying missing information and operational risks.

This project helped me better understand how AI agents can be applied to enterprise workflows, especially in logistics, customer service, business operations, and information systems.

## What's next

Next steps include:

1. Integrating Qwen Cloud API into the workflow.
2. Building a simple Streamlit demo interface.
3. Deploying the backend or demo environment on Alibaba Cloud.
4. Adding more realistic logistics inquiry test cases.
5. Creating an architecture diagram for the system.
6. Recording a demo video for Devpost submission.
7. Improving evaluation with field extraction accuracy, missing-field detection accuracy, risk note quality, and reply usability.
8. Exploring customer history and preference memory in future versions.
