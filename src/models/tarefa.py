class Tarefa:
    def __init__( self, titulo, descricao, prioridade="baixa", status="pendente", prazo=None,id_usuario=None): 
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = status
        self.prazo = prazo
        self.id_usuario = id_usuario