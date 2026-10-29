---
title: 대용량 버전 이력 테이블에서 최신 레코드 선택
description: 최적화된 쿼리 기법을 사용하여 PlaidCloud의 대용량 이력 테이블에서 최신 레코드를 효율적으로 선택하는 방법을 알아봅니다.
sidebar:
  label: 대용량 버전 이력 테이블에서 최신 레코드 선택
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/selecting-latest-record-in-large-history-table.md
---

## 과제

각 레코드의 버전이 여러 개 들어 있는 테이블이 있으며, 그중 최신 버전을 사용해야 합니다.

## 논의

이 문제는 ID와 최대 업데이트 날짜(MAX)를 임시 테이블에 선택한 다음, 그 임시 테이블을 이력 테이블에 INNER JOIN하여 결과를 얻는 방식으로 해결할 수 있습니다. 하지만 이 방법은 두 단계가 필요하고, 최신 업데이트를 찾는 것 외에는 아무 기능도 없는 중간 테이블을 저장해야 합니다.

이 작업을 단일 쿼리로 수행하는 더 우아한 해결 방법은 정렬이 포함된 윈도 함수와 필터를 사용하는 것입니다.

## 해결 방법

### 버전 이력 테이블

| employee_id | department | salary    | update_date  |
|-------------|------------|-----------|--------------|
| 3           | IT         | 90000     | 2024-09-17   |
| 2           | HR         | 85000     | 2024-09-17   |
| 5           | HR         | 82000     | 2024-09-17   |
| 3           | IT         | 77000     | 2023-10-01   |
| 3           | IT         | 75000     | 2022-10-04   |
| 5           | IT         | 72000     | 2024-07-12   |
| 2           | IT         | 67000     | 2024-03-18   |
| 1           | Sales      | 62000     | 2022-02-28   |
| 5           | Sales      | 60000     | 2023-01-14   |
| 4           | Sales      | 58000     | 2021-11-19   |

### 단계 설정
추출 단계에서 `Rank`라는 열에 다음과 같은 윈도 함수 식을 만듭니다.

```python
func.rank().over(order_by=table.updated_date.desc(), partition_by=table.employee_id)
```

추출 단계의 필터 탭에서 다음과 같은 필터를 설정합니다.

```python
table.Rank == 1
```

### 결과

| employee_id | department | salary    | update_date  | Rank |
|-------------|------------|-----------|--------------|------|
| 3           | IT         | 90000     | 2024-09-17   | 1    |
| 2           | HR         | 85000     | 2024-09-17   | 1    |
| 5           | HR         | 82000     | 2024-09-17   | 1    |
| 1           | Sales      | 62000     | 2022-02-28   | 1    |
| 4           | Sales      | 58000     | 2021-11-19   | 1    |

이 방식은 매우 효율적이며, 여러 버전이 있는 이력 테이블에서 최신 레코드를 한 단계로 선택할 수 있습니다. `employee_id` 그룹 내에서 각 레코드를 `update_date` 기준으로 순위를 매긴 다음 첫 번째 레코드만 선택하는 방식으로 동작합니다.

고유 행 키가 여러 열로 구성된다면 다음과 같이 `partition_by` 인수에 목록으로 추가할 수 있습니다.

```python
partition_by=[table.first_column, table.second_column, table.third_column]
```

여러 열로 정렬해야 한다면 마찬가지로 열 목록으로 적용할 수 있습니다.

```python
order_by=[table.first_column.desc(), table.second_column, table.third_column.desc()]
```
