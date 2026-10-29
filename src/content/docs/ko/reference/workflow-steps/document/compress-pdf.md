---
title: Compress PDF 단계
description: PlaidCloud 워크플로 단계에서 PDF 파일을 압축하여 문서 품질을 유지하면서 파일 크기를 줄이고 저장 효율을 높입니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/compress-pdf.md
---

문서 계정에 저장된 PDF의 파일 크기를 줄입니다. 용량이 큰 스캔 문서를 보관하거나, 알림에 첨부하거나, 문서 계정 간에 옮기기 전에 크기를 줄이는 데 유용합니다.

## 입력

- **입력 파일 또는 디렉터리** — 문서 계정에 있는 PDF 또는 PDF가 들어 있는 폴더입니다.
- **출력 파일 또는 디렉터리** — 압축된 PDF를 쓸 위치입니다.

## 작동 방식

PDF는 이미지가 화면 해상도(72dpi)로 축소되고 글꼴이 하위 집합으로 포함된 상태로 다시 작성되며, 스캔 문서의 크기를 크게 줄일 수 있습니다. 텍스트는 선명하게 유지됩니다. 페이지는 US Letter 크기에 맞춰집니다.

## 출력

출력 경로에 압축된 PDF가 생성됩니다. 폴더의 경우 각 PDF는 입력 폴더를 기준으로 한 상대 위치를 유지한 채 출력 경로 아래에 쓰입니다.

## 참고

- 출력 경로는 입력 경로와 같을 수 없으므로 원본이 덮어쓰이지 않습니다.
- 입력 경로가 없거나 그 안에 파일이 없으면 단계는 경로를 알려 주는 경고와 함께 아무것도 처리하지 않고 완료되며, 워크플로는 계속 진행됩니다.
- 압축할 수 없는 PDF가 있으면 파일 이름과 이유를 알려 주며 단계가 실패합니다.

## 일반적인 용도

- 스캔한 송장, 영수증 또는 계약서를 장기 보관하기 전에 크기 줄이기
- 이메일로 보내거나 알림에 첨부하기 전에 PDF 크기 줄이기
- 크기 제한이 있는 다운스트림 시스템에 업로드할 문서 준비

## 관련 항목

- [Convert PDF or Image to JPEG 단계](/ko/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Merge Multiple PDFs 단계](/ko/reference/workflow-steps/document/merge-multiple-pdfs/)
- [문서 가이드](/ko/guides/documents/)
