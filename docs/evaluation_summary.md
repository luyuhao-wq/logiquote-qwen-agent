# Evaluation Summary

## Overview

This document summarizes the initial evaluation of LogiQuote, a Qwen-powered AI agent for cross-border logistics quotation preparation.

The goal of this evaluation is to test whether the agent can handle different types of customer inquiries, extract key logistics fields, detect missing information, identify operational risks, and generate customer-service-ready follow-up replies.

## Evaluation Setup

The batch test was conducted using five sample logistics inquiries stored in `data/sample_inquiries.json`.

The tested workflow includes three main stages:

1. **Field Extraction**
   Extract structured quotation fields from an unstructured customer inquiry.

2. **Missing Field and Risk Check**
   Identify missing or unclear information required before a quotation can be prepared.

3. **Reply Generation**
   Generate a customer follow-up reply, follow-up questions, and internal operation notes for human review.

The batch test script `test_batch.py` runs the full workflow for all five sample cases and saves the result to:

```text
data/batch_test_results.json
```

## Test Cases

| Case ID  | Language | Scenario                                                  | Main Evaluation Focus                                                             |
| -------- | -------- | --------------------------------------------------------- | --------------------------------------------------------------------------------- |
| case_001 | English  | Standard shipment inquiry from Ningbo to Los Angeles      | Basic field extraction, missing trade term, missing pickup/delivery details       |
| case_002 | Chinese  | Bluetooth speakers from Shenzhen to a US Amazon warehouse | Chinese input handling, Amazon warehouse delivery, battery-related risk           |
| case_003 | English  | DDP quote for LED lights from Guangzhou to Toronto        | DDP requirement, missing weight/volume, customs and cargo value risk              |
| case_004 | English  | Furniture sea freight from Foshan to Sydney               | Sea freight preference, cheaper option, missing weight/volume                     |
| case_005 | Chinese  | Highly incomplete inquiry to Germany                      | Low-information input, missing field detection, insufficient information handling |

## Evaluation Criteria

The agent was evaluated based on the following criteria:

1. **Field Extraction Accuracy**
   Whether the agent correctly extracts origin, destination, cargo type, weight, volume, package details, shipping mode, delivery requirement, and trade term.

2. **Missing Field Detection**
   Whether the agent correctly identifies missing information required for quotation preparation.

3. **Risk Identification**
   Whether the agent identifies relevant logistics risks such as battery-related goods, DDP requirements, Amazon warehouse delivery, missing cargo value, or unclear delivery address type.

4. **Reply Usability**
   Whether the generated customer reply is polite, clear, practical, and suitable for customer service staff to review and edit.

5. **Human-in-the-loop Design**
   Whether the system avoids directly producing a final quotation and keeps logistics staff in control before any customer-facing response is sent.

## Results

### case_001: Standard English Inquiry

The agent correctly extracted the key fields, including origin, destination, cargo type, weight, volume, package details, delivery requirement, and preferred option. It also correctly identified missing fields such as shipping mode, trade term, cargo value, pickup address, delivery address type, insurance requirement, and customs clearance requirement.

The generated reply was concise and asked for the most important missing information first.

**Result:** Successful

### case_002: Chinese Bluetooth Speaker Inquiry

The agent correctly handled Chinese input and extracted Shenzhen as the origin, US Amazon warehouse as the destination, Bluetooth speakers as the cargo type, 200 kg as weight, 1.5 CBM as volume, and air freight with last-mile delivery as the shipping mode.

It also identified battery-related risk and Amazon warehouse delivery requirements. The generated Chinese reply was practical and suitable for customer service review.

**Result:** Successful

### case_003: DDP LED Lights Inquiry

The agent correctly identified Guangzhou as the origin, Toronto as the destination, LED lights as the cargo type, 10 cartons as package details, and DDP as the trade term. It also detected missing weight, volume, pickup address, delivery address type, cargo value, and insurance requirement.

The agent conservatively flagged possible battery-related risk and asked for confirmation instead of treating it as confirmed fact.

**Result:** Successful, with conservative risk flagging

### case_004: Furniture Sea Freight Inquiry

The agent correctly extracted Foshan as origin, Sydney as destination, furniture as cargo type, 3 pallets as package details, sea freight as shipping mode, not urgent as delivery requirement, and cheaper as the preferred option.

It correctly detected missing weight, volume, trade term, cargo value, pickup address, delivery address type, insurance requirement, and customs clearance requirement.

**Result:** Successful

### case_005: Highly Incomplete Chinese Inquiry

The agent correctly identified that the inquiry lacked most quotation-critical information. It extracted Germany as the destination and sea freight as the possible shipping mode, while marking origin, cargo type, weight, volume, package details, delivery requirement, trade term, cargo value, pickup address, delivery address type, insurance requirement, and customs clearance requirement as missing.

The system correctly set quotation readiness as `insufficient_information`.

**Result:** Successful

## Key Findings

The initial evaluation shows that LogiQuote can:

* Process both English and Chinese logistics inquiries.
* Extract structured quotation fields from unstructured messages.
* Detect missing quotation-critical information.
* Identify relevant operational and compliance risks.
* Generate practical customer follow-up replies.
* Support human-in-the-loop review instead of directly producing final quotations.

## Limitations

The current version is still an early prototype. It does not calculate real shipping prices, connect to carrier rate databases, or validate customs regulations with external data sources.

Some risk notes are intentionally conservative. For example, the agent may ask staff to confirm whether certain electronic products contain batteries. This is useful for safety and compliance, but future versions should improve risk classification with more precise product and regulatory data.

## Next Steps

Future improvements include:

1. Expanding the test set with more real-world logistics inquiries.
2. Adding structured scoring for extraction accuracy and missing-field detection.
3. Improving product risk classification.
4. Connecting the agent with external rate tables or quotation databases.
5. Building a dashboard-style interface for customer service staff.
6. Deploying the backend on Alibaba Cloud for hackathon submission.
7. Adding more detailed logging and error handling for production-readiness.
