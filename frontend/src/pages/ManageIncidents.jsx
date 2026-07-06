import {
  useMutation,
  useQuery,
  useQueryClient,
} from "@tanstack/react-query";

import { Trash2 } from "lucide-react";

import {
  getIncidents,
  deleteIncident,
  resolveIncident,
} from "../api/incidentApi";

export default function ManageIncidents() {
  const queryClient =
    useQueryClient();

  const {
    data: incidents = [],
    isLoading,
  } = useQuery({
    queryKey: ["incidents"],
    queryFn: getIncidents,
  });

  const deleteMutation =
    useMutation({
      mutationFn: deleteIncident,
      onSuccess: () => {
        queryClient.invalidateQueries({
          queryKey: ["incidents"],
        });
      },
    });

  const resolveMutation =
    useMutation({
      mutationFn: resolveIncident,
      onSuccess: () => {
        queryClient.invalidateQueries({
          queryKey: ["incidents"],
        });

        queryClient.invalidateQueries({
          queryKey: ["metrics"],
        });

        queryClient.invalidateQueries({
          queryKey: ["recent"],
        });
      },
    });

  if (isLoading) {
    return (
      <div className="text-xl">
        Loading incidents...
      </div>
    );
  }

  if (incidents.length === 0) {
    return (
      <div>
        <h1 className="text-5xl font-bold mb-10">
          Manage Incidents
        </h1>

        <div className="bg-slate-900 rounded-3xl border border-slate-800 p-10 text-center text-slate-400">
          No incidents found.
        </div>
      </div>
    );
  }

  return (
    <div>
      <h1 className="text-5xl font-bold mb-10">
        Manage Incidents
      </h1>

      <div className="bg-slate-900 rounded-3xl border border-slate-800 overflow-hidden">
        <table className="w-full">
          <thead>
            <tr className="border-b border-slate-800">
              <th className="p-5 text-left">
                ID
              </th>

              <th className="p-5 text-left">
                Title
              </th>

              <th className="p-5 text-left">
                Severity
              </th>

              <th className="p-5 text-left">
                Status
              </th>

              <th className="p-5 text-left">
                Actions
              </th>
            </tr>
          </thead>

          <tbody>
            {incidents.map((item) => (
              <tr
                key={item.id}
                className="border-b border-slate-800"
              >
                <td className="p-5">
                  #{item.id}
                </td>

                <td className="p-5">
                  {item.title}
                </td>

                <td className="p-5">
                  {item.severity}
                </td>

                <td className="p-5">
                  <span
                    className={`px-3 py-1 rounded-full text-sm font-semibold ${
                      item.status === "Resolved"
                        ? "bg-green-600"
                        : "bg-yellow-600"
                    }`}
                  >
                    {item.status}
                  </span>
                </td>

                <td className="p-5">
                  <div className="flex items-center gap-3">
                    {item.status !== "Resolved" && (
                      <button
                        onClick={() =>
                          resolveMutation.mutate(item.id)
                        }
                        className="bg-green-600 hover:bg-green-700 px-4 py-2 rounded-xl text-white mr-3"
                      >
                        Resolve
                      </button>
                    )}
                    <button
                      onClick={() => {
                        if (
                          window.confirm(
                            "Delete this incident?"
                          )
                        ) {
                          deleteMutation.mutate(
                            item.id
                          );
                        }
                      }}
                      disabled={deleteMutation.isPending}
                      className="flex items-center gap-2 bg-red-600 hover:bg-red-700 disabled:opacity-50 px-4 py-2 rounded-xl text-white transition"
                    >
                      <Trash2 size={16} />
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}