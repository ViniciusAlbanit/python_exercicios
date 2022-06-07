def coleta_canais(qtd_canais):

   canais = []

   for _ in range(qtd_canais):

       nome,inscritos,monetizacao,premium = input().split(';')

       inscritos= int(inscritos)

       monetizacao = float(monetizacao)

       premium = premium == 'sim'

       canais.append([nome,inscritos,monetizacao,premium])

   return canais  

def bonificacao(canais, fixo_premium,fixo_nao_premium):

   bonus = []

   for canal in canais:

       valor = canal[2]

       if canal [3]:

           valor += canal[1] // 1000 * fixo_premium

       else:

           valor +=canal[1] // 1000 * fixo_nao_premium

       bonus.append([canal[0], valor])  

   return bonus          

def exibe (bonus):

   print(5* '-')

   print('BÔNUS')

   print(5* '-')

   for registro in bonus:

       print(f'{registro[0]}: R$ {registro[1]:.2f}')

qtd_canais = int(input())

canais = coleta_canais(qtd_canais)

fixo_premium = float(input())

fixo_nao_premium = float(input())  

bonus = bonificacao(canais,fixo_premium,fixo_nao_premium)

exibe(bonus)
