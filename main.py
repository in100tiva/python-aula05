opcao = ""

while True:
  print("Menu: ")
  print("1. Opção 1")
  print("2. Opção 2")
  print("Digite 'sair' para encerrar")
  opcao = input("Escolha uma opção: ").lower()
  if opcao == "1":
    print("Você escolheu a opção 1")
  elif opcao == "2":
    print("Você escolheu a opção 2")
  elif opcao == "sair":
    print("encerrando o programa")
    break
  else:
    print("opção invalida, tente novamente")
