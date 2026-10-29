---
title: Fix File Extension 단계
description: PlaidCloud 워크플로 단계에서 실제 파일 형식을 감지하고 올바른 확장자로 이름을 바꾸어 파일 확장자를 바로잡습니다.
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/fix-file-extension.md
---

파일에 실제로 들어 있는 내용을 읽고, 그 내용이 확장자와 맞지 않으면 해당 형식이 보통 사용하는 확장자로 이름을 바꿉니다. 예를 들어 `.dat`로 저장된 PDF는 `.pdf`가 됩니다. 소스 시스템이 확장자가 잘못되었거나 없는 파일을 전달할 때 유용합니다.

## 입력

- **입력 파일 또는 디렉터리** — 문서 계정의 파일 하나 또는 각 파일을 검사할 폴더입니다. 파일은 제자리에서 이름이 바뀌므로 출력 위치는 없습니다.

## 작동 방식

이 단계는 내용을 보고 각 파일의 형식을 식별하며, 현재 이름에 확장자가 없거나 자리 표시자 확장자(`.dat`, `.tmp` 또는 `.bin`)가 있거나 단계가 인식하는 다른 형식을 가리킬 때만 파일 이름을 바꿉니다.

인식하는 형식은 PDF, JPEG·PNG·GIF·TIFF·BMP·WebP·HEIC 이미지, Excel(`.xlsx`, `.xls`)·Word(`.docx`, `.doc`)·PowerPoint(`.pptx`) 문서, ZIP 및 GZip 아카이브, 그리고 CSV, JSON, HTML, XML 및 일반 텍스트입니다.

다음과 같은 경우 파일은 이름을 유지합니다.

- 확장자가 이미 내용과 맞는 경우 — `.jpg`와 `.jpeg`는 모두 JPEG에, `.tif`와 `.tiff`는 TIFF에 맞습니다.
- 확장자가 `.sql`, `.log`, `.ai`처럼 단계가 인식하지 못하는 확장자인 경우 — 내용만으로는 SQL 스크립트와 다른 텍스트를 구분하거나 Illustrator 파일과 PDF를 구분할 수 없기 때문입니다.
- `.csv`, `.tsv`, `.json` 같은 텍스트 확장자에 일반 텍스트가 들어 있는 경우
- 한 텍스트 형식이 다른 형식의 확장자로 되어 있는 경우 — `.html` 파일 안의 XML, `.json` 파일 안의 CSV처럼 내용으로는 이들을 안정적으로 구분할 수 없기 때문입니다. `.txt` 파일 또는 확장자가 없거나 자리 표시자 확장자인 파일만 텍스트 형식으로 이름이 바뀝니다.
- Office 문서 이름이 붙은 ZIP 파일인 경우 — `.xlsx`, `.docx`, `.pptx` 파일은 내부적으로 ZIP 파일이기 때문입니다.
- 빈 파일처럼 형식을 확인할 수 없는 경우

아카이브는 자체 내용으로 판단하며 그 안의 구성원은 열거나 이름을 바꾸지 않습니다. 이름이 `.`로 시작하는 파일은 건너뜁니다.

## 예제

| 파일 | 내용 | 결과 |
|---|---|---|
| `invoice.dat` | PDF | `invoice.pdf`로 이름 변경 |
| `photo.png` | JPEG | `photo.jpg`로 이름 변경 |
| `export.txt` | CSV | `export.csv`로 이름 변경 |
| `readme` | 일반 텍스트 | `readme.txt`로 이름 변경 |
| `query.sql` | 일반 텍스트 | 변경 없음 |
| `budget.xlsx` | ZIP | 변경 없음 |

## 참고

- 입력 경로가 없거나 그 안에 파일이 없으면 단계는 경로를 알려 주는 경고와 함께 완료되며 아무것도 처리하지 않고 워크플로는 계속됩니다.

## 관련 항목

- [Concatenate Files 단계](/ko/reference/workflow-steps/document/concatenate-files/)
- [문서 가이드](/ko/guides/documents/)
