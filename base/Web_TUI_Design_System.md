# Web TUI Design System: PetroShield Aesthetic & UI Behavior

> [!NOTE]
> Este documento define as especificações estritas de UI/UX para a camada TUI baseada em Web do AxeGuard. Todo o design é guiado pelos princípios da identidade visual ciber-ofensiva (**Cyber-Sec_Ops-GranPrix_Nacional_2026**).

## 1. PetroShield Color Palette (Semantic Design Tokens)

Os componentes da interface devem ignorar temas genéricos. O padrão é rígido e segue a paleta *Deep Cyberpunk / Tactical SOC*:

*   **`--void-black`** (`#050505` a `#0A0A0A`): Fundo primário. Representa o silêncio da rede sob análise invisível.
*   **`--neon-matrix-green`** (`#00FF41`): Texto padrão de logs, bordas de status ativo e contornos de "Safe Traffic". Designa as operações normais do Swarm.
*   **`--fire-petroleum-orange`** (`#FF6200`): Usada EXCLUSIVAMENTE para a triagem de ameaças caras ("tricky expensive threats"). Indica que o *Agent_Supervisor* engajou numa negociação de Firewall ou identificou "Vendor Risk Cascade".
*   **`--warning-red-pulsing`** (`#FF003C`): Ação de severidade máxima. Utilizado durante o bloqueio definitivo de exfiltração via *Deep Packet Inspection* (Ex: bloqueio de GPS data de um wearable na plataforma P-74). Requer animação de pulso CSS.
*   **`--cyber-gray`** (`#1A1A1A`): Divisores de painel (Panels) e Backgrounds de tabelas secundárias.

## 2. Dynamic Charts & Stateful Widgets

O objetivo da UI é "mostrar a grana sendo salva" e os pacotes sendo estraçalhados para análises de segurança.

### A. The "Million Dollar Savings" ROI Counter
*   **Comportamento:** Um contador de números grande em fonte Mono (*VT323* ou *Courier New Bold*) posicionado no topo do C-Level Dashboard.
*   **Animação:** Quando um pacote perigoso é bloqueado no Edge, uma interpolação suave (Ticker effect) eleva o valor do ROI.
*   **Estilo:** Brilho sutil (Text-shadow green).
*   **Fórmula Conceptual:** Baseia-se no dataset `AGENTIC_WORKFLOWS`: `(Downtime Previsto em Horas * Custo da Operação Offshore)`.

### B. DPI Network Packet Matrix
*   **Componente:** Um Grid `Canvas` ou `SVG` super denso simulando bits de comunicação TCP/UDP.
*   **Estado:**
    *   Pacotes `HTTPS/443` limpos: Quadrados preenchidos com opacidade 30% Verde.
    *   Pacote de wearable HoloLens sendo inspecionado por vazamento OT: Quadrados piscando em amarelo.
    *   Bloqueio e Dissecção: Um quadrado salta do Grid, exibe o Payload Base64 modificado, fica Laranja (`#FF6200`), e a palavra `REJECTED_DLP_RULE_58` aparece piscando.

### C. The Multi-Agent Console (Swarm Theatre)
*   **Estrutura:** Painel fixo de rolagem automática à direita.
*   **Visual:** Semelhante à um `hTOP` colorido. Cada agente possui um prefixo com sua cor (ex: `[DLP_GUARDIAN]` em Ciano, `[SUPERVISOR_V2]` em Laranja).

## 3. Comportamento Interativo ("Stateful Effects")

Para passar a sensação de "Live Logs", as tabelas e grids web usarão micro-animações CSS. Não dependemos do React para gerenciar esse re-paint pesado; usaremos manipuladores diretos de DOM (Vanilla JS) ancorados em requisições WebSocket/BFF.

*   `class="threat-analyzing"`: Aplica um sutil filtro de desfoque (`blur(1px)`) com um SVG giratório sobre a linha da tabela de logs.
*   `class="egress-blocked"`: Agita rapidamente o elemento DOM na horizontal (shake keyframes) e colore o container de fundo como vermelho sólido apagando para preto de volta (`fadeIn/fadeOut`).
