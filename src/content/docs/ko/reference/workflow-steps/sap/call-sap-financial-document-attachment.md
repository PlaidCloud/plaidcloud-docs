---
title: Call SAP Financial Document Attachment 단계
description: PlaidCloud 워크플로 단계에서 SAP 재무 문서 첨부 파일을 가져와 문서 추출과 처리를 자동화합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-financial-document-attachment.md
---

## 설명



RFC(원격 함수 호출)를 통해 SAP ECC / S/4HANA의 특정 FI(재무 회계) 문서에 파일을 첨부합니다. 스캔한 송장, 승인 워크플로, 계약서 사본 같은 증빙 문서를 해당 재무 항목과 함께 전기할 때 유용합니다.

SAP 커넥터에 구성된 SAP RFC 자격 증명과 대상 FI 문서 번호(회사 코드, 문서 번호, 회계 연도)가 필요합니다.


## 저장할 때 검사하는 항목

단계는 **열** 탭의 출력 열 중 `relative_file_path` 열에서 각 파일의 경로를 읽으며, 이 열은 텍스트여야 합니다. 이 열이 없으면 다음 메시지와 함께 저장이 거부됩니다. *출력 열에 첨부할 각 파일의 경로인 relative_file_path가 포함되어야 합니다.* 다른 유형이면 다음 메시지와 함께 거부됩니다. *relative_file_path 열은 integer가 아니라 텍스트여야 합니다.*

소스 테이블을 선택했지만 소스 열이나 대상 열이 없는 상태로 저장하면 **두 매핑 테이블 모두 채우기**를 사용했을 때와 같이 비어 있는 쪽을 소스에서 채웁니다.


## 예제


### RFC 매개변수


사용할 에이전트를 선택합니다. 드롭다운 막대에서 대상 디렉터리를 선택하고, 아래에서 파일이 저장될 올바른 하위 폴더를 찾아봅니다. 그런 다음 “Target File Name”에 적절한 이름을 지정합니다. “Function Call Information”에서 함수, 반환 값 매개변수를 입력하고 매개변수를 선택합니다.



매개변수 섹션에서 행 삽입 또는 행 추가를 선택할 수 있으며, 매개변수의 이름을 지정하고 값을 지정할 수도 있습니다. 최대 동시 요청 수를 선택하고 Wait for RFC to Complete를 선택합니다. 저장한 다음 단계를 실행합니다(저장 및 실행).
