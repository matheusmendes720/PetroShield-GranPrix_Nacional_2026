/**
 * AxeGuard Unified State Tree (v4.2 Optimization)
 * Centraliza o estado do sistema, efeitos de UI e contadores financeiros.
 */

export interface SOCState {
    global_roi_saved: number; // Em milhões de reais
    active_threats_count: number;
    system_status: 'STABLE' | 'INVESTIGATING' | 'TRIGGERED' | 'CRITICAL_BLOCK';
    last_block_event?: {
        device: string;
        loss_prevented: number;
        timestamp: string;
    };
    fleet_health: Record<string, number>; // node name -> health %
}

export const INITIAL_STATE: SOCState = {
    global_roi_saved: 45.2, // Valor base inicial do pitch
    active_threats_count: 0,
    system_status: 'STABLE',
    fleet_health: {
        'Camaçari-01': 100,
        'Camaçari-02': 100,
        'Feira-01': 100,
        'Poço-Tupi-10': 94,
        'RLAM-Refinaria': 100
    }
};

/**
 * Reducer-like logic for state transitions based on DPI events.
 */
export function processThreatEvent(state: SOCState, event: any): SOCState {
    const newState = { ...state };
    
    // Simulação de impacto financeiro (Expensive Threats)
    if (event.level === 'CRITICAL') {
        const savings = Math.random() * 5 + 1; // R$ 1M a 6M salvos por prevenção crítica
        newState.global_roi_saved += savings;
        newState.active_threats_count += 1;
        newState.system_status = 'CRITICAL_BLOCK';
        newState.last_block_event = {
            device: event.node,
            loss_prevented: savings,
            timestamp: new Date().toISOString()
        };
        newState.fleet_health[event.node] = Math.max(0, (newState.fleet_health[event.node] || 100) - 15);
    } else if (event.level === 'WARN') {
        newState.system_status = 'INVESTIGATING';
    } else {
        newState.system_status = 'STABLE';
    }

    return newState;
}

/**
 * Mapping of state to UI colors (PetroShield Semantic Tokens)
 */
export function getSystemColor(status: SOCState['system_status']): string {
    const palette = {
        'STABLE': '#00FF41',           // Neon Matrix Green
        'INVESTIGATING': '#0A0A0A',    // Deep Void Black (Border glow only)
        'TRIGGERED': '#FF6200',        // Fire Petroleum Orange
        'CRITICAL_BLOCK': '#FF003C'    // Warning Red Pulsing
    };
    return palette[status];
}
