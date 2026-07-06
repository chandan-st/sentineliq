import { motion } from "framer-motion";

export default function MetricCard({
  title,
  value,
  icon: Icon,
  color,
}) {
  return (
    <motion.div
      whileHover={{
        y: -8,
        scale: 1.03,
      }}
      className="
        bg-slate-900
        rounded-3xl
        p-8
        border
        border-slate-800
        shadow-xl
      "
    >
      <div
        className={`
          w-14
          h-14
          rounded-2xl
          ${color}
          flex
          items-center
          justify-center
          mb-5
        `}
      >
        <Icon size={28} />
      </div>

      <h3 className="text-slate-400">
        {title}
      </h3>

      <h1 className="text-5xl font-bold mt-4">
        {value}
      </h1>
    </motion.div>
  );
}