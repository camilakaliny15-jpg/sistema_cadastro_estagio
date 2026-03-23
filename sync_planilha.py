import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def sincronizar_planilha(app):
    from database import listar_pessoas_dict, listar_instituicoes_dict

    with app.app_context():
        pessoas = listar_pessoas_dict()
        instituicoes = listar_instituicoes_dict()

        print("SINCRONIZANDO PLANILHA...")

        # 🔹 Conectar com Google Sheets
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "credenciais.json", scope
        )

        client = gspread.authorize(creds)

        # 🔹 Abrir planilha
        planilha = client.open("dados agenda_cadastros")

        # 🔹 Converter para DataFrame
        df_pessoas = pd.DataFrame(pessoas)
        df_instituicoes = pd.DataFrame(instituicoes)

        # 🔹 Atualizar aba de pessoas
        try:
            aba_pessoas = planilha.worksheet("Pessoas")
        except:
            aba_pessoas = planilha.add_worksheet(title="Pessoas", rows="1000", cols="20")

        aba_pessoas.clear()
        aba_pessoas.update([df_pessoas.columns.values.tolist()] + df_pessoas.values.tolist())

        # 🔹 Atualizar aba de instituições
        try:
            aba_inst = planilha.worksheet("Instituicoes")
        except:
            aba_inst = planilha.add_worksheet(title="Instituicoes", rows="1000", cols="20")

        aba_inst.clear()
        aba_inst.update([df_instituicoes.columns.values.tolist()] + df_instituicoes.values.tolist())

        print("PLANILHA ATUALIZADA COM SUCESSO!")
