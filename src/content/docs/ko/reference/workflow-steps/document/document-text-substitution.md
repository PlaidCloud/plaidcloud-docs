---
title: Document Text Substitution 단계
description: PlaidCloud 워크플로 단계에서 문서의 텍스트를 찾아 바꾸어 콘텐츠를 자동으로 변환합니다.
sidebar:
  order: 15
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/document-text-substitution.md
---

## 설명

텍스트 파일 안에서 찾아 바꾸기를 수행합니다. 특정 문자열이나 자리 표시자를 새 값으로 바꿉니다. `CUSTOMER_NAME`과 같은 자리 표시자를 실제 이름으로 바꾸는 템플릿 작업이나 특정 문자열을 제거하거나 가리는 텍스트 정리에 유용합니다.

크기에 관계없이 UTF-8 텍스트 파일(TXT, CSV, JSON, XML, HTML, RML)에서 작동합니다. PDF나 Office 문서처럼 UTF-8 텍스트가 아닌 파일은 단계를 실패시킵니다.

## 입력

- **입력 파일 또는 디렉터리** — 변경할 파일 또는 파일이 들어 있는 폴더입니다.
- **대상 파일 또는 디렉터리** — 결과를 기록할 위치입니다. 결과는 항상 입력의 문서 계정에 기록되며, 대상은 경로를 설정합니다.
- **압축** — 출력에 사용할 압축 방식으로 압축 안 함, Zip, GZip, BZip2, Zstandard, LZ4, Snappy, LZO 또는 Deflate(zlib)가 있습니다. Snappy와 LZ4는 Spark와 Hadoop이 읽는 블록 형식으로 기록되고, LZO는 `lzop` 파일로 기록됩니다.
- **텍스트 바꾸기 작업 순서** — 바꾸기마다 한 행이며, 각 행에 원본 텍스트와 바꿀 텍스트를 지정합니다. 바꿀 텍스트에는 변수를 사용할 수 있습니다.

## 작동 방식

- 바꾸기는 위에서 아래로 실행되며 각 바꾸기는 위쪽 바꾸기의 결과에 대해 작동합니다. 따라서 앞선 행이 넣은 텍스트를 바꿀 수도 있습니다.
- 일치는 정확하고 대/소문자를 구분하며 모든 항목이 바뀝니다.
- 원본 텍스트가 비어 있는 행은 무시됩니다.
- 폴더의 경우 각 파일은 대상 이름에서 확장자를 뺀 이름의 폴더 안에 파일 자체의 이름으로 기록됩니다.
- 입력 경로가 없거나 그 안에 파일이 없으면 단계는 경로를 알려 주는 경고와 함께 완료되며 아무것도 처리하지 않고 워크플로는 계속됩니다.

## 예제

| 원본 | 바꿀 텍스트 | `Dear CUSTOMER_NAME,`의 결과 |
|---|---|---|
| `CUSTOMER_NAME` | `Acme Ltd` | `Dear Acme Ltd,` |
