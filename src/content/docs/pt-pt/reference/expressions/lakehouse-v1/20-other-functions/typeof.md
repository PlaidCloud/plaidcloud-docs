---
title: TYPEOF (Lakehouse v1)
description: TYPEOF — a função TYPEOF é utilizada para devolver o nome de um tipo de dados.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/typeof.md
---

A função TYPEOF é utilizada para devolver o nome de um tipo de dados.

## Sintaxe do Analyze

```python
func.typeof( <expr> )
```

## Exemplos do Analyze

```python
func.typeof(1)
┌──────────────────┐
│ func.typeof(1)   │
├──────────────────┤
│ INT              │
└──────────────────┘
```

## Sintaxe SQL

```sql
TYPEOF( <expr> )
```

## Argumentos

| Argumentos  | Descrição |
| ----------- | ----------- |
| `<expr>` | Qualquer expressão. <br /> Pode ser o nome de uma coluna, o resultado de outra função ou uma operação matemática.

## Tipo de retorno

Cadeia de caracteres

## Exemplos de SQL

```sql
SELECT typeof(1::INT);
┌──────────────────┐
│ typeof(1::Int32) │
├──────────────────┤
│ INT              │
└──────────────────┘
```
