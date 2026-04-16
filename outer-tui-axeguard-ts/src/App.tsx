/**
 * App principal do PetroShield AxeGuard TUI.
 * Gerencia estado global e navegação por abas.
 */
import React, { useState, useEffect } from "react";
import { Box, Text, useInput, useApp } from "ink";
import Dashboard from "./components/Dashboard.js";
import Operations from "./components/Operations.js";
import Theatre from "./components/Theatre.js";
import { COLORS } from "./mocks/data.js";

type Tab = "dashboard" | "operations" | "theatre";

export function App() {
  const { exit } = useApp();
  const [tab, setTab] = useState<Tab>("dashboard");
  const [tick, setTick] = useState(0);

  useEffect(() => {
    const id = setInterval(() => setTick((t) => t + 1), 1000);
    return () => clearInterval(id);
  }, []);

  useInput((input, key) => {
    if (key.escape || input === "q") {
      exit();
    }
    if (input === "1") setTab("dashboard");
    if (input === "2") setTab("operations");
    if (input === "3") setTab("theatre");
    if (key.leftArrow) {
      setTab((t) => (t === "dashboard" ? "theatre" : t === "operations" ? "dashboard" : "operations"));
    }
    if (key.rightArrow) {
      setTab((t) => (t === "dashboard" ? "operations" : t === "operations" ? "theatre" : "dashboard"));
    }
  });

  return (
    <Box flexDirection="column" width="100%" height="100%">
      <Box borderStyle="round" borderColor={COLORS.fireOrange} paddingX={1}>
        <Text color={COLORS.neonGreen} bold>
          ███ PetroShield AxeGuard — SOC Agentic v2.5 ███{" "}
        </Text>
        <Text color={COLORS.cyan}>Grand Prix SENAI Nacional 2026</Text>
      </Box>

      <Box paddingX={1}>
        <Text dimColor>[1] Dashboard  [2] Operações  [3] Theatre  [←/→] Navegar  [Q] Sair</Text>
      </Box>

      <Box flexDirection="column" flexGrow={1}>
        {tab === "dashboard" && <Dashboard tick={tick} />}
        {tab === "operations" && <Operations tick={tick} />}
        {tab === "theatre" && <Theatre />}
      </Box>

      <Box paddingX={1} borderStyle="single" borderColor={COLORS.fireOrange}>
        <Text color={COLORS.neonGreen}>Status:</Text>
        <Text> Sistema operacional | Tick: {tick} | Memória: ~12MB | Bun v1.3</Text>
      </Box>
    </Box>
  );
}

export default App;
