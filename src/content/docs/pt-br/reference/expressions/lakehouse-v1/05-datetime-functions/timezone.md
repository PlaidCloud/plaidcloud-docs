---
title: TIMEZONE (Lakehouse v1)
description: TIMEZONE — retorna o fuso horário da conexão atual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/timezone.md
---

Retorna o fuso horário da conexão atual. 

O PlaidCloud Lakehouse usa UTC (Tempo Universal Coordenado) como fuso horário padrão e permite alterar o fuso horário para a sua localização geográfica atual. Para ver os valores disponíveis que você pode atribuir à configuração `timezone`, consulte https://docs.rs/chrono-tz/latest/chrono_tz/enum.Tz.html. Veja os exemplos a seguir para mais detalhes.

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

## Exemplos de SQL

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
