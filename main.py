from GerenciadorUsuarios import GerenciadorUsuarios

def main():
    sistema = GerenciadorUsuarios()

    # Simulação de Cadastro
    print("--- Cadastro Inicial ---")
    sistema.cadastrar_usuario("joao", "joao@alunos.com", "123", "aluno")
    sistema.cadastrar_usuario("maria", "maria@institucional.edu", "adm456", "funcionario")

    print("\n--- Teste de Login ---")
    user_usuario = input("Digite seu nome de usuário: ")
    user_senha = input("Digite sua senha: ")

    sessao_ativa = sistema.realizar_login(user_usuario, user_senha)

    if sessao_ativa:
        print(f"Usuário Logado: {sessao_ativa['username']} | Tipo: {sessao_ativa['tipo']}")
        # O ID abaixo é usado para rastrear reportes de vagas na HU-05 [cite: 58]
        print(f"ID da Sessão para rastreamento: {sessao_ativa['id']}")
    
if __name__ == "__main__":
    main()