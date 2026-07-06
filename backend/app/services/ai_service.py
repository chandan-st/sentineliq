import json
import re
import requests
from app.services.incident_similarity import find_similar_incidents

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
        "title": message[:60] if message else "Incident Analysis",
        "severity": "Medium",
        "risk_score": 50,
        "summary": message,
        "recommendations": [
            "Review logs manually."
        ]
    }

def analyze_incident_with_context(message: str):
    similar_incidents = find_similar_incidents(
        message,
        top_k=5
    )

    context = ""

    for i, incident in enumerate(similar_incidents, start=1):
        context += f"""
Incident {i}
Event: {incident['event']}
Severity: {incident['severity']}
Root Cause: {incident['root_cause']}
Recommendation:
{incident['recommendation']}

"""

    prompt = f"""
You are a Senior Site Reliability Engineer.

Current Incident:
{message}
You MUST infer the most likely enterprise incident even if the input is short or ambiguous. NEVER return 'Unknown' for title, root_cause, or business_impact. If information is missing, make a reasonable engineering assumption.

Historical Similar Incidents:
{context}

Do not blindly copy historical incidents.
Use them only as references.
Infer the most probable root cause and recommendations based on the current incident symptoms.

Analyze the current incident using the historical incidents.

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
    "root_cause": "",
    "summary": "",
    "recommendations": [],
    "business_impact": ""
}}

The title should be a concise incident name like 'CPU Saturation Detected', 'Database Timeout', 'Authentication Failure', or 'Network Connectivity Issue'.

Rules:
- recommendations MUST contain at least 3 actionable steps.
- Never return an empty recommendations array.
- risk_score must be between 1 and 100.
- summary MUST contain 1-2 sentences describing the incident.
- business_impact MUST explain how users or services are affected.
- Never leave summary or business_impact empty.
- Use historical incidents to infer root causes and recommendations.
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

        print("\n===== CONTEXT AWARE RESPONSE =====")
        print(result)
        print("==================================\n")

        try:
            data = json.loads(result)

            recommendations = data.get(
                "recommendations",
                []
            )

            if recommendations and isinstance(recommendations[0], dict):
                recommendations = [
                    item.get("step", "")
                    for item in recommendations
                ]

            data["recommendations"] = recommendations

            if not data.get("title"):
                data["title"] = message[:60] if message else "Incident Analysis"

            if not data.get("summary"):
                data["summary"] = (
                    f"{data['title']} detected. Immediate investigation is recommended."
                )

            if not data.get("business_impact"):
                data["business_impact"] = (
                    "Potential service degradation affecting users and dependent systems."
                )

            if not data.get("root_cause"):
                data["root_cause"] = "Likely application or infrastructure degradation requiring investigation"

            return data
        except:
            match = re.search(r"\{.*\}", result, re.DOTALL)

            if match:
                data = json.loads(match.group(0))

                recommendations = data.get(
                    "recommendations",
                    []
                )

                if recommendations and isinstance(recommendations[0], dict):
                    recommendations = [
                        item.get("step", "")
                        for item in recommendations
                    ]

                data["recommendations"] = recommendations

                if not data.get("title"):
                    data["title"] = message[:60] if message else "Incident Analysis"

                if not data.get("summary"):
                    data["summary"] = (
                        f"{data['title']} detected. Immediate investigation is recommended."
                    )

                if not data.get("business_impact"):
                    data["business_impact"] = (
                        "Potential service degradation affecting users and dependent systems."
                    )

                if not data.get("root_cause"):
                    data["root_cause"] = "Likely application or infrastructure degradation requiring investigation"

                return data

    except Exception as e:
        print("CONTEXT AI ERROR:", e)

    return {
        "title": message[:60] if message else "Incident Analysis",
        "severity": "Medium",
        "risk_score": 50,
        "root_cause": "Likely application or infrastructure degradation requiring investigation",
        "summary": (
            f"{message[:60]} detected. Immediate investigation is recommended."
            if message else
            "Incident detected. Immediate investigation is recommended."
        ),
        "recommendations": [
            "Review application and infrastructure logs.",
            "Inspect CPU, memory, and network metrics.",
            "Escalate to the engineering team if the issue persists."
        ],
        "business_impact": "Potential service degradation affecting users and dependent systems."
    }