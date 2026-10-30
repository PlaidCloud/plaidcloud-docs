---
title: Convert Document Encoding 단계
description: PlaidCloud 워크플로 단계에서 문자 집합 간에 문서 파일 인코딩을 변환하여 인코딩 호환성 문제를 해결합니다.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding.md
---

## 설명



텍스트 파일을 한 문자 인코딩에서 다른 인코딩으로 다시 인코딩합니다. 소스 파일이 레거시 인코딩(Windows-1252, ISO-8859-1)으로 도착하지만 다운스트림 도구에는 UTF-8이 필요한 경우, 또는 그 반대의 경우에 유용합니다.

소스 파일이 UTF-8이 아니면 파일 내용으로 인코딩을 추정합니다. 매우 짧거나 반복이 심한 파일은 단서가 너무 적어 잘못 읽힐 수 있으므로, 그런 파일은 변환된 출력을 확인하십시오.

대상 인코딩으로 표현할 수 없는 문자가 있으면 기본적으로 단계가 실패합니다. **대상 인코딩에서 표현할 수 없는 문자를 ?로 바꾸기**를 선택하면 Java 라이터처럼 해당 문자 대신 `?`를 쓰고 단계가 완료됩니다.

단계 구성에서 대상 인코딩을 선택합니다. 특정 인코딩용 바로 가기는 [UTF-8](/ko/reference/workflow-steps/document/convert-document-encoding-to-utf-8/), [UTF-16](/ko/reference/workflow-steps/document/convert-document-encoding-to-utf-16/), [ASCII](/ko/reference/workflow-steps/document/convert-document-encoding-to-ascii/) 변형을 참조하십시오.


## 예시


소스 입력을 만들고 입력 파일을 선택한 다음 해당 위치에서 파일을 찾아봅니다. 원하는 출력 위치를 선택하고 파일을 저장할 위치를 찾아 선택합니다. 저장한 후 실행합니다.
