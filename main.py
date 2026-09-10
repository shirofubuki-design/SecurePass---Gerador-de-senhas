import tkinter as tk
from tkinter import ttk, messagebox, filedialog

from gerador import gerar_senha
from avaliador import avaliar_senha


# ---------------------------------
# GERAR SENHA
# ---------------------------------

def gerar():
    try:
        tamanho = int(campo_tamanho.get())

        senha = gerar_senha(
            tamanho=tamanho,
            usar_minusculas=var_minusculas.get(),
            usar_maiusculas=var_maiusculas.get(),
            usar_numeros=var_numeros.get(),
            usar_simbolos=var_simbolos.get()
        )

        campo_senha.delete(0, tk.END)
        campo_senha.insert(0, senha)

        resultado = avaliar_senha(senha)

        label_forca.config(
            text=f"Força: {resultado['nivel']} ({resultado['pontos']} pontos)"
        )

        barra_forca["value"] = resultado['pontos']

    except ValueError as erro:
        messagebox.showerror(
            "Erro",
            str(erro)
        )


# ---------------------------------
# COPIAR SENHA
# ---------------------------------

def copiar():
    senha = campo_senha.get()

    if not senha:
        messagebox.showwarning(
            "Aviso",
            "Gere uma senha primeiro."
        )
        return

    janela.clipboard_clear()
    janela.clipboard_append(senha)

    messagebox.showinfo(
        "Copiado",
        "Senha copiada para a área de transferência."
    )


# ---------------------------------
# EXPORTAR
# ---------------------------------

def exportar():
    senha = campo_senha.get()

    if not senha:
        messagebox.showwarning(
            "Aviso",
            "Gere uma senha primeiro."
        )
        return

    caminho = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[
            ("Arquivo de texto", "*.txt") #exporta para um arquivo de texto
        ]
    )

    if caminho:
        with open(
            caminho,
            "w",
            encoding="utf-8"
        ) as arquivo:

            arquivo.write(senha)

        messagebox.showinfo(
            "Exportado",
            "Senha exportada com sucesso."
        )


# ---------------------------------
# MOSTRAR / OCULTAR
# ---------------------------------

def mostrar_ocultar():
    if campo_senha.cget("show") == "":
        campo_senha.config(show="•")
        botao_mostrar.config(
            text="Mostrar"
        )

    else:
        campo_senha.config(show="")
        botao_mostrar.config(
            text="Ocultar"
        )


# ---------------------------------
# LIMPAR
# ---------------------------------

def limpar():
    campo_senha.delete(0, tk.END)

    label_forca.config(
        text="Força: -"
    )

    barra_forca["value"] = 0


# ---------------------------------
# JANELA
# ---------------------------------

janela = tk.Tk()

janela.title(
    "SecurePass - Gerador de Senhas"
)

janela.geometry(
    "500x520"
)

janela.resizable(
    False,
    False
)


# ---------------------------------
# TÍTULO
# ---------------------------------

titulo = tk.Label(
    janela,
    text="🔐 SecurePass",
    font=("Arial", 22, "bold")
)

titulo.pack(
    pady=20
)


subtitulo = tk.Label(
    janela,
    text="Gerador Seguro de Senhas",
    font=("Arial", 11)
)

subtitulo.pack()


# ---------------------------------
# TAMANHO
# ---------------------------------

frame_tamanho = tk.Frame(janela)

frame_tamanho.pack(
    pady=20
)


tk.Label(
    frame_tamanho,
    text="Tamanho da senha:"
).pack(
    side="left"
)


campo_tamanho = tk.Entry(
    frame_tamanho,
    width=8
)

campo_tamanho.pack(
    side="left",
    padx=10
)

campo_tamanho.insert(
    0,
    "16"
)


# ---------------------------------
# CHECKBOXES
# ---------------------------------

var_minusculas = tk.BooleanVar(
    value=True
)

var_maiusculas = tk.BooleanVar(
    value=True
)

var_numeros = tk.BooleanVar(
    value=True
)

var_simbolos = tk.BooleanVar(
    value=True
)


frame_opcoes = tk.Frame(janela)

frame_opcoes.pack()


tk.Checkbutton(
    frame_opcoes,
    text="Letras minúsculas",
    variable=var_minusculas
).pack(
    anchor="w"
)


tk.Checkbutton(
    frame_opcoes,
    text="Letras maiúsculas",
    variable=var_maiusculas
).pack(
    anchor="w"
)


tk.Checkbutton(
    frame_opcoes,
    text="Números",
    variable=var_numeros
).pack(
    anchor="w"
)


tk.Checkbutton(
    frame_opcoes,
    text="Símbolos",
    variable=var_simbolos
).pack(
    anchor="w"
)


# ---------------------------------
# BOTÃO GERAR
# ---------------------------------

botao_gerar = tk.Button(
    janela,
    text="GERAR SENHA",
    command=gerar,
    width=25,
    height=2
)

botao_gerar.pack(
    pady=20
)


# ---------------------------------
# CAMPO DA SENHA
# ---------------------------------

frame_senha = tk.Frame(janela)

frame_senha.pack()


campo_senha = tk.Entry(
    frame_senha,
    width=35,
    font=("Consolas", 12),
    justify="center"
)

campo_senha.pack(
    side="left",
    padx=5
)


botao_mostrar = tk.Button(
    frame_senha,
    text="Ocultar",
    command=mostrar_ocultar
)

botao_mostrar.pack(
    side="left"
)


# ---------------------------------
# FORÇA DA SENHA
# ---------------------------------

label_forca = tk.Label(
    janela,
    text="Força: -",
    font=("Arial", 11, "bold")
)

label_forca.pack(
    pady=(20, 5)
)


barra_forca = ttk.Progressbar(
    janela,
    length=300,
    maximum=6
)

barra_forca.pack()


# ---------------------------------
# BOTÕES
# ---------------------------------

frame_botoes = tk.Frame(janela)

frame_botoes.pack(
    pady=25
)


tk.Button(
    frame_botoes,
    text="Copiar",
    command=copiar,
    width=10
).pack(
    side="left",
    padx=5
)


tk.Button(
    frame_botoes,
    text="Exportar",
    command=exportar,
    width=10
).pack(
    side="left",
    padx=5
)


tk.Button(
    frame_botoes,
    text="Limpar",
    command=limpar,
    width=10
).pack(
    side="left",
    padx=5
)


# ---------------------------------
# AVISO
# ---------------------------------

aviso = tk.Label(
    janela,
    text="Nenhuma senha é armazenada automaticamente.",
    font=("Arial", 9)
)

aviso.pack(
    pady=10
)


# ---------------------------------
# INICIAR PROGRAMA
# ---------------------------------

janela.mainloop()