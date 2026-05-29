import json
import os

ARQUIVO = "pedidos.json"

def carregar_pedidos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_pedidos(pedidos):
    with open(ARQUIVO, "w") as f:
        json.dump(pedidos, f, indent=4)

def registrar_pedido(cliente, produto, quantidade):
    pedidos = carregar_pedidos()
    pedido = {
        "numero": len(pedidos) + 1,
        "cliente": cliente,
        "produto": produto,
        "quantidade": quantidade,
        "status": "reservado"
    }
    pedidos.append(pedido)
    salvar_pedidos(pedidos)
    print(f"\nPedido registrado com sucesso!")
    print(f"Numero do pedido: {pedido['numero']}")
    print(f"Cliente: {cliente}")
    print(f"Produto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Status: reservado")

def listar_pedidos():
    pedidos = carregar_pedidos()
    if len(pedidos) == 0:
        print("\nNenhum pedido registrado ainda.")
        return
    print("\n===== PEDIDOS CONIBASE =====")
    for pedido in pedidos:
        print(f"\nPedido #{pedido['numero']}")
        print(f"  Cliente:    {pedido['cliente']}")
        print(f"  Produto:    {pedido['produto']}")
        print(f"  Quantidade: {pedido['quantidade']}")
        print(f"  Status:     {pedido['status']}")
    print("============================")

def buscar_pedido(nome):
    pedidos = carregar_pedidos()
    for pedido in pedidos:
        if pedido["cliente"].lower() == nome.lower():
            print(f"\nPedido encontrado!")
            print(f"Numero: {pedido['numero']}")
            print(f"Produto: {pedido['produto']}")
            print(f"Status: {pedido['status']}")
            return
    print("\nCliente nao encontrado.")

while True:
    print("\n===== CONIBASE PEDIDOS =====")
    print("1 - Registrar pedido")
    print("2 - Listar pedidos")
    print("3 - Buscar por cliente")
    print("4 - Sair")
    opcao = input("\nEscolha: ")
    if opcao == "1":
        cliente = input("Nome do cliente: ")
        produto = input("Produto (ex: Porcelanato 60x60): ")
        quantidade = input("Quantidade (m2 ou caixas): ")
        registrar_pedido(cliente, produto, quantidade)
    elif opcao == "2":
        listar_pedidos()
    elif opcao == "3":
        nome = input("Nome do cliente: ")
        buscar_pedido(nome)
    elif opcao == "4":
        print("\nSaindo...")
        break
    else:
        print("\nOpcao invalida.")