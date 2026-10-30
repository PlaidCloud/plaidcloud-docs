---
title: IGNORE (Lakehouse v1)
description: IGNORE — użycie instrukcji insert ignore powoduje pominięcie wierszy z nieprawidłowymi danymi, które powodują błąd.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/ignore.md
---

Użycie instrukcji insert ignore powoduje, że wiersze z nieprawidłowymi danymi, które powodują błąd, są pomijane, a wiersze z prawidłowymi danymi są wstawiane do tabeli.

## Składnia SQL

```sql
INSERT ignore INTO TABLE(column_list)
VALUES( value_list),
      ( value_list),
      ...
```
