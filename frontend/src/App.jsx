import { Routes, Route, Navigate } from "react-router-dom";
import Sidebar from "./components/Sidebar";
import Dashboard from "./pages/Dashboard";
import Incidents from "./pages/Incidents";
import History from "./pages/History";
import ManageIncidents from "./pages/ManageIncidents";
import Reports from "./pages/Reports";

function Page({ title }) {
  return (
    <div className="text-5xl font-bold">
      {title}
    </div>
  );
}

export default function App() {
  return (
    <div className="flex h-screen bg-slate-950 text-white">
      <Sidebar />

      <main className="flex-1 overflow-auto p-10">
        <Routes>
          <Route
            path="/"
            element={<Navigate to="/dashboard" />}
          />

          <Route
            path="/dashboard"
            element={<Dashboard />}
          />

          <Route
            path="/analysis"
            element={<Page title="AI Analysis (Coming Soon)" />}
          />


          <Route
            path="/incidents"
            element={<Incidents />}
          />
          <Route
            path="/history"
            element={<History />}
          />

          <Route
            path="/manage-incidents"
            element={<ManageIncidents />}
          />
          <Route
            path="/reports"
            element={<Reports />}
          />    

        </Routes>
      </main>
    </div>
  );
}