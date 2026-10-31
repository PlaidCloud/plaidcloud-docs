---
title: ANY (Lakehouse v1)
description: ANY — 집합에서 처음 만나는 NULL이 아닌 값을 반환합니다. 실행 순서가 달라지면 결과는 확정되지 않습니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/aggregate-any.md
---

집계 함수입니다.

ANY() 함수는 해당 열의 모든 행이 NULL인 경우를 제외하고, 처음 만나는 (NULL이 아닌) 값을 선택합니다. 쿼리는 어떤 순서로든 실행될 수 있고 실행할 때마다 순서가 달라질 수도 있으므로, 이 함수의 결과는 확정되지 않습니다. 확정된 결과를 얻으려면 'any' 대신 'min' 또는 'max' 함수를 사용하십시오.

## Analyze 구문

```python
func.any(<expr>)
```

## Analyze 예제

```python
func.any(table.product_name).alias('any_product_name')

| any_product_name |
|------------------|
| Laptop           |
```

## SQL 구문

```sql
ANY(<expr>)
```

## 인수

| 인수 | 설명 |
|-----------|----------------|
| `<expr>`  | 모든 식 |

## 반환 형식

처음 만나는 (NULL이 아닌) 값이며, 해당 값의 형식으로 반환됩니다. 모든 값이 NULL이면 반환 값은 NULL입니다.

## SQL 예제

**테이블을 만들고 샘플 데이터 삽입**
```sql
CREATE TABLE product_data (
  id INT,
  product_name VARCHAR NULL,
  price FLOAT NULL
);

INSERT INTO product_data (id, product_name, price)
VALUES (1, 'Laptop', 1000),
       (2, NULL, 800),
       (3, 'Keyboard', NULL),
       (4, 'Mouse', 25),
       (5, 'Monitor', 150);
```

**쿼리 데모: 처음 만나는 NULL이 아닌 제품 이름 가져오기**
```sql
SELECT ANY(product_name) AS any_product_name
FROM product_data;
```

**결과**
```sql
| any_product_name |
|------------------|
| Laptop           |
```
