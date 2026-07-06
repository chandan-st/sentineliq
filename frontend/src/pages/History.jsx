import { useQuery } from "@tanstack/react-query";
import { getHistory } from "../api/historyApi";

export default function History() {
  const { data = [] } = useQuery({
    queryKey: ["history"],
    queryFn: getHistory,
  });

  return (
    <div>
      <h1 className="text-5xl font-bold mb-10">
        Analysis History
      </h1>

      <div className="space-y-6">
        {data.map((item) => (
          <div
            key={item.id}
            className="
              bg-slate-900
              p-6
              rounded-3xl
              border
              border-slate-800
            "
          >
            <h2 className="text-2xl font-bold">
              {item.title}
            </h2>

            <p className="text-red-400">
              {item.severity}
            </p>

            <p className="mt-2 text-yellow-400 font-medium">
              Risk Score: {item.risk_score ?? "N/A"}
            </p>

            <p className="mt-2 text-slate-500 text-sm">
              {item.created_at
                ? new Date(item.created_at).toLocaleString()
                : "Unknown time"}
            </p>

            <div className="mt-4">
              <h3 className="font-semibold mb-2">
                Summary
              </h3>
              <p>{item.summary}</p>
            </div>

            <div className="mt-4 text-slate-300">
              <h3 className="font-semibold mb-2">
                Root Cause
              </h3>
              <p>{item.root_cause}</p>
            </div>

            <div className="mt-4 text-cyan-400">
              <h3 className="font-semibold mb-2 text-white">
                Business Impact
              </h3>
              <p>{item.business_impact}</p>
            </div>

            <div className="mt-5">
              <h3 className="font-semibold mb-2">
                Recommendations
              </h3>

              <ul className="list-disc ml-6 space-y-2 text-slate-300">
                {(item.recommendations || []).map(
                  (rec, index) => (
                    <li key={index}>
                      {typeof rec === "string"
                        ? rec
                        : rec.step}
                    </li>
                  )
                )}
              </ul>
            </div>

            <div className="mt-5 text-slate-500 border-t border-slate-800 pt-4">
              <h3 className="font-semibold mb-2 text-slate-400">
                Original Event
              </h3>
              <p>{item.event}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}