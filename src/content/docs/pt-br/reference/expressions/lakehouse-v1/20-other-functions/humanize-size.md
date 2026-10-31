---
title: HUMANIZE_SIZE (Lakehouse v1)
description: HUMANIZE_SIZE — retorna o tamanho legível com um sufixo (KiB, MiB etc.).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/humanize-size.md
---

Retorna o tamanho legível com um sufixo (KiB, MiB etc.).

## Sintaxe no Analyze

```python
func.humanize_size(x);
```

## Exemplos no Analyze

```python
func.humanize_size(1024 * 1024)
┌────────────────────────────────────────┐
│ func.func.humanize_size((1024 * 1024)) │
├────────────────────────────────────────┤
│ 1 MiB                                  │
└────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
HUMANIZE_SIZE(x);
```

## Argumentos

| Argumentos | Descrição                  |
|-----------|----------------------------|
| x         | O tamanho numérico.        |


## Tipo de retorno

String.

## Exemplos de SQL

```sql
SELECT HUMANIZE_SIZE(1024 * 1024)
┌─────────────────────────┐
│ HUMANIZE_SIZE((1024 * 1024)) │
├─────────────────────────┤
│ 1 MiB                    │
└─────────────────────────┘
```
