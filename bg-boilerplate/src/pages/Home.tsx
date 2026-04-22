import TopBanner from '../components/TopBanner';
import ShieldCard from '../components/ShieldCard';

export default function Home() {
  return (
    <div className="home-content" style={{ 
      position: 'relative', 
      width: '100%', 
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: '60px',
      paddingBottom: '100px',
      overflowX: 'hidden'
    }}>
      <TopBanner />

      {/* Grid de Escudos / Relíquias */}
      <div className="shields-grid" style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        gap: '40px',
        width: '100%',
        maxWidth: '1200px',
        marginTop: '20px',
        flexWrap: 'wrap'
      }}>
        {/* 1 - The Beacon (Tocha / Fogo) */}
        <ShieldCard 
          imagePath="/elements/finc_dash.png"
          glowColor="rgba(255, 98, 0, 0.6)"
          effectType="fire"
          label="The Beacon"
        />

        {/* 2 - The Enforcer (Machados / Neon) */}
        <ShieldCard 
          imagePath="/elements/axe_guard.png"
          glowColor="rgba(0, 255, 255, 0.6)"
          effectType="neon"
          label="The Enforcer"
        />

        {/* 3 - The Vault (Cadeado / Elétrico) */}
        <ShieldCard 
          imagePath="/elements/soc_admin.png"
          glowColor="rgba(0, 255, 65, 0.6)"
          effectType="electric"
          label="The Vault"
        />
      </div>
    </div>
  )
}
