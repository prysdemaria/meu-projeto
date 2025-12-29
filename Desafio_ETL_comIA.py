import pandas as pd
import google.generativeai as genai
import json

from pathlib import Path


diretorio_atual = Path(__file__).parent
caminho_csv = diretorio_atual / 'arquivo_ids.csv'

# Parte 1 - EXTRACT - Lê o CSV e converte para uma lista de dicionários
users = pd.read_csv(caminho_csv).to_dict(orient='records')
user_ids = [user['UserID'] for user in users]
print(f"Lista de Ids criada: {user_ids}")

# Parte 2: TRANSFORM - Gera as mensagens para isenção de anuidade do cartão

genai.configure(api_key="gen-lang-client-0625549928")

def gerar_mensagem_com_ia(user):
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"Você é um gerente de banco. Crie uma frase curta e motivadora de marketing para o cliente {user['nome']} sobre investimentos, focando em quem tem limite de cartão de {user['invest']}. Seja gentil e use no máximo 100 caracteres."
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return "Invista no seu futuro com o Santander!" # Mensagem padrão caso a IA falhe

for user in users:
    if not isinstance(user.get('news'), list): user['news'] = []
    
    nova_noticia = gerar_mensagem_com_ia(user)
    
    user['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": nova_noticia
    })
# Parte 3: LOAD (Simulando o Load) ---
print("### PROCESSO ETL FINALIZADO (MOCK) ###\n")
print(json.dumps(users, indent=2))