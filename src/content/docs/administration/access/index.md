---
title: Identity and Access Management (IAM)
description: Manage PlaidCloud identity and access controls including user authentication, role-based permissions, and security groups.
sidebar:
  label: Identity and Access Management (IAM)
---

PlaidCloud's access controls are organized around a few core concepts:

- **Organization** — the top-level billing and identity boundary. An organization contains workspaces and members.
- **Workspace** — an isolated environment where actual work happens. Members get access at the workspace level.
- **Member** — a user with credentials who belongs to one or more workspaces in one or more organizations.
- **Security group** — a bundle of permissions inside a workspace. Members are assigned to security groups to grant them specific capabilities.
- **Single sign-on (SSO)** — optional SAML-based federation that delegates authentication to your identity provider (Okta, Auth0, Microsoft Entra, Google, AWS).

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 260" role="img" aria-label="PlaidCloud access model. An organization contains a workspace. Inside the workspace, members are assigned to security groups, each of which bundles a set of permissions. Optional single sign-on delegates authentication to an external identity provider." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="ac-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="150" y="22" width="522" height="216" rx="12" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="164" y="42" font-size="12" font-weight="700" fill="var(--sl-color-text)">Organization</text>
  <rect x="176" y="56" width="480" height="166" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="190" y="76" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Workspace</text>
  <rect x="196" y="104" width="150" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="271" y="130" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Members</text>
  <text x="271" y="147" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">people with access</text>
  <path d="M346 128 L400 128" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#ac-arrow)" />
  <text x="373" y="120" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">assigned to</text>
  <rect x="402" y="96" width="238" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="414" y="117" font-size="11" fill="var(--sl-color-text)">Security group · Analysts</text>
  <rect x="402" y="136" width="238" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="414" y="157" font-size="11" fill="var(--sl-color-text)">Security group · Admins</text>
  <text x="402" y="192" font-size="10" fill="var(--sl-color-gray-3)">each group = a bundle of permissions</text>
  <rect x="8" y="104" width="120" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" stroke-dasharray="5 4" />
  <text x="68" y="128" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Identity</text>
  <text x="68" y="144" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">provider (SSO)</text>
  <path d="M128 134 C150 134 240 128 262 122" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#ac-arrow)" />
  <text x="150" y="250" font-size="10" fill="var(--sl-color-gray-3)">SSO authenticates members before they reach the workspace</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">An organization contains workspaces; members belong to a workspace and are assigned to security groups, each a bundle of permissions. Optional SSO delegates sign-in to your identity provider.</figcaption>
</figure>

## Where to Start

If you're setting up a new organization:

1. **[Organizations and workspaces explained](/administration/access/overview/organizations-and-workspaces-explained/)** — the boundaries between them and when to use each
2. **[Managing workspace members](/administration/access/overview/managing-workspace-members/)** — invite users, assign them to workspaces, grant capabilities
3. **[Managing security groups](/administration/access/managing-security-groups-and-assignments/)** — bundle permissions and assign them

If you're integrating with an existing identity provider:

- **[Managing single sign-on for organization](/administration/access/advanced/managing-single-sign-on-for-organization/)** — overview of the SSO flow
- Vendor-specific guides:
  - [Okta SAML setup](/administration/access/advanced/okta-saml-setup/)
  - [Auth0 SAML setup](/administration/access/advanced/auth0-saml-setup/)
  - [Microsoft Entra SAML setup](/administration/access/advanced/entra-saml-setup/)
  - [Google SAML setup](/administration/access/advanced/google-saml-setup/)
  - [AWS SAML setup](/administration/access/advanced/aws-saml-setup/)

## Related

- [Member authentication](/administration/access/member-authentication/) — password and MFA options for non-SSO members
- [Member management](/administration/access/member-management/) — adding, removing, and updating members
- [Member user identity](/administration/access/member-user-identity/) — identity attributes and how PlaidCloud uses them
- [Setting member expiration](/administration/access/advanced/setting-member-expiration-period/) — automatic deactivation policies
