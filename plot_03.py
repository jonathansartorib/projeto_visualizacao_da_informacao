import matplotlib.pyplot as plt
import pandas as pd

dados = pd.read_csv('https://raw.githubusercontent.com/jonathansartorib/projeto_visualizacao_da_informacao/main/console.csv')

ordem = dados['Ano_Lancamento']
ordem = dados.sort_values(by='Ano_Lancamento')

anos = ordem['Ano_Lancamento']
vendas = ordem['Vendas']

plt.plot(anos, vendas, color = "k", linestyle = "-", linewidth = 3)
plt.title('Vendas no decorrer dos anos.')
plt.xlabel('Anos')
plt.ylabel('Vendas em milhões')
plt.scatter(anos, vendas, label = "Vendas", color = "r", marker = "*", s =
100)

plt.xlim(1988,2012)
plt.legend()
plt.grid(color='coral', linestyle='--', linewidth=1)
plt.tight_layout()

plt.show()
