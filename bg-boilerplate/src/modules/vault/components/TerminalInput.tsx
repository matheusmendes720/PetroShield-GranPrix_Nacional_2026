/**
 * TerminalInput — Input de terminal interativo com histórico.
 */
import { useState, useRef } from 'react';
import type { KeyboardEvent } from 'react';

interface Props {
  onExecute: (cmd: string) => void;
}

export default function TerminalInput({ onExecute }: Props) {
  const [cmd, setCmd] = useState('');
  const inputRef = useRef<HTMLInputElement>(null);

  const handleKeyDown = (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && cmd.trim()) {
      onExecute(cmd.trim());
      setCmd('');
    }
  };

  return (
    <div className="flex items-center gap-2 text-[9px] font-mono">
      <span className="text-[#00FF41]/60 shrink-0">axeguard@soc:~$</span>
      <input
        ref={inputRef}
        type="text"
        className="flex-1 bg-transparent text-[#00FF41] outline-none placeholder:text-white/10"
        placeholder="Type command..."
        value={cmd}
        onChange={e => setCmd(e.target.value)}
        onKeyDown={handleKeyDown}
      />
      <span className="tui-cursor" />
    </div>
  );
}
