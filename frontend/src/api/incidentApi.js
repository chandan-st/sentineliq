import api from "./api";

export const checkIncident = async (event) => {
  const res = await api.post(
    "/api/incidents/check",
    {
      event,
    }
  );

  return res.data;


};

export const deleteIncident = async (
  id
) => {
  const res = await api.delete(
    `/api/incidents/${id}`
  );

  return res.data;
};

export const resolveIncident = async (
  id
) => {
  const res = await api.put(
    `/api/incidents/${id}/resolve`
  );

  return res.data;
};

export const getIncidents = async () => {
  const res = await api.get(
    "/api/incidents"
  );

  return res.data;
};