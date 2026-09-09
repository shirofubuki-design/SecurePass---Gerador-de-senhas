# SecurePass---Gerador-de-senhas
SecurePass - Gerador de Senhas

Gerador de senhas desenvolvido em Python com interface gráfica utilizando Tkinter.

O projeto permite criar senhas personalizadas e avaliar sua força, mantendo o foco em segurança e privacidade.

# Funcionalidades

- Geração segura de senhas
- Configuração do tamanho da senha
- Letras maiúsculas e minúsculas
- Números
- Símbolos
- Avaliação da força da senha
- Barra visual de força
- Mostrar ou ocultar senha
- Copiar senha para a área de transferência
- Exportação opcional para arquivo
- Nenhuma senha é armazenada automaticamente

# Segurança

A geração das senhas utiliza o módulo `secrets` do Python, apropriado para geração de valores criptograficamente seguros.

O programa não possui banco de dados e não mantém histórico das senhas geradas.

As senhas somente são exportadas quando o usuário solicita explicitamente.

# Tecnologias

- Python
- Tkinter
- Secrets
- String
- Regex

