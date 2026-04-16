import { useEffect, useRef, useState, useCallback } from 'react';

/**
 * CircuitBackground — Animated canvas with:
 * 1. Electric circuit traces (neon green)
 * 2. Floating nano particles
 * 3. Matrix rain (subtle)
 * 4. Mouse-driven 3D parallax
 */
export default function CircuitBackground() {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const mouseRef = useRef({ x: 0.5, y: 0.5 });
  const [dims, setDims] = useState({ w: window.innerWidth, h: window.innerHeight });

  const handleResize = useCallback(() => {
    setDims({ w: window.innerWidth, h: window.innerHeight });
  }, []);

  useEffect(() => {
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, [handleResize]);

  useEffect(() => {
    const handleMouse = (e: MouseEvent) => {
      mouseRef.current = { x: e.clientX / dims.w, y: e.clientY / dims.h };
    };
    window.addEventListener('mousemove', handleMouse);
    return () => window.removeEventListener('mousemove', handleMouse);
  }, [dims]);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    canvas.width = dims.w;
    canvas.height = dims.h;

    // ── Circuit Nodes ──
    const nodeCount = 60;
    const nodes = Array.from({ length: nodeCount }, () => ({
      x: Math.random() * dims.w,
      y: Math.random() * dims.h,
      vx: (Math.random() - 0.5) * 0.3,
      vy: (Math.random() - 0.5) * 0.3,
      r: 1 + Math.random() * 2,
      depth: 0.3 + Math.random() * 0.7, // parallax layer
      pulse: Math.random() * Math.PI * 2,
    }));

    // ── Particles (nano banana sparkle) ──
    const particleCount = 80;
    const particles = Array.from({ length: particleCount }, () => ({
      x: Math.random() * dims.w,
      y: Math.random() * dims.h,
      vx: (Math.random() - 0.5) * 0.5,
      vy: -0.2 - Math.random() * 0.8,
      life: Math.random(),
      maxLife: 0.5 + Math.random() * 0.5,
      size: 0.5 + Math.random() * 1.5,
      hue: Math.random() > 0.7 ? 25 : 135, // orange or green
    }));

    // ── Matrix Rain ──
    const cols = Math.floor(dims.w / 18);
    const drops = Array.from({ length: cols }, () => Math.random() * dims.h);
    const chars = 'ァアカサタナハマヤラワ01AXEGUARD';

    let animId: number;
    let frame = 0;

    function draw() {
      ctx!.fillStyle = 'rgba(10, 10, 10, 0.12)';
      ctx!.fillRect(0, 0, dims.w, dims.h);

      const mx = mouseRef.current.x;
      const my = mouseRef.current.y;
      frame++;

      // ── Layer 1: Matrix Rain (deep background) ──
      ctx!.font = '14px VT323, monospace';
      for (let i = 0; i < cols; i++) {
        const char = chars[Math.floor(Math.random() * chars.length)];
        const px = (mx - 0.5) * -8; // subtle parallax
        const py = (my - 0.5) * -5;
        ctx!.fillStyle = `rgba(0, 255, 65, ${0.04 + Math.random() * 0.03})`;
        ctx!.fillText(char, i * 18 + px, drops[i] + py);

        if (drops[i] > dims.h && Math.random() > 0.975) {
          drops[i] = 0;
        }
        drops[i] += 12;
      }

      // ── Layer 2: Circuit Nodes + Connections ──
      for (const node of nodes) {
        // Parallax offset
        const ox = (mx - 0.5) * 30 * node.depth;
        const oy = (my - 0.5) * 20 * node.depth;
        const nx = node.x + ox;
        const ny = node.y + oy;

        node.x += node.vx;
        node.y += node.vy;
        node.pulse += 0.02;

        // Wrap
        if (node.x < 0) node.x = dims.w;
        if (node.x > dims.w) node.x = 0;
        if (node.y < 0) node.y = dims.h;
        if (node.y > dims.h) node.y = 0;

        // Draw node
        const alpha = 0.2 + Math.sin(node.pulse) * 0.15;
        ctx!.beginPath();
        ctx!.arc(nx, ny, node.r, 0, Math.PI * 2);
        ctx!.fillStyle = `rgba(0, 255, 65, ${alpha})`;
        ctx!.fill();

        // Draw connections to nearby nodes
        for (const other of nodes) {
          const ox2 = (mx - 0.5) * 30 * other.depth;
          const oy2 = (my - 0.5) * 20 * other.depth;
          const dx = nx - (other.x + ox2);
          const dy = ny - (other.y + oy2);
          const dist = Math.sqrt(dx * dx + dy * dy);
          if (dist < 120 && dist > 10) {
            ctx!.beginPath();
            ctx!.moveTo(nx, ny);
            // Circuit-style: L-shaped connections
            if (Math.abs(dx) > Math.abs(dy)) {
              ctx!.lineTo(other.x + ox2, ny);
              ctx!.lineTo(other.x + ox2, other.y + oy2);
            } else {
              ctx!.lineTo(nx, other.y + oy2);
              ctx!.lineTo(other.x + ox2, other.y + oy2);
            }
            const lineAlpha = (1 - dist / 120) * 0.08;
            ctx!.strokeStyle = `rgba(0, 255, 65, ${lineAlpha})`;
            ctx!.lineWidth = 0.5;
            ctx!.stroke();
          }
        }
      }

      // ── Layer 3: Floating Particles (nano sparkle) ──
      for (const p of particles) {
        const ox = (mx - 0.5) * 15;
        const oy = (my - 0.5) * 10;

        p.x += p.vx;
        p.y += p.vy;
        p.life += 0.005;

        // Reset
        if (p.life > p.maxLife || p.y < 0) {
          p.x = Math.random() * dims.w;
          p.y = dims.h + 10;
          p.life = 0;
          p.vx = (Math.random() - 0.5) * 0.5;
          p.vy = -0.2 - Math.random() * 0.8;
        }

        const fadeIn = Math.min(p.life / 0.1, 1);
        const fadeOut = Math.max(1 - p.life / p.maxLife, 0);
        const alpha = fadeIn * fadeOut * 0.6;

        ctx!.beginPath();
        ctx!.arc(p.x + ox, p.y + oy, p.size, 0, Math.PI * 2);
        if (p.hue === 25) {
          ctx!.fillStyle = `rgba(255, 98, 0, ${alpha})`;
        } else {
          ctx!.fillStyle = `rgba(0, 255, 65, ${alpha})`;
        }
        ctx!.fill();

        // Glow
        if (alpha > 0.3) {
          ctx!.beginPath();
          ctx!.arc(p.x + ox, p.y + oy, p.size * 3, 0, Math.PI * 2);
          ctx!.fillStyle = p.hue === 25
            ? `rgba(255, 98, 0, ${alpha * 0.1})`
            : `rgba(0, 255, 65, ${alpha * 0.1})`;
          ctx!.fill();
        }
      }

      // ── Scanline effect ──
      if (frame % 300 < 40) {
        const scanY = ((frame % 300) / 40) * dims.h;
        ctx!.fillStyle = 'rgba(0, 255, 65, 0.015)';
        ctx!.fillRect(0, scanY, dims.w, 2);
      }

      animId = requestAnimationFrame(draw);
    }

    draw();
    return () => cancelAnimationFrame(animId);
  }, [dims]);

  return (
    <canvas
      ref={canvasRef}
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        width: '100vw',
        height: '100vh',
        zIndex: 0,
        pointerEvents: 'none',
      }}
    />
  );
}
