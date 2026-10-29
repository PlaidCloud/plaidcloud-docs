---
title: ID 및 액세스 관리(IAM)
description: 사용자 인증, 역할 기반 권한, 보안 그룹을 포함한 PlaidCloud의 ID 및 액세스 제어를 관리합니다.
sidebar:
  label: 개요
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/administration/access/index.md
---

PlaidCloud의 액세스 제어는 몇 가지 핵심 개념을 중심으로 구성됩니다.

- **조직** — 최상위 결제 및 ID 경계입니다. 조직에는 워크스페이스와 멤버가 포함됩니다.
- **워크스페이스** — 실제 작업이 이루어지는 격리된 환경입니다. 멤버는 워크스페이스 수준에서 액세스 권한을 받습니다.
- **멤버** — 하나 이상의 조직에 있는 하나 이상의 워크스페이스에 속하며 자격 증명을 가진 사용자입니다.
- **보안 그룹** — 워크스페이스 내 권한 모음입니다. 멤버를 보안 그룹에 할당하여 특정 기능을 사용할 수 있게 합니다.
- **싱글 사인온(SSO)** — 인증을 ID 공급자(Okta, Auth0, Microsoft Entra, Google, AWS)에 위임하는 선택적 SAML 기반 페더레이션입니다.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 260" role="img" aria-label="PlaidCloud 액세스 모델. 조직에는 워크스페이스가 포함됩니다. 워크스페이스 안에서 멤버는 보안 그룹에 할당되며, 각 보안 그룹은 권한 집합을 묶은 것입니다. 선택적 싱글 사인온은 인증을 외부 ID 공급자에 위임합니다." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="ac-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="150" y="22" width="522" height="216" rx="12" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="164" y="42" font-size="12" font-weight="700" fill="var(--sl-color-text)">조직</text>
  <rect x="176" y="56" width="480" height="166" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="190" y="76" font-size="12" font-weight="700" fill="var(--sl-color-accent)">워크스페이스</text>
  <rect x="196" y="104" width="150" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="271" y="130" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">멤버</text>
  <text x="271" y="147" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">액세스 권한이 있는 사용자</text>
  <path d="M346 128 L400 128" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#ac-arrow)" />
  <text x="373" y="120" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">할당</text>
  <rect x="402" y="96" width="238" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="414" y="117" font-size="11" fill="var(--sl-color-text)">보안 그룹 · Analysts</text>
  <rect x="402" y="136" width="238" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="414" y="157" font-size="11" fill="var(--sl-color-text)">보안 그룹 · Admins</text>
  <text x="402" y="192" font-size="10" fill="var(--sl-color-gray-3)">각 그룹 = 권한 모음</text>
  <rect x="8" y="104" width="120" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" stroke-dasharray="5 4" />
  <text x="68" y="128" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">ID 공급자</text>
  <text x="68" y="144" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">(SSO)</text>
  <path d="M128 134 C150 134 240 128 262 122" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#ac-arrow)" />
  <text x="150" y="250" font-size="10" fill="var(--sl-color-gray-3)">SSO는 멤버가 워크스페이스에 접속하기 전에 인증합니다</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">조직에는 워크스페이스가 포함됩니다. 멤버는 워크스페이스에 속하며 권한 모음인 보안 그룹에 할당됩니다. 선택적 SSO는 로그인을 ID 공급자에 위임합니다.</figcaption>
</figure>

## 시작하기

새 조직을 설정하는 경우 다음 순서로 진행합니다.

1. **[조직과 워크스페이스 이해](/ko/administration/access/overview/organizations-and-workspaces-explained/)** — 둘 사이의 경계와 각각을 사용하는 경우
2. **[워크스페이스 멤버 관리](/ko/administration/access/overview/managing-workspace-members/)** — 사용자를 초대하고, 워크스페이스에 할당하고, 기능 권한을 부여
3. **[보안 그룹 관리](/ko/administration/access/managing-security-groups-and-assignments/)** — 권한을 묶고 할당

기존 ID 공급자와 통합하는 경우 다음을 참조하십시오.

- **[조직의 싱글 사인온 관리](/ko/administration/access/advanced/managing-single-sign-on-for-organization/)** — SSO 흐름 개요
- 공급업체별 가이드:
  - [Okta SAML 설정](/ko/administration/access/advanced/okta-saml-setup/)
  - [Auth0 SAML 설정](/ko/administration/access/advanced/auth0-saml-setup/)
  - [Microsoft Entra SAML 설정](/ko/administration/access/advanced/entra-saml-setup/)
  - [Google SAML 설정](/ko/administration/access/advanced/google-saml-setup/)
  - [AWS SAML 설정](/ko/administration/access/advanced/aws-saml-setup/)

## 관련 항목

- [멤버 인증](/ko/administration/access/member-authentication/) — SSO를 사용하지 않는 멤버를 위한 비밀번호 및 MFA 옵션
- [멤버 관리](/ko/administration/access/member-management/) — 멤버 추가, 제거, 업데이트
- [멤버 사용자 ID](/ko/administration/access/member-user-identity/) — ID 속성과 PlaidCloud가 이를 사용하는 방법
- [사용 현황 보고서](/ko/administration/access/usage-reports/) — 앱, Superset, 패널 앱, JupyterHub 전반에서 누가 무엇을 사용하는지
- [멤버 만료 설정](/ko/administration/access/advanced/setting-member-expiration-period/) — 자동 비활성화 정책
