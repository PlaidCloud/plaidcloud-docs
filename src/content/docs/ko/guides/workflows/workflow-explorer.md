---
title: 워크플로 탐색기
description: PlaidCloud 워크플로 탐색기를 사용하여 워크플로 세부 정보, 단계 구성, 실행 이력, 종속성 정보를 확인합니다.
sidebar:
  order: 1.1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/workflow-explorer.md
---

워크플로 안의 세부 정보를 보려면 프로젝트에서 워크플로를 찾아 두 번 클릭하여 탐색기에서 엽니다.

![워크플로 탐색기](/images/workflow_explorer.png)

여기에서 워크플로 단계를 관리할 수 있습니다. 워크플로 단계를 만들거나 기존 단계를 수정하고, 순서를 변경하고, 단계를 실행하는 등의 작업이 가능합니다.

## 단계 만들기

**단계 만들기**를 클릭하고 단계 유형을 선택합니다. 목록에서 단계 하나를 선택한 경우, 새 Table Extract, Table Inner Join, Table Outer Join, Table Anti Join, Table Cross Join 또는 Table Lookup 단계는 선택한 단계가 기록하는 테이블에서 시작합니다. 그 테이블이 새 단계의 소스가 되며(조인의 경우 **Table 1**), 열은 **소스 검사**가 채울 때와 같이 채워집니다. 양식 맨 아래의 참고 문구에 이 내용이 표시됩니다. 새 단계가 다른 대상을 읽어야 한다면 소스를 변경하십시오. 단계를 저장하기 전에는 아무것도 저장되지 않습니다.
