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
