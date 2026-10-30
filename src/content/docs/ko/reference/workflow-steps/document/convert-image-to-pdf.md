---
title: Convert Image to PDF 단계
description: PlaidCloud 워크플로 단계에서 이미지 파일을 PDF 문서로 변환하여 표준화된 문서 출력과 보관용 형식을 만듭니다.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-image-to-pdf.md
---

이미지(PNG, GIF, TIFF, JPEG 또는 HEIC)를 한 페이지짜리 PDF로 변환하거나, 기존 PDF를 표준 페이지 크기에 맞춰 다시 조정합니다.

## 입력

- **입력 파일 또는 디렉터리** — 문서 계정에 있는 이미지 또는 PDF, 또는 이들이 들어 있는 폴더입니다.
- **대상 위치** — PDF를 쓸 위치입니다.
- **페이지 크기** — US Letter, US Legal, A3, A4 또는 A5입니다.
- **압축** — **Lossy**는 이미지를 화면 해상도로 줄여 파일 크기를 크게 줄일 수 있으며, 기본값인 **Lossless**는 이미지 데이터를 그대로 유지합니다.

## 작동 방식

- 이미지는 선택한 크기의 페이지에 배치되며, 비율을 바꾸지 않고 페이지 안에 맞도록 크기가 조정됩니다. 스캔한 TIFF처럼 여러 페이지나 프레임이 있는 이미지는 첫 번째 페이지나 프레임에서 변환됩니다.
- **Lossy**를 사용하면 결과가 압축되며, PDF 입력은 압축되는 동안 선택한 페이지 크기에 맞춰집니다.
- **Lossless**를 사용하면 PDF 입력은 변경 없이 그대로 전달되어 고유한 페이지 크기를 유지합니다.

## 출력

입력 파일당 PDF 하나가 생성됩니다. 폴더의 경우 각 파일의 PDF는 대상 위치에서 확장자를 뺀 이름의 폴더 안에 소스 파일의 이름으로 쓰입니다. 여러 PDF를 하나의 문서로 결합하려면 이 단계 뒤에 [Merge Multiple PDFs 단계](/ko/reference/workflow-steps/document/merge-multiple-pdfs/)를 이어서 사용하십시오.

## 참고

- 입력 경로가 없거나 그 안에 파일이 없으면 단계는 경로를 알려 주는 경고와 함께 아무것도 처리하지 않고 완료되며, 워크플로는 계속 진행됩니다.
- 대상 위치는 입력 경로와 같을 수 없습니다.

## 일반적인 용도

- 영수증이나 송장 이미지를 보관용 형식으로 표준화
- PDF 입력만 허용하는 시스템에 제출할 이미지 증빙 자료 준비

## 관련 항목

- [Convert PDF or Image to JPEG 단계](/ko/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Compress PDF 단계](/ko/reference/workflow-steps/document/compress-pdf/)
- [Merge Multiple PDFs 단계](/ko/reference/workflow-steps/document/merge-multiple-pdfs/)
