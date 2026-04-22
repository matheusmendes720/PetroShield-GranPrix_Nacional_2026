import React from 'react';
import { motion, useMotionValue, useSpring, useTransform, useMotionTemplate } from 'framer-motion';

interface ShieldCardProps {
  imagePath: string;
  glowColor: string;
  effectType: 'fire' | 'neon' | 'electric';
  label: string;
}

const ShieldCard: React.FC<ShieldCardProps> = ({ imagePath, glowColor, effectType }) => {
  // Gyro-tracking logic (Normalized mouse position -0.5 to 0.5)
  const x = useMotionValue(0);
  const y = useMotionValue(0);

  // Smooth springs for realistic inertia, tuned for higher responsiveness but retaining weight
  const mouseXSpring = useSpring(x, { stiffness: 180, damping: 20, mass: 1.2 });
  const mouseYSpring = useSpring(y, { stiffness: 180, damping: 20, mass: 1.2 });

  // Tilt mapping (Enhanced to ±18° X, ±25° Y for deeper 3D depth)
  const rotateX = useTransform(mouseYSpring, [-0.5, 0.5], ["18deg", "-18deg"]);
  const rotateY = useTransform(mouseXSpring, [-0.5, 0.5], ["-25deg", "25deg"]);

  // Fresnel Glare mapping (moves inversely to tilt for realistic light reflection)
  const glareX = useTransform(mouseXSpring, [-0.5, 0.5], [100, 0]);
  const glareY = useTransform(mouseYSpring, [-0.5, 0.5], [100, 0]);
  const glareBackground = useMotionTemplate`radial-gradient(circle at ${glareX}% ${glareY}%, rgba(255, 255, 255, 0.25) 0%, rgba(255, 255, 255, 0) 50%)`;

  // Dynamic Shadow Parallax (Increased to ±40px to match the higher tilt)
  const shadowX = useTransform(mouseXSpring, [-0.5, 0.5], [-40, 40]);
  const shadowY = useTransform(mouseYSpring, [-0.5, 0.5], [-40, 40]);

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    const rect = e.currentTarget.getBoundingClientRect();
    const width = rect.width;
    const height = rect.height;
    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;
    x.set(mouseX / width - 0.5);
    y.set(mouseY / height - 0.5);
  };

  const handleMouseLeave = () => {
    x.set(0);
    y.set(0);
  };

  return (
    <motion.div
      className="shield-card-container"
      onMouseMove={handleMouseMove}
      onMouseLeave={handleMouseLeave}
      initial={{ opacity: 0.8, scale: 1, y: 0 }}
      animate={{ y: [0, -8, 0] }}
      transition={{ 
        y: { duration: 4, repeat: Infinity, ease: "easeInOut" }
      }}
      whileHover={{ 
        opacity: 1, 
        scale: 1.08, 
        z: 60, // Pushed Z out slightly further for more pop
        y: -15, // Lift up when hovered, overriding the infinite animation
        transition: { type: "spring", mass: 1.2, stiffness: 180, damping: 20 }
      }}
      style={{
        width: '320px',
        height: '560px',
        position: 'relative',
        cursor: 'pointer',
        transformStyle: 'preserve-3d',
        perspective: '2000px',
        rotateX,
        rotateY,
      }}
    >
      {/* Sombras Dinâmicas */}
      <motion.div className="dynamic-shadow" style={{
        position: 'absolute',
        bottom: '-20px',
        left: '10%',
        width: '80%',
        height: '40px',
        background: 'rgba(0,0,0,0.6)',
        filter: 'blur(15px)',
        borderRadius: '50%',
        zIndex: -1,
        x: shadowX,
        y: shadowY,
        transition: 'background 0.4s ease, filter 0.4s ease'
      }} />

      {/* L3: Aura Neon / Fogo / Elétrico no Contorno */}
      <motion.div
        className="glow-aura"
        whileHover={{
          boxShadow: `0 0 80px 15px ${glowColor}`,
          opacity: 1,
        }}
        style={{
          position: 'absolute',
          inset: '0',
          borderRadius: '20px',
          opacity: 0,
          transition: 'all 0.5s ease',
          pointerEvents: 'none',
          zIndex: 0,
        }}
      />

      {/* O Escudo Real */}
      <div className="shield-frame" style={{
        width: '100%',
        height: '100%',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        position: 'relative',
        zIndex: 2,
        overflow: 'hidden', // Contain the glare and VFX inside the card
        borderRadius: '20px',
        background: 'rgba(10, 10, 10, 0.8)',
        border: '1px solid rgba(255, 255, 255, 0.05)',
        boxShadow: 'inset 0 0 20px rgba(0,0,0,0.8)'
      }}>
        
        {/* L3: Fresnel Glare Overlay */}
        <motion.div
          className="fresnel-glare"
          style={{
            position: 'absolute',
            inset: 0,
            background: glareBackground,
            pointerEvents: 'none',
            zIndex: 10,
            opacity: 0,
            transition: 'opacity 0.6s cubic-bezier(0.4, 0, 0.2, 1)',
            mixBlendMode: 'overlay'
          }}
        />

        <div style={{
          width: '90%',
          height: '90%',
          background: `url(${imagePath})`,
          backgroundSize: 'contain',
          backgroundPosition: 'center',
          backgroundRepeat: 'no-repeat',
          position: 'relative',
          zIndex: 5
        }}>
           {/* Efeitos de Faíscas e Identidade Visual L3 */}
           <VFXMatrix effectType={effectType} color={glowColor} mouseX={mouseXSpring} mouseY={mouseYSpring} />
        </div>
      </div>

      <style>{`
        .shield-card-container {
          transition: filter 0.5s ease;
        }
        .shield-card-container:hover .dynamic-shadow {
          background: rgba(0,0,0,0.2);
          filter: blur(30px);
          transform: scale(1.1) translateY(20px);
        }
        .shield-card-container:hover .fresnel-glare {
          opacity: 1 !important;
        }
        .shield-card-container:hover .vfx-layer {
          opacity: 1 !important;
        }
      `}</style>
    </motion.div>
  );
};

// Módulo 2.2: Matriz VFX Exclusiva
const VFXMatrix: React.FC<{ 
  effectType: 'fire' | 'neon' | 'electric', 
  color: string,
  mouseX: any,
  mouseY: any
}> = ({ effectType, color, mouseX, mouseY }) => {
  return (
    <motion.div className="vfx-layer" style={{ 
      position: 'absolute', inset: 0, pointerEvents: 'none', opacity: 0, transition: 'opacity 0.6s ease' 
    }}>
      {effectType === 'fire' && <FireVFX color={color} mouseX={mouseX} mouseY={mouseY} />}
      {effectType === 'neon' && <NeonVFX color={color} mouseX={mouseX} mouseY={mouseY} />}
      {effectType === 'electric' && <ElectricVFX color={color} mouseX={mouseX} mouseY={mouseY} />}
    </motion.div>
  );
};

const FireVFX: React.FC<{color: string, mouseX: any, mouseY: any}> = ({ color, mouseX, mouseY }) => {
  const driftX = useTransform(mouseX, [-0.5, 0.5], [-30, 30]);
  
  return (
    <>
      {/* Fogo Verde-Neon + Fuligem Ascendente (24 partículas para mais densidade) */}
      {[...Array(24)].map((_, i) => (
        <motion.div
          key={`fire-${i}`}
          animate={{
            y: ['10%', '-140%'],
            x: [0, (Math.random() - 0.5) * 80],
            opacity: [0, 1, 0.5, 0],
            scale: [0.5, 2.5, 0],
          }}
          style={{ x: driftX }}
          transition={{
            duration: 1.2 + Math.random() * 0.8,
            repeat: Infinity,
            delay: Math.random() * 2,
            ease: "easeOut"
          }}
          style={{
            position: 'absolute',
            bottom: '10%',
            left: `${15 + Math.random() * 70}%`,
            width: `${Math.random() * 4 + 2}px`,
            height: `${Math.random() * 4 + 2}px`,
            background: color,
            borderRadius: '50%',
            boxShadow: `0 0 15px ${color}, 0 0 30px ${color}`,
            filter: 'blur(1px)',
            willChange: 'transform'
          }}
        />
      ))}
    </>
  );
};

const NeonVFX: React.FC<{color: string, mouseX: any, mouseY: any}> = ({ color, mouseX, mouseY }) => {
  const skewX = useTransform(mouseX, [-0.5, 0.5], [-10, 10]);
  const skewY = useTransform(mouseY, [-0.5, 0.5], [-10, 10]);

  return (
    <>
      {/* Arcos Ciano + Runas + Glitch de Faíscas */}
      {[...Array(12)].map((_, i) => (
        <motion.div
          key={`neon-${i}`}
          animate={{
            opacity: [0, 1, 0, 0.8, 0],
            scale: [0.5, 1.2, 0.8, 1.5, 0.5],
            x: [(Math.random() - 0.5) * 20, (Math.random() - 0.5) * 20],
            y: [(Math.random() - 0.5) * 20, (Math.random() - 0.5) * 20],
          }}
          style={{ skewX, skewY }}
          transition={{
            duration: 0.15 + Math.random() * 0.2,
            repeat: Infinity,
            repeatDelay: Math.random() * 2,
          }}
          style={{
            position: 'absolute',
            top: `${Math.random() * 90}%`,
            left: `${Math.random() * 90}%`,
            width: `${Math.random() * 50 + 10}px`,
            height: '1px',
            background: color,
            boxShadow: `0 0 15px ${color}, 0 0 5px white`,
            transform: `rotate(${Math.random() * 360}deg)`,
            willChange: 'transform, opacity'
          }}
        />
      ))}
    </>
  );
};

const ElectricVFX: React.FC<{color: string, mouseX: any, mouseY: any}> = ({ color, mouseX, mouseY }) => {
  const pulseScale = useTransform(mouseX, [-0.5, 0.5], [0.8, 1.2]);

  return (
    <>
      {/* Fluxo de Dados + Núcleo Reativo */}
      <motion.div
        animate={{ opacity: [0.6, 1, 0.6], scale: [0.9, 1.1, 0.9] }}
        style={{ scale: pulseScale }}
        transition={{ duration: 1.5, repeat: Infinity, ease: "easeInOut" }}
        style={{
          position: 'absolute',
          top: '35%',
          left: '35%',
          width: '30%',
          height: '30%',
          background: `radial-gradient(circle, ${color} 0%, transparent 80%)`,
          mixBlendMode: 'screen',
          filter: 'blur(10px)'
        }}
      />
      {[...Array(15)].map((_, i) => (
        <motion.div
          key={`elec-${i}`}
          animate={{
            y: i % 2 === 0 ? ['-20%', '120%'] : [0, 0],
            x: i % 2 !== 0 ? ['-20%', '120%'] : [0, 0],
            opacity: [0, 1, 0],
          }}
          transition={{
            duration: 0.8 + Math.random() * 1.2,
            repeat: Infinity,
            delay: Math.random() * 1.5,
            ease: "linear"
          }}
          style={{
            position: 'absolute',
            top: i % 2 !== 0 ? `${Math.random() * 100}%` : '-10%',
            left: i % 2 === 0 ? `${Math.random() * 100}%` : '-10%',
            width: i % 2 === 0 ? '1px' : '60px',
            height: i % 2 !== 0 ? '1px' : '60px',
            background: `linear-gradient(${i % 2 === 0 ? 'to bottom' : 'to right'}, transparent, ${color}, transparent)`,
            boxShadow: `0 0 10px ${color}`,
            willChange: 'transform'
          }}
        />
      ))}
    </>
  );
};

export default ShieldCard;
