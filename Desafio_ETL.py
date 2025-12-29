import pandas as pd
import json

# Parte 1 - EXTRACT - Lê o CSV e converte para uma lista de dicionários
users = pd.read_csv(r'c:\Users\Pryscilla\Documents\Curso Analise de Dados Santander\Python\arquivo_ids.csv').to_dict(orient='records')
user_ids = [user['UserID'] for user in users]
print(f"Lista de Ids criada: {user_ids}")

# Parte 2: TRANSFORM - Gera as mensagens para quem tem mais de 50000 investido
def gerar_mensagem(user):
    nome = user['nome']
    invest = user.get('invest', 0)
    vlcard = user.get('vlcard', 0)

    if invest >= 50000 or vlcard >= 5000:
        return f"Ola {nome}, Aproveite os beneficios da isencao da sua anuidade"
    else:
        return f"Oi {nome}, a sua anuidade no valor de 150,00 sera debitada no quinto dia util. Invista mais e garanta anuidade zero! Preparamos dicas exclusivas para voce melhorar seus investimentos hoje! "

for user in users:
    nova_noticia = gerar_mensagem(user)

    if not isinstance(user.get('news'), list):
        user['news'] = []
    
    # Criando o dicionário da notícia
    noticia_completa = {
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": nova_noticia
    }
    
    # Adicionando na lista de news do usuário
    user['news'].append(noticia_completa)

# Parte 3: LOAD (Simulando o Load) ---
print("### PROCESSO ETL FINALIZADO (MOCK) ###\n")
print(json.dumps(users, indent=2))