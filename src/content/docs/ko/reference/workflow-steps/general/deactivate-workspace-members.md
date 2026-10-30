---
title: Deactivate Workspace Members 단계
description: 프로젝트 테이블에 나열된 워크스페이스 멤버를 이메일 주소 또는 사용자 이름으로 일치시켜 비활성화합니다.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/deactivate-workspace-members.md
---

import { Aside } from '@astrojs/starlight/components';

## 설명

소스 테이블에 지정된 워크스페이스 멤버를 비활성화합니다. 사람을 일일이 비활성화하는 대신, 인사 데이터 추출이나 액세스 검토 같은 신뢰할 수 있는 목록을 기준으로 퇴사 처리를 자동화할 때 사용합니다.

[Get Workspace Members 단계](/ko/reference/workflow-steps/general/get-workspace-members/)와 함께 사용하면 더 이상 액세스 권한이 없어야 하는 사람의 목록을 만들 수 있습니다.

<Aside type="caution" title="액세스가 취소됩니다">
  단계가 실행되면 일치하는 모든 멤버가 액세스 권한을 잃습니다. 이 단계를
  일정에 등록하기 전에 소스 테이블에 의도한 사람만 포함되어 있는지 확인하십시오.
</Aside>

## 목록에 포함된 워크스페이스 관리자

[워크스페이스 관리자만 워크스페이스 관리자를 비활성화할 수 있습니다](/ko/administration/access/member-management/#워크스페이스-관리자-변경). 워크스페이스 관리자 권한 없이 단계를 실행했는데 목록에 관리자가 포함되어 있으면, 단계는 해당 관리자를 활성 상태로 두고 나머지 모든 멤버를 비활성화한 다음, 비활성화한 멤버 수와 활성 상태로 남긴 각 관리자의 이름을 알려 주는 메시지와 함께 오류로 종료됩니다. 이미 비활성화된 멤버는 비활성화된 상태로 유지됩니다. 관리자를 비활성화하려면 워크스페이스 관리자가 Identity에서 직접 비활성화해야 합니다.

## 구성

### 멤버 검색 매개변수

소스 테이블의 행을 멤버와 일치시키는 방법입니다. 다음 중 하나를 선택합니다.

- **이메일**(기본값)
- **사용자 이름**

## 관련 항목

- [일반 단계](/ko/reference/workflow-steps/general/)
- [Get Workspace Members 단계](/ko/reference/workflow-steps/general/get-workspace-members/)
- [멤버 관리](/ko/administration/access/)
