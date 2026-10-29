---
title: Dimension Create 단계
description: PlaidCloud 워크플로 단계에서 새 계층형 차원을 만들어 데이터 분류 체계를 구성합니다.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-create.md
---

## 설명
로드하고 사용할 차원을 만듭니다.


![Dimension Create](/images/dimension_create.png)

## 만들 차원
### 이름
만들 차원에 특정 이름을 사용하거나 변수를 포함하여 동적으로 이름을 지정할 수 있습니다.


차원을 주기적으로 업데이트하면서 과거 보기를 유지하려는 경우 변수가 유용합니다.

`current_month` 변수를 사용하여 차원 이름을 동적으로 지정하는 예제:

```text
dimension_name_{current_month}
```
### 경로
경로를 사용하면 차원이 저장되는 폴더 구조를 만들 수 있습니다. 여기에도 변수를 사용하여 폴더 구조를 동적으로 만들 수 있습니다.
`current_month` 변수를 사용하여 폴더 이름을 동적으로 지정하는 예제:

```text
/Dimensions/{current_month}/Product/
```

### 메모
메모 필드는 의견이나 참고 사항을 저장하는 데 사용합니다.
