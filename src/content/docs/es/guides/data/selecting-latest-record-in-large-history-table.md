---
title: Selección del registro más reciente en una tabla grande de historial de versiones
description: Aprenda a seleccionar de forma eficiente el registro más reciente de tablas de historial grandes en PlaidCloud mediante técnicas de consulta optimizadas.
sidebar:
  label: Selección del registro más reciente en una tabla grande de historial de versiones
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/selecting-latest-record-in-large-history-table.md
---

## Desafío

Dispone de una tabla que contiene muchas versiones de cada registro, pero debe usar la versión más reciente.

## Análisis

Este problema podría resolverse seleccionando el ID y la fecha de actualización máxima (MAX) en una tabla temporal. Después, esa tabla temporal podría combinarse mediante INNER JOIN con la tabla de historial para obtener el resultado. Por desgracia, esto requiere dos pasos y almacenar una tabla intermedia que no tiene otra función que encontrar la última actualización.

La solución más elegante para realizar esta operación en una sola consulta utiliza una función de ventana con ordenación más un filtro.

## Solución

### La tabla de historial de versiones

| employee_id | department | salary    | update_date  |
|-------------|------------|-----------|--------------|
| 3           | IT         | 90000     | 2024-09-17   |
| 2           | HR         | 85000     | 2024-09-17   |
| 5           | HR         | 82000     | 2024-09-17   |
| 3           | IT         | 77000     | 2023-10-01   |
| 3           | IT         | 75000     | 2022-10-04   |
| 5           | IT         | 72000     | 2024-07-12   |
| 2           | IT         | 67000     | 2024-03-18   |
| 1           | Sales      | 62000     | 2022-02-28   |
| 5           | Sales      | 60000     | 2023-01-14   |
| 4           | Sales      | 58000     | 2021-11-19   |

### Configuración del paso
Con un paso de extracción, cree una expresión de función de ventana en una columna llamada `Rank` como esta:

```python
func.rank().over(order_by=table.updated_date.desc(), partition_by=table.employee_id)
```

En la pestaña de filtro del paso Extract, establezca un filtro como este:

```python
table.Rank == 1
```

### El resultado

| employee_id | department | salary    | update_date  | Rank |
|-------------|------------|-----------|--------------|------|
| 3           | IT         | 90000     | 2024-09-17   | 1    |
| 2           | HR         | 85000     | 2024-09-17   | 1    |
| 5           | HR         | 82000     | 2024-09-17   | 1    |
| 1           | Sales      | 62000     | 2022-02-28   | 1    |
| 4           | Sales      | 58000     | 2021-11-19   | 1    |

Este enfoque es muy eficiente y permite seleccionar el registro más reciente de una tabla de historial con varias versiones en un solo paso. Funciona clasificando cada registro dentro del grupo `employee_id` según `update_date` y eligiendo después solo el primer registro.

Si la clave única de la fila se compone de varias columnas, puede agregarlas al argumento `partition_by` como una lista, así:

```python
partition_by=[table.first_column, table.second_column, table.third_column]
```

Si necesita aplicar ordenaciones por varias columnas, también puede hacerlo con una lista de columnas, así:

```python
order_by=[table.first_column.desc(), table.second_column, table.third_column.desc()]
```
