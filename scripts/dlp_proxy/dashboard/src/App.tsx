import { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route, NavLink, Navigate } from 'react-router-dom';
import CircuitBackground from './components/CircuitBackground';
import CommandCenter from './pages/CommandCenter';
import SOCMetrics from './pages/SOCMetrics';
import FleetIntelligence from './pages/FleetIntelligence';

function Clock() {
  const [time, setTime] = useState(new Date());
  useEffect(() => {
    const timer = setInterval(() => setTime(new Date()), 1000);
    return () => clearInterval(timer);
  }, []);
  return <span className="topbar-clock">{time.toLocaleTimeString('pt-BR')}</span>;
}

function App() {
  return (
    <BrowserRouter>
      <CircuitBackground />
      <div className="app-layout">
        {/* Sidebar */}
        <nav className="sidebar">
          <div className="sidebar-logo">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          </div>

          <div className="sidebar-nav">
            <NavLink to="/command" className={({ isActive }) => `sidebar-link ${isActive ? 'active' : ''}`} title="Command Center">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <polyline points="4 17 10 11 4 5" />
                <line x1="12" y1="19" x2="20" y2="19" />
              </svg>
            </NavLink>

            <NavLink to="/metrics" className={({ isActive }) => `sidebar-link ${isActive ? 'active' : ''}`} title="SOC Metrics">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <line x1="18" y1="20" x2="18" y2="10" />
                <line x1="12" y1="20" x2="12" y2="4" />
                <line x1="6" y1="20" x2="6" y2="14" />
              </svg>
            </NavLink>

            <NavLink to="/fleet" className={({ isActive }) => `sidebar-link ${isActive ? 'active' : ''}`} title="Fleet Intelligence">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <rect x="4" y="4" width="16" height="16" rx="2" ry="2" />
                <rect x="9" y="9" width="6" height="6" />
                <line x1="9" y1="1" x2="9" y2="4" />
                <line x1="15" y1="1" x2="15" y2="4" />
                <line x1="9" y1="20" x2="9" y2="23" />
                <line x1="15" y1="20" x2="15" y2="23" />
                <line x1="20" y1="9" x2="23" y2="9" />
                <line x1="20" y1="14" x2="23" y2="14" />
                <line x1="1" y1="9" x2="4" y2="9" />
                <line x1="1" y1="14" x2="4" y2="14" />
              </svg>
            </NavLink>
          </div>

          <div className="sidebar-footer">
            <div className="sidebar-status" title="System Online" />
          </div>
        </nav>

        {/* Main Content */}
        <main className="app-main">
          {/* Top Bar */}
          <header className="topbar">
            <div className="topbar-title">PetroShield AxeGuard SOC</div>
            <div className="topbar-right">
              <div className="topbar-indicator">
                <span className="dot" />
                ONLINE
              </div>
              <Clock />
            </div>
          </header>

          {/* Routes */}
          <Routes>
            <Route path="/command" element={<CommandCenter />} />
            <Route path="/metrics" element={<SOCMetrics />} />
            <Route path="/fleet" element={<FleetIntelligence />} />
            <Route path="*" element={<Navigate to="/command" replace />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;
