---
title: STRCMP (Lakehouse v1)
description: STRCMP — 문자열이 같으면 0을, 첫 번째 인수가 두 번째보다 작으면 -1을, 그 외에는 1을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/strcmp.md
---

문자열이 같으면 0을, 첫 번째 인수가 두 번째보다 작으면 -1을, 그 외에는 1을 반환합니다.

## Analyze 구문

```python
func.strcmp(<expr1> ,<expr2>)
```

## Analyze 예제

```python
func.strcmp('text', 'text2')
┌──────────────────────────────┐
│ func.strcmp('text', 'text2') │
├──────────────────────────────┤
│                           -1 │
└──────────────────────────────┘

func.strcmp('text2', 'text')
┌──────────────────────────────┐
│ func.strcmp('text2', 'text') │
├──────────────────────────────┤
│                            1 │
└──────────────────────────────┘

func.strcmp('text', 'text')
┌──────────────────────────────┐
│ func.strcmp('text', 'text')  │
├──────────────────────────────┤
│                            0 │
└──────────────────────────────┘
```

## SQL 구문

```sql
STRCMP(<expr1> ,<expr2>)
```

## 인수

| 인수 | 설명 |
|-----------|-------------|
| `<expr1>` | 문자열입니다. |
| `<expr2>` | 문자열입니다. |

## 반환 형식

`BIGINT`

## SQL 예제

```sql
SELECT STRCMP('text', 'text2');
┌─────────────────────────┐
│ STRCMP('text', 'text2') │
├─────────────────────────┤
│                      -1 │
└─────────────────────────┘

SELECT STRCMP('text2', 'text');
┌─────────────────────────┐
│ STRCMP('text2', 'text') │
├─────────────────────────┤
│                       1 │
└─────────────────────────┘

SELECT STRCMP('text', 'text');
┌────────────────────────┐
│ STRCMP('text', 'text') │
├────────────────────────┤
│                      0 │
└────────────────────────┘
```
