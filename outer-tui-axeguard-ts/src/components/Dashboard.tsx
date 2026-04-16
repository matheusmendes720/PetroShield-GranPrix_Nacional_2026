/**
 * Dashboard com métricas em tempo real (mock).
 */
import React, { useMemo } from "react";
import { Box, Text } from "ink";
import { XR_DEVICES, AUTH_SESSIONS, INCIDENTS, MONTHLY_METRICS, COLORS } from "../mocks/data.js";
import { expandDataset, generateIncidents, generateAuthSessions } from "../mocks/generators.js";

interface Props {
  tick: number;
}

export default function Dashboard({ tick }: Props) {
  const liveIncidents = useMemo(() => expandDataset(INCIDENTS, generateIncidents, 5), []);
  const liveSessions = useMemo(() => expandDataset(AUTH_SESSIONS, generateAuthSessions, 5), []);
  const latestMetric = MONTHLY_METRICS[MONTHLY_METRICS.length - 1];
  const compromised = XR_DEVICES.filter((d) => d.mdm_enrollment_status === "compromised").length;
  const openCritical = liveIncidents.filter((i) => i.status === "open" && i.severity === "critical").length;

  return (
    <Box flexDirection="row" flexGrow={1}>
      {/* Painel esquerdo: Métricas */}
      <Box flexDirection="column" width="50%" borderStyle="single" borderColor={COLORS.cyan} paddingX={1}>
        <Text bold underline color={COLORS.fireOrange}>
          Métricas Mensais ({latestMetric.month})
        </Text>
        <Text>Dispositivos monitorados: <Text color={COLORS.neonGreen}>{latestMetric.devices_monitored}</Text></Text>
        <Text>Ameaças bloqueadas: <Text color={COLORS.neonGreen}>{latestMetric.threats_blocked}</Text></Text>
        <Text>Incidentes fechados: <Text color={COLORS.neonGreen}>{latestMetric.incidents_closed}</Text></Text>
        <Text>MTTR (horas): <Text color={COLORS.neonGreen}>{latestMetric.mttr_hours}h</Text></Text>
        <Text>Compliance: <Text color={COLORS.gold}>{latestMetric.compliance_score}%</Text></Text>

        <Box marginTop={1}>
          <Text bold underline color={COLORS.fireOrange}>Frota XR</Text>
        </Box>
        <Text>Total: {XR_DEVICES.length} | Comprometidos: <Text color={COLORS.alertRed}>{compromised}</Text></Text>
        <Text>Open Critical Incidents: <Text color={COLORS.alertRed}>{openCritical}</Text></Text>
        <Text>Sessões ativas: {liveSessions.length}</Text>
      </Box>

      {/* Painel direito: Incidentes Recentes */}
      <Box flexDirection="column" width="50%" borderStyle="single" borderColor={COLORS.neonGreen} paddingX={1}>
        <Text bold underline color={COLORS.fireOrange}>Incidentes Recentes (live)</Text>
        {liveIncidents.slice(0, 8).map((inc) => (
          <Box key={inc.incident_id} flexDirection="row" gap={2}>
            <Text color={inc.severity === "critical" ? COLORS.alertRed : inc.severity === "high" ? COLORS.fireOrange : COLORS.cyan}>
              [{inc.severity.toUpperCase()}]
            </Text>
            <Text wrap="truncate-end">{inc.incident_id}</Text>
            <Text dimColor>{inc.status}</Text>
          </Box>
        ))}
        <Box marginTop={1}>
          <Text dimColor>Atualizado a cada segundo • tick={tick}</Text>
        </Box>
      </Box>
    </Box>
  );
}
