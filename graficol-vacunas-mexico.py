## Tutorial generando mi primer gráfico lineal con phyton.

## PASO 1: Importar librerias
import pandas as pd
import plotly.express as px

## PASO 2: Importar datos de origen de vacunacion 
df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/Mexico.csv')
print(df.head())

## PASO 3: Generando el grafico lineal con plotly
fig = px.line(df, 
                x = 'date', 
                y = ['total_vaccinations', 'people_vaccinated','people_fully_vaccinated'],
                title='Histórico de aplicación de vacunas COVID19 en México'
               )

## Para personalizar los ejes del gráfico se utiliza la función update_?axes.
fig.update_xaxes(title_text='Fecha')
fig.update_yaxes(title_text='Dosis / Personas Vacunadas')

## Para personalizar el titulo de la leyenda
#fig.update_layout(legend_title_text='Leyenda')

## Actualizamos las leyendas de los datos a mostrar.
## Mostramos el array donde encontramos nuestras leyendas (opcional, solo para visualizar el contenido de nuestro gráfico)
#print(fig.data)
## Actualizamos la leyenda (se puede mejorar con iteración)
fig.data[0].name = "Total vacunas aplicadas"
fig.data[1].name = "Personas con 1 dosis"
fig.data[2].name = "Personas con tratamiento completo (2 dosis)"

## Customizando los ejes de nuestro gráfico
## Desactivando los ejes de la cuadrícula
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False, zeroline=False)

## Mostrando y aplicando formato a los ejes base de nuestro gráfico
fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black')

##fig.show()
fig.write_html('grafico-vacunacion-mexico.html', auto_open=True)