import secrets
import string


def gerar_senha(
    tamanho=16,
    usar_minusculas=True,
    usar_maiusculas=True,
    usar_numeros=True,
    usar_simbolos=True
):
    grupos = []
    senha = []

    if usar_minusculas:
        grupos.append(string.ascii_lowercase)

    if usar_maiusculas:
        grupos.append(string.ascii_uppercase)

    if usar_numeros:
        grupos.append(string.digits)

    if usar_simbolos:
        grupos.append("!@#$%&*()-_=+?")

    if not grupos:
        raise ValueError(
            "Selecione pelo menos um tipo de caractere."
        )

    if tamanho < len(grupos):
        raise ValueError(
            "O tamanho da senha é muito pequeno."
        )

    # Garante pelo menos um caractere de cada grupo
    for grupo in grupos:
        senha.append(secrets.choice(grupo))

    todos_caracteres = "".join(grupos)

    # Completa o restante da senha
    while len(senha) < tamanho:
        senha.append(
            secrets.choice(todos_caracteres)
        )

    # Embaralhamento seguro
    secrets.SystemRandom().shuffle(senha)

    return "".join(senha)