import { useQuery } from "@tanstack/react-query";
import {
  AlertTriangle,
  Activity,
  Server,
  ShieldAlert,
} from "lucide-react";

import {
  getMetrics,
  getRecentIncidents,
  getSeverity,
} from "../api/dashboardApi";

import MetricCard from "../components/MetricCard";

import {
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
  Tooltip,
} from "recharts";

const COLORS = [
  "#ef4444",
  "#f97316",
  "#facc15",
  "#22c55e",
];

export default function Dashboard() {
  const { data: metrics } = useQuery({
    queryKey: ["metrics"],
    queryFn: getMetrics,
  });

  const { data: severity } = useQuery({
    queryKey: ["severity"],
    queryFn: getSeverity,
  });

  const { data: incidents } = useQuery({
    queryKey: ["recent"],
    queryFn: getRecentIncidents,
  });

  const pieData = severity
    ? Object.entries(severity).map(
        ([name, value]) => ({
          name,
          value,
        })
      )
    : [];

  return (
    <div>
      <div className="mb-10">
        <h1 className="text-5xl font-bold">
          Dashboard
        </h1>

        <p className="text-slate-400 mt-2">
          AI-powered incident intelligence.
        </p>
      </div>

      {/* KPI */}

      <div className="grid grid-cols-4 gap-8 mb-10">
        <MetricCard
          title="Total"
          value={metrics?.total_incidents || 0}
          icon={Activity}
          color="bg-cyan-500"
        />

        <MetricCard
          title="Critical"
          value={metrics?.critical || 0}
          icon={ShieldAlert}
          color="bg-red-500"
        />

        <MetricCard
          title="Open"
          value={metrics?.open || 0}
          icon={AlertTriangle}
          color="bg-yellow-500"
        />

        <MetricCard
          title="Resolved"
          value={metrics?.resolved || 0}
          icon={Server}
          color="bg-green-500"
        />
      </div>

      {/* CHART */}

      <div
        className="
          bg-slate-900
          rounded-3xl
          p-8
          border
          border-slate-800
          mb-10
        "
      >
        <h2 className="text-2xl font-bold mb-8">
          Severity Distribution
        </h2>

        <ResponsiveContainer
          width="100%"
          height={350}
        >
          <PieChart>
            <Pie
              data={pieData}
              dataKey="value"
              outerRadius={120}
            >
              {pieData.map((_, index) => (
                <Cell
                  key={index}
                  fill={COLORS[index]}
                />
              ))}
            </Pie>

            <Tooltip />
          </PieChart>
        </ResponsiveContainer>
      </div>

      {/* TABLE */}

      <div
        className="
          bg-slate-900
          rounded-3xl
          p-8
          border
          border-slate-800
        "
      >
        <h2 className="text-2xl font-bold mb-8">
          Recent Incidents
        </h2>

        <table className="w-full">
          <thead>
            <tr className="text-slate-500">
              <th className="text-left pb-4">
                ID
              </th>

              <th className="text-left pb-4">
                Title
              </th>

              <th className="text-left pb-4">
                Severity
              </th>

              <th className="text-left pb-4">
                Status
              </th>
            </tr>
          </thead>

          <tbody>
            {incidents?.map((item) => (
              <tr
                key={item.id}
                className="border-t border-slate-800"
              >
                <td className="py-5">
                  #{item.id}
                </td>

                <td>{item.title}</td>

                <td>{item.severity}</td>

                <td>{item.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}