import React from 'react';

const TopBanner: React.FC = () => {
  return (
    <header className="top-banner" style={{
      width: '90%',
      maxWidth: '1200px',
      height: '180px',
      marginTop: '40px',
      position: 'relative',
      background: '#121212', // Base metal escuro
      borderLeft: '4px solid #333',
      borderRight: '4px solid #333',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      boxShadow: '0 20px 50px rgba(0,0,0,0.8)',
      overflow: 'visible' // Para as chamas saírem da borda
    }}>
      {/* Camada de Textura PCB (Placeholder via CSS) */}
      <div className="pcb-texture" style={{
        position: 'absolute',
        inset: 0,
        opacity: 0.2,
        backgroundImage: `linear-gradient(90deg, transparent 95%, rgba(0,255,65,0.1) 95%),
                          linear-gradient(rgba(0,255,65,0.1) 5%, transparent 5%)`,
        backgroundSize: '20px 20px',
        pointerEvents: 'none'
      }} />

      {/* Bordas de Fogo (Animação de brilho Laranja) */}
      <div className="fire-border top" style={{
        position: 'absolute',
        top: '-10px',
        left: '0',
        right: '0',
        height: '20px',
        background: 'linear-gradient(to bottom, transparent, #FF6200, #FFD000)',
        filter: 'blur(8px)',
        opacity: 0.8,
        animation: 'pulse-fire 2s infinite alternate'
      }} />
      <div className="fire-border bottom" style={{
        position: 'absolute',
        bottom: '-10px',
        left: '0',
        right: '0',
        height: '20px',
        background: 'linear-gradient(to top, transparent, #FF6200, #FFD000)',
        filter: 'blur(8px)',
        opacity: 0.8,
        animation: 'pulse-fire 2s infinite alternate'
      }} />

      {/* Flag Esquerda (BR) */}
      <div className="tag-left" style={{
        position: 'absolute',
        left: '20px',
        top: '20px',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: '5px'
      }}>
        <div className="br-flag" style={{
          width: '50px',
          height: '30px',
          background: '#009739',
          border: '2px solid #fff',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontSize: '12px',
          fontWeight: 'bold',
          color: '#fff',
          fontFamily: 'monospace'
        }}>BR</div>
        <div className="status-icon" style={{
          width: '24px',
          height: '24px',
          borderRadius: '50%',
          border: '2px solid #555',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontSize: '14px',
          color: '#555'
        }}>⊘</div>
      </div>

      {/* Logotipo Central */}
      <div className="logo-container" style={{ textAlign: 'center', position: 'relative' }}>
        <h1 className="logo-text" style={{
          fontSize: '5rem',
          margin: 0,
          fontFamily: 'var(--font-ui)',
          fontWeight: 900,
          letterSpacing: '-2px',
          color: '#121212',
          WebkitTextStroke: '2px var(--neon-green)',
          textShadow: '0 0 20px var(--neon-green-glow)',
          position: 'relative',
          zIndex: 2
        }}>
          Petro<span style={{ color: 'var(--neon-green)' }}>Shield</span>
        </h1>
        {/* Glow de Brasa interno (Laranja) */}
        <div className="logo-ember" style={{
          position: 'absolute',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          width: '100%',
          height: '40px',
          background: 'rgba(255, 98, 0, 0.4)',
          filter: 'blur(30px)',
          zIndex: 1
        }} />
      </div>

      {/* Ícone Direita (GitHub) */}
      <div className="tag-right" style={{
        position: 'absolute',
        right: '40px',
        top: '20px'
      }}>
        <svg height="32" viewBox="0 0 16 16" width="32" style={{ fill: '#fff', opacity: 0.8 }}>
          <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
        </svg>
      </div>

      <style>{`
        @keyframes pulse-fire {
          from { opacity: 0.6; filter: blur(8px) scaleY(1); }
          to { opacity: 1; filter: blur(12px) scaleY(1.2); }
        }
      `}</style>
    </header>
  );
};

export default TopBanner;
