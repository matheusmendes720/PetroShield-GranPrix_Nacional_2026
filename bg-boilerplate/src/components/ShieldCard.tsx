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

  // PREMIUM SPRING CONFIG: Tuned for "Heavy Metal" feel (from MASTER_SPEC)
  // Stiffness lowered for organic sway, Damping increased for elegant settlement
  const springConfig = { stiffness: 120, damping: 25, mass: 1.2 };
  const mouseXSpring = useSpring(x, springConfig);
  const mouseYSpring = useSpring(y, springConfig);

  // 1. TILT MAPPING: Deep 3D rotation
  const rotateX = useTransform(mouseYSpring, [-0.5, 0.5], ["18deg", "-18deg"]);
  const rotateY = useTransform(mouseXSpring, [-0.5, 0.5], ["-25deg", "25deg"]);

  // 2. GYRO-POSITIONING: Horizontal/Vertical sliding for parallax depth
  const translateX = useTransform(mouseXSpring, [-0.5, 0.5], ["-12px", "12px"]);
  const translateY = useTransform(mouseYSpring, [-0.5, 0.5], ["-12px", "12px"]);

  // 3. FRESNEL GLARE: Sharp specular reflection tracking
  const glareX = useTransform(mouseXSpring, [-0.5, 0.5], [100, 0]);
  const glareY = useTransform(mouseYSpring, [-0.5, 0.5], [100, 0]);
  
  // Concentrated radial focus (0% to 40%) for a more "polished glass/metal" look
  const glareBackground = useMotionTemplate`radial-gradient(circle at ${glareX}% ${glareY}%, rgba(255, 255, 255, 0.35) 0%, rgba(255, 255, 255, 0) 40%)`;

  // 4. DYNAMIC SHADOW: Inverse movement for realistic ambient occlusion
  const shadowX = useTransform(mouseXSpring, [-0.5, 0.5], [-45, 45]);
  const shadowY = useTransform(mouseYSpring, [-0.5, 0.5], [-45, 45]);

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    const rect = e.currentTarget.getBoundingClientRect();
    x.set((e.clientX - rect.left) / rect.width - 0.5);
    y.set((e.clientY - rect.top) / rect.height - 0.5);
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
      animate={{ 
        y: [0, -12, 0], // Subtle idle float
      }}
      transition={{ 
        y: { duration: 5, repeat: Infinity, ease: "easeInOut" }
      }}
      whileHover={{ 
        opacity: 1, 
        scale: 1.1, 
        z: 80,
        y: -20, // Lift when active
        transition: { type: "spring", ...springConfig }
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
        x: translateX,
        y: translateY,
      }}
    >
      {/* L0: Deep Environmental Shadow */}
      <motion.div className="dynamic-shadow" style={{
        position: 'absolute',
        bottom: '-30px',
        left: '10%',
        width: '80%',
        height: '50px',
        background: 'rgba(0,0,0,0.7)',
        filter: 'blur(20px)',
        borderRadius: '50%',
        zIndex: -1,
        x: shadowX,
        y: shadowY,
        transition: 'background 0.4s ease, filter 0.4s ease'
      }} />

      {/* L1: Glow Aura */}
      <motion.div
        className="glow-aura"
        whileHover={{
          boxShadow: `0 0 100px 20px ${glowColor}44`,
          opacity: 1,
        }}
        style={{
          position: 'absolute',
          inset: '-5px',
          borderRadius: '25px',
          opacity: 0,
          transition: 'all 0.6s cubic-bezier(0.23, 1, 0.32, 1)',
          pointerEvents: 'none',
          zIndex: 0,
        }}
      />

      {/* L2: The Main Chassis */}
      <div className="shield-frame" style={{
        width: '100%',
        height: '100%',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        position: 'relative',
        zIndex: 2,
        overflow: 'hidden',
        borderRadius: '20px',
        background: 'rgba(8, 8, 8, 0.9)',
        border: '1.5px solid rgba(255, 255, 255, 0.08)',
        boxShadow: 'inset 0 0 40px rgba(0,0,0,0.9)',
        backdropFilter: 'blur(10px)'
      }}>
        
        {/* L3: Specular Fresnel Overlay */}
        <motion.div
          className="fresnel-glare"
          style={{
            position: 'absolute',
            inset: -50, // Slightly larger to cover edges during tilt
            background: glareBackground,
            pointerEvents: 'none',
            zIndex: 10,
            opacity: 0,
            transition: 'opacity 0.8s ease',
            mixBlendMode: 'overlay'
          }}
        />

        {/* L4: Asset Content & VFX Layer */}
        <div style={{
          width: '85%',
          height: '85%',
          background: `url(${imagePath})`,
          backgroundSize: 'contain',
          backgroundPosition: 'center',
          backgroundRepeat: 'no-repeat',
          position: 'relative',
          zIndex: 5,
          filter: 'drop-shadow(0 0 20px rgba(0,0,0,0.5))'
        }}>
           <VFXMatrix effectType={effectType} color={glowColor} mouseX={mouseXSpring} mouseY={mouseYSpring} />
        </div>

        {/* Micro-label for status */}
        <div style={{
          position: 'absolute',
          bottom: '20px',
          left: '50%',
          transform: 'translateX(-50%)',
          fontFamily: "'VT323', monospace",
          fontSize: '12px',
          color: glowColor,
          letterSpacing: '2px',
          opacity: 0.6,
          textTransform: 'uppercase',
          zIndex: 6
        }}>
          Status: Operational
        </div>
      </div>

      <style>{`
        .shield-card-container:hover .dynamic-shadow {
          background: rgba(0,0,0,0.3);
          filter: blur(40px);
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

// V3 REACTIVE VFX MATRIX
const VFXMatrix: React.FC<{ 
  effectType: 'fire' | 'neon' | 'electric', 
  color: string,
  mouseX: any,
  mouseY: any
}> = ({ effectType, color, mouseX, mouseY }) => {
  return (
    <motion.div className="vfx-layer" style={{ 
      position: 'absolute', inset: -20, pointerEvents: 'none', opacity: 0, transition: 'opacity 0.8s ease' 
    }}>
      {effectType === 'fire' && <FireVFX color={color} mouseX={mouseX} mouseY={mouseY} />}
      {effectType === 'neon' && <NeonVFX color={color} mouseX={mouseX} mouseY={mouseY} />}
      {effectType === 'electric' && <ElectricVFX color={color} mouseX={mouseX} mouseY={mouseY} />}
    </motion.div>
  );
};

const FireVFX: React.FC<{color: string, mouseX: any, mouseY: any}> = ({ color, mouseX, mouseY }) => {
  // Lateral wind effect based on mouse velocity/position
  const windX = useTransform(mouseX, [-0.5, 0.5], [-50, 50]);
  
  return (
    <>
      {[...Array(30)].map((_, i) => (
        <motion.div
          key={`fire-${i}`}
          animate={{
            y: ['20%', '-120%'],
            x: [0, (Math.random() - 0.5) * 120],
            opacity: [0, 1, 0.8, 0],
            scale: [0.5, 2.8, 0],
            rotate: [0, Math.random() * 360]
          }}
          style={{ translateX: windX }}
          transition={{
            duration: 1 + Math.random() * 1,
            repeat: Infinity,
            delay: Math.random() * 2,
            ease: "easeOut"
          }}
          style={{
            position: 'absolute',
            bottom: '10%',
            left: `${10 + Math.random() * 80}%`,
            width: `${Math.random() * 5 + 3}px`,
            height: `${Math.random() * 5 + 3}px`,
            background: color,
            borderRadius: '20% 50% 50% 50%', // Slightly "flame" shaped
            boxShadow: `0 0 20px ${color}, 0 0 40px ${color}88`,
            filter: 'blur(1px)',
            willChange: 'transform'
          }}
        />
      ))}
    </>
  );
};

const NeonVFX: React.FC<{color: string, mouseX: any, mouseY: any}> = ({ color, mouseX, mouseY }) => {
  const skewX = useTransform(mouseX, [-0.5, 0.5], [-15, 15]);
  const driftY = useTransform(mouseY, [-0.5, 0.5], [-20, 20]);

  return (
    <>
      {[...Array(16)].map((_, i) => (
        <motion.div
          key={`neon-${i}`}
          animate={{
            opacity: [0, 1, 0, 1, 0],
            scaleX: [1, 1.5, 1, 2, 1],
            x: [(Math.random() - 0.5) * 40, (Math.random() - 0.5) * 40],
          }}
          style={{ skewX, translateY: driftY }}
          transition={{
            duration: 0.2 + Math.random() * 0.3,
            repeat: Infinity,
            repeatDelay: Math.random() * 1.5,
          }}
          style={{
            position: 'absolute',
            top: `${Math.random() * 100}%`,
            left: `${Math.random() * 10}%`,
            width: `${Math.random() * 100 + 50}%`,
            height: '1px',
            background: `linear-gradient(90deg, transparent, ${color}, white, ${color}, transparent)`,
            boxShadow: `0 0 20px ${color}`,
            willChange: 'transform, opacity'
          }}
        />
      ))}
      {/* Particle dust under cursor */}
      {[...Array(8)].map((_, i) => (
        <motion.div
          key={`dust-${i}`}
          animate={{
            scale: [0, 1.5, 0],
            opacity: [0, 1, 0],
          }}
          style={{
            x: useTransform(mouseX, [-0.5, 0.5], [-160, 160]),
            y: useTransform(mouseY, [-0.5, 0.5], [-280, 280]),
          }}
          transition={{ duration: 0.5, repeat: Infinity, delay: i * 0.1 }}
          style={{
            position: 'absolute',
            top: '50%',
            left: '50%',
            width: '4px',
            height: '4px',
            background: 'white',
            borderRadius: '50%',
            boxShadow: `0 0 10px ${color}`,
            zIndex: 11
          }}
        />
      ))}
    </>
  );
};

const ElectricVFX: React.FC<{color: string, mouseX: any, mouseY: any}> = ({ color, mouseX, mouseY }) => {
  const intensity = useTransform(mouseX, [-0.5, 0.5], [0.5, 1.5]);

  return (
    <>
      <motion.div
        animate={{ 
          opacity: [0.4, 1, 0.4], 
          scale: [0.85, 1.15, 0.85],
          filter: ['blur(10px) brightness(1)', 'blur(15px) brightness(1.5)', 'blur(10px) brightness(1)']
        }}
        style={{ opacity: intensity }}
        transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
        style={{
          position: 'absolute',
          top: '30%',
          left: '30%',
          width: '40%',
          height: '40%',
          background: `radial-gradient(circle, ${color} 40%, transparent 80%)`,
          mixBlendMode: 'screen',
        }}
      />
      {[...Array(20)].map((_, i) => (
        <motion.div
          key={`elec-${i}`}
          animate={{
            pathLength: [0, 1],
            opacity: [0, 1, 0],
          }}
          transition={{
            duration: 0.3 + Math.random() * 0.5,
            repeat: Infinity,
            delay: Math.random() * 2,
          }}
          style={{
            position: 'absolute',
            top: `${Math.random() * 100}%`,
            left: `${Math.random() * 100}%`,
            width: '2px',
            height: `${Math.random() * 40 + 20}px`,
            background: `linear-gradient(to bottom, transparent, white, ${color}, transparent)`,
            boxShadow: `0 0 15px ${color}`,
            transform: `rotate(${Math.random() * 360}deg)`,
            willChange: 'transform'
          }}
        />
      ))}
    </>
  );
};

export default ShieldCard;

