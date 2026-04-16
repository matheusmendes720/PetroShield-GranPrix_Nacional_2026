/**
 * App principal Classic TUI usando neo-blessed.
 * Layout cyberpunk retro com painéis de logs, dispositivos e ameaças.
 */
import blessed from "blessed";
import { XR_DEVICES, LOGS, THREATS, COLORS } from "./mocks/data.js";
import { expandDataset, generateLogs, generateDevices } from "./mocks/generators.js";

export function createApp() {
  const screen = blessed.screen({
    smartCSR: true,
    title: "PetroShield Classic — Cyber-Ops TUI",
    mouse: true,
  });

  // Header
  const header = blessed.box({
    top: 0,
    left: 0,
    width: "100%",
    height: 3,
    content: "{center}███ PetroShield Classic — Cyber-Ops TUI ███   Grand Prix SENAI 2026{/center}",
    tags: true,
    style: { fg: COLORS.neonGreen, bg: COLORS.deepVoid, bold: true },
    border: { type: "line" },
  });

  // Logs panel
  const logsPanel = blessed.log({
    label: " System Logs ",
    top: 3,
    left: 0,
    width: "60%",
    height: "60%",
    tags: true,
    scrollable: true,
    alwaysScroll: true,
    border: { type: "line" },
    style: { fg: COLORS.cyan, border: { fg: COLORS.fireOrange } },
  });

  // Threats panel
  const threatsPanel = blessed.list({
    label: " Active Threats ",
    top: 3,
    left: "60%",
    width: "40%",
    height: "60%",
    tags: true,
    scrollable: true,
    border: { type: "line" },
    style: { fg: COLORS.gold, border: { fg: COLORS.alertRed } },
  });

  // Devices panel
  const devicesPanel = blessed.list({
    label: " XR Fleet ",
    top: "63%",
    left: 0,
    width: "100%",
    height: "37%",
    tags: true,
    scrollable: true,
    border: { type: "line" },
    style: { fg: COLORS.neonGreen, border: { fg: COLORS.cyan } },
  });

  // Footer / help bar
  const footer = blessed.box({
    bottom: 0,
    left: 0,
    width: "100%",
    height: 1,
    content: " [Q] Quit  [R] Refresh  [L] Inject Log  [D] Inject Device ",
    style: { fg: "white", bg: "blue" },
    tags: true,
  });

  screen.append(header);
  screen.append(logsPanel);
  screen.append(threatsPanel);
  screen.append(devicesPanel);
  screen.append(footer);

  function renderLogs() {
    logsPanel.setContent("");
    expandDataset(LOGS, generateLogs, 8).forEach((log) => {
      const color = log.level === "CRIT" ? COLORS.alertRed : log.level === "ALERT" ? COLORS.fireOrange : log.level === "WARN" ? COLORS.gold : COLORS.neonGreen;
      logsPanel.log(`{${color}-fg}[${log.level}]{/${color}-fg} ${log.timestamp} {bold}${log.source}{/bold}: ${log.message}`);
    });
  }

  function renderThreats() {
    threatsPanel.setItems(
      THREATS.map((t) => `[${t.severity.toUpperCase()}] ${t.id} — ${t.technique} @ ${t.target}`)
    );
  }

  function renderDevices() {
    devicesPanel.setItems(
      expandDataset(XR_DEVICES, generateDevices, 6).map((d) => {
        const color = d.mdm_enrollment_status === "compromised" ? COLORS.alertRed : COLORS.neonGreen;
        return `{${color}-fg}${d.device_id}{/${color}-fg} | ${d.device_type} | ${d.facility_zone} | ${d.network_segment} | ${d.last_seen}`;
      })
    );
  }

  function refresh() {
    renderLogs();
    renderThreats();
    renderDevices();
    screen.render();
  }

  // Keybindings
  screen.key(["q", "C-c"], () => process.exit(0));
  screen.key(["r"], refresh);
  screen.key(["l"], () => {
    logsPanel.log(`{${COLORS.gold}-fg}[INJECT]{/${COLORS.gold}-fg} Log sintético inserido em runtime`);
    screen.render();
  });
  screen.key(["d"], () => {
    devicesPanel.add(`{cyan-fg}synth-${Date.now()}{/cyan-fg} | HoloLens2 | Base_Camacari | OT_Isolated | -0m`);
    screen.render();
  });

  // Auto-refresh a cada 3s
  setInterval(refresh, 3000);

  refresh();
}
