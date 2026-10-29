---
title: Pronóstico
description: Genere pronósticos de series temporales a partir de una tabla de proyecto y escriba los valores previstos en una tabla de salida.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/forecast.md
---

## Descripción

El paso **Pronóstico** lee una serie temporal de una tabla de entrada, ajusta un modelo de pronóstico y escribe los valores futuros previstos en una tabla de salida. Úselo cuando tenga valores históricos por fecha y quiera que el flujo de trabajo genere un pronóstico repetible.

## Configuración

### Parámetros de pronóstico

* **Tabla de entrada** *(obligatorio)*: la tabla que contiene la serie temporal histórica.
* **Tabla de salida** *(obligatorio)*: la tabla en la que se escriben las filas del pronóstico.
* **Columna de fecha** *(obligatorio)*: la columna de destino asignada que contiene la fecha o la marca de tiempo de cada observación. El valor predeterminado es `ds`.
* **Columna de valor** *(obligatorio)*: la columna de destino asignada que contiene el valor numérico que se pronosticará.
* **Columnas de serie** *(opcional)*: columnas de destino asignadas que identifican series distintas dentro de la misma tabla, como cliente, producto, región o cuenta.
* **Frecuencia**: `Auto`, `Hourly`, `Daily`, `Weekly`, `Monthly` o `Quarterly`. Use una frecuencia explícita cuando las fechas de entrada sean dispersas o irregulares.
* **Horizonte**: número de períodos futuros que se pronosticarán. El valor predeterminado es 12.
* **Modelo**: `Automatic` de forma predeterminada. También puede seleccionar `AutoETS`, `AutoARIMA`, `Seasonal Naive`, `Naive` o `AutoTheta`.

### Selección de datos de la tabla

Use la pestaña de selección de datos de la tabla para dar forma a la tabla de entrada antes de pronosticar. Las columnas de destino asignadas deben incluir la **Columna de fecha**, la **Columna de valor** y cualquier **Columna de serie**.

Use **Inspeccionar origen** para rellenar la asignación a partir de la tabla de entrada seleccionada. Puede rellenar ambos lados de la asignación, solo el lado de origen o solo el lado de destino antes de ajustar las columnas.

No se permite guardar hasta que la asignación tenga columnas de origen (*Source columns are required: use Populate to read them from the input table.*) ni mientras sus columnas de destino omitan la **Columna de fecha**, la **Columna de valor** o una **Columna de serie**.

### Filtros de datos

Use la pestaña de filtros para limitar las filas, aplicar condiciones, agregar los datos de entrada o segmentar el resultado antes de que se ejecute el pronóstico.

## Comportamiento

El paso crea o actualiza la tabla de salida configurada con las filas del pronóstico para el horizonte seleccionado. Cuando configura **Columnas de serie**, PlaidCloud pronostica cada serie por separado e incluye los valores de la serie en la salida.

## Modelos ARIMA, ajuste y diagnósticos

La sección **Configuración del modelo** tiene estos campos:

* **Modelo** (`forecast_model`): además de los modelos anteriores (`automatic`, `auto_ets`, `auto_arima`, `seasonal_naive`, `naive`, `auto_theta`), **ARIMA**, **ARIMA estacional (SARIMA)** y **ARIMA estacional con regresores (SARIMAX)** (`arima`, `sarima`, `sarimax`) ajustan el orden que usted indique, mediante **Orden ARIMA (p, d, q)** (`order`) es `[p, d, q]`, **Orden estacional (P, D, Q, m)** (`seasonal_order`) es `[P, D, Q, s]` (`sarima`, `sarimax`), y **Columnas de regresores** (`exog_columns`) nombra las columnas de regresores exógenos (`sarimax`).
* **Modo** (`mode`): `forecast` (predeterminado) escribe el pronóstico de cada serie. `fit` ajusta una serie con `arima`, `sarima` o `sarimax` y escribe el modelo como una tabla. `apply` escribe los pronósticos de la tabla de modelo indicada en **Tabla del modelo** (`model_frame`); para un modelo `sarimax`, la tabla de entrada contiene los regresores futuros.
* **Ajustar el logaritmo de los valores** (`log_transform`): ajusta sobre el logaritmo natural de los valores. Con `apply`, indica si los pronósticos se devuelven desde la escala logarítmica.
* **Escribir diagnósticos en su lugar** (`diagnostics`): escribe una tabla en lugar de un pronóstico: `residuals` o `coefficients` del modelo de `model_frame`, `autocorrelation` (ACF y PACF) o `residual_stats` de la columna de valor de entrada, o `ljung_box`, el estadístico Q y el valor p para cada retardo de los residuos del modelo o, si no hay modelo, de la columna de valor de entrada. **Retardo máximo** (`max_lag`, predeterminado 40) es el mayor retardo para `autocorrelation` y `ljung_box`, y **Pronosticar de forma dinámica (realimentar las predicciones)** (`dynamic`) hace que `residuals` use la predicción dinámica dentro de la muestra.
* **Nodo de series temporales de KNIME** (`knime_config`): ejecuta un nodo de preparación de series temporales de KNIME en lugar de un pronóstico: `aggregate_granularity` agrega los valores a un año, trimestre, mes, semana, día, hora, minuto o segundo, y `align_timestamps` los alinea a un período.

Un asistente de IA o la API REST también puede establecer `interval_levels`, los niveles de los intervalos de predicción; `95` es el único nivel.

## Recursos

El procesamiento del pronóstico se ejecuta en un trabajo independiente. Habilite la **Administración avanzada de recursos** solo cuando el pronóstico necesite más CPU o memoria que la solicitud predeterminada. Aumentar las solicitudes de recursos puede retrasar el inicio de los pronósticos mientras se programa la capacidad. Establezca con ella `cpu` (de 1 a 7, predeterminado 1) y `memory` (de 8 a 56 GiB, predeterminado 8).
