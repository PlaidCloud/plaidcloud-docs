---
title: Get Workspace Members 단계
description: 워크스페이스의 멤버를 프로젝트 테이블에 기록하며, 포함할 ID 및 활동 필드를 선택합니다.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-members.md
---

## 설명

워크스페이스의 멤버를 프로젝트 테이블에 기록합니다. 액세스 현황을 보고하거나, 멤버 목록을 HR 피드와 대조하거나, 현재 액세스 권한이 있는 사람을 기준으로 후속 단계를 구동하는 데 사용하십시오.

## 구성

### 포함할 정보

기본으로 켜져 있는 항목은 **성**, **이름**, **이메일**, **사용자 이름**, **멤버 생성 날짜**, **마지막 로그인 타임스탬프**입니다.

### 추가 설정

기본으로 꺼져 있는 항목은 다음과 같습니다.

- **비활성화된 멤버 포함** — 출력을 활성 멤버 이상으로 넓힙니다.
- **로그인 기록 모드** — 마지막 로그인만이 아니라 로그인 기록을 반환합니다.

## 보안 로그

실행할 때마다 기록된 열, 대상 테이블, 워크플로, 단계, 실행을 기록하는 항목이 보안 로그에 기록됩니다.

## 관련 문서

- [일반 단계](/ko/reference/workflow-steps/general/)
- [Deactivate Workspace Members 단계](/ko/reference/workflow-steps/general/deactivate-workspace-members/)
- [Get Workspace Usage 단계](/ko/reference/workflow-steps/general/get-workspace-usage/)
- [멤버 관리](/ko/administration/access/)
