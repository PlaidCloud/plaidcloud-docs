---
title: Convert Document Encoding to UTF-8 단계
description: PlaidCloud 워크플로 단계에서 문서 파일 인코딩을 UTF-8로 변환하여 최신 시스템 및 애플리케이션과의 폭넓은 호환성을 확보합니다.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding-to-utf-8.md
---

## 설명

텍스트 파일을 UTF-8로 다시 씁니다. 정보 소스에 여러 인코딩이 섞여 있거나 다른 도구가 특정 인코딩을 지원하지 않을 때 특히 유용합니다.

## 작동 방식

- 소스의 인코딩이 감지됩니다. UTF-8 파일은 UTF-8로 읽으며, Word나 Excel에서 붙여 넣은 곡선 따옴표 같은 Windows 문자도 몇 개든 그대로 처리됩니다. 다른 인코딩의 파일은 유효한 UTF-8이 아닌 첫 부분에서 감지된 인코딩으로 읽습니다.
- 텍스트는 변경 없이 기록됩니다. 악센트가 있는 문자, 기호, 기타 문자가 원래 그대로 유지됩니다.
- 인코딩을 감지할 수 없는 파일이 있으면 파일 이름을 알려 주며 단계가 실패합니다.
- 입력 경로가 없거나 그 안에 파일이 없으면 단계는 경로를 알려 주는 경고와 함께 아무것도 처리하지 않고 완료되며, 워크플로는 계속 진행됩니다.

## 예시

입력 파일을 선택하고 해당 위치에서 파일을 찾아봅니다. 원하는 출력 위치를 선택하고 파일을 저장할 위치를 찾아 선택합니다. 저장한 후 실행합니다.
