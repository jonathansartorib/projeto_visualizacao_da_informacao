import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dados = pd.read_csv('https://raw.githubusercontent.com/jonathansartorib/projeto_visualizacao_da_informacao/main/console.csv')

console_id = dados['ConsoleID']
indice = np.arange(len(console_id))
vendas = dados['Vendas']

plt.bar(indice, vendas, color=["cyan","red","gray","yellow","green"], edgecolor='black' ) 
plt.xticks(indice, console_id) 
plt.ylabel('Vendas em milhões') 
plt.xlabel('Console')
plt.title('Venda de Consoles Portáteis') 

plt.show() 


