---
title: Dimension Sort 단계
description: 워크플로 단계에서 차원 멤버를 자동으로 정렬하여 계층 내 순서를 일관되게 유지합니다.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-sort.md
---

## 설명

차원의 멤버를 상위 항목 아래에서 정렬합니다. 알파벳순, 값 기준, 속성 기준 또는 사용자 지정 순서 열을 기준으로 정렬할 수 있습니다. 계층 멤버를 올바른 순서로 일일이 끌어다 놓는 번거로움을 없애 주며, 대량 로드나 대규모 구조 개편 후에 특히 유용합니다.

차원을 직접 처리하므로 소스 테이블이나 대상 테이블이 필요하지 않습니다.


## 차원 선택
### 차원을 동적으로 지정
**차원** 또는 **경로**를 동적으로 만들었다면 같은 변수를 사용하여 정렬할 수도 있습니다. 정렬 과정에서 변수를 사용하면 Dimension Sort 단계를 주기적으로 수동 업데이트할 필요가 없어 편리합니다.



`current_month` 변수를 사용하여 Materials 차원을 동적으로 정렬하는 예:

```text
/Dimensions/{current_month}/Products/Materials
```

### 특정 차원 사용

드롭다운 메뉴를 사용하여 정렬할 특정 차원을 선택합니다.
