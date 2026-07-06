import { useQuery } from "@tanstack/react-query";
import {
  getMetrics,
  getRecentIncidents,
} from "../api/dashboardApi";

export default function Reports() {
  const { data: metrics } = useQuery({
    queryKey: ["metrics"],
    queryFn: getMetrics,
  });

  const { data: incidents = [] } =
    useQuery({
      queryKey: ["recent"],
      queryFn: getRecentIncidents,
    });

  const downloadCSV = () => {
    const headers = [
      "ID",
      "Title",
      "Severity",
      "Status",
      "Created At",
    ];

    const rows = incidents.map((i) => [
      i.id,
      i.title,
      i.severity,
      i.status,
      i.created_at,
    ]);

    const csv = [
      headers,
      ...rows,
    ]
      .map((r) => r.join(","))
      .join("\n");

    const blob = new Blob(
      [csv],
      {
        type: "text/csv",
      }
    );

    const url =
      window.URL.createObjectURL(blob);

    const a =
      document.createElement("a");

    a.href = url;
    a.download =
      "sentineliq-report.csv";

    a.click();

    window.URL.revokeObjectURL(url);
  };

  return (
    <div>
      <h1 className="text-5xl font-bold mb-10">
        Reports
      </h1>

      <div className="grid grid-cols-4 gap-8 mb-10">
        <Card
          title="Total"
          value={
            metrics?.total_incidents || 0
          }
        />

        <Card
          title="Critical"
          value={
            metrics?.critical || 0
          }
        />

        <Card
          title="Open"
          value={metrics?.open || 0}
        />

        <Card
          title="Resolved"
          value={
            metrics?.resolved || 0
          }
        />
      </div>

      <button
        onClick={downloadCSV}
        className="
          bg-cyan-500
          px-6
          py-3
          rounded-2xl
          font-semibold
        "
      >
        Download CSV Report
      </button>
    </div>
  );
}

function Card({
  title,
  value,
}) {
  return (
    <div
      className="
        bg-slate-900
        rounded-3xl
        border
        border-slate-800
        p-8
      "
    >
      <h3 className="text-slate-400">
        {title}
      </h3>

      <p className="text-4xl font-bold mt-4">
        {value}
      </p>
    </div>
  );
}