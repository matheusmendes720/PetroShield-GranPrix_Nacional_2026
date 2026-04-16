/**
 * Aba de Operações — Lista de dispositivos XR e sessões ativas.
 */
import React, { useMemo } from "react";
import { Box, Text } from "ink";
import { XR_DEVICES, AUTH_SESSIONS, COLORS } from "../mocks/data.js";
import { expandDataset, generateXRDevices, generateAuthSessions } from "../mocks/generators.js";

interface Props {
  tick: number;
}

export default function Operations({ tick }: Props) {
  const devices = useMemo(() => expandDataset(XR_DEVICES, generateXRDevices, 6), []);
  const sessions = useMemo(() => expandDataset(AUTH_SESSIONS, generateAuthSessions, 6), []);

  return (
    <Box flexDirection="row" flexGrow={1}>
      <Box flexDirection="column" width="50%" borderStyle="single" borderColor={COLORS.cyan} paddingX={1}>
        <Text bold underline color={COLORS.fireOrange}>Dispositivos XR</Text>
        {devices.map((d) => (
          <Box key={d.device_id} flexDirection="row" gap={2}>
            <Text color={d.mdm_enrollment_status === "compromised" ? COLORS.alertRed : COLORS.neonGreen}>
              {d.mdm_enrollment_status}
            </Text>
            <Text wrap="truncate-middle">{d.device_id}</Text>
            <Text dimColor>{d.facility_zone}</Text>
          </Box>
        ))}
      </Box>

      <Box flexDirection="column" width="50%" borderStyle="single" borderColor={COLORS.neonGreen} paddingX={1}>
        <Text bold underline color={COLORS.fireOrange}>Sessões de Autenticação</Text>
        {sessions.map((s) => (
          <Box key={s.session_id} flexDirection="row" gap={2}>
            <Text color={s.risk_score > 70 ? COLORS.alertRed : s.risk_score > 40 ? COLORS.fireOrange : COLORS.neonGreen}>
              {s.risk_score}
            </Text>
            <Text wrap="truncate-middle">{s.session_id}</Text>
            <Text dimColor>{s.auth_method}</Text>
          </Box>
        ))}
        <Box marginTop={1}>
          <Text dimColor>tick={tick}</Text>
        </Box>
      </Box>
    </Box>
  );
}
