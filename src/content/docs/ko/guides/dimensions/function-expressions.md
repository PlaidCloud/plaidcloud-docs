---
title: 식 및 집계를 위한 차원 함수
description: PlaidCloud 차원에서 함수 식을 사용하여 계산된 값, 조건부 논리, 동적 멤버 속성을 정의합니다.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dimensions/function-expressions.md
---

## 차원 계층 식에서 사용하는 함수

차원 계층 화면에서는 '집계'와 '식'을 추가할 수 있습니다. 각각에 대한 설명은 아래와 같습니다.

## 집계
집계는 테이블의 집계된 값을 표시하는 데 사용합니다('Sum', 'Count', 'Min', 'Max' 중 하나).
다음 이미지는 계층의 각 '기간'에 대한 값을 표시할 수 있도록 '라인 항목 값' 테이블에서 값을 가져오도록 구성한 집계를 보여 줍니다.

![차원 로드](/images/dimensions/expressions/dimension_expressions_1_agg.png)

집계를 필터링하면 필터와 일치하는 항목만 표시됩니다. 다음 이미지에서는 '계정' 차원에서 선택한 항목의 값을 표시하도록 집계를 설정했습니다.

![차원 로드](/images/dimensions/expressions/dimension_expressions_2_agg.png)

이러한 필터를 비워 두면 다음 이미지와 같이 화면 맨 위의 차원 필터 표시줄로 데이터를 필터링할 수 있습니다.

![차원 로드](/images/dimensions/expressions/dimension_expressions_3_agg.png)

## 식

식을 사용하면 차원에 표시된 집계 값을 기반으로 계산된 값을 표시할 수 있습니다.
식은 다양한 종류의 연산자와 몇 가지 특수 함수를 포함할 수 있는 수학 공식으로 작성합니다. [연산자 목록](https://mathjs.org/docs/expressions/syntax.html)을 참조하십시오. 사용할 수 있는 함수는 아래에 설명되어 있습니다.


## 함수
### Column(`<column_name>`)
현재 행/노드에서 이름이 지정된 열의 값을 가져옵니다.

아래는 라인 항목 값에 2를 곱한 결과를 표시하도록 식을 정의한 예입니다.

![차원 로드](/images/dimensions/expressions/dimension_expressions_4_func_column.png)


![차원 로드](/images/dimensions/expressions/dimension_expressions_5_func_column.png)

### Childcount()

현재 행/노드의 하위 노드 수를 반환합니다. 현재 행/노드가 리프 항목이면 0을 반환합니다.

다음 예에서는 상위 노드의 하위 노드에 대한 평균값을 반환하는 데 사용합니다.

![차원 로드](/images/dimensions/expressions/dimension_expressions_6_func_childcount.png)

![차원 로드](/images/dimensions/expressions/dimension_expressions_7_func_childcount.png)

### Leafcount()
현재 행/노드에 대해 트리에서 찾은 리프 항목 수를 반환합니다. 현재 행/노드가 리프 항목이면 1을 반환합니다.

![차원 로드](/images/dimensions/expressions/dimension_expressions_8_func_leafcount.png)

### Descendantcount()
현재 행/노드에 대해 트리에서 찾은 전체 항목 수를 반환합니다. 현재 행/노드가 리프 항목이면 0을 반환합니다.

![차원 로드](/images/dimensions/expressions/dimension_expressions_9_func_desccount.png)


### Siblingcount()
현재 행/노드의 형제 항목 수를 반환합니다. 반환되는 값에는 현재 노드가 포함됩니다.

![차원 로드](/images/dimensions/expressions/dimension_expressions_10_func_siblingcount.png)


### Nodevalue("`<node_name>`","`<column_name>`")
이름이 지정된 노드에서 이름이 지정된 열의 값을 반환합니다.
다음은 각 행/노드가 "LIV" 합계에서 차지하는 비율을 표시하는 데 사용하는 예입니다.

![차원 로드](/images/dimensions/expressions/dimension_expressions_11_func_nodevalue.png)

![차원 로드](/images/dimensions/expressions/dimension_expressions_12_func_nodevalue.png)


### Parentvalue("<column_name")
현재 노드의 상위 노드에서 지정된 열의 값을 반환합니다.
이 예는 상위 노드의 값 중 하위 노드가 사용하는 비율을 보여 줍니다.

![차원 로드](/images/dimensions/expressions/dimension_expressions_13_func_parentvalue.png)

![차원 로드](/images/dimensions/expressions/dimension_expressions_14_func_parentvalue.png)

### Columntextcompare("<column_name", "`<text>`")

이름이 지정된 열의 텍스트가 제공된 값보다 큰지, 작은지, 같은지를 나타내는 숫자 결과를 반환합니다.

열의 텍스트가 제공된 텍스트와 같으면 이 함수는 0을 반환합니다.

열의 텍스트가 제공된 텍스트보다 작으면 이 함수는 -1을 반환합니다.

열의 텍스트가 제공된 텍스트보다 크면 이 함수는 0을 반환합니다.


다음 예에서는 기간 이름을 "Jun"과 비교합니다.


![차원 로드](/images/dimensions/expressions/dimension_expressions_15_func_textcompare.png)

![차원 로드](/images/dimensions/expressions/dimension_expressions_16_func_textcompare.png)


## 조건식
위에 나온 예는 비교적 단순합니다. 식 안에서 조건문을 사용하면 더 복잡한 식을 만들 수 있습니다.
식 안에서 조건문은 다음 형식을 취합니다.
`<condition>` ? `<value_if_true>` : `<value_if_false>`
예: '12 > 6 ? 1000: 0'

조건문과 함수를 모두 포함한 식을 조합하면 더 복잡한 식을 만들 수 있습니다. 다음 예에서는 월이 "Jun"이면 라인 항목 값에 100,000을 더합니다.

![차원 로드](/images/dimensions/expressions/dimension_expressions_17_cond.png)

![차원 로드](/images/dimensions/expressions/dimension_expressions_18_cond.png)


## 또 다른 예: 간단한 배부

이 예는 리프 노드의 리소스 드라이버 값을 사용하여 상위 노드의 라인 항목 값 중 소비된 금액을 보여 줍니다.

![차원 로드](/images/dimensions/expressions/dimension_expressions_19_alloc.png)

![차원 로드](/images/dimensions/expressions/dimension_expressions_20_alloc.png)

## 제한 사항:
현재는 다른 식의 값을 기반으로 하는 식을 만들 수 없습니다. 식은 집계의 값만 사용하여 만들 수 있습니다.
