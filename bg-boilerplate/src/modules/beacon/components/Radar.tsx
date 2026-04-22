import React, { useEffect, useState } from 'react';
import { motion } from 'motion/react';

export const Radar: React.FC = () => {
  const [rotation, setRotation] = useState(0);
  const [blips, setBlips] = useState<{ id: number; x: number; y: number; opacity: number }[]>([]);

  useEffect(() => {
    const interval = setInterval(() => {
      setRotation((prev) => (prev + 2) % 360);
    }, 50);
    const blipInterval = setInterval(() => {
      if (Math.random() > 0.7) {
        const newBlip = {
          id: Date.now(),
          x: 30 + Math.random() * 40,
          y: 30 + Math.random() * 40,
          opacity: 1,
        };
        setBlips((prev) => [...prev.slice(-5), newBlip]);
      }
    }, 2000);
    return () => {
      clearInterval(interval);
      clearInterval(blipInterval);
    };
  }, []);

  return (
    <div className="relative w-full aspect-square max-w-[250px] mx-auto">
      <div className="absolute top-2 left-2 text-[9px] text-accent-cyan/60 font-mono tracking-wider">Zone-4</div>
      <div className="absolute bottom-2 right-2 text-[9px] text-accent-green/60 font-mono tracking-wider">TARGET:OIL_PUMP_01</div>
      <svg viewBox="0 0 100 100" className="w-full h-full">
        {/* Radar Circles */}
        {[15, 25, 35, 45].map((r) => (
          <circle key={r} cx="50" cy="50" r={r} fill="none" stroke="rgba(0,242,255,0.1)" strokeWidth="0.3" />
        ))}
        {/* Crosshair */}
        <line x1="50" y1="5" x2="50" y2="95" stroke="rgba(0,242,255,0.08)" strokeWidth="0.3" />
        <line x1="5" y1="50" x2="95" y2="50" stroke="rgba(0,242,255,0.08)" strokeWidth="0.3" />
        {/* Sweeper */}
        <line
          x1="50" y1="50"
          x2={50 + 45 * Math.cos((rotation * Math.PI) / 180)}
          y2={50 + 45 * Math.sin((rotation * Math.PI) / 180)}
          stroke="rgba(0,242,255,0.4)" strokeWidth="0.5"
        />
        {/* Blips */}
        {blips.map((blip) => (
          <motion.circle
            key={blip.id}
            cx={blip.x} cy={blip.y} r="1.5"
            fill="#39ff14"
            initial={{ opacity: 0, scale: 0 }}
            animate={{ opacity: [1, 0.3], scale: [0, 1.5] }}
            transition={{ duration: 3, ease: "easeOut" }}
          />
        ))}
      </svg>
    </div>
  );
};
