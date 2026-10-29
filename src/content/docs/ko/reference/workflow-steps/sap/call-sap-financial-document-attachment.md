---
title: Call SAP Financial Document Attachment 단계
description: PlaidCloud 워크플로 단계에서 SAP 재무 문서 첨부 파일을 가져와 문서 추출과 처리를 자동화합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-financial-document-attachment.md
---

## 설명



RFC(Remote Function Call)를 통해 SAP ECC / S/4HANA의 특정 FI(Financial Accounting) 문서에 파일을 첨부합니다. 스캔한 송장, 승인 워크플로, 계약서 사본 등 증빙 자료를 해당 재무 항목과 함께 전기할 때 유용합니다.

SAP 커넥터에 구성된 SAP RFC 자격 증명과 대상 FI 문서 번호(회사 코드, 문서 번호, 회계 연도)가 필요합니다.


## 저장 시 검사 항목

이 단계는 **테이블 데이터 선택** 탭의 출력 열 중 `relative_file_path` 열에서 각 파일의 경로를 읽으며, 이 열은 텍스트여야 합니다. 이 열이 없으면 — *The output columns must include relative_file_path, the path of each file to attach.* — 또는 다른 유형이면 — *The relative_file_path column must be text, not integer.* — 저장이 거부됩니다.

소스 테이블을 선택했지만 소스 열이나 대상 열이 없는 상태로 저장하면, **두 매핑 테이블 모두 채우기**를 선택한 것처럼 비어 있는 쪽이 소스에서 채워집니다.


## 예제


### RFC 매개변수


사용할 에이전트를 선택합니다. 드롭다운 막대에서 대상 디렉터리를 선택하고, 아래에서 파일을 저장할 올바른 하위 폴더를 찾습니다. 그다음 “Target File Name”에 적절한 이름을 지정합니다. “Function Call Information”에서 Function과 반환 값 매개변수를 입력하고 매개변수를 선택합니다.



Parameters 섹션에서 행 삽입 또는 행 추가를 선택할 수 있으며, 매개변수의 이름과 값을 지정할 수도 있습니다. 최대 동시 요청 수를 선택하고 Wait for RFC to Complete를 선택합니다. 저장 및 실행을 클릭합니다.
