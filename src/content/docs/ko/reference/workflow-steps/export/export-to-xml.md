---
title: Export to XML 단계
description: PlaidCloud 워크플로 단계에서 XML 파일로 데이터를 내보내 구조화된 데이터 교환과 시스템 통합에 사용합니다.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-to-xml.md
---

## 설명

PlaidCloud 프로젝트 테이블을 XML 파일로 문서 계정에 기록합니다. 다운스트림 시스템에서 XML 입력을 요구할 때 사용하며, 오래된 엔터프라이즈 통합, 정부 신고, 특정 업계의 데이터 교환 형식에서 흔히 쓰입니다.

XML 구조는 테이블을 그대로 반영하여, 행마다 요소 하나를 만들고 열마다 자식 요소를 만듭니다. 구조를 더 세밀하게 제어하려면 템플릿 파일에 [Document Text Substitution 단계](/ko/reference/workflow-steps/document/document-text-substitution/)를 적용하는 템플릿 방식을 사용하십시오.

## 파일이 있는 경우

**파일이 있는 경우** 아래의 **이미 있는 파일**(`if_exists`)은 파일이 이미 있을 때의 동작을 결정합니다. **덮어쓰기**(`overwrite`, 기본값)는 이미 있는 파일을 대체하고, **아무것도 기록하지 않고 단계 실패**(`fail`)는 기록하려는 파일이 이미 있으면 아무것도 기록하지 않고 단계를 중단합니다.
