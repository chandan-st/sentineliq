import api from "./api";

export const getMetrics = async () => {
  const res = await api.get("/api/dashboard/metrics");
  return res.data;
};

export const getSeverity = async () => {
  const res = await api.get("/api/dashboard/severity");
  return res.data;
};

export const getRecentIncidents = async () => {
  const res = await api.get("/api/dashboard/recent");
  return res.data;
};