---
title: SHA (Lakehouse v1)
description: SHA berechnet eine 160-Bit-SHA-1-Prüfsumme für die Zeichenfolge, wie in RFC 3174 (Secure Hash Algorithm) beschrieben.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/sha.md
---

Berechnet eine 160-Bit-SHA-1-Prüfsumme für die Zeichenfolge, wie in RFC 3174 (Secure Hash Algorithm) beschrieben. Der Wert wird als Zeichenfolge aus 40 Hexadezimalziffern zurückgegeben oder als NULL, wenn das Argument NULL war.

## Analyze-Syntax

```python
func.sha(<expr>)
```

## Analyze-Beispiele

```python
func.sha('1234567890')

┌──────────────────────────────────────────┐
│ func.sha('1234567890')                   │
├──────────────────────────────────────────┤
│ 01b307acba4f54f55aafc33bb06bbbf6ca803e9a │
└──────────────────────────────────────────┘
```

## SQL-Syntax

```sql
SHA(<expr>)
```

## Aliasse

- [SHA1](../sha1)

## SQL-Beispiele

```sql
SELECT SHA('1234567890'), SHA1('1234567890');

┌─────────────────────────────────────────────────────────────────────────────────────┐
│             sha('1234567890')            │            sha1('1234567890')            │
├──────────────────────────────────────────┼──────────────────────────────────────────┤
│ 01b307acba4f54f55aafc33bb06bbbf6ca803e9a │ 01b307acba4f54f55aafc33bb06bbbf6ca803e9a │
└─────────────────────────────────────────────────────────────────────────────────────┘
```
