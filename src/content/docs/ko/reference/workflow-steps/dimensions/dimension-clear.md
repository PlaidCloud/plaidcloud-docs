---
title: Dimension Clear 단계
description: 차원 구조와 구성은 유지한 채 워크플로 단계에서 PlaidCloud 차원의 모든 멤버를 지웁니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-clear.md
---

## 설명
구조, 값, 별칭, 속성, 대체 계층을 포함하여 차원의 내용을 지웁니다.


![Dimension Clear 단계](/images/dimension_clear.png)



## 차원 선택
### 차원을 동적으로 지정
**차원** 또는 **경로**를 동적으로 만들었다면 같은 변수를 사용하여 지울 수도 있습니다. 지우기 과정에서 변수를 사용하면 Dimension Clear 단계를 주기적으로 수동 업데이트할 필요가 없어 편리합니다.



`current_month` 변수를 사용하여 Materials 차원을 동적으로 지우는 예:

```text
/Dimensions/{current_month}/Products/Materials
```

### 특정 차원 사용

드롭다운 메뉴를 사용하여 지울 특정 차원을 선택합니다.
