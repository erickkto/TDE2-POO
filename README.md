# Sistema de Gerenciamento de Tarefas

Desenvolvi este sistema para a disciplina de Programação Orientada a Objetos. Ele permite criar, listar, alterar status e excluir tarefas.

## Estrutura
- Classe `Tarefa`: armazena título, descrição, status e data de criação.
- Classe `Gerenciador`: mantém uma lista de tarefas e oferece os métodos para CRUD.

## Exemplo de uso

```
=== MENU ===
1 - Adicionar tarefa
2 - Listar todas
3 - Marcar como concluída
0 - Sair
Escolha: 1
Título: Estudar POO
Descrição: 1. Entenda os conceitos de classes, objetos e o método __init__ para fixar a base da estrutura e, em seguida, 2. Domine os 4 pilares (herança, encapsulamento, polimorfismo e abstração) praticando com projetos como contas bancárias ou sistemas de RPG.
Tarefa adicionada!

Escolha: 2
0 - Título: Estudar POO | Status: pendente | Criada: 25/06/2026 14:30

Escolha: 3
0 - Título: Estudar POO | Status: pendente | Criada: 25/06/2026 14:30
Digite o índice da tarefa: 0
Status alterado para concluído.

Escolha: 2
0 - Título: Estudar POO | Status: concluido | Criada: 25/06/2026 14:30

Escolha: 0
Saindo...

## Repositório
[Link para o GitHub](https://github.com/erickkto/TDE2-POO)

```
