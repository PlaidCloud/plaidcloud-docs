---
title: Concatenate Files 단계
description: PlaidCloud 워크플로 단계에서 여러 파일을 하나의 파일로 연결하여 텍스트, CSV 또는 기타 문서 출력을 결합합니다.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/concatenate-files.md
---

문서 계정에 있는 둘 이상의 파일을 하나의 출력 파일로 결합합니다. 바이트 단위로 동작하므로 단순 연결만으로 올바른 출력이 만들어지는 일반 텍스트 형식(CSV, 로그 파일, JSON Lines)에 유용합니다.

## 입력

- **소스 파일** — 순서대로 연결할 파일 목록
- **출력 경로** — 결합된 파일의 대상 위치
- **구분 기호** — 소스 파일 사이에 삽입할 선택적 바이트 시퀀스(보통 줄 바꿈)

## 출력

나열한 순서대로 모든 소스 파일의 내용이 구성된 구분 기호로 이어진 단일 파일입니다.

존재하지 않는 소스 파일은 결합된 파일에서 제외되며, 단계는 해당 파일을 알려 주는 경고와 함께 완료되므로 워크플로는 계속 진행됩니다.

## 일반적인 용도

- 일별 로그 파일을 월별 아카이브로 결합
- 스키마가 같은 CSV 파일 병합(첫 번째 파일을 제외한 나머지의 헤더는 제거)
- 처리하기 전에 여러 소스의 JSON Lines 내보내기 결합

## 적합하지 않은 경우

- PDF — 대신 [Merge Multiple PDFs 단계](/ko/reference/workflow-steps/document/merge-multiple-pdfs/)를 사용하십시오
- 헤더가 있는 바이너리 형식(XLSX, ZIP, 이미지 파일) — 바이트를 연결해도 올바른 파일이 만들어지지 않습니다

## 관련 항목

- [Merge Multiple PDFs 단계](/ko/reference/workflow-steps/document/merge-multiple-pdfs/)
- [문서 가이드](/ko/guides/documents/)
