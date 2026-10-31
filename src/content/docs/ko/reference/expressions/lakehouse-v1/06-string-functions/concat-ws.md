---
title: CONCAT_WS (Lakehouse v1)
description: CONCAT_WS — CONCAT_WS()는 구분자를 사용한 연결(Concatenate With Separator)을 의미하며 CONCAT()의 특수한 형태입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/concat-ws.md
---

CONCAT_WS()는 구분자를 사용한 연결(Concatenate With Separator)을 의미하며 CONCAT()의 특수한 형태입니다. 첫 번째 인수는 나머지 인수에 사용할 구분자입니다. 구분자는 연결할 문자열 사이에 추가됩니다. 구분자는 문자열일 수 있으며, 나머지 인수도 마찬가지입니다. 구분자가 NULL이면 결과는 NULL입니다.

CONCAT_WS()는 빈 문자열을 건너뛰지 않습니다. 그러나 구분자 인수 뒤에 오는 NULL 값은 건너뜁니다.

## Analyze 구문

```python
func.concat_ws(<separator>, <expr1>, ...)
```

## Analyze 예제

```python
func.concat_ws(',', 'data', 'fuse', 'labs', '2021')
┌─────────────────────────────────────────────────────┐
│ func.concat_ws(',', 'data', 'fuse', 'labs', '2021') │
├─────────────────────────────────────────────────────┤
│ data,fuse,labs,2021                                 │
└─────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
CONCAT_WS(<separator>, <expr1>, ...)
```

## 인수

| 인수 | 설명 |
|---------------| ------------- |
| `<separator>` | 문자열 열 |
| `<expr1>`     | 값 열  |

## 반환 형식

`VARCHAR` 데이터 형식 값 또는 `NULL` 데이터 형식입니다.

## SQL 예제

```sql
SELECT CONCAT_WS(',', 'data', 'fuse', 'labs', '2021');
┌────────────────────────────────────────────────┐
│ CONCAT_WS(',', 'data', 'fuse', 'labs', '2021') │
├────────────────────────────────────────────────┤
│ data,fuse,labs,2021                            │
└────────────────────────────────────────────────┘

SELECT CONCAT_WS(',', 'data', NULL, 'bend');
┌──────────────────────────────────────┐
│ CONCAT_WS(',', 'data', NULL, 'bend') │
├──────────────────────────────────────┤
│ data,bend                            │
└──────────────────────────────────────┘


SELECT CONCAT_WS(',', 'data', NULL, NULL, 'bend');
┌────────────────────────────────────────────┐
│ CONCAT_WS(',', 'data', NULL, NULL, 'bend') │
├────────────────────────────────────────────┤
│ data,bend                                  │
└────────────────────────────────────────────┘


SELECT CONCAT_WS(NULL, 'data', 'fuse', 'labs');
┌─────────────────────────────────────────┐
│ CONCAT_WS(NULL, 'data', 'fuse', 'labs') │
├─────────────────────────────────────────┤
│                                    NULL │
└─────────────────────────────────────────┘

SELECT CONCAT_WS(',', NULL);
┌──────────────────────┐
│ CONCAT_WS(',', NULL) │
├──────────────────────┤
│                      │
└──────────────────────┘
```
