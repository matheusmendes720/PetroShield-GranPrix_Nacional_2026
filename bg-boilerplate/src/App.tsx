import { BrowserRouter, Routes, Route, Outlet } from 'react-router-dom'
import CircuitBackground from './components/CircuitBackground'
import Home from './pages/Home'

function AppLayout() {
  return (
    <div className="app-layout">
      {/* L0: Deep Canvas */}
      <CircuitBackground />
      
      {/* L1-L3: Underlay to Overlay VFX */}
      <main className="page-container">
        <Outlet />
      </main>

      {/* L4: Post-Process Scanlines */}
      <div className="scanline-sweep" />
    </div>
  )
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<AppLayout />}>
          <Route index element={<Home />} />
          {/* TODO: adicione novas rotas aqui */}
          <Route path="*" element={<Home />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
