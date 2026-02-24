import requests

SUPABASE_URL = "https://bjzbnvjgsmiumlkucvtl.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJqemJudmpnc21pdW1sa3VjdnRsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjUxMjAzODUsImV4cCI6MjA4MDY5NjM4NX0.yv850FKtEbtnsQeOk16iWc4MDOVy3JuWgBdFc9_5G_A"  # chave anon pública

headers={
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}
# 🔹 LISTAR INSTITUIÇÕES
def listar_instituicoes():
    url = f"{SUPABASE_URL}/rest/v1/instituicoes?select=*"
    response = requests.get(url, headers=headers)
    return response.json()

# 🔹 BUSCAR INSTITUIÇÃO POR ID
def buscar_instituicao(id):
    url = f"{SUPABASE_URL}/rest/v1/instituicoes?id=eq.{id}&select=*"
    response = requests.get(url, headers=headers)
    dados = response.json()
    return dados[0] if dados else None

# 🔹 ADICIONAR INSTITUIÇÃO
def adicionar_instituicao(dados):
    url = f"{SUPABASE_URL}/rest/v1/instituicoes"
    response = requests.post(url, headers=headers, json=dados)
    return response.status_code
# 🔹 ATUALIZAR INSTITUIÇÃO
def atualizar_instituicao(id, dados):
    url = f"{SUPABASE_URL}/rest/v1/instituicoes?id=eq.{id}"
    response = requests.patch(url, headers=headers, json=dados)
    return response.status_code

# 🔹 EXCLUIR INSTITUIÇÃO
def excluir_instituicao(id):
    url = f"{SUPABASE_URL}/rest/v1/instituicoes?id=eq.{id}"
    response = requests.delete(url, headers=headers)
    return response.status_code

# BUSCAR INSTITUICAO POR EMAIL CNPJ E NOME
def buscar_instituicoes_por_termo(termo):
    termo = termo.lower()
    url = (
        f"{SUPABASE_URL}/rest/v1/instituicoes?"
        f"or=("
        f"nome_oficial.ilike.*{termo}*,"
        f"email_oficial.ilike.*{termo}*,"
        f"cnpj.ilike.*{termo}*"
        f")&select=*"
    )
    response = requests.get(url, headers=headers)
    return response.json()




#-----------------Parte de pessoas---------------------#

# 🔹 LISTAR PESSOAS
def listar_pessoas():
    url = f"{SUPABASE_URL}/rest/v1/pessoas?select=*"
    response = requests.get(url, headers=headers)
    return response.json()

# 🔹 ADICIONAR PESSOA
def adicionar_pessoa(dados):
    url = f"{SUPABASE_URL}/rest/v1/pessoas"
    response = requests.post(url, json=dados, headers=headers)

    if response.status_code >= 400:
        print("ERRO:", response.status_code, response.text)

    return response.status_code

# 🔹 BUSCAR PESSOA PELO ID
def buscar_pessoa(id):
    url = f"{SUPABASE_URL}/rest/v1/pessoas?id=eq.{id}&select=*"
    response = requests.get(url, headers=headers)
    dados = response.json()
    return dados[0] if dados else None
# atualizar pessoa
def atualizar_pessoa(id, dados):
    url = f"{SUPABASE_URL}/rest/v1/pessoas?id=eq.{id}"
    response = requests.patch(url, json=dados, headers=headers)
    return response.status_code
# 🔹 DELETAR PESSOA
def excluir_pessoa(id):
    url = f"{SUPABASE_URL}/rest/v1/pessoas?id=eq.{id}"
    requests.delete(url, headers=headers)
    return True
