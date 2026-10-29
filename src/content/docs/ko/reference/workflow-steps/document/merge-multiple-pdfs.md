---
title: Merge Multiple PDFs 단계
description: PlaidCloud 워크플로 단계에서 여러 PDF 파일을 하나의 문서로 병합하여 보고서를 조립하고 통합합니다.
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/merge-multiple-pdfs.md
---

폴더에 있는 PDF를 하나의 PDF로 결합합니다. [Concatenate Files 단계](/ko/reference/workflow-steps/document/concatenate-files/)와 달리 이 단계는 PDF 형식을 이해하며 유효한 병합 문서를 만듭니다.

## 입력

- **입력 디렉터리** — 문서 계정에서 PDF를 병합할 폴더입니다. PDF가 들어 있는 ZIP과 같은 단일 아카이브를 대신 지정할 수 있으며, 이 경우 그 안의 PDF가 병합됩니다.
- **병합된 출력 파일** — 병합된 PDF를 기록할 위치입니다.

## 작동 방식

- PDF는 경로 순서로 병합되며 숫자는 값으로 비교됩니다. 따라서 `page2.pdf`가 `page10.pdf`보다 앞에 오므로 순서를 제어하려면 번호를 붙이십시오. 각 PDF는 자체 페이지 순서를 유지합니다.
- 이름이 `.pdf`인 파일만 병합됩니다. 폴더의 다른 파일은 제외되며 폴더에 있는 아카이브는 열지 않습니다.
- 하위 폴더의 파일은 문서 계정이 나열하는 경우에 포함됩니다. S3, Wasabi, Google Cloud Storage 계정은 전체 폴더 트리를 나열하지만 OneDrive, SFTP, Azure 계정은 최상위 수준만 나열합니다.
- 최대 100개의 PDF가 병합되며 그보다 많으면 단계가 실패합니다.

## 출력

병합된 모든 PDF의 모든 페이지가 들어 있는 단일 PDF가 출력 경로에 만들어집니다.

## 참고

- PDF가 없거나 존재하지 않는 폴더는 폴더 이름을 알려 주는 경고와 함께 단계가 완료되며 아무것도 병합하지 않고 워크플로는 계속됩니다.
- 출력 경로는 입력 경로와 같을 수 없습니다.

## 일반적인 용도

- 개별 보고서 PDF로 월간 보고서 조립
- 표지, 본문, 부록을 하나의 산출물로 결합
- 생성된 청구서를 고객별 또는 기간별 아카이브로 묶기

## 관련 항목

- [Compress PDF 단계](/ko/reference/workflow-steps/document/compress-pdf/) — 병합된 결과의 크기를 줄입니다
- [Convert Image to PDF 단계](/ko/reference/workflow-steps/document/convert-image-to-pdf/) — 병합하기 전에 이미지를 PDF로 변환합니다
