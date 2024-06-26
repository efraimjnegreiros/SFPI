primeiro_numero = int(input("Digite o Primeiro Número do Intervalo: "))
segundo_numero = int(input("Digite o Segundo Número do Intervalo: "))

primos = []
soma_dos_fatoriais_dos_primos = 0

for i in range(primeiro_numero, segundo_numero + 1, 1):
  numero_de_divisores = 0
  for j in range(1,i+1,1):
    if i % j == 0:
      numero_de_divisores += 1
  if numero_de_divisores == 2:
    primos.append(i)

if len(primos) != 0:
  fatoriais_dos_primos = []

  for i in primos:
    fatorial = 1
    for j in range(1, i+1, 1):
      fatorial *= j
    fatoriais_dos_primos.append(fatorial)
  soma = sum(fatoriais_dos_primos)
  mensagem = f"A soma dos fatoriais dos primos de {primeiro_numero} até {segundo_numero} é {soma} ."
  print(mensagem)
else:
  print('Não há primos no intervalo digitado!')
