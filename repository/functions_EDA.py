
import pandas as pd 
import matplotlib as plt  
import seaborn as sns 
import plotly.express as px
import plotly as py  
from plotly.subplots import make_subplots
import plotly.graph_objects as go 
import numpy as np 
pd.options.display.max_colwidth = 100
import os # Creamos una condición para que nos autogenere las carpetas necesarias en caso de que no existan
if not os.path.exists("figures"):
    os.mkdir("figures")
data = pd.read_csv("Trade_Crops_Livestock_E_All_Data_(Normalized)_COUNTRIES_ONLY.csv", sep='|', encoding='latin-1', delimiter=",")


def explain_data_example(country, year):
    """
    Con esta función simple, obtenemos los productos más exportados en el año seleccionado    
    """
    filter1 = data[data.Area == country]
    filter1 = filter1[filter1.Year == year]
    filter1 = filter1[filter1.Element == "Export Quantity"]
    filter1 = filter1.sort_values(by="Value", ascending=False)
    fig1 = px.bar(filter1.head(10), 
        x="Item", 
        y="Value",
        color="Value",
        title= "Value of the ten principal products and facilities of Spain", #Falta poder introducir la variable como cuerpo de texto para que cambie el titulo automaticamente
        labels= {
            "Value": "Values in 1.000$",
            "Item": "Groups and facilities of exports"
                }
        )
    fig1.write_image("figures/figura1_spain_pre.png") # Aquí debe recibir también la variable para que cambie el nombre del archivo
explain_data_example(country="Spain", year=1999) # Al llamar a la función le pasamos tanto el pais como el año que queremos estudiar. Falta desarrollarlo para que podamos pasarle un rango de fechas

def explain_data_example(country, year):
    # Duplicamos la función para generar otra imagen con la que explicar y comparar la presentación
    filter1 = data[data.Area == country]
    filter1 = filter1[filter1.Year == year]
    filter1 = filter1[filter1.Element == "Export Quantity"]
    filter1 = filter1.sort_values(by="Value", ascending=False)
    fig1 = px.bar(filter1.head(10), 
        x="Item", 
        y="Value",
        color="Value",
        title= "Value of the ten principal products and facilities of Italy",
        labels= {
            "Value": "Values in 1.000$",
            "Item": "Groups and facilities of exports"
                }
        )
    fig1.write_image("figures/figura1_italy_pre.png") #La parte ''figures'' indica la ruta de la carpeta donde guardaremos todas las gráficas de aqui en adelante
explain_data_example(country="Italy", year=1999)

# A continuación se definen funciones útiles para cada tipo de estudio y evitar máscaras recurrentes
def import_quant(country):
    filter = data[data["Element"] == "Import Quantity"]
    filter = filter[filter["Area"] == country]
    return filter
def import_value(country):
    filter = data[data["Element"] == "Import Value"]
    filter = filter[filter["Area"] == country]
    return filter
def export_quant(country):
    filter = data[data["Element"] == "Export Quantity"]
    filter = filter[filter["Area"] == country]
    return filter
def export_value(country):
    filter = data[data["Element"] == "Export Value"]
    filter = filter[filter["Area"] == country]
    return filter

# Ahora comparamos la evolución de precios y toneladas exportadas por producto y país seleccionado
def fig_export_merged(item):
    country = "Italy" #input("Select a country")
    # Función para unir los dos gráficos en uno
    df = export_quant(country)
    df= df[df["Item"]==item]
    # Estas dos variables llaman hacia el dataframe de las cantidades de exportacion
    df1 = export_value(country)
    df1 = df1[df1["Item"]==item]
    # Estas dos variables llaman hacia el dataframe de precios de exportacion
    p1 = px.line(df[df.Item == item], x="Year", y="Value", color="Element", labels= {"Value": "Values in tonnes", "Year": "Year"})
    p2 = px.line(df1[df1.Item == item], x="Year", y="Value", color="Element", labels= {"Value": "Values in 1.0000$", "Year": "Year"})
    p1.update_traces(line_color="purple")
    p2.update_traces(line_color="orange")
    # A partir de aqui usamos "make_subplots" para unir las dos gráficas
    fig = make_subplots(specs=[[{"secondary_y": True}]], y_title= "<b>Quantity in tonnes</b>", x_title="<b>Years</b>") # Da formato a los ejes y títulos de los mismos
    fig.add_trace(p1.data[0], secondary_y=False)
    fig.add_trace(p2.data[0], secondary_y=True)
    fig.update_yaxes(title_text="<b>Value in 1.000$</b>", secondary_y=True) # Introduce una etiqueta para diferenciar eje secundario en la "y"
    fig.update_layout(width=1000, height=600, hovermode='x', title = "<b>Anual evolution of tons and prices of virgin olive oil in Italy</b>", title_x=0.5) # Da formato al título 
    fig.write_image("figures/figura2_spain_oil_olive_virgin_italy.png")
fig_export_merged(item= "Oil, olive, virgin") # Aqui se puede poner un imput para llamar al valor que se quiera de estudio

def fig_export_merged(item):
    country = "Spain" #input("Select a country")
    # Función para unir los dos gráficos en uno
    df = export_quant(country)
    df= df[df["Item"]==item]
    # Estas dos variables llaman hacia el dataframe de las cantidades de exportacion
    df1 = export_value(country)
    df1 = df1[df1["Item"]==item]
    # Estas dos variables llaman hacia el dataframe de precios de exportacion
    p1 = px.line(df[df.Item == item], x="Year", y="Value", color="Element", labels= {"Value": "Values in tonnes", "Year": "Year"})
    p2 = px.line(df1[df1.Item == item], x="Year", y="Value", color="Element", labels= {"Value": "Values in 1.0000$", "Year": "Year"})
    p1.update_traces(line_color="purple")
    p2.update_traces(line_color="orange")
    # A partir de aqui usamos "make_subplots" para unir las dos gráficas
    fig = make_subplots(specs=[[{"secondary_y": True}]], y_title= "<b>Quantity in tonnes</b>", x_title="<b>Years</b>") # Da formato a los ejes y títulos de los mismos
    fig.add_trace(p1.data[0], secondary_y=False)
    fig.add_trace(p2.data[0], secondary_y=True)
    fig.update_yaxes(title_text="<b>Value in 1.000$</b>", secondary_y=True) # Introduce una etiqueta para diferenciar eje secundario en la "y"
    fig.update_layout(width=1000, height=600, hovermode='x', title = "<b>Anual evolution of tons and prices of virgin olive oil in Spain</b>", title_x=0.5) # Da formato al título 
    fig.write_image("figures/figura2_spain_oil_olive_virgin_spain.png")
fig_export_merged(item= "Oil, olive, virgin") # Aqui se puede poner un imput para llamar al valor que se quiera de estudio

def factor_of_export_general_by_amount(year, item):
    """
    Analizamos aqui la evolución antes del Euro
    """
    #Esta función realiza lo mismo que la anterior pero nos excluye los países que no producen unos ingresos relevantes para el estudio
    filtro1 = data[data["Year"]==int(year)]
    filtro1 = filtro1[filtro1["Item"] == item]
    fact1= filtro1[filtro1["Element"] == "Export Quantity"]
    fact2 = filtro1[filtro1["Element"] == "Export Value"]
    # Ahora definimos el factor de estudio, que corresponde a dividir la cantidad de toneladas exportadas entre el dinero que se ha ingresado por esa exportacion
    fact2["Factor"] = fact1["Value"].values / fact2["Value"].values
    # Quitamos los posibles valores infinitos y los substituimos por NaN. Despues ordenamos de mayor a menor asegurandonos de dejar los NaN en última posición
    fact2 = fact2.replace([np.inf, -np.inf], np.nan)
    fact2 = fact2.sort_values(by="Factor", ascending=False, na_position="last")
    fact2 = fact2[fact2["Value"] > 1000] # Aquí determinamos el mínimo para incluir en el estudio
    fig1 = px.bar(fact2.head(10), x="Area", y="Factor",
        title= "<b>Export performance factor ranking before EURO arrival</b>",
        color = "Factor",
        labels= {"Area": "Country (no continents or groups)",
                "Factor": "EPF"})   
    fig1.write_image("figures/factor_ranking_preEuro.png")
factor_of_export_general_by_amount(year=1999, item="Oil, olive, virgin")

def factor_of_export_general_by_amount(year, item):
    """
    Analizamos aqui la evolución DESPUES del Euro
    """
    #Esta función realiza lo mismo que la anterior pero nos excluye los países que no producen unos ingresos relevantes para el estudio
    filtro1 = data[data["Year"]==int(year)]
    filtro1 = filtro1[filtro1["Item"] == item]
    fact1= filtro1[filtro1["Element"] == "Export Quantity"]
    fact2 = filtro1[filtro1["Element"] == "Export Value"]
    # Ahora definimos el factor de estudio, que corresponde a dividir la cantidad de toneladas exportadas entre el dinero que se ha ingresado por esa exportacion
    fact2["Factor"] = fact1["Value"].values / fact2["Value"].values
    # Quitamos los posibles valores infinitos y los substituimos por NaN. Despues ordenamos de mayor a menor asegurandonos de dejar los NaN en última posición
    fact2 = fact2.replace([np.inf, -np.inf], np.nan)
    fact2 = fact2.sort_values(by="Factor", ascending=False, na_position="last")
    fact2 = fact2[fact2["Value"] > 1000] # Aquí determinamos el mínimo para incluir en el estudio
    fig1 = px.bar(fact2.head(10), x="Area", y="Factor",
        title= "<b>Export performance factor ranking after EURO arrival</b>",
        color = "Factor",
        labels= {"Area": "Country (no continents or groups)",
                "Factor": "EPF"})   
    fig1.write_image("figures/factor_ranking_postEuro.png")
factor_of_export_general_by_amount(year=2005, item="Oil, olive, virgin")

def principal_exporters(year, item):
    """
    PRE EURO
    """
    filter1 = data[data.Item == item]
    filter1 = filter1[filter1.Element == "Export Value"]
    filter1 = filter1[filter1.Year == year]
    fig1 = px.bar(filter1.sort_values(by="Value", ascending=False).head(10), x="Area", y="Value",
        title= "<b>Ranking of principal exporters before EURO arrival</b>",
        color = "Value",
        labels= {"Area": "Country (no continents or groups)",
        "Value": "1.000$ per year"}
        )
    fig1.write_image("figures/export_ranking_bar_preEuro.png")
principal_exporters(year=1999, item= "Oil, olive, virgin")

def principal_exporters_pie(year, item):
    filter1 = data[data.Item == item]
    filter1 = filter1[filter1.Element == "Export Quantity"]
    filter1 = filter1[filter1.Year == year]
    fig1 = px.pie(filter1.sort_values(by="Value", ascending=False).head(10),values="Value",names="Area",color="Area",title="<b>Principal exporters of virgin olive oil before EURO arrival</b>")
    fig1.write_image("figures/export_ranking_pie_preEuro.png")

principal_exporters_pie(year=1999, item= "Oil, olive, virgin")

def principal_exporters(year, item):
    """
    POST EURO
    """
    filter1 = data[data.Item == item]
    filter1 = filter1[filter1.Element == "Export Value"]
    filter1 = filter1[filter1.Year == year]
    fig1 = px.bar(filter1.sort_values(by="Value", ascending=False).head(10), x="Area", y="Value",
        title= "<b>Ranking of principal exporters after EURO arrival</b>",
        color = "Value",
        labels= {"Area": "Country (no continents or groups)",
        "Value": "1.000$ per year"}
        )
    fig1.write_image("figures/export_ranking_bar_postEuro.png")
principal_exporters(year=2005, item= "Oil, olive, virgin")

def principal_exporters_pie(year, item):
    filter1 = data[data.Item == item]
    filter1 = filter1[filter1.Element == "Export Quantity"]
    filter1 = filter1[filter1.Year == year]
    fig1 = px.pie(filter1.sort_values(by="Value", ascending=False).head(10),values="Value",names="Area",color="Area",title="<b>Principal exporters of virgin olive oil after EURO arrival</b>")
    fig1.write_image("figures/export_ranking_pie_postEuro.png")

principal_exporters_pie(year=2005, item= "Oil, olive, virgin")