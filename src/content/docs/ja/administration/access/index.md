---
title: IDとアクセス管理（IAM）
description: ユーザー認証、ロールベースの権限、セキュリティグループなど、PlaidCloudのIDとアクセス制御を管理します。
sidebar:
  label: 概要
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/administration/access/index.md
---

PlaidCloudのアクセス制御は、いくつかの中核となる概念を中心に構成されています。

- **組織** — 請求とIDの最上位の境界です。組織には、ワークスペースとメンバーが含まれます。
- **ワークスペース** — 実際の作業を行う分離された環境です。メンバーには、ワークスペース単位でアクセス権が付与されます。
- **メンバー** — 認証情報を持ち、1つ以上の組織の1つ以上のワークスペースに所属するユーザーです。
- **セキュリティグループ** — ワークスペース内の権限をまとめたものです。メンバーをセキュリティグループに割り当てることで、特定の機能を使用できるようにします。
- **シングルサインオン（SSO）** — 認証をIDプロバイダー（Okta、Auth0、Microsoft Entra、Google、AWS）に委任する、SAMLベースのオプションのフェデレーションです。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 260" role="img" aria-label="PlaidCloudのアクセスモデル。組織にはワークスペースが含まれます。ワークスペース内では、メンバーがセキュリティグループに割り当てられ、各グループが権限のセットをまとめています。オプションのシングルサインオンは、認証を外部のIDプロバイダーに委任します。" style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="ac-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="150" y="22" width="522" height="216" rx="12" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="164" y="42" font-size="12" font-weight="700" fill="var(--sl-color-text)">組織</text>
  <rect x="176" y="56" width="480" height="166" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="190" y="76" font-size="12" font-weight="700" fill="var(--sl-color-accent)">ワークスペース</text>
  <rect x="196" y="104" width="150" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="271" y="130" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">メンバー</text>
  <text x="271" y="147" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">アクセス権を持つユーザー</text>
  <path d="M346 128 L400 128" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#ac-arrow)" />
  <text x="373" y="120" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">割り当て</text>
  <rect x="402" y="96" width="238" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="414" y="117" font-size="11" fill="var(--sl-color-text)">セキュリティグループ · Analysts</text>
  <rect x="402" y="136" width="238" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="414" y="157" font-size="11" fill="var(--sl-color-text)">セキュリティグループ · Admins</text>
  <text x="402" y="192" font-size="10" fill="var(--sl-color-gray-3)">各グループ ＝ 権限のセット</text>
  <rect x="8" y="104" width="120" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" stroke-dasharray="5 4" />
  <text x="68" y="128" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">IDプロバイダー</text>
  <text x="68" y="144" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">（SSO）</text>
  <path d="M128 134 C150 134 240 128 262 122" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#ac-arrow)" />
  <text x="150" y="250" font-size="10" fill="var(--sl-color-gray-3)">SSOは、メンバーがワークスペースに到達する前に認証します</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">組織にはワークスペースが含まれ、メンバーはワークスペースに所属してセキュリティグループに割り当てられます。各グループは権限のセットです。オプションのSSOは、サインインをIDプロバイダーに委任します。</figcaption>
</figure>

## 最初に行うこと

新しい組織をセットアップする場合は、次の順に進めます。

1. **[組織とワークスペースの解説](/ja/administration/access/overview/organizations-and-workspaces-explained/)** — 両者の境界と、それぞれの使い分け
2. **[ワークスペースメンバーの管理](/ja/administration/access/overview/managing-workspace-members/)** — ユーザーの招待、ワークスペースへの割り当て、機能の付与
3. **[セキュリティグループの管理](/ja/administration/access/managing-security-groups-and-assignments/)** — 権限をまとめて割り当て

既存のIDプロバイダーと連携する場合は、次を参照してください。

- **[組織のシングルサインオンの管理](/ja/administration/access/advanced/managing-single-sign-on-for-organization/)** — SSOフローの概要
- ベンダー別のガイド：
  - [Okta SAMLの設定](/ja/administration/access/advanced/okta-saml-setup/)
  - [Auth0 SAMLの設定](/ja/administration/access/advanced/auth0-saml-setup/)
  - [Microsoft Entra SAMLの設定](/ja/administration/access/advanced/entra-saml-setup/)
  - [Google SAMLの設定](/ja/administration/access/advanced/google-saml-setup/)
  - [AWS SAMLの設定](/ja/administration/access/advanced/aws-saml-setup/)

## 関連項目

- [メンバー認証](/ja/administration/access/member-authentication/) — SSOを使用しないメンバー向けのパスワードとMFAのオプション
- [メンバー管理](/ja/administration/access/member-management/) — メンバーの追加、削除、更新
- [メンバーのユーザーID](/ja/administration/access/member-user-identity/) — IDの属性と、PlaidCloudでの使われ方
- [利用状況レポート](/ja/administration/access/usage-reports/) — アプリ、Superset、Panelアプリ、JupyterHub全体での利用状況
- [メンバーの有効期限の設定](/ja/administration/access/advanced/setting-member-expiration-period/) — 自動無効化ポリシー
