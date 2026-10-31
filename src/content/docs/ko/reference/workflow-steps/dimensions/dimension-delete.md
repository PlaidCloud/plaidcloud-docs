---
title: Dimension Delete 단계
description: 워크플로 단계에서 PlaidCloud 차원을 삭제하여 더 이상 필요하지 않은 계층형 데이터 구조를 제거합니다.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-delete.md
---

## 설명
관련된 모든 구조, 값, 속성, 별칭, 대체 계층과 함께 차원을 삭제합니다.


![Dimension Clear 단계](/images/dimension_clear.png)



## 차원 선택
### 차원을 동적으로 지정
**차원** 또는 **경로**를 동적으로 만들었다면 같은 변수를 사용하여 삭제할 수도 있습니다. 삭제 과정에서 변수를 사용하면 Dimension Delete 단계를 주기적으로 수동 업데이트할 필요가 없어 편리합니다.



`current_month` 변수를 사용하여 Materials 차원을 동적으로 삭제하는 예:

```text
/Dimensions/{current_month}/Products/Materials
```

### 특정 차원 사용

드롭다운 메뉴를 사용하여 삭제할 특정 차원을 선택합니다.
