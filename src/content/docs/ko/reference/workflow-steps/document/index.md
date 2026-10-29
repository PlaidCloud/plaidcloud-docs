---
title: 문서 단계
description: 파일 변환, 복사, 이름 바꾸기, 삭제 및 PDF 작업 단계를 사용하여 PlaidCloud 워크플로에서 문서를 관리합니다.
sidebar:
  label: 문서 단계
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/index.md
---

문서 계정에 저장된 파일을 다루는 워크플로 단계입니다. 데이터 워크플로와 함께 문서를 이동, 변환 및 전환하는 데 사용합니다.

## 파일 작업

- [Copy Document File 단계](/ko/reference/workflow-steps/document/copy-document-file/) · [Copy Document Directory 단계](/ko/reference/workflow-steps/document/copy-document-directory/)
- [Create Document Directory 단계](/ko/reference/workflow-steps/document/create-document-directory/)
- [Delete Document File 단계](/ko/reference/workflow-steps/document/delete-document-file/) · [Delete Document Directory 단계](/ko/reference/workflow-steps/document/delete-document-directory/)
- [디렉터리 목록](/ko/reference/workflow-steps/document/directory-listing/) — 폴더에 있는 파일의 테이블을 작성합니다
- [Update Excel Cells 단계](/ko/reference/workflow-steps/document/document-excel-update/) — 통합 문서의 지정한 셀에 값을 기록하거나 서식을 지정합니다
- [Fix File Extension 단계](/ko/reference/workflow-steps/document/fix-file-extension/)
- [Rename Document File 단계](/ko/reference/workflow-steps/document/rename-document-file/) · [Rename Document Directory 단계](/ko/reference/workflow-steps/document/rename-document-directory/)

복사 및 이름 바꾸기 단계는 소스가 없는 경우를 정상으로 처리합니다. 복사하거나 이름을 바꿀 파일이나 폴더가 없거나 폴더가 비어 있으면 단계는 아무 작업도 하지 않고 경로를 알려 주는 경고와 함께 완료되며 워크플로는 계속됩니다. 그날 파일이 없는 폴더에 대해 일정에 따라 실행해도 더 이상 실패하지 않습니다.

## 암호화

- [파일 암호화 · 암호 해독](/ko/reference/workflow-steps/document/encrypt-decrypt-file/) — AES, Blowfish 또는 Excel 통합 문서 암호

## PDF 작업

- [Compress PDF 단계](/ko/reference/workflow-steps/document/compress-pdf/)
- [Convert Image to PDF 단계](/ko/reference/workflow-steps/document/convert-image-to-pdf/)
- [Convert PDF or Image to JPEG 단계](/ko/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Merge Multiple PDFs 단계](/ko/reference/workflow-steps/document/merge-multiple-pdfs/)

## 이미지 작업

- [Crop Image to Headshot 단계](/ko/reference/workflow-steps/document/crop-image-to-headshot/)

## 텍스트 작업

- [Concatenate Files 단계](/ko/reference/workflow-steps/document/concatenate-files/) — 여러 파일을 하나로 결합합니다
- [Document Text Substitution 단계](/ko/reference/workflow-steps/document/document-text-substitution/) — 문서 안에서 찾아 바꾸기

## 인코딩 변환

- [Convert Document Encoding 단계](/ko/reference/workflow-steps/document/convert-document-encoding/) — 대상 인코딩을 선택합니다
- [Convert Document Encoding to ASCII 단계](/ko/reference/workflow-steps/document/convert-document-encoding-to-ascii/)
- [Convert Document Encoding to UTF-16 단계](/ko/reference/workflow-steps/document/convert-document-encoding-to-utf-16/)
- [Convert Document Encoding to UTF-8 단계](/ko/reference/workflow-steps/document/convert-document-encoding-to-utf-8/)

## 참고 항목

- [Convert Dashboard to PDF 단계](/ko/reference/workflow-steps/document/dashboard-to-pdf/)
- [Delete Old Files 단계](/ko/reference/workflow-steps/document/document-delete-old-files/)
- [문서 계정](/ko/guides/documents/adding-accounts/) — 이 단계를 사용하기 전에 문서 계정을 연결합니다
- [문서 가이드](/ko/guides/documents/) — 같은 작업에 대한 작업 중심 안내
