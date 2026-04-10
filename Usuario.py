import csv
import uuid
import os

class Usuario:
    """Representa a entidade usuário com os campos necessários para o sistema."""
    def __init__(self, username, email, senha, tipo, user_id=None):
        # Gera ID automático se não for fornecido (novo cadastro) [cite: 58]
        self.id = user_id if user_id else str(uuid.uuid4())[:8]
        self.username = username
        self.email = email
        self.senha = senha
        # Diferencia entre 'aluno' e 'funcionario' 
        self.tipo = tipo.lower()

    def para_lista(self):
        """Converte o objeto para uma lista compatível com a escrita em CSV."""
        return [self.id, self.username, self.email, self.senha, self.tipo]

