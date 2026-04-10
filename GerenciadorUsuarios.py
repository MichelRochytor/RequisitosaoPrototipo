import csv
import uuid
import os
from Usuario import Usuario

class GerenciadorUsuarios:
    """Gerencia a persistência de dados utilizando a biblioteca CSV padrão."""
    def __init__(self, arquivo_db='usuarios.csv'):
        self.arquivo_db = arquivo_db
        self.cabecalho = ['id', 'username', 'email', 'senha', 'tipo']
        self._inicializar_arquivo()

    def _inicializar_arquivo(self):
        """Cria o arquivo CSV com cabeçalho caso ele não exista."""
        if not os.path.exists(self.arquivo_db):
            with open(self.arquivo_db, mode='w', newline='', encoding='utf-8') as f:
                escritor = csv.writer(f)
                escritor.writerow(self.cabecalho)

    def cadastrar_usuario(self, username, email, senha, tipo):
        """Registra um novo usuário no sistema, validando se o email já existe."""
        # Verifica duplicidade antes de cadastrar
        if self._buscar_por_email(email):
            print(f"Erro: O e-mail {email} já está cadastrado.")
            return

        novo_usuario = Usuario(username, email, senha, tipo)
        
        with open(self.arquivo_db, mode='a', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            escritor.writerow(novo_usuario.para_lista())
        
        print(f"Sucesso: {tipo.capitalize()} {username} cadastrado com ID {novo_usuario.id}.")

    def realizar_login(self, email, senha):
        """Valida as credenciais para permitir o acesso rápido sem login repetido. [cite: 33, 53]"""
        usuario_dados = self._buscar_por_email(email)
        
        if usuario_dados and usuario_dados['senha'] == str(senha):
            print(f"\nLogin bem-sucedido! Bem-vindo(a), {usuario_dados['username']}.")
            # Retorna os dados para gerenciar a sessão do usuário [cite: 56]
            return usuario_dados
        
        print("\nErro: Email ou senha incorretos.")
        return None

    def _buscar_por_email(self, email):
        """Método auxiliar para ler o CSV e encontrar um registro por email."""
        if not os.path.exists(self.arquivo_db):
            return None
            
        with open(self.arquivo_db, mode='r', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                if linha['email'] == email:
                    return linha
        return None