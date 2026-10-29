---
title: TIMEZONE (Lakehouse v1)
description: TIMEZONE — devuelve la zona horaria de la conexión actual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/timezone.md
---

Devuelve la zona horaria de la conexión actual. 

PlaidCloud Lakehouse usa UTC (hora universal coordinada) como zona horaria predeterminada y le permite cambiarla a su ubicación geográfica actual. Para consultar los valores disponibles que puede asignar a la configuración `timezone`, consulte https://docs.rs/chrono-tz/latest/chrono_tz/enum.Tz.html. Vea los ejemplos a continuación para más detalles.

## Sintaxis de Analyze

```python
func.timezone()
```

## Ejemplos de Analyze

```python
func.timezone()
┌─────────────────────┐
│ timezone            │
├─────────────────────┤
│ UTC                 │
└─────────────────────┘
```

## Sintaxis de SQL

```sql
SELECT TIMEZONE();
```

## Ejemplos de SQL

```sql
-- Return the current timezone
SELECT TIMEZONE();
┌─────────────────┐
│ TIMEZONE('UTC') │
├─────────────────┤
│ UTC             │
└─────────────────┘

-- Set the timezone to China Standard Time
SET timezone='Asia/Shanghai';

SELECT TIMEZONE();
┌───────────────────────────┐
│ TIMEZONE('Asia/Shanghai') │
├───────────────────────────┤
│ Asia/Shanghai             │
└───────────────────────────┘
```
