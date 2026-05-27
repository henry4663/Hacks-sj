# APK Maker Termux Beta
# Feito para Termux
# by ChatGPT

import os
import time
import json

SAVE_FILE = "app_config.json"

config = {
    "sdk": "",
    "nome": "MeuApp",
    "icone": "android",
    "cor": "white"
}

# ==========================
# FUNÇÕES
# ==========================

def clear():
    os.system("clear")

def pause():
    input("\nENTER pra continuar...")

def salvar():
    with open(SAVE_FILE, "w") as f:
        json.dump(config, f)

def carregar():
    global config
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            config = json.load(f)

def banner():
    print("""
╔══════════════════════════╗
║      APK MAKER BETA      ║
║         TERMUX           ║
╚══════════════════════════╝
""")

# ==========================
# MENU SDK
# ==========================

def menu_sdk():
    while True:
        clear()
        banner()

        print("01 - Botar SDK")
        print("02 - ALL SDK")
        print("03 - Kill App")
        print("04 - Salvar")
        print("00 - Voltar")

        op = input("\nEscolha: ")

        if op == "1" or op == "01":
            sdk = input("Nome SDK: ")
            config["sdk"] = sdk
            print("SDK salvo.")

        elif op == "2" or op == "02":
            print("""
SDKS:
- Android SDK
- Build Tools
- Java SDK
- Kotlin SDK
- Python SDK
""")

        elif op == "3" or op == "03":
            app = input("Nome app pra matar: ")
            os.system(f"pkill {app}")
            print("Tentativa enviada.")

        elif op == "4" or op == "04":
            salvar()
            print("Salvo.")

        elif op == "0" or op == "00":
            break

        pause()

# ==========================
# CONFIG APP
# ==========================

def menu_config():
    while True:
        clear()
        banner()

        print("01 - Nome do app")
        print("02 - Ícone opcional")
        print("03 - Salvar")
        print("00 - Voltar")

        op = input("\nEscolha: ")

        if op == "1" or op == "01":
            nome = input("Nome app: ")
            config["nome"] = nome

        elif op == "2" or op == "02":
            icon = input("Ícone ou ENTER padrão: ")

            if icon == "":
                icon = "android"

            config["icone"] = icon

        elif op == "3" or op == "03":
            salvar()
            print("Config salva.")

        elif op == "0" or op == "00":
            break

        pause()

# ==========================
# EDITOR
# ==========================

def criar_pastas():
    nome = config["nome"]

    os.makedirs(f"{nome}/assets", exist_ok=True)
    os.makedirs(f"{nome}/sounds", exist_ok=True)
    os.makedirs(f"{nome}/android", exist_ok=True)

    print("Pastas criadas.")

def editor_texto():
    nome = config["nome"]

    texto = input("Texto app: ")

    with open(f"{nome}/main.txt", "w") as f:
        f.write(texto)

    print("Texto salvo.")

def editor_audio():
    nome = config["nome"]

    audio = input("ID som beta: ")

    with open(f"{nome}/audio.txt", "w") as f:
        f.write(audio)

    print("Áudio salvo.")

def editor_cor():
    nome = config["nome"]

    cor = input("Cor fundo: ")
    config["cor"] = cor

    with open(f"{nome}/cor.txt", "w") as f:
        f.write(cor)

    print("Cor salva.")

def menu_editor_basico():
    while True:
        clear()
        banner()

        print("01 - Criar texto")
        print("02 - Botar áudio ID")
        print("03 - Cor de fundo")
        print("04 - Salvar")
        print("00 - Voltar")

        op = input("\nEscolha: ")

        if op == "1" or op == "01":
            editor_texto()

        elif op == "2" or op == "02":
            editor_audio()

        elif op == "3" or op == "03":
            editor_cor()

        elif op == "4" or op == "04":
            salvar()
            print("Tudo salvo.")

        elif op == "0" or op == "00":
            break

        pause()

def menu_editor():
    while True:
        clear()
        banner()

        print("01 - Criar automaticamente pastas")
        print("02 - Script PY editor")
        print("03 - Criar pasta Android")
        print("04 - Editor básico")
        print("05 - Salvar")
        print("00 - Voltar")

        op = input("\nEscolha: ")

        if op == "1" or op == "01":
            criar_pastas()

        elif op == "2" or op == "02":
            nome = config["nome"]

            py = input("Nome script py: ")

            with open(f"{nome}/{py}.py", "w") as f:
                f.write("# script python")

            print("Script criado.")

        elif op == "3" or op == "03":
            criar_pastas()

            with open(f"{config['nome']}/android/config.txt", "w") as f:
                f.write("android config")

            print("Android básico criado.")

        elif op == "4" or op == "04":
            menu_editor_basico()

        elif op == "5" or op == "05":
            salvar()
            print("Salvo.")

        elif op == "0" or op == "00":
            break

        pause()

# ==========================
# EXPORTAR
# ==========================

def exportar():
    clear()
    banner()

    nome = config["nome"]

    os.makedirs("exports", exist_ok=True)

    apk = f"exports/{nome}.apk"

    with open(apk, "w") as f:
        f.write("APK FAKE BETA")

    print(f"""
APK exportado!

Local:
{apk}
""")

    pause()

# ==========================
# MENU PRINCIPAL
# ==========================

def main():
    carregar()

    while True:
        clear()
        banner()

        print("01 - Criar APK")
        print("02 - Configurar")
        print("03 - Editor App")
        print("04 - Exportar APK")
        print("00 - Sair")

        op = input("\nEscolha: ")

        if op == "1" or op == "01":
            menu_sdk()

        elif op == "2" or op == "02":
            menu_config()

        elif op == "3" or op == "03":
            menu_editor()

        elif op == "4" or op == "04":
            exportar()

        elif op == "0" or op == "00":
            break

if __name__ == "__main__":
    main()