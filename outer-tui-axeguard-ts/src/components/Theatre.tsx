/**
 * Aba Theatre — Roteiro de demonstração com cenários mockados.
 */
import React, { useState, useEffect } from "react";
import { Box, Text, useInput } from "ink";
import { DEMO_SCENARIOS, COLORS } from "../mocks/data.js";

const AGENTS = ["supervisor", "dlp_edge", "intel_cloud", "fleet_vaccinator", "clevel_reporter"];

export default function Theatre() {
  const [sceneIndex, setSceneIndex] = useState(0);
  const [step, setStep] = useState(0);
  const [running, setRunning] = useState(false);
  const [logs, setLogs] = useState<string[]>([]);

  const scenario = DEMO_SCENARIOS[sceneIndex];

  useInput((input) => {
    if (input === "r") {
      setRunning(true);
      setStep(0);
      setLogs([`▶ Iniciando ${scenario.scene_id}: ${scenario.scene_title}`]);
    }
    if (input === "n") {
      setRunning(false);
      setStep(0);
      setLogs([]);
      setSceneIndex((i) => (i + 1) % DEMO_SCENARIOS.length);
    }
    if (input === "p") {
      setRunning(false);
      setStep(0);
      setLogs([]);
      setSceneIndex((i) => (i - 1 + DEMO_SCENARIOS.length) % DEMO_SCENARIOS.length);
    }
  });

  useEffect(() => {
    if (!running) return;
    if (step >= AGENTS.length) {
      setLogs((prev) => [...prev, "✓ Cena completa. Pressione [N] para próxima."]);
      setRunning(false);
      return;
    }
    const id = setTimeout(() => {
      const agent = AGENTS[step];
      setLogs((prev) => [...prev, `→ ${agent} processando… OK`]);
      setStep((s) => s + 1);
    }, 600);
    return () => clearTimeout(id);
  }, [running, step]);

  return (
    <Box flexDirection="column" flexGrow={1} borderStyle="single" borderColor={COLORS.fireOrange} paddingX={1}>
      <Text bold underline color={COLORS.cyan}>
        Theatre Engine — {scenario.scene_id}: {scenario.scene_title}
      </Text>
      <Text dimColor>
        Evento: {scenario.event_type} | Device: {scenario.device_id} | IP: {scenario.ip}
      </Text>
      <Text dimColor>Query: “{scenario.query}”</Text>

      <Box marginTop={1} flexDirection="column">
        <Text color={COLORS.neonGreen}>Controles: [R] Rodar cena  [N] Próxima  [P] Anterior</Text>
      </Box>

      <Box marginTop={1} flexDirection="column">
        {logs.map((l, i) => (
          <Text key={i} color={l.startsWith("✓") ? COLORS.gold : l.startsWith("▶") ? COLORS.fireOrange : COLORS.neonGreen}>
            {l}
          </Text>
        ))}
        {running && <Text color={COLORS.cyan}>Executando agente {AGENTS[step]}…</Text>}
      </Box>
    </Box>
  );
}
