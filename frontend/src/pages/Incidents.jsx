import { useState } from "react";
import { checkIncident } from "../api/incidentApi";


export default function Incidents() {
  const [event, setEvent] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleCheck = async () => {
    if (!event.trim()) return;

    try {
      setLoading(true);

      const data = await checkIncident(
        event
      );

      setResult(data);
      setEvent("");
    } catch (err) {
      console.error(err);
      alert("Failed to analyze incident.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-5xl font-bold">
          Check Incident
        </h1>

        <p className="text-slate-400 mt-2">
          Analyze logs using RAG + Llama3.
        </p>
      </div>

      <div className="bg-slate-900 rounded-3xl p-8 border border-slate-800">
        <textarea
          rows={8}
          value={event}
          onChange={(e) =>
            setEvent(e.target.value)
          }
          placeholder="Paste logs or incident description..."
          className="
            w-full
            bg-slate-950
            border
            border-slate-700
            rounded-2xl
            p-5
            text-white
            outline-none
          "
        />

        <button
          onClick={handleCheck}
          disabled={loading}
          className="
            mt-5
            bg-cyan-500
            hover:bg-cyan-600
            px-8
            py-3
            rounded-xl
            font-semibold
          "
        >
          {loading
            ? "Analyzing..."
            : "Check Incident"}
        </button>
      </div>

      {result && (
        <div className="bg-slate-900 rounded-3xl p-8 border border-slate-800">
          <h2 className="text-3xl font-bold mb-6">
            AI Analysis
          </h2>

          <div className="space-y-4">
            <p>
              <strong>Title:</strong>{" "}
              {result.title}
            </p>

            <p>
              <strong>Severity:</strong>{" "}
              {result.severity}
            </p>

            <p>
              <strong>Risk Score:</strong>{" "}
              {result.risk_score}
            </p>

            <p>
              <strong>Root Cause:</strong>{" "}
              {result.root_cause}
            </p>

            <p>
              <strong>Business Impact:</strong>{" "}
              {result.business_impact}
            </p>

            <div>
              <strong>
                Recommendations:
              </strong>

              <ul className="list-disc pl-6 mt-3 space-y-2">
                {result.recommendations?.map(
                  (r, i) => (
                    <li key={i}>{r}</li>
                  )
                )}
              </ul>
            </div>

            <p className="text-green-400 pt-4">
              Incident #{result.incident_id}
              {" "}
              created successfully.
            </p>
          </div>
        </div>
      )}
    </div>
  );
}