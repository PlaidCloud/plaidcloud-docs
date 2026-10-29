---
title: Call SAP Master Data Table RFC 단계
description: 마스터 데이터 테이블에 액세스하도록 설계된 SAP ECC / S/4HANA RFC(Remote Function Call)를 호출하여 데이터를 표 형식으로 가져옵니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-master-data-table-rfc.md
---

## 설명


마스터 데이터 테이블에 액세스하도록 설계된 SAP ECC / S/4HANA RFC(Remote Function Call)를 호출하여 데이터를 표 형식으로 가져옵니다. 이 데이터는 PlaidCloud의 변환 프로세스에서 사용할 수 있습니다. 또한 열 이름, 데이터 유형, 열 순서 정보가 포함된 마스터 데이터 테이블 구조를 별도의 파일로 내보낼 수도 있습니다.


## 예제


### RFC 매개변수


사용할 에이전트를 선택합니다. 드롭다운 막대에서 대상 디렉터리를 선택하고, 아래에서 파일을 저장할 올바른 하위 폴더를 찾습니다. 그다음 “Target File Name”에 적절한 이름을 지정합니다. “Function Call Information”에서 Function과 반환 값 매개변수를 입력하고 매개변수를 선택합니다.



Parameters 섹션에서 행 삽입 또는 행 추가를 선택할 수 있으며, 매개변수의 이름과 값을 지정할 수도 있습니다. 최대 동시 요청 수를 선택하고 Wait for RFC to Complete를 선택합니다. 저장 및 실행을 클릭합니다.
