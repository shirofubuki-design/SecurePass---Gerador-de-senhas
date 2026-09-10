import re


def avaliar_senha(senha):
    pontos = 0

    if len(senha) >= 8:
        pontos += 1

    if len(senha) >= 12:
        pontos += 1

    if re.search(r"[a-z]", senha):
        pontos += 1

    if re.search(r"[A-Z]", senha):
        pontos += 1

    if re.search(r"\d", senha):
        pontos += 1

    if re.search(r"[^a-zA-Z0-9]", senha):
        pontos += 1

    if pontos <= 2:
        nivel = "Fraca"

    elif pontos <= 4:
        nivel = "Média"

    elif pontos == 5:
        nivel = "Forte"

    else:
        nivel = "Muito forte"

    return {
    "nivel": nivel,
    "pontos": pontos,
}