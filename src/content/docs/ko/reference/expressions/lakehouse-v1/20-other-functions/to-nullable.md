---
title: TO_NULLABLE (Lakehouse v1)
description: TO_NULLABLE — 값을 해당하는 nullable 값으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/to-nullable.md
---

값을 해당하는 nullable 값으로 변환합니다.

이 함수를 값에 적용하면 해당 값이 이미 NULL 값을 가질 수 있는지 확인합니다. 값이 이미 NULL 값을 가질 수 있으면 함수는 아무 변경 없이 값을 그대로 반환합니다.

하지만 값이 NULL 값을 가질 수 없으면 TO_NULLABLE 함수는 값이 NULL 값을 가질 수 있도록 수정합니다. 이를 위해 NULL 값을 담을 수 있는 구조로 값을 감싸며, 이후 해당 값이 NULL 값을 가질 수 있게 됩니다.

## Analyze 구문

```python
func.to_nullable(x);
```

## Analyze 예제

```python
func.typeof(3), func.to_nullable(3), func.typeof(func.to_nullable(3))

func.typeof(3)   | func.to_nullable(3) | func.typeof(func.to_nullable(3)) |
-----------------+---------------------+----------------------------------+
TINYINT UNSIGNED |                   3 | TINYINT UNSIGNED NULL            |

```

## SQL 구문

```sql
TO_NULLABLE(x);
```

## 인수

| 인수 | 설명 |
|-----------|----------------------------|
| x         | 원래 값입니다.        |


## 반환 유형

입력 값과 같은 데이터 유형의 값을 반환하되, 입력 값이 아직 nullable이 아니면 nullable 컨테이너로 감싸서 반환합니다.

## SQL 예제

```sql
SELECT typeof(3), TO_NULLABLE(3), typeof(TO_NULLABLE(3));

typeof(3)       |to_nullable(3)|typeof(to_nullable(3))|
----------------+--------------+----------------------+
TINYINT UNSIGNED|             3|TINYINT UNSIGNED NULL |

```
