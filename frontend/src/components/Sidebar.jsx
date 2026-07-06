import {
  LayoutDashboard,
  AlertTriangle,
  History as HistoryIcon,
  BrainCircuit,
  FileBarChart,
  ClipboardList,
} from "lucide-react";
import { NavLink } from "react-router-dom";

const menu = [
  {
    title: "Dashboard",
    icon: LayoutDashboard,
    path: "/dashboard",
  },
  {
    title: "Incidents",
    icon: AlertTriangle,
    path: "/incidents",
  },
  {
    title: "AI Analysis",
    icon: BrainCircuit,
    path: "/analysis",
  },
  {
    title: "Reports",
    icon: FileBarChart,
    path: "/reports",
  },

  {
    title: "History",
    icon: HistoryIcon,
    path: "/history",
  },
  {
  title: "Manage Incidents",
  icon: ClipboardList,
  path: "/manage-incidents",
},
];

export default function Sidebar() {
  return (
    <aside className="w-72 h-screen bg-[#0B1120] border-r border-slate-800 flex flex-col">
      <div className="p-8 border-b border-slate-800">
        <h1 className="text-3xl font-bold text-cyan-400">
          SentinelIQ
        </h1>

        <p className="text-slate-500 mt-2">
          Incident Intelligence Platform
        </p>
      </div>

      <div className="p-5 flex-1">
        <div className="space-y-3">
          {menu.map((item) => {
            const Icon = item.icon;

            return (
              <NavLink
                key={item.title}
                to={item.path}
                className={({ isActive }) =>
                  `
                  flex
                  items-center
                  gap-4
                  px-5
                  py-4
                  rounded-2xl
                  transition-all
                  duration-300
                  border
                  ${
                    isActive
                      ? "bg-cyan-500/20 border-cyan-500 text-cyan-400"
                      : "border-slate-800 text-slate-400 hover:bg-slate-900 hover:border-slate-700"
                  }
                `
                }
              >
                <Icon size={22} />

                <span className="font-medium text-lg">
                  {item.title}
                </span>
              </NavLink>
            );
          })}
        </div>
      </div>

      <div className="p-5 border-t border-slate-800">
        <div className="bg-slate-900 rounded-2xl p-4">
          <h3 className="font-semibold">
            Chandan S T
          </h3>

          <p className="text-slate-500 text-sm">
            Administrator
          </p>
        </div>
      </div>
    </aside>
  );
}