---
title: 身份与访问管理 (IAM)
description: 管理 PlaidCloud 的身份与访问控制，包括用户身份验证、基于角色的权限和安全组。
sidebar:
  label: 概览
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/administration/access/index.md
---

PlaidCloud 的访问控制围绕几个核心概念组织：

- **组织** — 最顶层的计费和身份边界。一个组织包含工作区和成员。
- **工作区** — 实际开展工作的隔离环境。成员在工作区层级获得访问权限。
- **成员** — 拥有凭据的用户，属于一个或多个组织中的一个或多个工作区。
- **安全组** — 工作区内的一组权限。将成员分配到安全组即可授予其特定能力。
- **单点登录 (SSO)** — 可选的基于 SAML 的联合身份验证，将身份验证委托给您的身份提供商（Okta、Auth0、Microsoft Entra、Google、AWS）。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 260" role="img" aria-label="PlaidCloud 访问模型。一个组织包含一个工作区。在工作区内，成员被分配到安全组，每个安全组包含一组权限。可选的单点登录将身份验证委托给外部身份提供商。" style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="ac-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="150" y="22" width="522" height="216" rx="12" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="164" y="42" font-size="12" font-weight="700" fill="var(--sl-color-text)">组织</text>
  <rect x="176" y="56" width="480" height="166" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="190" y="76" font-size="12" font-weight="700" fill="var(--sl-color-accent)">工作区</text>
  <rect x="196" y="104" width="150" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="271" y="130" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">成员</text>
  <text x="271" y="147" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">拥有访问权限的人员</text>
  <path d="M346 128 L400 128" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#ac-arrow)" />
  <text x="373" y="120" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">分配到</text>
  <rect x="402" y="96" width="238" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="414" y="117" font-size="11" fill="var(--sl-color-text)">安全组 · 分析师</text>
  <rect x="402" y="136" width="238" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="414" y="157" font-size="11" fill="var(--sl-color-text)">安全组 · 管理员</text>
  <text x="402" y="192" font-size="10" fill="var(--sl-color-gray-3)">每个分组 = 一组权限</text>
  <rect x="8" y="104" width="120" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" stroke-dasharray="5 4" />
  <text x="68" y="128" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">身份提供商</text>
  <text x="68" y="144" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">(SSO)</text>
  <path d="M128 134 C150 134 240 128 262 122" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#ac-arrow)" />
  <text x="150" y="250" font-size="10" fill="var(--sl-color-gray-3)">SSO 在成员进入工作区之前对其进行身份验证</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">组织包含工作区；成员隶属于工作区，并被分配到安全组，每个安全组是一组权限。可选的 SSO 将登录委托给您的身份提供商。</figcaption>
</figure>

## 从哪里开始

如果要设置新的组织：

1. **[组织与工作区详解](/zh-cn/administration/access/overview/organizations-and-workspaces-explained/)** — 两者之间的边界以及各自的适用场景
2. **[管理工作区成员](/zh-cn/administration/access/overview/managing-workspace-members/)** — 邀请用户、将其分配到工作区并授予能力
3. **[管理安全组](/zh-cn/administration/access/managing-security-groups-and-assignments/)** — 打包权限并进行分配

如果要与现有身份提供商集成：

- **[管理组织的单点登录](/zh-cn/administration/access/advanced/managing-single-sign-on-for-organization/)** — SSO 流程概述
- 各厂商专用指南：
  - [Okta SAML 设置](/zh-cn/administration/access/advanced/okta-saml-setup/)
  - [Auth0 SAML 设置](/zh-cn/administration/access/advanced/auth0-saml-setup/)
  - [Microsoft Entra SAML 设置](/zh-cn/administration/access/advanced/entra-saml-setup/)
  - [Google SAML 设置](/zh-cn/administration/access/advanced/google-saml-setup/)
  - [AWS SAML 设置](/zh-cn/administration/access/advanced/aws-saml-setup/)

## 相关内容

- [成员身份验证](/zh-cn/administration/access/member-authentication/) — 非 SSO 成员的密码和 MFA 选项
- [成员管理](/zh-cn/administration/access/member-management/) — 添加、移除和更新成员
- [成员用户身份](/zh-cn/administration/access/member-user-identity/) — 身份属性及 PlaidCloud 如何使用它们
- [使用情况报告](/zh-cn/administration/access/usage-reports/) — 谁在应用、Superset、Panel 应用和 JupyterHub 中使用了什么
- [设置成员过期](/zh-cn/administration/access/advanced/setting-member-expiration-period/) — 自动停用策略
