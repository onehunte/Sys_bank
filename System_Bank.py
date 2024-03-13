menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair 
==> """

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0 
LIMITE_SAQUES = 3

while True: 
  
  opcao = input(menu)
  
  if opcao == "d":
    saldo = float(input('Qual valor voce deseja depositar?: '))
    continuar = input('Quer continuar depositando S/N: ')
    #
    while continuar.lower() == 's':
      saldo += float(input('Adicione o valor: '))
      continuar = input(f'saldo atual: R$ {saldo} ,\n Quer continuar depositando (S/N): ')
    #
    if saldo < 0:
      print("Valor recusado por favor somente valores positivos")
      saldo = 0  
    print(f"Seu saldo atual e de atualmente {round(float(saldo),2)}")
    extrato += f"Deposito: R$ {saldo:.2f}\n"
  
  elif opcao == "s":
    print("Saque")
    saque = 0
    while True:
      if saque > saldo:
        print("Saldo insulficiente")
      elif saque > limite:
        print(f"Valor ultrapassou o limite máximo para saque, limite máximo: R${limite}")
      elif numeros_saques >= LIMITE_SAQUES:
        print("Você excedeu o limite diario de saques.")
      else:
        saldo -= saque
        numeros_saques += 1
        print(f"Saques de R${saque} realizado com sucesso")
        print(f"Saldo atua: R${saldo}")
        extrato += f"Saque: R$ {saldo:.2f}\n"
      continuarSacando = input("Quer continuar sacando? (S/N): ")
      if continuarSacando.upper() != "S":
        break
      saque = float(input("Adicione o valor: "))
      
    
  elif opcao == "e":
    print("Extrato")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
  elif opcao == "q":
    break

  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")