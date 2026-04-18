/**
 * PetroShield AxeGuard - Scalable Mock Data Factory (TypeScript/Node.js)
 * Designed for massive synthetic data injection (10,000+ entities).
 */

import { IXRDevice, IVendorRisk, IMonthlyMetric, RiskLevel, DeviceType, NetworkSegment, MDMStatus } from './petroshield_types';

export class PetroShieldMockFactory {
  
  /**
   * Generates a massive fleet of XR devices.
   */
  public static generateLargeFleet(count: number): IXRDevice[] {
    const fleet: IXRDevice[] = [];
    const deviceTypes: DeviceType[] = ["HoloLens2", "MetaQuest3", "RealWear", "VuzixM400", "NrealAir", "VisionProEE"];
    const segments: NetworkSegment[] = ["OT_Isolated", "IT_Corporate", "Vendor_VPN"];
    const zones = ["FPSO_P93", "FPSO_P68", "Refinaria_REPLAN", "Base_Camacari", "Unidade_Amazonas"];

    for (let i = 0; i < count; i++) {
      const id = `xr-fleet-${i.toString().padStart(5, '0')}`;
      fleet.push({
        device_id: id,
        device_type: deviceTypes[Math.floor(Math.random() * deviceTypes.length)],
        asset_tag: `PETRO-XR-2047-${i}`,
        assigned_operator_id: `OP-${Math.floor(Math.random() * 90000) + 10000}`,
        assigned_vendor_id: Math.random() > 0.2 ? "OCEANICA_ENG" : null,
        mdm_enrollment_status: Math.random() > 0.05 ? "enrolled" : "compromised",
        kiosk_mode_enabled: true,
        facility_zone: zones[Math.floor(Math.random() * zones.length)],
        network_segment: segments[Math.floor(Math.random() * segments.length)],
        encryption_status: "AES-256",
        remote_wipe_capable: true,
        geofence_locked: Math.random() > 0.5,
        firmware_version: "25.0.0",
        last_seen: new Date().toISOString()
      });
    }
    return fleet;
  }

  /**
   * Generates extended historical metrics for multi-year trend analysis.
   */
  public static generateHistoricalMetrics(months: number): IMonthlyMetric[] {
    const metrics: IMonthlyMetric[] = [];
    const startDate = new Date();
    startDate.setMonth(startDate.getMonth() - months);

    for (let i = 0; i < months; i++) {
      const current = new Date(startDate);
      current.setMonth(current.getMonth() + i);
      
      metrics.push({
        month: current.toISOString().substring(0, 7),
        queries_processed: Math.floor(Math.random() * 80000) + 40000,
        leaks_prevented: Math.floor(Math.random() * 1000) + 500,
        incidents_blocked: Math.floor(Math.random() * 200) + 100,
        incidents_escalated: Math.floor(Math.random() * 50) + 20,
        avg_latency_ms: Math.floor(Math.random() * 15) + 10,
        cost_avoided_brl: Math.floor(Math.random() * 30000000) + 10000000,
        biometric_reauths: Math.floor(Math.random() * 5000) + 2000,
        shadow_it_blocks: Math.floor(Math.random() * 50) + 10,
        compliance_deadlines_met: 20 + Math.floor(Math.random() * 10)
      });
    }
    return metrics;
  }

  /**
   * Simulates a live event stream emitter for the Theatre Engine.
   */
  public static *liveEventGenerator(intervalMs: number) {
    let index = 0;
    while (true) {
      yield {
        log_id: index++,
        agent: "AGENT_SUPERVISOR",
        type: "PHASE",
        content: `Analyzing high-risk query from node-delta-${index}`,
        timestamp: new Date().toISOString()
      };
    }
  }
}
