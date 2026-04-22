/**
 * MetricsControllers — Sliders para ajustar o MetricsEngine em tempo real.
 */
import type { MetricsConfig } from '../services/metricsService';

interface Props {
  config: MetricsConfig;
  onChange: (c: Partial<MetricsConfig>) => void;
}

export default function MetricsControllers({ config, onChange }: Props) {
  return (
    <div className="acrylic-card space-y-2">
      <div className="text-[7px] font-mono text-white/30">ENGINE_CONFIG</div>
      <Slider label="SENSITIVITY" value={config.sensitivity} max={100} onChange={v => onChange({ sensitivity: v })} />
      <Slider label="THRESHOLD" value={config.threshold} max={100} onChange={v => onChange({ threshold: v })} />
      <Slider label="LIFECYCLE_SPD" value={config.lifecycleSpeed} max={10} onChange={v => onChange({ lifecycleSpeed: v })} />
    </div>
  );
}

function Slider({ label, value, max, onChange }: { label: string; value: number; max: number; onChange: (v: number) => void }) {
  return (
    <div>
      <div className="flex justify-between text-[7px] font-mono text-white/20">
        <span>{label}</span><span className="text-[#00FF41]">{typeof value === 'number' ? value.toFixed(0) : value}</span>
      </div>
      <input
        type="range" min={0} max={max} step={1}
        value={value}
        onChange={e => onChange(Number(e.target.value))}
        className="w-full h-1 appearance-none bg-white/5 rounded-full cursor-pointer accent-[#00FF41]"
      />
    </div>
  );
}
