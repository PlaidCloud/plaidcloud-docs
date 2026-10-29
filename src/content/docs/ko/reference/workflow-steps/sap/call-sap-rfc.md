---
title: Call SAP RFC 단계
description: PlaidCloud 워크플로 단계에서 SAP RFC 함수 모듈을 호출하여 SAP ECC 및 S/4HANA 시스템과 직접 통합합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-rfc.md
---

## 설명


SAP ECC / S/4HANA RFC(Remote Function Call)를 호출하여 데이터를 표 형식으로 가져옵니다. 이 데이터는 PlaidCloud의 변환 프로세스에서 사용할 수 있습니다.


## 데이터 대상

RFC 결과를 파일 또는 테이블에 저장합니다.

**파일**은 결과를 **JSON**, **쉼표로 구분**, **탭으로 구분**, **파이프로 구분** 또는 **Parquet** 형식으로 기록합니다. Parquet 파일은 테이블과 동일한 열 유형을 유지합니다.

**테이블**은 RFC 함수 자체의 필드 정의에 따라 유형을 지정하여 결과를 **대상 테이블**에 저장합니다.

| SAP 필드 유형 | 저장되는 형식 |
|---|---|
| Date | 날짜. 비어 있거나 초기 상태인 날짜는 빈 값으로 저장됩니다. 잘못된 날짜는 빈 값으로 저장되고, 단계는 해당 열 이름을 알리는 경고와 함께 완료됩니다. |
| Packed decimal | 정확한 10진수. 소수 자릿수가 10자리를 초과하거나 정수 자릿수가 28자리를 초과하면 대신 텍스트로 저장되고, 단계는 해당 열 이름을 알리는 경고와 함께 완료됩니다. |
| Integer | 정수. |
| `FLOAT` | 배정밀도 부동 소수점. |
| Decimal float | 정확한 텍스트. |
| `NUMC`, `CHAR` | 텍스트, 선행 0 유지. |
| Time | 텍스트, `HH:MM:SS` 형식. |
| Raw bytes | 16진수 텍스트. |
| `UTCLONG` | 텍스트. |

SAP가 함수의 필드를 설명할 수 없으면 10진수는 대신 정확한 텍스트로 저장됩니다.

SAP가 함수를 설명하면 각 매개변수는 SAP가 기대하는 유형으로 변환됩니다. 날짜는 `YYYYMMDD`, 시간은 `HHMMSS`, 정수와 10진수는 숫자, 텍스트 필드는 텍스트로 변환되며, 구조 및 테이블 매개변수는 필드별로 변환됩니다. 정수 또는 10진수 매개변수로 변환할 수 없는 값이 있으면 단계가 실패합니다.

## 예제


### RFC 매개변수


사용할 에이전트를 선택합니다. 드롭다운 막대에서 대상 디렉터리를 선택하고, 아래에서 파일을 저장할 올바른 하위 폴더를 찾습니다. 그다음
“Target File Name”에 적절한 이름을 지정합니다. “Function Call Information”에서 Function과 반환 값 매개변수를 입력하고 매개변수를 선택합니다.

Parameters 섹션에서 행 삽입 또는 행 추가를 선택할 수 있으며, 매개변수의 이름과 값을 지정할 수도 있습니다. 최대 동시 요청 수를
선택하고 Wait for RFC to Complete를 선택합니다. 저장 및 실행을 클릭합니다.



### 고급 값 반복


이 탭 맨 위에서 “No Iterators”를 선택한 다음 원하면 저장 및 실행을 클릭하거나, 직접 지정할 수 있습니다.


여기에서 반복 대상으로 “Specify Argument Values”를 선택하고 인수를 만든 다음 반복 값으로 이동할 수 있습니다.


값을 편집할 반복 인수 선택 옆에는 행 삽입, 행 추가, 행 삭제, 행 아래로 이동 또는 맨 아래 행으로 이동 옵션이 있습니다.
아래에서 같은 드롭다운 메뉴를 사용하여 범위 반복자를 선택할 수 있습니다. 마지막 섹션은 “Exclusions for Selected Range Iteration”이며
행마다 추가, 삭제 등을 할 수 있는 동일한 옵션이 있습니다. 제외할 값은 아래에 입력할 수 있습니다. 저장 및 실행을 클릭합니다.
