import gspread
from oauth2client.service_account import ServiceAccountCredentials

def sincronizar_planilha(app):
    from database import listar_pessoas_dict, listar_instituicoes_dict

    with app.app_context():
        pessoas = listar_pessoas_dict()
        instituicoes = listar_instituicoes_dict()

        print("SINCRONIZANDO PLANILHA...")

        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = ServiceAccountCredentials.from_json_keyfile_name(
            "credenciais.json", scope
        )

        client = gspread.authorize(creds)

        planilha = client.open("dados agenda_cadastros")

        # 🔹 PESSOAS
        try:
            aba_pessoas = planilha.worksheet("Pessoas")
        except:
            aba_pessoas = planilha.add_worksheet(title="Pessoas", rows="1000", cols="20")

        aba_pessoas.clear()

        if pessoas:
            cabecalho = list(pessoas[0].keys())
            dados = [list(p.values()) for p in pessoas]
            aba_pessoas.update([cabecalho] + dados)

        # 🔹 INSTITUIÇÕES
        try:
            aba_inst = planilha.worksheet("Instituicoes")
        except:
            aba_inst = planilha.add_worksheet(title="Instituicoes", rows="1000", cols="20")

        aba_inst.clear()

        if instituicoes:
            cabecalho = list(instituicoes[0].keys())
            dados = [list(i.values()) for i in instituicoes]
            aba_inst.update([cabecalho] + dados)

        print("PLANILHA ATUALIZADA COM SUCESSO!")
