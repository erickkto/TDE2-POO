from datetime import datetime


class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.status = "pendente"          # "pendente" ou "concluído"
        self.data = datetime.now()        # data e hora atuais

    def __str__(self):
        # Retorna uma string para exibir a tarefa
        data_formatada = self.data.strftime("%d/%m/%Y %H:%M")
        return f"Título: {self.titulo} | Status: {self.status} | Criada: {data_formatada}"

# Classe Gerenciador - lista e funções
class Gerenciador:
    def __init__(self):
        self.tarefas = []   # lista vazia

    def adicionar(self, titulo, descricao):
        nova = Tarefa(titulo, descricao)
        self.tarefas.append(nova)
        print("Tarefa adicionada!")

    def listar_todas(self):
        if len(self.tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
            return
        for i in range(len(self.tarefas)):
            print(f"{i} - {self.tarefas[i]}")

    def marcar_concluida(self, indice):
        if indice < 0 or indice >= len(self.tarefas):
            print("Índice inválido.")
            return
        self.tarefas[indice].status = "concluído"
        print("Status alterado para concluído.")

    def marcar_pendente(self, indice):
        if indice < 0 or indice >= len(self.tarefas):
            print("Índice inválido.")
            return
        self.tarefas[indice].status = "pendente"
        print("Status alterado para pendente.")

    def excluir(self, indice):
        if indice < 0 or indice >= len(self.tarefas):
            print("Índice inválido.")
            return
        removida = self.tarefas.pop(indice)
        print(f"Tarefa '{removida.titulo}' excluída.")

# Menu interativo
def main():
    gerenciador = Gerenciador()

    while True:
        print("\n=== MENU ===")
        print("1 - Adicionar tarefa")
        print("2 - Listar todas")
        print("3 - Marcar como concluída")
        print("4 - Marcar como pendente")
        print("5 - Excluir tarefa")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            gerenciador.adicionar(titulo, descricao)

        elif opcao == "2":
            gerenciador.listar_todas()

        elif opcao == "3":
            gerenciador.listar_todas()   # mostra os índices
            try:
                ind = int(input("Digite o índice da tarefa: "))
                gerenciador.marcar_concluida(ind)
            except:
                print("Digite um número válido.")

        elif opcao == "4":
            gerenciador.listar_todas()
            try:
                ind = int(input("Digite o índice da tarefa: "))
                gerenciador.marcar_pendente(ind)
            except:
                print("Digite um número válido.")

        elif opcao == "5":
            gerenciador.listar_todas()
            try:
                ind = int(input("Digite o índice da tarefa: "))
                gerenciador.excluir(ind)
            except:
                print("Digite um número válido.")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

# executar
if __name__ == "__main__":
    main()