# Technical Architecture & Viability Analysis: PetroShield XR

Este plano arquitetural traduz a dor do cliente (Petrobras) em um diagrama de camadas de alta fidelidade. Para atingir o "nível enterprise de produção", nós não reinventaremos a roda: aplicaremos integração de soluções SaaS estabelecidas no mercado de Cibersegurança que podem ser conectadas via API e proxy para um protótipo hiper-realista.

## User Review Required

> [!IMPORTANT]
> Confirmar a profundidade do código a ser gerado: No hackathon, a demonstração será focada apenas na parte do **Middleware/Proxy** interceptando requisições, simulando a resposta, ou precisamos de um frontend simulando a visão do óculos?

## Proposed Changes e Camadas da Arquitetura

O ambiente seguro (Zero-Trust) para a realidade mista industrial exige fatiar o problema nas 4 camadas abaixo. Cada camada usa tecnologias *Commercial Off-the-Shelf* (COTS).

### 1. O Endpoint Híbrido (Mobile Device Management)
Óculos VR/AR rodam versões customizadas do Android (ex: AOSP no Meta Quest). A Petrobras jamais faria o deploy sem um MDM forte. O MDM tranca o AOSP para evitar exploração de backdoors e sideloading de apps ransomware.
- **Solução de Mercado (Prototipagem):** **ArborXR** (especialista em gestão VR empresarial), VMware Workspace ONE ou Hexnode UEM.
- **Implementação:** Os dispositivos rodam em *Kiosk Mode*. O desenvolvedor não tem acesso ao SO nativo. O óculos inicia diretamente no App da companhia e a rede usa Perfis de Certificados VPN geridos pelo MDM.

### 2. Autenticação OAuth2.0 Device Flow (Identity IAM)
A entrada de dados (digitar senhas) via sensores no ar em Smart Glasses não é apenas ineficiente, é vetorialmente perigosa para *shoulder surfing* (sniffing visual no site ou via captura de tela oculta no backdoor).
- **Solução de Mercado (Prototipagem):** Microsoft Entra ID (Azure AD), Okta ou Keycloak.
- **Implementação:** Usa-se o framework de RFC 8628 (OAuth 2.0 Device Authorization Grant). Ao tentar utilizar a Inteligência Artificial, o óculos exibe um QR Code temporal. O operador foca a tela de seu celular (autenticado por biometria no MDM local) com o MS Authenticator no QR Code, destravando um token JWT (JSON Web Token) blindado para o uso temporário da máquina. Se os óculos não têm token JWT válido o Firewall restringe 100% da rede.

### 3. Middleware de Data Loss Prevention (DLP Proxy)
O aplicativo do smart glasses não conversa com a LLM. Esta é a regra de ouro do vazamento de dados. 
- **Solução de Mercado (Prototipagem):** Ngrok, Cloudflare Zero Trust Access Tunnels, somado com um pipeline FastAPI (Python) contendo bibliotecas de NLP como Spacy (ou ferramentas enterprise como Microsoft Purview e Nightfall AI DLP).
- **Implementação:** O Proxy recebe a requisição transladada de áudio->texto (STT) com o token JWT. Primeiro, valida a autorização. Segundo: usa Regex e PNL Leve para *Masking* / *Redação* de PII (Ex: "Poço do Pré-Sal Tupi-10" vira "[ATIVO_RESTRITO_01]"). Só depois, um Payload higienizado segue para a camada 4.

### 4. Enterprise AI Enclave (Confidential Computations)
Nunca enviar dados da Indústria para endpoints comuns da OpenAI, Anthropic, etc. sob redes não corporativas.
- **Solução de Mercado (Prototipagem):** Azure OpenAI Service provisionado sob uma **Rede Virtual Privada (VNet) via Private Endpoint**. A Azure assina contratos *No-Train* B2B. Alternativa: Deploy de um LLM local em nuvem privada (AWS Bedrock + Llama 3).
- **Implementação:** Somente o IP e a VPC proveniente da Camada 3 (DLP Proxy) consegue chegar na IA. Se o backdoor do VR for injetado, ele tentará varrer a rede e bater na API da Inteligência, tomando um bloqueio de infraestrutura L3/L4 (Network level).

---

## Open Questions

Para eu começar a quebrar essa arquitetura em código e testes locais para as entregas [E2 e E3] dos próximos dias, pense:

> [!WARNING]
> Dado o tempo de 48h da hackathon, nós precisaremos escolher em construir **Apenas 1 Camada** de forma codificada e simular as restantes em fluxograma/Figma. **O Middleware DLP** em API de Python interceptando o terminal geralmente é a "melhor mágica técnica" em Hackathons. Faremos ele?

## Verification Plan

### Teste de Autenticação (OAuth Device Flow Simulator)
Validar se o bloqueio de sessão ocorre requisitando dados sem o token JWT correto.

### Teste de Retenção de Dados (DLP Test)
Rodar uma bateria de Prompts em um Mock enviando dados sensíveis via CURL. Esperar que o LOG do nosso Proxy demonstre o Masking Automático censurando os dados.
