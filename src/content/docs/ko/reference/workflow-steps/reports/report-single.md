---
title: Report Single 단계
description: 템플릿, 데이터 소스, 구성 가능한 레이아웃 옵션을 사용하여 PlaidCloud 워크플로 단계에서 단일 PDF 보고서를 생성합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/reports/report-single.md
---

## 설명



하나 이상의 PlaidCloud 테이블 데이터를 채워 넣은 RML(Report Markup Language) 템플릿으로 PDF 보고서를 렌더링합니다. 청구서, 재무제표, 규제 신고서, 브랜드 요약 자료와 같이 서식을 갖춘 공식 보고서에 사용하십시오.

RML 템플릿은 레이아웃(페이지 크기, 글꼴, 고정 텍스트, 테이블 위치)을 정의하고, 입력 테이블은 가변 데이터를 제공합니다. 하나의 템플릿으로 많은 보고서(예: 고객별 보고서 하나씩)를 생성해야 한다면 [Reports Batch](/ko/reference/workflow-steps/reports/reports-batch/) 단계를 비교해 보십시오.


## 템플릿이 읽는 이름

템플릿은 **보고서 데이터** 탭의 각 소스와 **보고서 상수(고정 값)** 아래의 각 상수를 이름으로 읽습니다. 새 소스의 이름은 `new_source`, `new_source_2` 등으로 지정되며 템플릿이 그대로 읽을 수 있습니다. 담고 있는 내용을 알 수 있도록 이름을 바꾸십시오.


## 저장할 때 검사하는 항목

모든 소스 및 상수 이름은 다음 조건을 충족해야 합니다.

- **지정되어 있어야 합니다** — 빈 이름은 거부됩니다.
- **고유해야 합니다** — 템플릿에서는 둘 중 하나만 보이므로, 소스 두 개, 상수 두 개 또는 소스 하나와 상수 하나가 같은 이름을 공유할 수 없습니다. *Source name 'sales' is also a constant name; rename one of them.*
- **템플릿이 읽을 수 있어야 합니다** — 문자, 숫자, 밑줄만 사용하며 문자 또는 밑줄로 시작해야 합니다. *Constant name 'fiscal year' can't be read by the template: use letters, digits and underscores, starting with a letter or underscore.*
- **템플릿이 예약한 단어가 아니어야 합니다** — `True`, `False`, `None`, `true`, `false`, `none`, `not`, `self`는 데이터가 아닌 다른 것으로 읽힙니다. *Source name 'self' is a word the template reserves, so it can't be read as a name.*


## 예제

아직 예제가 없습니다...
