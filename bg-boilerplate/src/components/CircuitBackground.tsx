import { useEffect, useRef, useCallback } from 'react'

/* ============================================================================
   CircuitBackground v3.1 — The Digital Void (Deep Glow)
   Features:
   • Electric Glowing Circuits: Multi-layered neon bloom effect
   • Deep 3D Parallax: 150+ nodes with expanded depth range (0.1 to 2.0)
   • Chromatic Aberration: Color splitting on movement
   • Hexagonal Neural Grid & Glitch Distortions
   ============================================================================ */

/* ─── Types ──────────────────────────────────────────────────────────────── */
interface Vec2 {
  x: number
  y: number
}

interface Node {
  x: number
  y: number
  ox: number
  oy: number
  vx: number
  vy: number
  r: number
  depth: number
  pulse: number
  pulseSpeed: number
  baseR: number
}

interface Particle {
  x: number
  y: number
  vx: number
  vy: number
  life: number
  maxLife: number
  size: number
  hue: number
}

interface TrailPoint {
  x: number
  y: number
  life: number
  maxLife: number
  size: number
  velocity: number
}

interface Ripple {
  x: number
  y: number
  radius: number
  maxRadius: number
  strength: number
  life: number
  maxLife: number
}

/* ─── Constants ──────────────────────────────────────────────────────────── */
const NODE_COUNT = 150
const PARTICLE_COUNT = 120
const TRAIL_LENGTH = 15
const IDLE_THRESHOLD_MS = 3000
const LERP_FACTOR = 0.08
const PROXIMITY_RADIUS = 220
const MAGNETIC_RADIUS = 140
const GLITCH_CHANCE = 0.002

/* ─── Utilities ──────────────────────────────────────────────────────────── */
function lerp(a: number, b: number, t: number) {
  return a + (b - a) * t
}

function clamp(v: number, min: number, max: number) {
  return Math.max(min, Math.min(max, v))
}

function dist(a: Vec2, b: Vec2) {
  const dx = a.x - b.x
  const dy = a.y - b.y
  return Math.sqrt(dx * dx + dy * dy)
}

/* ─── Component ──────────────────────────────────────────────────────────── */
export default function CircuitBackground() {
  const canvasRef = useRef<HTMLCanvasElement>(null)

  const dimsRef = useRef({
    w: window.innerWidth,
    h: window.innerHeight,
    dpr: Math.min(window.devicePixelRatio || 1, 2),
  })

  const mouseRef = useRef({
    x: 0.5,
    y: 0.5,
    sx: 0.5,
    sy: 0.5,
    vx: 0,
    vy: 0,
    lastMove: performance.now(),
    velocity: 0,
  })

  const idleRef = useRef({ breathing: false, phase: 0 })
  const ripplesRef = useRef<Ripple[]>([])
  const trailRef = useRef<TrailPoint[]>([])
  const resizeRef = useRef(false)

  const handleResize = useCallback(() => {
    dimsRef.current = {
      w: window.innerWidth,
      h: window.innerHeight,
      dpr: Math.min(window.devicePixelRatio || 1, 2),
    }
    resizeRef.current = true
  }, [])

  useEffect(() => {
    window.addEventListener('resize', handleResize)
    return () => window.removeEventListener('resize', handleResize)
  }, [handleResize])

  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return
    const ctx = canvas.getContext('2d')
    if (!ctx) return

    let w = dimsRef.current.w
    let h = dimsRef.current.h
    const dpr = dimsRef.current.dpr

    function setupCanvas() {
      canvas!.width = w * dpr
      canvas!.height = h * dpr
      ctx!.setTransform(dpr, 0, 0, dpr, 0, 0)
    }
    setupCanvas()

    // ── Initialize Nodes ──
    const nodes: Node[] = Array.from({ length: NODE_COUNT }, () => {
      const x = Math.random() * w
      const y = Math.random() * h
      return {
        x, y,
        ox: x, oy: y,
        vx: (Math.random() - 0.5) * 0.25,
        vy: (Math.random() - 0.5) * 0.25,
        r: 1.5 + Math.random() * 2,
        depth: 0.1 + Math.random() * 1.9, // Deep to foreground (0.1 to 2.0)
        pulse: Math.random() * Math.PI * 2,
        pulseSpeed: 0.015 + Math.random() * 0.02,
        baseR: 1.5 + Math.random() * 2,
      }
    })

    // ── Initialize Particles ──
    const particles: Particle[] = Array.from({ length: PARTICLE_COUNT }, () => ({
      x: Math.random() * w,
      y: Math.random() * h,
      vx: (Math.random() - 0.5) * 0.4,
      vy: -0.15 - Math.random() * 0.6,
      life: Math.random(),
      maxLife: 0.6 + Math.random() * 0.6,
      size: 0.4 + Math.random() * 1.8,
      hue: Math.random() > 0.8 ? 25 : Math.random() > 0.7 ? 180 : 135,
    }))

    // ── Hex Grid Cache ──
    const hexCanvas = document.createElement('canvas')
    let hexCtx = hexCanvas.getContext('2d')
    function rebuildHexGrid() {
      hexCanvas.width = w * dpr
      hexCanvas.height = h * dpr
      hexCtx = hexCanvas.getContext('2d')
      if (!hexCtx) return
      hexCtx.setTransform(dpr, 0, 0, dpr, 0, 0)
      hexCtx.strokeStyle = 'rgba(0, 255, 65, 0.02)'
      hexCtx.lineWidth = 0.5
      const r = 40
      const hexW = r * Math.sqrt(3)
      const hexH = r * 1.5
      for (let y = 0; y < h + r; y += hexH) {
        for (let x = 0; x < w + hexW; x += hexW) {
          const cx = (y / hexH) % 2 === 0 ? x : x + hexW / 2
          hexCtx.beginPath()
          for (let i = 0; i < 6; i++) {
            const angle = (Math.PI / 3) * i + Math.PI / 6
            const px = cx + r * Math.cos(angle)
            const py = y + r * Math.sin(angle)
            if (i === 0) hexCtx.moveTo(px, py)
            else hexCtx.lineTo(px, py)
          }
          hexCtx.closePath()
          hexCtx.stroke()
        }
      }
    }
    rebuildHexGrid()

    // ── Matrix drops ──
    let cols = Math.floor(w / 20)
    let drops = Array.from({ length: cols }, () => Math.random() * h)
    const chars = '0123456789ABCDEFァアカサタナ'

    const onMouseMove = (e: MouseEvent) => {
      const now = performance.now()
      const m = mouseRef.current
      const prevX = m.x * w
      const prevY = m.y * h
      m.x = e.clientX / w
      m.y = e.clientY / h
      m.vx = e.clientX - prevX
      m.vy = e.clientY - prevY
      m.velocity = Math.sqrt(m.vx * m.vx + m.vy * m.vy)
      m.lastMove = now
      idleRef.current.breathing = false

      if (m.velocity > 10) {
        trailRef.current.push({
          x: e.clientX,
          y: e.clientY,
          life: 1.0,
          maxLife: 1.0,
          size: clamp(m.velocity * 0.1, 2, 6),
          velocity: m.velocity,
        })
        if (trailRef.current.length > TRAIL_LENGTH) trailRef.current.shift()
      }
    }

    const onClick = (e: MouseEvent) => {
      ripplesRef.current.push({
        x: e.clientX,
        y: e.clientY,
        radius: 0,
        maxRadius: 400,
        strength: 1.2,
        life: 1,
        maxLife: 1,
      })
    }

    window.addEventListener('mousemove', onMouseMove)
    window.addEventListener('click', onClick)

    let animId: number
    let frame = 0

    function draw(timestamp: number) {
      if (resizeRef.current) {
        resizeRef.current = false
        w = dimsRef.current.w; h = dimsRef.current.h
        setupCanvas(); rebuildHexGrid()
        cols = Math.floor(w / 20)
        drops = Array.from({ length: cols }, () => Math.random() * h)
      }

      const m = mouseRef.current
      m.sx = lerp(m.sx, m.x, LERP_FACTOR)
      m.sy = lerp(m.sy, m.y, LERP_FACTOR)
      
      const timeSinceMove = timestamp - m.lastMove
      if (timeSinceMove > IDLE_THRESHOLD_MS) {
        idleRef.current.breathing = true
        idleRef.current.phase += 0.01
      }
      
      const mx = m.sx * w; const my = m.sy * h
      frame++

      // ── Core Rendering Logic ──
      function renderScene(offsetX = 0, colorFilter?: string) {
        ctx!.save()
        if (colorFilter) {
          ctx!.globalCompositeOperation = 'screen'
          ctx!.translate(offsetX, 0)
        }

        // Layer: BG Void
        if (!colorFilter) {
          const grad = ctx!.createRadialGradient(mx, my, 0, w / 2, h / 2, Math.max(w, h))
          grad.addColorStop(0, 'rgba(0, 30, 15, 0.25)')
          grad.addColorStop(1, '#050505')
          ctx!.fillStyle = grad
          ctx!.fillRect(0, 0, w, h)
        }

        // Layer: Hex Grid (parallax 10x)
        ctx!.globalAlpha = colorFilter ? 0.3 : 0.6
        ctx!.drawImage(hexCanvas, (m.sx - 0.5) * -10, (m.sy - 0.5) * -8, w, h)
        ctx!.globalAlpha = 1

        // Layer: Circuit Nodes & Connections
        const px = (m.sx - 0.5) * 45
        const py = (m.sy - 0.5) * 35
        
        for (let i = 0; i < nodes.length; i++) {
          const n = nodes[i]
          const d = n.depth
          const nx = n.x + px * d
          const ny = n.y + py * d

          n.pulse += n.pulseSpeed * (idleRef.current.breathing ? 0.5 : 1)
          n.x += n.vx; n.y += n.vy
          if (n.x < -40) n.x = w + 40; if (n.x > w + 40) n.x = -40
          if (n.y < -40) n.y = h + 40; if (n.y > h + 40) n.y = -40

          const distM = dist({x: nx, y: ny}, {x: mx, y: my})
          let s = 1, a = 1
          if (distM < PROXIMITY_RADIUS) {
            const t = 1 - distM / PROXIMITY_RADIUS
            s = 1 + t * 2.0; a = 1 + t * 4
            if (distM < MAGNETIC_RADIUS) {
              const str = (1 - distM / MAGNETIC_RADIUS) * 0.03
              n.x += (mx - nx) * str; n.y += (my - ny) * str
            }
          }

          const nodeAlpha = clamp((0.25 + Math.sin(n.pulse) * 0.15) * a, 0, 1)
          ctx!.fillStyle = colorFilter ? colorFilter : (distM < PROXIMITY_RADIUS ? '#00FFFF' : '#00FF41')
          
          // Node Glow
          if (!colorFilter) {
            ctx!.shadowBlur = distM < PROXIMITY_RADIUS ? 15 : 5
            ctx!.shadowColor = distM < PROXIMITY_RADIUS ? '#00FFFF' : '#00FF41'
          }
          
          ctx!.globalAlpha = nodeAlpha
          ctx!.beginPath(); ctx!.arc(nx, ny, n.baseR * s, 0, Math.PI * 2); ctx!.fill()
          ctx!.shadowBlur = 0
          ctx!.globalAlpha = 1

          // Connections
          for (let j = i + 1; j < nodes.length; j += 6) { // Optimized sparsity for higher node count
            const o = nodes[j]
            const ox = o.x + px * o.depth; const oy = o.y + py * o.depth
            const dV = dist({x: nx, y: ny}, {x: ox, y: oy})
            if (dV < 140) {
              const baseConnAlpha = (1 - dV / 140) * 0.08 * a
              
              ctx!.beginPath()
              ctx!.strokeStyle = colorFilter ? colorFilter : (distM < 120 ? '#00FFFF' : '#00FF41')
              
              // Electric Glow Layer
              if (!colorFilter) {
                ctx!.shadowBlur = distM < 120 ? 12 : 4
                ctx!.shadowColor = distM < 120 ? '#00FFFF' : '#00FF41'
              }
              
              ctx!.globalAlpha = clamp(baseConnAlpha, 0, 0.8)
              ctx!.lineWidth = distM < 120 ? 1.5 : 0.6
              ctx!.moveTo(nx, ny)
              
              // Orthogonal Routing (L-shape)
              if (Math.abs(nx - ox) > Math.abs(ny - oy)) {
                ctx!.lineTo(ox, ny); ctx!.lineTo(ox, oy)
              } else {
                ctx!.lineTo(nx, oy); ctx!.lineTo(ox, oy)
              }
              ctx!.stroke()
              ctx!.shadowBlur = 0
            }
          }
        }
        ctx!.restore()
      }

      // ── Apply Chromatic Aberration ──
      // Ativado apenas quando mouseVelocity > 100px/frame. Deslocamento máximo de 6px nos canais R e B.
      const shift = m.velocity > 100 ? clamp((m.velocity - 100) * 0.1, 2, 6) : 0;
      if (shift > 0) {
        ctx!.clearRect(0, 0, w, h)
        renderScene(-shift, 'rgba(255, 0, 0, 0.35)')
        renderScene(shift, 'rgba(0, 255, 255, 0.35)')
        renderScene(0) 
      } else {
        ctx!.clearRect(0, 0, w, h)
        renderScene(0)
      }

      // ── Particles ──
      for (const p of particles) {
        p.x += p.vx; p.y += p.vy
        p.life += 0.005
        if (p.life > p.maxLife || p.y < -10) {
          p.x = Math.random() * w; p.y = h + 10; p.life = 0
        }
        const alpha = Math.min(p.life / 0.1, 1) * Math.max(1 - p.life / p.maxLife, 0)
        ctx!.fillStyle = p.hue === 25 ? `rgba(255, 98, 0, ${alpha * 0.5})` : `rgba(0, 255, 65, ${alpha * 0.5})`
        ctx!.beginPath(); ctx!.arc(p.x + (m.sx-0.5)*20, p.y + (m.sy-0.5)*15, p.size, 0, Math.PI * 2); ctx!.fill()
      }

      // ── Glitch Displacement ──
      // 0.2% chance, lateral shift ±30px
      if (Math.random() < GLITCH_CHANCE && canvas) {
        const gy = Math.random() * h
        const gh = 20 + Math.random() * 80
        const gx = (Math.random() - 0.5) * 60 // ±30px
        ctx!.drawImage(canvas, 0, gy, w, gh, gx, gy, w, gh)
      }

      // ── Matrix Rain ──
      ctx!.font = '12px VT323, monospace'
      ctx!.fillStyle = 'rgba(0, 255, 65, 0.06)'
      for (let i = 0; i < cols; i++) {
        ctx!.fillText(chars[Math.floor(Math.random()*chars.length)], i*20 + (m.sx-0.5)*-12, drops[i] + (m.sy-0.5)*-10)
        if (drops[i] > h && Math.random() > 0.985) drops[i] = 0
        drops[i] += 8
      }

      animId = requestAnimationFrame(draw)
    }

    animId = requestAnimationFrame(draw)
    return () => {
      cancelAnimationFrame(animId)
      window.removeEventListener('mousemove', onMouseMove)
      window.removeEventListener('click', onClick)
    }
  }, [])

  return <canvas ref={canvasRef} style={{ position: 'fixed', top: 0, left: 0, width: '100vw', height: '100vh', zIndex: 0, pointerEvents: 'none', background: '#050505' }} />
}

