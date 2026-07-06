import { Link, useLocation } from "react-router-dom";

export default function Navbar() {
  const location = useLocation();

  const linkClass = (path) =>
    `
      px-5
      py-3
      rounded-xl
      transition
      ${
        location.pathname === path
          ? "bg-cyan-500 text-white"
          : "text-slate-300 hover:bg-slate-800"
      }
    `;

  return (
    <div
      className="
        w-72
        min-h-screen
        bg-slate-950
        border-r
        border-slate-800
        p-8
      "
    >
      <h1
        className="
          text-3xl
          font-bold
          text-cyan-400
          mb-12
        "
      >
        SentinelIQ
      </h1>

      <nav className="flex flex-col gap-4">
        <Link
          to="/dashboard"
          className={linkClass(
            "/dashboard"
          )}
        >
          Dashboard
        </Link>

        <Link
          to="/incidents"
          className={linkClass(
            "/incidents"
          )}
        >
          Check Incident
        </Link>
      </nav>
    </div>
  );
}