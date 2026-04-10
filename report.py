from datetime import datetime

vagas = {
    **{f"A{i}": {"setor": "A", "tipo": "reservada", "status": "livre"} for i in range(1, 6)},
    **{f"A{i}": {"setor": "A", "tipo": "comum",     "status": "livre"} for i in range(6, 11)},
    **{f"B{i}": {"setor": "B", "tipo": "comum",     "status": "livre"} for i in range(1, 11)},
}

# Lista de reportes salvos em memória (substitui o arquivo JSON)
reportes = []

# ─── Funções ──────────────────────────────────────────────────────────────────

def _tempo_desde_ultimo_reporte(usuario_id: str, vaga_id: str) -> float:
    """Retorna quantos segundos se passaram desde o último reporte do usuário para essa vaga."""
    agora = datetime.now()
    for r in reversed(reportes):
        if r["usuario_id"] == usuario_id and r["vaga_id"] == vaga_id:
            diff = (agora - r["horario"]).total_seconds()
            return diff
    return float("inf")  # nunca reportou


def reportar_vaga(usuario_id: str, vaga_id: str, novo_status: str) -> str:
    """
    Tenta registrar um reporte de vaga.

    Parâmetros:
        usuario_id  — identificador do usuário (vindo da Pessoa 2)
        vaga_id     — ex: 'A1', 'B2'
        novo_status — 'livre' ou 'ocupada'

    Retorna uma mensagem de resultado (str).
    """
    # 1. Vaga existe?
    if vaga_id not in vagas:
        return f"❌ Vaga '{vaga_id}' não encontrada no sistema."

    vaga = vagas[vaga_id]

    # 2. Vaga reservada? Alunos não podem reportar.
    if vaga["tipo"] == "reservada":
        return "🚫 Esta vaga é reservada para funcionários e não pode ser reportada por alunos."

    # 3. Status válido?
    if novo_status not in ("livre", "ocupada"):
        return "❌ Status inválido. Use 'livre' ou 'ocupada'."

    # 4. Reporte duplicado nos últimos 5 minutos?
    segundos = _tempo_desde_ultimo_reporte(usuario_id, vaga_id)
    if segundos < 300:  # 5 min = 300 s
        restante = int(300 - segundos)
        return (
            f"⏳ Você já reportou esta vaga recentemente. "
            f"Tente novamente em {restante} segundos."
        )

    # 5. Tudo certo — registra o reporte
    reporte = {
        "usuario_id": usuario_id,
        "vaga_id":    vaga_id,
        "status":     novo_status,
        "horario":    datetime.now(),
    }
    reportes.append(reporte)

    # Atualiza o status da vaga na estrutura principal
    vagas[vaga_id]["status"] = novo_status

    horario_fmt = reporte["horario"].strftime("%H:%M:%S")
    return (
        f"✅ Reporte registrado! Vaga {vaga_id} marcada como '{novo_status}' às {horario_fmt}."
    )


def mostrar_vagas_disponiveis() -> None:
    """Exibe todas as vagas separadas por setor, mostrando livres e ocupadas."""
    setores = {}
    for vaga_id, info in vagas.items():
        setor = info["setor"]
        if setor not in setores:
            setores[setor] = {
                "livres_comuns": [], "livres_reservadas": [],
                "ocupadas_comuns": [], "ocupadas_reservadas": [],
            }
        if info["status"] == "livre":
            if info["tipo"] == "reservada":
                setores[setor]["livres_reservadas"].append(vaga_id)
            else:
                setores[setor]["livres_comuns"].append(vaga_id)
        else:
            if info["tipo"] == "reservada":
                setores[setor]["ocupadas_reservadas"].append(vaga_id)
            else:
                setores[setor]["ocupadas_comuns"].append(vaga_id)

    print(f"\n{'─'*50}")
    print(f"{'STATUS DAS VAGAS':^50}")
    print(f"{'─'*50}")
    for setor, g in sorted(setores.items()):
        total_livres   = len(g["livres_comuns"]) + len(g["livres_reservadas"])
        total_ocupadas = len(g["ocupadas_comuns"]) + len(g["ocupadas_reservadas"])
        print(f"\n  📍 Setor {setor}  ({total_livres} livres / {total_ocupadas} ocupadas)")
        print(f"     🟢 Livres   — comuns:     {', '.join(g['livres_comuns'])    or 'nenhuma'}")
        print(f"     🔵 Livres   — reservadas: {', '.join(g['livres_reservadas']) or 'nenhuma'}")
        print(f"     🔴 Ocupadas — comuns:     {', '.join(g['ocupadas_comuns'])  or 'nenhuma'}")
        print(f"     🔴 Ocupadas — reservadas: {', '.join(g['ocupadas_reservadas']) or 'nenhuma'}")
    print(f"\n{'─'*50}\n")


def listar_reportes() -> None:
    """Exibe todos os reportes registrados na sessão."""
    if not reportes:
        print("Nenhum reporte registrado ainda.")
        return
    print(f"\n{'─'*45}")
    print(f"{'HISTÓRICO DE REPORTES':^45}")
    print(f"{'─'*45}")
    for r in reportes:
        print(
            f"  Usuário: {r['usuario_id']:<10} | "
            f"Vaga: {r['vaga_id']:<4} | "
            f"Status: {r['status']:<8} | "
            f"Hora: {r['horario'].strftime('%H:%M:%S')}"
        )
    print(f"{'─'*45}\n")

