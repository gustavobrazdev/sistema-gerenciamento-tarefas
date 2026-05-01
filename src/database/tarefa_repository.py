from datetime import date, datetime

from database.conexao import conexao_banco_dados


def salvar_tarefa(tarefa):
    conexao = conexao_banco_dados()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO tarefa
        (titulo_tarefa, descricao_tarefa, prioridade_tarefa, status_tarefa, prazo_tarefa, id_usuario)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    valores = (
        tarefa.titulo,
        tarefa.descricao,
        tarefa.prioridade,
        tarefa.status,
        tarefa.prazo,
        tarefa.id_usuario
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()


def listar_tarefas(id_usuario):
    conexao = conexao_banco_dados()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT id_tarefa, titulo_tarefa, descricao_tarefa, prioridade_tarefa,
               status_tarefa, data_criacao, prazo_tarefa
        FROM tarefa
        WHERE id_usuario = %s
        ORDER BY id_tarefa DESC
    """

    cursor.execute(sql, (id_usuario,))
    tarefas = cursor.fetchall()

    cursor.close()
    conexao.close()

    hoje = date.today()
    for tarefa in tarefas:
        prazo = tarefa.get("prazo_tarefa")
        if isinstance(prazo, datetime):
            prazo = prazo.date()
        if prazo and prazo < hoje and tarefa["status_tarefa"] != "concluida":
            tarefa["status_tarefa"] = "pendente"
            tarefa["prazo_vencido"] = True
        else:
            tarefa["prazo_vencido"] = False

    return tarefas


def excluir_tarefa(id_tarefa, id_usuario):
    conexao = conexao_banco_dados()
    cursor = conexao.cursor()

    sql = """
        DELETE FROM tarefa
        WHERE id_tarefa = %s AND id_usuario = %s
    """

    cursor.execute(sql, (id_tarefa, id_usuario))
    conexao.commit()

    cursor.close()
    conexao.close()

def buscar_tarefa_id(id_tarefa, id_usuario):
    conexao = conexao_banco_dados()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT id_tarefa, titulo_tarefa, descricao_tarefa, prioridade_tarefa,
               status_tarefa, prazo_tarefa, id_usuario
        FROM tarefa
        WHERE id_tarefa = %s AND id_usuario = %s
    """

    cursor.execute(sql, (id_tarefa, id_usuario))
    tarefa = cursor.fetchone()

    cursor.close()
    conexao.close()

    return tarefa


def atualizar_tarefa(tarefa, id_tarefa):
    conexao = conexao_banco_dados()
    cursor = conexao.cursor()

    sql = """
        UPDATE tarefa
        SET titulo_tarefa = %s,
            descricao_tarefa = %s,
            prioridade_tarefa = %s,
            status_tarefa = %s,
            prazo_tarefa = %s
        WHERE id_tarefa = %s AND id_usuario = %s
    """

    valores = (
        tarefa.titulo,
        tarefa.descricao,
        tarefa.prioridade,
        tarefa.status,
        tarefa.prazo,
        id_tarefa,
        tarefa.id_usuario
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()    