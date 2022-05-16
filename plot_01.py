import plotly.graph_objects as go 
import pandas as pd 

df = pd.read_csv('https://raw.githubusercontent.com/ismarfrango/visualizacaoCS/master/southAmerica-pop.csv')

fig = go.Figure(data=go.Choropleth(
    locations=df['name'], # Nome do país
    z = df['pop'].astype(int), # Dados para o Choropleth
    locationmode = 'country names', # Tipo de identificção geográfica
    colorscale = 'Reds', #escala contínua em tons de vermelho
    colorbar_title = "População",
))
                              
fig.update_layout(
    title_text = 'População da América do Sul - 2019',     
    geo_scope='south america', # Limita escopo para a América do Sul 
)  

fig.show()

