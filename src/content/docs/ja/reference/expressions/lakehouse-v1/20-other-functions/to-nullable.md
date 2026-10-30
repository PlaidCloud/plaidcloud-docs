---
title: TO_NULLABLE（Lakehouse v1）
description: TO_NULLABLE — 値を、NULLを保持できる同等の値に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/to-nullable.md
---

値を、NULLを保持できる同等の値に変換します。

この関数を値に適用すると、その値がすでにNULL値を保持できるかどうかを確認します。値がすでにNULL値を保持できる場合、関数は何も変更せずにその値を返します。

一方、値がNULL値を保持できない場合、TO_NULLABLE関数は、その値がNULL値を保持できるように変更します。これは、NULL値を保持できる構造で値をラップすることで行われます。その結果、その値は以降NULL値を保持できるようになります。

## Analyzeの構文

```python
func.to_nullable(x);
```

## Analyzeの例

```python
func.typeof(3), func.to_nullable(3), func.typeof(func.to_nullable(3))

func.typeof(3)   | func.to_nullable(3) | func.typeof(func.to_nullable(3)) |
-----------------+---------------------+----------------------------------+
TINYINT UNSIGNED |                   3 | TINYINT UNSIGNED NULL            |

```

## SQLの構文

```sql
TO_NULLABLE(x);
```

## 引数

| 引数 | 説明                |
|-----------|----------------------------|
| x         | 元の値。        |


## 戻り値の型

入力値と同じデータ型の値を返します。入力値がまだNULLを保持できない場合は、NULLを保持できるコンテナーでラップされます。

## SQLの例

```sql
SELECT typeof(3), TO_NULLABLE(3), typeof(TO_NULLABLE(3));

typeof(3)       |to_nullable(3)|typeof(to_nullable(3))|
----------------+--------------+----------------------+
TINYINT UNSIGNED|             3|TINYINT UNSIGNED NULL |

```
