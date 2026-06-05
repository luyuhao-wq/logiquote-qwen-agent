import json
from pathlib import Path
from agent_workflow import run_logiquote_agent


def load_sample_inquiries():
    sample_path = Path("data/sample_inquiries.json")
    return json.loads(sample_path.read_text(encoding="utf-8"))


def main():
    samples = load_sample_inquiries()
    results = []

    for sample in samples:
        print(f"\n===== Running {sample['case_id']} =====")
        inquiry = sample["inquiry"]

        result = run_logiquote_agent(inquiry)
        result["case_id"] = sample["case_id"]
        result["language"] = sample["language"]
        result["expected_output_focus"] = sample["expected_output_focus"]

        results.append(result)

        print(json.dumps(result, ensure_ascii=False, indent=2))

    output_path = Path("data/batch_test_results.json")
    output_path.write_text(
        json.dumps(results, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print("\nBatch test completed.")
    print("Results saved to data/batch_test_results.json")


if __name__ == "__main__":
    main()
