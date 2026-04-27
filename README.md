# Sistema de Gerenciamento de Tarefas

## Descrição do Projeto

Este projeto está sendo desenvolvido para a disciplina de Engenharia de Software. O objetivo é criar um sistema web básico de gerenciamento de tarefas, utilizando boas práticas de organização de código, versionamento com Git/GitHub, metodologia ágil com Kanban, testes automatizados e integração contínua com GitHub Actions.

O sistema permite que um usuário realize cadastro, login e gerencie suas tarefas por meio de funcionalidades como criação, visualização, edição e exclusão de tarefas.

## Objetivo

Desenvolver um sistema de gerenciamento de tarefas para simular um projeto ágil de software, aplicando conceitos de Engenharia de Software na prática.

O projeto busca demonstrar:

- Organização de repositório no GitHub
- Uso de Kanban para controle de tarefas
- Separação de responsabilidades no código
- Cadastro e autenticação de usuários
- CRUD de tarefas
- Validação de dados
- Testes automatizados
- Pipeline de integração contínua com GitHub Actions

## Escopo Inicial

O escopo inicial do projeto inclui:

- Cadastro de usuários
- Login de usuários
- Criação de tarefas
- Visualização de tarefas
- Edição de tarefas
- Exclusão de tarefas
- Organização das tarefas por status e prioridade

## Metodologia Utilizada

A metodologia utilizada no projeto é baseada no Kanban.

O quadro Kanban foi organizado no GitHub Projects com as seguintes colunas:

- A Fazer
- Em Progresso
- Concluído

Essa organização permite acompanhar o andamento das atividades, visualizar o fluxo de desenvolvimento e controlar melhor as entregas do projeto.

## Tecnologias Utilizadas

- Python
- Flask
- HTML
- CSS
- MySQL
- Git
- GitHub
- GitHub Projects
- GitHub Actions
- Pytest

## Estrutura do Projeto

```text
sistema-gerenciamento-tarefas/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── docs/
│
├── src/
│   ├── app.py
│   ├── database/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── static/
│   ├── templates/
│   └── validators/
│
├── tests/
│
├── .gitignore
├── README.md
└── requirements.txt

Funcionalidades
Usuário
Cadastro de usuário
Login de usuário
Validação de dados do usuário
Autenticação para acessar o sistema
Tarefas
Criar tarefa
Visualizar tarefas cadastradas
Editar tarefa
Excluir tarefa
Definir prioridade da tarefa
Definir status da tarefa
Como Executar o Projeto

1. Clonar o repositório
git clone https://github.com/gustavobrazdev/sistema-gerenciamento-tarefas.git

2. Acessar a pasta do projeto
cd sistema-gerenciamento-tarefas

3. Criar o ambiente virtual
python -m venv venv

4. Ativar o ambiente virtual

No Windows: venv\Scripts\activate

5. Instalar as dependências
pip install -r requirements.txt

6. Executar o sistema
python src/app.py

Depois, acesse no navegador: http://127.0.0.1:5000


Controle de Qualidade

O projeto utilizará testes automatizados com Pytest para validar partes importantes do sistema, como validações de usuário, login e tarefas.

Também será configurado um pipeline com GitHub Actions para executar os testes automaticamente a cada envio de código para o repositório.

Mudança de Escopo

Durante o desenvolvimento, foi identificada a necessidade de melhorar o controle das tarefas cadastradas. Por isso, o escopo foi ampliado para incluir prioridade e status nas tarefas.

Essa alteração permite organizar melhor as demandas, acompanhar o andamento das atividades e simular uma mudança de escopo em um projeto ágil.

Status do Projeto

Em desenvolvimento.

Autor: Desenvolvido por Gustavo Braz para a disciplina de Engenharia de Software.


Depois de colar e salvar, faça no terminal:

```bash
git status
git add README.md
git commit -m "docs: adiciona README inicial do projeto"
git push
