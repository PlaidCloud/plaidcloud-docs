---
title: Convert PDF or Image to JPEG 단계
description: PlaidCloud 워크플로 단계에서 PDF 페이지 또는 이미지를 JPEG 형식으로 변환하여 웹 호환 출력과 이미지 처리 작업에 사용합니다.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg.md
---

PDF 또는 이미지를 JPEG로 변환합니다. PDF의 첫 페이지가 JPEG가 되며, 이미지는 다시 인코딩됩니다. 스캔한 TIFF처럼 여러 페이지나 프레임이 있는 이미지는 첫 번째 페이지나 프레임에서 변환됩니다.

## 입력

- **입력 파일 또는 디렉터리** — 문서 계정에 있는 PDF 또는 이미지(PNG, GIF, TIFF, JPEG 또는 HEIC), 또는 이들이 들어 있는 폴더입니다.
- **출력 파일 또는 디렉터리** — JPEG를 쓸 위치입니다.

## 출력

입력 파일당 JPEG 하나가 생성됩니다. 폴더의 경우 각 파일의 JPEG는 출력 경로에서 확장자를 뺀 이름의 폴더 안에 소스 파일의 이름으로 쓰입니다.

## 참고

- 그 밖의 형식의 파일이 있으면 허용되는 형식을 알려 주며 단계가 실패합니다.
- 입력 경로가 없거나 그 안에 파일이 없으면 단계는 경로를 알려 주는 경고와 함께 아무것도 처리하지 않고 완료되며, 워크플로는 계속 진행됩니다.
- 출력 경로는 입력 경로와 같을 수 없습니다.

## 일반적인 용도

- 웹 표시용 미리 보기 이미지 생성
- PDF를 처리할 수 없는 시스템을 위한 이미지 전용 버전의 PDF 생성

## 관련 항목

- [Convert Image to PDF 단계](/ko/reference/workflow-steps/document/convert-image-to-pdf/)
- [Compress PDF 단계](/ko/reference/workflow-steps/document/compress-pdf/)
- [Crop Image to Headshot 단계](/ko/reference/workflow-steps/document/crop-image-to-headshot/)
