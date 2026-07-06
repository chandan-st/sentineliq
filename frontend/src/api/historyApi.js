import api from "./api";

export const getHistory = async () => {
  const res = await api.get(
    "/api/history"
  );

  return res.data;
};