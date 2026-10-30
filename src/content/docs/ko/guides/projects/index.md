---
title: 프로젝트
description: PlaidCloud 프로젝트를 설정하고 관리하여 워크플로, 테이블, 데이터 가져오기 및 기타 분석 개체를 목적별로 구성합니다.
sidebar:
  label: 프로젝트
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/index.md
---

**프로젝트**는 PlaidCloud의 작업 단위입니다. 각 프로젝트는 자체 데이터, 워크플로, 차원, 감사 기록을 소유합니다. 프로젝트끼리는 상태를 공유하지 않고 서로 격리되어 있으므로, 서로 다른 분석, 비즈니스 프로세스, 데이터 제품을 구분하는 자연스러운 경계가 됩니다.

대부분의 팀은 분석 영역마다 프로젝트 하나로 시작합니다. 인건비 배부를 위한 프로젝트, 매출 분석을 위한 프로젝트, 월 마감을 위한 프로젝트 등 팀이 업무를 생각하는 방식에 맞는 프로젝트를 만듭니다.

## 이 섹션의 내용

- [프로젝트 관리](/ko/guides/projects/managing-projects/) — 워크스페이스에서 프로젝트 만들기, 구성, 정리
- [Data Foundation: Common Finance Model](/ko/guides/projects/data-foundation/) — 여러 ERP 시스템과 인스턴스의 ERP 데이터를 직접 연결을 통해 가져와 보고서, 지표, AI 어시스턴트가 모두 읽는 하나의 Common Finance Model로 통합
- [프로젝트 보기](/ko/guides/projects/viewing-projects/) — 기존 프로젝트 찾기와 열기
- [계층 관리](/ko/guides/projects/managing-hierarchies/) — 많은 프로젝트를 정리하기 위한 폴더 구조
- [테이블 및 뷰 관리](/ko/guides/projects/managing-tables-and-views/) — 프로젝트 내부의 데이터 계층
- [데이터 편집기 관리](/ko/guides/projects/managing-data-editors/) — 프로젝트 데이터를 수정할 수 있는 사용자
- [프로젝트 로그 보기](/ko/guides/projects/viewing-the-project-log/) — 변경 사항의 감사 추적
- [프로젝트 아카이브](/ko/guides/projects/archive-a-project/) — 삭제하지 않고 완료된 작업 보존
- [이동 경로와 링크](/ko/guides/projects/breadcrumbs-and-shareable-links/) — 어떤 창에서든 위로 이동하고, 보고 있는 대상의 링크 공유
- [프로젝트 비교 및 병합](/ko/guides/projects/compare-and-merge-projects/) — 두 프로젝트를 비교하고 변경 사항을 선택하여 복사
- [이식 가능한 형식으로 내보내기](/ko/guides/projects/export-to-portable-format/) — 프로젝트를 플랫폼 밖에서 실행되는 독립형 Python + DuckDB 프로그램으로 패키징
- [스토리지 관리](/ko/guides/projects/managing-storage/) — 워크스페이스에 저장된 항목을 확인하고 테이블이 기록을 유지하는 기간 설정
- [레이블로 작업 구성](/ko/guides/projects/organizing-with-labels/) — 워크플로, 단계, 테이블 및 기타 개체에 태그를 지정하여 그룹화하고 필터링
- [링크 공유](/ko/guides/projects/sharing-links/) — 주소 표시줄에서 링크를 복사하여 프로젝트, 워크플로, 테이블 또는 차원을 바로 열기

## 관련 문서

- [개념](/ko/get-started/concepts/) — 프로젝트가 워크스페이스, 멤버, 더 넓은 데이터 모델과 어떻게 관련되는지
- [워크플로](/ko/guides/workflows/) — 프로젝트 안에 있는 자동화 기본 요소
- [액세스 관리](/ko/administration/access/) — 프로젝트를 볼 수 있고 편집할 수 있는 사용자를 제어하는 워크스페이스 수준 제어
