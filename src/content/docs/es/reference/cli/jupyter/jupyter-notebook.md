---
title: Cuadernos de Jupyter
description: Ejecute Cuadernos de Jupyter en PlaidCloud para el análisis interactivo de datos, la visualización y los flujos de exploración de datos basados en Python.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/jupyter-notebook.md
---

Jupyter Notebook y Jupyter Lab ofrecen excelentes capacidades interactivas para analizar, explorar, explicar y reportar datos.  PlaidCloud permite usar la información directamente en los cuadernos.

PlaidCloud proporciona JupyterHub dentro de cada espacio de trabajo de inquilino si está activado para su uso.  La documentación siguiente ayuda a configurar Jupyter por separado en un equipo de escritorio o en un servidor independiente.

## Instalar Jupyter Notebook
Se da por hecho que ya tiene una instalación de Jupyter Notebook en funcionamiento.

### Instalación de un Jupyter Notebook independiente
Para obtener más información sobre cómo instalar un Jupyter Notebook localmente, consulte la [documentación de instalación de Jupyter](https://jupyter.org/install).

### Agregar a VS Code
VS Code también ofrece una extensión que permite ejecutar cuadernos directamente en VS Code.  Instale la extensión desde el [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)


## Instalar las utilidades de PlaidCloud
Aunque se puede acceder a PlaidCloud mediante solicitudes OAuth y JSON-RPC estándar, se recomienda usar nuestras bibliotecas prediseñadas para simplificar el acceso.  Además, la biblioteca de utilidades de PlaidCloud incluye prácticos ayudantes de datos para usar con los dataframes de Pandas.

Para instalar las utilidades de PlaidCloud, ejecute las siguientes instalaciones con pip:

```bash
pip install plaidcloud-rpc@git+https://github.com/PlaidCloud/plaid-rpc.git@v1.4.0#egg=plaidcloud-rpc
```

```bash
pip install plaidcloud-utilities@git+https://github.com/PlaidCloud/plaid-utilities.git@v1.5.2#egg=plaidcloud-utilities
```

## Obtención de un token OAuth

Consulte la [configuración de OAuth](/es/reference/cli/jupyter/oauth-setup/) para obtener más información sobre cómo obtener un token OAuth y cómo configurar el sistema para la autenticación automatizada.


## Abrir la interfaz de usuario de Jupyter Notebook

Inicie su servidor de cuadernos para comenzar.



Una vez que haya iniciado sesión en su servidor de Jupyter Notebook, cree un cuaderno nuevo desde la interfaz de usuario.

Se abrirá un cuaderno en blanco.



Cree una conexión para comunicarse con PlaidCloud a través de los endpoints de la API

```python
from plaidcloud.utilities.connect import PlaidConnection

conn = PlaidConnection()
```


Establezca un objeto de tabla local y luego consúltelo; los resultados se colocan automáticamente en un dataframe de [Pandas](https://pandas.pydata.org/).

```python
tbl_sf_cust_master = conn.get_table('Salesforce_Customer_Master') # This gets a table object
df_sf_cust_master = conn.get_data(tbl_sf_cust_master) # This retrieves all the data into a dataframe
```


Con ese mismo objeto de tabla también puede escribir consultas más avanzadas con la sintaxis estándar de SQLAlchemy.

```python
df_sf_cust_master_w_sales = conn.get_data(
    tbl_sf_cust_master.select().with_only_columns(
        [tbl_sf_cust_master.c.Id, tbl_sf_cust_master.c.CurrencyIsoCode, tbl_sf_cust_master.c.SyDSalesRegion]
    ).where(
        tbl_sf_cust_master.c.TotalSalesPast3Years > 0
    )
)
```
