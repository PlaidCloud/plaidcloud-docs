---
title: FUSE_STATISTIC (Lakehouse v1)
description: FUSE_STATISTIC — zwraca szacowaną liczbę unikatowych wartości każdej kolumny tabeli.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-statistic.md
---

Zwraca szacowaną liczbę unikatowych wartości każdej kolumny tabeli.


## Składnia SQL

```sql
FUSE_STATISTIC('<database_name>', '<table_name>')
```

## Przykłady SQL

Najczęściej użyjesz tej funkcji razem z `ANALYZE TABLE <table_name>`, aby wygenerować i sprawdzić informacje statystyczne tabeli. Więcej wyjaśnień i przykładów znajdziesz w opisie OPTIMIZE TABLE.
