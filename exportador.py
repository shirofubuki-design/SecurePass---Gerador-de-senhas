from pathlib import Path


def exportar_senha(senha, caminho="senha.txt"):
    arquivo = Path(caminho)

    with arquivo.open("w", encoding="utf-8") as f:
        f.write(senha)

    return arquivo