---
title: FUSE_STATISTIC (Lakehouse v1)
description: FUSE_STATISTIC — retorna o número estimado de valores distintos de cada coluna de uma tabela.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-statistic.md
---

Retorna o número estimado de valores distintos de cada coluna de uma tabela.


## Sintaxe SQL

```sql
FUSE_STATISTIC('<database_name>', '<table_name>')
```

## Exemplos de SQL

Você provavelmente usará essa função junto com `ANALYZE TABLE <table_name>` para gerar e consultar as informações estatísticas de uma tabela. Para mais explicações e exemplos, consulte OPTIMIZE TABLE.
