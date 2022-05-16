import matplotlib.pyplot as plt
import pandas as pd


dados = pd.read_csv('https://raw.githubusercontent.com/jonathansartorib/projeto_visualizacao_da_informacao/main/console.csv')


df_nintendo = dados.loc[(dados['Fabricante']=='Nintendo')]
vendas_nintendo = df_nintendo['Vendas'].sum()

df_sony = dados.loc[(dados['Fabricante']=='Sony')]
vendas_sony = df_sony['Vendas'].sum()

df_sega = dados.loc[(dados['Fabricante']=='Sega')]
vendas_sega = df_sega['Vendas'].sum()

df_bandai = dados.loc[(dados['Fabricante']=='Bandai')]
vendas_bandai = df_bandai['Vendas'].sum()

df_nokia = dados.loc[(dados['Fabricante']=='Nokia')]
vendas_nokia = df_nokia['Vendas'].sum()

df_atari = dados.loc[(dados['Fabricante']=='Atari')]
vendas_atari = df_atari['Vendas'].sum()



venda = [vendas_nintendo, vendas_sony, vendas_sega, vendas_bandai, vendas_nokia, vendas_atari]

fabricante = dados['Fabricante']
fabricante = fabricante.unique()

colors = [ 'lightgray', 'orange', 'coral', 'red','yellow', 'black']


patches, texts, autotexts = plt.pie(venda, colors=colors, autopct="",
startangle=90, explode=(0,0,0.1,0.1,0.2,0.3),)

plt.title('Venda de Consoles Portáteis por Fabricante')
plt.legend(patches, fabricante, loc="lower right")
plt.axis('equal')

plt.tight_layout()
plt.show()