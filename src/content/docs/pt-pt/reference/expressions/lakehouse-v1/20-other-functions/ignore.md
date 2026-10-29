---
title: IGNORE (Lakehouse v1)
description: IGNORE — ao utilizar a instrução insert ignore, as linhas com dados inválidos que causam o erro são ignoradas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/ignore.md
---

Ao utilizar a instrução insert ignore, as linhas com dados inválidos que causam o erro são ignoradas e as linhas com dados válidos são inseridas na tabela.

## Sintaxe SQL

```sql
INSERT ignore INTO TABLE(column_list)
VALUES( value_list),
      ( value_list),
      ...
```
