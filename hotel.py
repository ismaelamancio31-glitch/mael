print('    RESERVAS HOTEL   ')
print('CADASTRO')

valores_quartos = {
'Simples: R$ 100,00 por dia.'
'Duplo: R$ 150,00 por dia.'
'Luxo: R$ 250,00 por dia.'   
   }

clientes = []

for i in range(3):
   nome = str(input('qual seu nome?:'))
   idade = int(input('qual sua idade'))

print('/ntipos de quartos')
print( '1 - simples ( R$ 100,00)')
print( '2 - duplo ( R$ 150,00)')
print( '3 - luxo ( R$ 250,00)')

escolha = int(input('qual tipo de quarto? (1 , 2, 3)'))

if escolha == 1:
   valores_quartos = 'simples'

elif escolha == 2:
   valores_quartos =  'duplo'
   
elif escolha == 3:
   valores_quartos = 'luxo'
   
else:
    print('opção ivalida, atribuindo (simples) por padrao')
tipo_quarto = 'simples'

dias = int(input('quantos dias o cliente ficara no hotel?:'))

valor_total =  valores_quartos[tipo_quarto] * dias

cliente = {
  'nome': nome,
  'idade' : idade,  
  'tipo_quartos' : tipo_quarto,
  'dias' : dias,
  'valor_total': valor_total,
}

clientes.append(cliente)
  
print('  RESUMO DA RESERVA   ')  
for c in clientes:
   print(f'cliente: {c['nome']}')
   print(f'idade: {c['idade']}')
   print(f'tipo de quarto: {c['tipo_quartos']}')
   print(f'dia hospedado: {c['dias']}')  
   print(f'valor total: R$ {c['valor_total']}. 2f')

print('   RESERVA FINALIZADA   ')