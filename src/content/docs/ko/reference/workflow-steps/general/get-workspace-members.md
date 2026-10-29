---
title: Get Workspace Members 단계
description: 워크스페이스의 멤버를 프로젝트 테이블에 기록하며, 포함할 ID 및 활동 필드를 선택할 수 있습니다.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-members.md
---

## 설명

워크스페이스의 멤버를 프로젝트 테이블에 기록합니다. 액세스 현황을 보고하거나, 멤버 목록을 인사 피드와 대조하거나, 현재 액세스 권한이 있는 사람을 기준으로 다운스트림 단계를 실행할 때 사용합니다.

## 구성

### 포함할 정보

기본적으로 켜져 있는 항목은 **성**, **이름**, **이메일**, **사용자 이름**, **멤버 생성 날짜**, **마지막 로그인 타임스탬프**입니다.

### 추가 설정

기본적으로 꺼져 있는 항목입니다.

- **비활성화된 멤버 포함** — 출력 범위를 활성 멤버 이외로 넓힙니다.
- **로그인 기록 모드** — 마지막 로그인만이 아니라 로그인 기록을 반환합니다.

## 관련 항목

- [일반 단계](/ko/reference/workflow-steps/general/)
- [Deactivate Workspace Members 단계](/ko/reference/workflow-steps/general/deactivate-workspace-members/)
- [멤버 관리](/ko/administration/access/)
