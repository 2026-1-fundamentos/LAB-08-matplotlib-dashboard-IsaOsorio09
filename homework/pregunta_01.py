# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import webbrowser

def load_data(data_path):
    """
    Load the shipping data from the CSV file.
    """
    return pd.read_csv(data_path)

def create_visual_shipping_per_warehouse(df, docs_path):
    """
    Create a bar chart showing the number of shipments per warehouse block.
    """
    plt.figure(figsize=(10, 6))
    df['Warehouse_block'].value_counts().plot(kind='bar', color='tab:blue', fontsize=8)
    plt.title('Number of Shipments per Warehouse Block')
    plt.xlabel('Warehouse Block')
    plt.ylabel('Record Count')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig(docs_path / 'shipping_per_warehouse.png')
    plt.close()

def create_visual_for_shipping_mode(df, docs_path):
    """
    Create a bar chart showing the number of shipments per mode of shipment.
    """
    plt.figure(figsize=(10, 6))
    df['Mode_of_Shipment'].value_counts().plot(kind='pie', colors=['tab:blue', 'tab:orange', 'tab:green'], wedgeprops=dict(width=0.35))
    plt.title('Mode of Shipment')
    plt.ylabel('')  # Hide the y-label for pie chart
    plt.savefig(docs_path / 'mode_of_shipment.png')
    plt.close()

def create_visual_for_average_customer_rating(df, docs_path):
    df = df.copy()
    df = (df[['Mode_of_Shipment', 'Customer_rating']].groupby('Mode_of_Shipment').describe())
    df.columns = df.columns.droplevel()
    df = df[['mean', 'max', 'min']]
    plt.figure(figsize=(10, 6))
    plt.barh(y=df.index.values, width=df['max'].values-1, left=df['min'].values, color='lightgray', alpha=0.8, height=0.9)
    plt.title('Average Customer Rating')
    colors = ['tab:green' if x > 3 else 'tab:orange' for x in df['mean'].values]
    plt.barh(y=df.index.values, width=df['mean'].values-1, left=df['min'].values, color=colors, alpha=1, height=0.5)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_color('gray')
    plt.gca().spines['bottom'].set_color('gray') 
    plt.savefig(docs_path / 'average_customer_rating.png')
    plt.close()

def create_visual_for_weight_distribution(df, docs_path):
    """
    Create a histogram showing the distribution of weights in grams.
    """
    plt.figure(figsize=(10, 6))
    df['Weight_in_gms'].plot(kind='hist', color='tab:orange', edgecolor='white')
    plt.title('Shipped Weights Distribution')
    plt.xlabel('Weight (gms)')
    plt.ylabel('Frequency')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig(docs_path / 'weight_distribution.png')
    plt.close()

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`., files input

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    data_path = Path(__file__).parent.parent / "files" / "input" / "shipping-data.csv"
    docs_path = Path(__file__).parent.parent / "docs"

    # Create the docs directory if it doesn't exist
    docs_path.mkdir(exist_ok=True)
    df = load_data(data_path)

    create_visual_shipping_per_warehouse(df, docs_path)
    create_visual_for_shipping_mode(df, docs_path)
    create_visual_for_average_customer_rating(df, docs_path)
    create_visual_for_weight_distribution(df, docs_path)
    webbrowser.open((docs_path / 'index.html').as_uri())  # Open the index.html file in the default web browser
    return df

if __name__ == "__main__":
    df = pregunta_01()
    print(df.head())