---
title: Call SAP General Ledger Posting 단계
description: 해당 부가가치세(VAT)와 원천징수세를 포함한 분개 전표를 전기하도록 설계된 SAP ECC / S/4HANA RFC(Remote Function Call)를 호출합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-general-ledger-posting.md
---

## 설명


해당 부가가치세(VAT)와 원천징수세를 포함한 분개 전표를 전기하도록 설계된 SAP ECC / S/4HANA RFC(Remote Function Call)를 호출합니다. 테스트 모드로도 실행할 수 있으며, 이 경우 전기 프로세스를 수행하지만 전기를 완료하지는 않습니다. 따라서 계정이 마감되었거나 지정한 회사 코드에 고객이 없는 것과 같이 감지 가능한 오류를 미리 수집할 수 있습니다. 오류 검사가 철저하여 한 번의 테스트에서 감지된 여러 오류를 반환할 수 있습니다.


## 예제


### RFC 매개변수


사용할 에이전트를 선택합니다. 드롭다운 막대에서 대상 디렉터리를 선택하고, 아래에서 파일을 저장할 올바른 하위 폴더를 찾습니다. 그다음 “Target File Name”에 적절한 이름을 지정합니다. “Function Call Information”에서 Function과 반환 값 매개변수를 입력하고 매개변수를 선택합니다. 



Parameters 섹션에서 행 삽입 또는 행 추가를 선택할 수 있으며, 매개변수의 이름과 값을 지정할 수도 있습니다. 최대 동시 요청 수를 선택하고 Wait for RFC to Complete를 선택합니다. 저장 및 실행을 클릭합니다.


## 문서 전기로 변환

저장된 단계에는 **문서 전기로 변환…** 버튼이 있습니다. 이 버튼은 먼저 변환될 내용, 즉 문서 필드에 매칭된 열의 수와 시스템으로 라우팅된 엔터티의 수를 보여 주며, 확인하면 단계를 **문서 전기** 단계로 바꿉니다([ERP 시스템에 문서 전기](/ko/guides/connections/post-documents/) 참조). 이전 설정은 단계의 버전에 남습니다.
