import json
import re

class ValidatorEngine:
    def __init__(self):
        print("Validator-Engine-Pro: Initialized Natively (Upgraded).")

    def repair_and_validate(self, raw_stream: str) -> dict:
        cleaned = raw_stream.strip()
        repaired = False
        error_logs = []

        if "```json" in cleaned:
            match = re.search(r"```json\s*(.*?)\s*```", cleaned, re.DOTALL)
            if not match:
                match = re.search(r"```json\s*(.*)", cleaned, re.DOTALL)
            if match:
                cleaned = match.group(1).strip()
                repaired = True
                error_logs.append("Sanitized markdown wrappers.")

        if cleaned.startswith("{") and not cleaned.endswith("}"):
            cleaned += "}"
            repaired = True
            error_logs.append("Appended missing brace.")

        try:
            parsed_data = json.loads(cleaned)
            return {
                "status": "SUCCESS",
                "repaired": repaired,
                "logs": error_logs,
                "payload": parsed_data
            }
        except json.JSONDecodeError as e:
            return {
                "status": "FALLBACK_TRIGGERED",
                "repaired": False,
                "logs": [f"Exception: {str(e)}"],
                "payload": {"raw_recovered_text": raw_stream}
            }

if __name__ == "__main__":
    engine = ValidatorEngine()
    broken_ai_payload = '```json\n{\n   "status": "active",\n   "message": "Processing data stream" '
    result = engine.repair_and_validate(broken_ai_payload)
    print("\n--- Upgraded Test Verification Output ---")
    print(f"Engine Status: {result['status']}")
    print(f"Repairs Made: {result['repaired']}")
    print(f"Action Logs: {result['logs']}")
    print(f"Clean Payload Out: {result['payload']}")
