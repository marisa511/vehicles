import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
# Crear una casilla de verificación para construir un histograma
hist_checkbox = st.checkbox('Construir histograma')

# Crear una casilla de verificación para construir un gráfico de dispersión
scatter_checkbox = st.checkbox('Construir gráfico de dispersión')

if hist_checkbox:  # Si se selecciona la casilla del histograma
    # Escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

if scatter_checkbox:  # Si se selecciona la casilla del gráfico de dispersión
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price",
                             title="Relación entre el odómetro y el precio")

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
