import plotly.graph_objects as go 
import pandas as pd 

df = pd.read_csv('https://raw.github.com/jonathansartorib/projeto_visualizacao_da_informacao/blob/main/console.csv')

fig = go.Figure(data=go.Choropleth(
    locations=df['Console_Name'], # Nome do país
    z = df['Vendas'].astype(int), # Dados para o Choropleth
    locationmode = 'country names', # Tipo de identificção geográfica
    colorscale = 'Reds', #escala contínua em tons de vermelho
    colorbar_title = "População",
))
                              
fig.update_layout(
    title_text = 'Vendas de Consoles',     
    geo_scope='south america', # Limita escopo para a América do Sul 
)  

fig.show()

