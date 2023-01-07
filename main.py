# PACOTES DE INSTALAÇÃO
# pandas
# openpyxl
# twilio

import pandas as pd 
from twilio.rest import Client

# TOKEN E SID CONT CADASTRADO NA PLATAFORMA DA TWILIO
account_sid = "AC6acd0e299375d8f12e4ebdade8c3d965"
auth_token = "51ae058a076ec1127c0890126c270535"

# CONECTANDO ID E TOKEN
client = Client(account_sid, auth_token)

# Abri os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:     
    # Armazenando o arquivo do tipo excel
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    # Buscando um valor especifico nas linhas da tabela
    if (tabela_vendas['Vendas'] > 55000).any():
        # Listando o nome e valor nas colunas especificas
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]

        print(f'No Mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
                     body="f'No Mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}'",
                     from_="+14308085987",
                     to="85986931429"
                 )

        print(message.sid)





