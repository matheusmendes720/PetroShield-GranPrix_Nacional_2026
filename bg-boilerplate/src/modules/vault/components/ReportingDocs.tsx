/**
 * ReportingDocs — Relatórios de incidentes gerados pelos agentes.
 */
import type { ReportLog } from '../services/metricsService';

interface Props {
  reports: ReportLog[];
}

export default function ReportingDocs({ reports }: Props) {
  return (
    <div className="acrylic-card flex flex-col overflow-hidden">
      <div className="text-[7px] font-mono text-white/30 mb-2">CLEVEL_REPORTING_DOCS</div>
      <div className="flex-1 overflow-y-auto custom-scrollbar space-y-2">
        {reports.map((r, i) => (
          <div key={i} className="p-2 rounded bg-white/[0.02] border border-white/5">
            <div className="flex justify-between text-[7px] font-mono mb-1">
              <span className="text-[#00FFFF]">{r.title}</span>
              <span className={r.status === 'FINALIZED' ? 'text-[#00FF41]' : 'text-[#FF6200]'}>{r.status}</span>
            </div>
            <pre className="text-[7px] text-white/30 whitespace-pre-wrap font-mono leading-relaxed">{r.content.slice(0, 200)}...</pre>
          </div>
        ))}
        {reports.length === 0 && (
          <div className="text-[8px] font-mono text-white/15 text-center py-4">NO_REPORTS_GENERATED</div>
        )}
      </div>
    </div>
  );
}
