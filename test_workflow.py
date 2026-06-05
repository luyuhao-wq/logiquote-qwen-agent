import json
from agent_workflow import run_logiquote_agent


def main():
    customer_inquiry = """
Hi, I need to ship 20 cartons of home decor products from Ningbo to Los Angeles.
Total weight is around 480 kg and volume is 3.2 CBM.
Could you quote me the cheapest option within 25 days?
"""

    result = run_logiquote_agent(customer_inquiry)

    print("===== LogiQuote Agent Workflow Result =====")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
