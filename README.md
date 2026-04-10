# Sistema de Estacionamento no Campus

## Descrição
Este projeto foi desenvolvido como atividade da disciplina de Engenharia de Software.  
O objetivo foi transformar requisitos definidos anteriormente em um protótipo inicial funcional em Python, sem interface gráfica, simulando a lógica de um sistema de estacionamento no campus.

O sistema busca ajudar os alunos a visualizarem vagas disponíveis, diferenciarem vagas reservadas e realizarem reportes manuais de ocupação.

https://chatgpt.com/share/69d95d16-37d8-83e9-b5fc-123dd2a32b46

## Funcionalidades implementadas

### Gestão de vagas
- Estrutura de dados com as vagas do estacionamento
- Identificação de:
  - ID da vaga
  - setor
  - tipo da vaga
  - status
- Listagem de vagas disponíveis por setor
- Diferenciação de vagas por tipo no terminal:
  - comum = verde
  - reservada = azul
  - desconhecida = cinza
- Simulação de atualização automática do status das vagas

### Login
- Cadastro e acesso do usuário
- Simulação de sessão para evitar login repetido

### Reporte manual
- Reporte manual de vagas livres ou ocupadas
- Controle de reportes
- Integração com o restante do sistema no protótipo

## Divisão das responsabilidades
- **Michel**: funcionalidade de login
- **Isabelle**: gestão de vagas
- **João**: reporte manual

## Estrutura do projeto
Exemplo de organização dos arquivos:

```bash
app.py
gestao_vagas.py
login.py
reporte.py

AI Joao: https://claude.ai/share/03248c9e-e325-4196-8524-a92850cd902f
