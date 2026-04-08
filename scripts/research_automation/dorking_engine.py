import sys

def generate_dorks(target_domain):
    """
    Gera uma lista de Google Dorks avançados para reconhecimento técnico de um alvo.
    """
    dorks = [
        f'site:{target_domain} "index of" /admin',
        f'site:github.com "{target_domain}" "DB_PASSWORD" OR "SECRET_KEY"',
        f'site:{target_domain} ext:log "error" OR "connection failed"',
        f'site:{target_domain} intitle:"dashboard" "Grafana" OR "Kibana"',
        f'site:{target_domain} inurl:admin | inurl:login | inurl:setup',
        f'site:pastebin.com "{target_domain}"',
        f'site:trello.com "{target_domain}"',
        f'site:s3.amazonaws.com "{target_domain}"'
    ]
    return dorks

def main():
    if len(sys.argv) < 2:
        print("Uso: python dorking_engine.py <dominio_alvo>")
        sys.exit(1)

    target = sys.argv[1]
    print(f"[*] Gerando Dorks para: {target}")
    
    dorks = generate_dorks(target)
    
    print("\n[!] Dorks Gerados (Copie e cole no Google ou use via API):")
    for i, dork in enumerate(dorks, 1):
        print(f"{i}. {dork}")

    print("\n[*] Dica: Para automação em larga escala, utilize a API do Serper.dev ou similar.")

if __name__ == "__main__":
    main()
