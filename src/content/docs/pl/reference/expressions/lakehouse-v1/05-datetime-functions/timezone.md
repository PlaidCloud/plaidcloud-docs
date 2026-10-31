---
title: TIMEZONE (Lakehouse v1)
description: TIMEZONE — zwraca strefę czasową bieżącego połączenia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/timezone.md
---

Zwraca strefę czasową bieżącego połączenia. 

PlaidCloud Lakehouse domyślnie używa czasu UTC (uniwersalny czas koordynowany) jako strefy czasowej i pozwala zmienić ją na odpowiednią dla Twojej lokalizacji geograficznej. Dostępne wartości, które można przypisać do ustawienia `timezone`, znajdziesz pod adresem https://docs.rs/chrono-tz/latest/chrono_tz/enum.Tz.html. Szczegóły zawierają poniższe przykłady.

## Składnia Analyze

```python
func.timezone()
```

## Przykłady Analyze

```python
func.timezone()
┌─────────────────────┐
│ timezone            │
├─────────────────────┤
│ UTC                 │
└─────────────────────┘
```

## Składnia SQL

```sql
SELECT TIMEZONE();
```

## Przykłady SQL

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
