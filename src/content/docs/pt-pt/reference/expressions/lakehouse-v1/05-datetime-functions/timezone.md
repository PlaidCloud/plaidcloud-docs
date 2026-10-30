---
title: TIMEZONE (Lakehouse v1)
description: TIMEZONE — devolve o fuso horário da ligação atual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/timezone.md
---

Devolve o fuso horário da ligação atual. 

O PlaidCloud Lakehouse usa UTC (Tempo Universal Coordenado) como fuso horário predefinido e permite-lhe alterar o fuso horário para a sua localização geográfica atual. Para consultar os valores disponíveis que pode atribuir à definição `timezone`, consulte https://docs.rs/chrono-tz/latest/chrono_tz/enum.Tz.html. Veja os exemplos abaixo para mais detalhes.

## Sintaxe do Analyze

```python
func.timezone()
```

## Exemplos do Analyze

```python
func.timezone()
┌─────────────────────┐
│ timezone            │
├─────────────────────┤
│ UTC                 │
└─────────────────────┘
```

## Sintaxe SQL

```sql
SELECT TIMEZONE();
```

## Exemplos SQL

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
