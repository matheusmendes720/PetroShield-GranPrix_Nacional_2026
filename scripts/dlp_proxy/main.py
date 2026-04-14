from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel
import re

app = FastAPI(title="PetroShield XR DLP Proxy", description="API Middleware para Sanitização de Prompts de IA de Borda")

@app.get("/")
async def root():
    return {
        "message": "PetroShield XR Gateway Ativo",
        "status": "online",
        "docs": "/docs",
        "version": "1.0.0-high-fidelity"
    }

class PromptRequest(BaseModel):
    query: str
    device_id: str

class RedactionEngine:
    def redact(self, text: str) -> str:
        # Padrões Regex para simular a Prevenção de Perda de Dados (DLP)
        
        # Redatar CPF Brasileiro
        text = re.sub(r'\d{3}\.\d{3}\.\d{3}-\d{2}', '[CPF_BLOQUEADO]', text)
        
        # Redatar Ativos Operacionais Estratégicos (Ex: Plataforma P-XX, Poço xyz)
        text = re.sub(r'(?i)\bp-\d{2,3}\b', '[ATIVO_RESTRITO]', text)
        text = re.sub(r'(?i)\bpo[çc]o\s+[a-z0-9-]+\b', '[ATIVO_RESTRITO]', text)
        
        # Redatar senhas eventualmente ditas pelo microfone do VR
        text = re.sub(r'(?i)(senha|password)\s+([a-zA-Z0-9@#$]+)', r'\1 [CREDENCIAL_BLOQUEADA]', text)
        
        return text

redactor = RedactionEngine()

def verify_token(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Header de Autorização ausente ou inválido. O Smart Glasses deve usar OAuth Device Flow Token.")
    
    token = authorization.split("Bearer ")[1]
    # Token MOCK fixo para uso em testes reais da demonstração da Hackathon
    if token != "jwt_token_xr_session_9942":
        raise HTTPException(status_code=403, detail="Token de Sessão Inválido. Potencial movimento lateral detectado (Device Hijacking).")
    return True

@app.post("/api/v1/secure-prompt")
async def secure_prompt(request: PromptRequest, authorized: bool = Depends(verify_token)):
    original_query = request.query
    
    # Roda o motor de DLP de Higienização de Dados (Sanitization/Redacting)
    sanitized_query = redactor.redact(original_query)
    
    # Simulando a comunicação "Traseira" (Backend-to-Backend) para a IA (Azure OpenAI)
    mock_llm_response = (
        f"Sou a IA Copilot Corporativa (LLM Privado). "
        f"Estou analisando a sua query de forma segura. O meu acesso local recebeu os seguintes dados limpos: '{sanitized_query}'"
    )
    
    return {
        "status": "success",
        "dlp_audit_log": {
            "device_id": request.device_id,
            "original_query_length": len(original_query),
            "sanitized_query": sanitized_query,
            "data_leak_prevented": original_query != sanitized_query
        },
        "llm_response": mock_llm_response
    }

@app.get("/api/v1/auth/device-flow-status")
async def device_flow(device_id: str):
    # Simula o endpoint em que o óculos checa continuamente se o técnico 
    # já aprovou o QR code no seu próprio celular (Device Authorization Grant - RFC 8628).
    return {
        "device_id": device_id, 
        "status": "pending_smartphone_approval", 
        "verification_uri": "https://auth.corp.petrobras.com.br/device",
        "instruction": "Abra o link no celular e use o FaceID para destravar a sessão deste Óculos VR."
    }

if __name__ == "__main__":
    import uvicorn
    # Para rodar: uvicorn main:app --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)
