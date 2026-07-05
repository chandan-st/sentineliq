import json
import re
import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"


def analyze_incident(message: str):
    prompt = f"""
You are a Senior Site Reliability Engineer (SRE).

Analyze the following system event.

Event:
{message}

IMPORTANT RULES:
1. Return ONLY raw JSON.
2. Do NOT explain anything.
3. Do NOT use markdown.
4. Do NOT write any text before or after the JSON.

Return EXACTLY this schema:

{{
    "title": "",
    "severity": "",
    "risk_score": 0,
    "summary": "",
    "recommendations": []
}}

Rules:
- recommendations MUST contain at least 3 actionable steps.
- Never return an empty recommendations array.
- Recommendations should be specific remediation steps.
- risk_score must be between 1 and 100.

Severity must be one of:
Low
Medium
High
Critical
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0
                }
            },
            timeout=180,
        )

        response.raise_for_status()

        result = response.json().get("response", "").strip()

        print("\n===== RAW LLM RESPONSE =====")
        print(result)
        print("============================\n")

        # Try direct JSON parsing
        try:
            parsed = json.loads(result)

            recommendations = parsed.get("recommendations", [])
            severity = str(
                parsed.get("severity", "Medium")
            ).capitalize()

            if not recommendations:
                default_recommendations = {
                    "Critical": [
                        "Investigate system logs immediately.",
                        "Restart affected services.",
                        "Escalate to the on-call engineering team."
                    ],
                    "High": [
                        "Check service health and dependencies.",
                        "Review application and database logs.",
                        "Monitor the system for further degradation."
                    ],
                    "Medium": [
                        "Review system metrics and logs.",
                        "Investigate the root cause.",
                        "Continue monitoring the incident."
                    ],
                    "Low": [
                        "Document the issue.",
                        "Monitor for recurrence.",
                        "Schedule preventive maintenance."
                    ]
                }

                parsed["recommendations"] = default_recommendations.get(
                    severity,
                    ["Review logs manually."]
                )
            print('FINAL PARSED RESPONSE:', parsed)
            return parsed
        except:
            pass

        # Extract JSON object from text
        match = re.search(r"\{.*\}", result, re.DOTALL)

        if match:
            json_text = match.group(0)

            # Remove trailing commas
            json_text = re.sub(r",(\s*[}\]])", r"\1", json_text)

            data = json.loads(json_text)

            # Normalize severity
            severity = str(
                data.get("severity", "Medium")
            ).capitalize()

            allowed = [
                "Low",
                "Medium",
                "High",
                "Critical",
            ]

            if severity not in allowed:
                severity = "Medium"

            data["severity"] = severity

            # Ensure risk score exists
            try:
                data["risk_score"] = int(
                    data.get("risk_score", 50)
                )
            except:
                data["risk_score"] = 50

            # Ensure recommendations is a list
            recommendations = data.get(
                "recommendations",
                []
            )

            if isinstance(recommendations, str):
                recommendations = [recommendations]

            elif isinstance(recommendations, dict):
                recommendations = [
                    f"{k}: {v}"
                    for k, v in recommendations.items()
                ]

            elif not isinstance(
                recommendations,
                list,
            ):
                recommendations = []

            if len(recommendations) == 0:
                default_recommendations = {
                    "Critical": [
                        "Investigate system logs immediately.",
                        "Restart affected services.",
                        "Escalate to the on-call engineering team."
                    ],
                    "High": [
                        "Check service health and dependencies.",
                        "Review application and database logs.",
                        "Monitor the system for further degradation."
                    ],
                    "Medium": [
                        "Review system metrics and logs.",
                        "Investigate the root cause.",
                        "Continue monitoring the incident."
                    ],
                    "Low": [
                        "Document the issue.",
                        "Monitor for recurrence.",
                        "Schedule preventive maintenance."
                    ]
                }

                recommendations = default_recommendations.get(
                    severity,
                    ["Review logs manually."]
                )

            data["recommendations"] = recommendations
            return data

    except Exception as e:
        print("OLLAMA ERROR:", e)

    return {
        "title": "Unknown Incident",
        "severity": "Medium",
        "risk_score": 50,
        "summary": message,
        "recommendations": [
            "Review logs manually."
        ]
    }