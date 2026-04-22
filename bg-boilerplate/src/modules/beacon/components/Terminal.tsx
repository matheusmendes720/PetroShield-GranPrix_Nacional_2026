import React, { useState, useEffect, useRef } from 'react';
import { motion } from 'motion/react';
import { Terminal as TerminalIcon } from 'lucide-react';
import { cn } from '../lib/utils';

interface LogEntry {
  id: string;
  timestamp: string;
  type: 'info' | 'warn' | 'error' | 'success' | 'agent';
  message: string;
}

export const Terminal: React.FC = () => {
  const [logs, setLogs] = useState<LogEntry[]>([]);
  const [input, setInput] = useState('');
  const scrollRef = useRef<HTMLDivElement>(null);

  const addLog = (message: string, type: LogEntry['type'] = 'info') => {
    const newLog: LogEntry = {
      id: Math.random().toString(36).substr(2, 9),
      timestamp: new Date().toLocaleTimeString(),
      type,
      message,
    };
    setLogs((prev) => [...prev.slice(-50), newLog]);
  };

  useEffect(() => {
    addLog('Initializing Agent LUMEN-7... OK', 'info');
    addLog('Scanning Star Schema records for Petrol Distribution...', 'agent');
    addLog('Identified anomaly in SCADA Protocol: Node_ID 492 (Valve Pressure)', 'agent');
    addLog('AxeGuard Middleware: ACTIVE', 'success');

    // Simulated log feed (replaces /api/threats fetch)
    const interval = setInterval(() => {
      const types: LogEntry['type'][] = ['info', 'warn', 'agent', 'success'];
      const messages = [
        '[AXEGUARD] Leak Prevented at Refinery DMZ',
        '[SANITIZED] Query contained PII pattern',
        '[ACTION] Redacted & Logged (Score: 0.94)',
        '[SYSTEM] Routine scan complete - all clear',
        '[AGENT] SCADA Node 12 health check: OK',
      ];
      const randomType = types[Math.floor(Math.random() * types.length)];
      const randomMsg = messages[Math.floor(Math.random() * messages.length)];
      addLog(randomMsg, randomType);
    }, 10000);

    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [logs]);

  const handleCommand = (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;
    addLog(`system@nebula-soc:~$ ${input}`, 'info');
    const cmd = input.toLowerCase().trim();
    if (cmd === 'help') {
      addLog('Available commands: help, status, scan, agent-eval, clear', 'info');
    } else if (cmd === 'status') {
      addLog('System Status: OPERATIONAL', 'success');
      addLog('Active Threats: 0', 'success');
      addLog('Profit Saved (Today): $42,400', 'agent');
    } else if (cmd === 'scan') {
      addLog('Initiating deep scan of SCADA assets...', 'warn');
      setTimeout(() => addLog('Scan complete. No vulnerabilities found.', 'success'), 2000);
    } else if (cmd === 'clear') {
      setLogs([]);
    } else {
      addLog(`Command not recognized: ${cmd}`, 'error');
    }
    setInput('');
  };

  return (
    <div className="glass-panel rounded-xl p-0 overflow-hidden h-full flex flex-col">
      <div className="flex items-center gap-2 px-4 py-2 border-b border-white/5 text-[10px] text-accent-cyan/70 font-mono tracking-widest">
        <TerminalIcon className="w-3 h-3" />
        system@nebula-soc:~$ agent-loop --eval --mode=defensive
      </div>
      <div ref={scrollRef} className="flex-1 overflow-y-auto p-4 space-y-1 text-[11px] font-mono">
        {logs.map((log) => (
          <motion.div
            key={log.id}
            initial={{ opacity: 0, x: -10 }}
            animate={{ opacity: 1, x: 0 }}
            className="flex gap-2"
          >
            <span className={cn(
              "shrink-0",
              log.type === 'info' && 'text-accent-cyan/50',
              log.type === 'warn' && 'text-yellow-400/80',
              log.type === 'error' && 'text-accent-red',
              log.type === 'success' && 'text-accent-green',
              log.type === 'agent' && 'text-purple-400',
            )}>
              {log.type === 'info' && '[INFO]'}
              {log.type === 'warn' && '[WARN]'}
              {log.type === 'error' && '[ERROR]'}
              {log.type === 'success' && '[RESULT]'}
              {log.type === 'agent' && '[AGENT]'}
            </span>
            <span className="text-white/70">{log.message}</span>
          </motion.div>
        ))}
      </div>
      <form onSubmit={handleCommand} className="flex items-center gap-2 px-4 py-2 border-t border-white/5 relative">
        <span className="text-accent-cyan/40 text-[10px] font-mono">system@nebula-soc:~$</span>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="bg-transparent border-none outline-none flex-1 font-mono text-accent-cyan placeholder:text-accent-cyan/20 z-10 text-xs"
          placeholder="Enter command..."
          autoFocus
        />
      </form>
    </div>
  );
};
