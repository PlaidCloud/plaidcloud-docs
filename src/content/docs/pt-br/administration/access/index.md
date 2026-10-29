---
title: Gerenciamento de identidade e acesso (IAM)
description: Gerencie a identidade e os controles de acesso do PlaidCloud, incluindo autenticação de usuários, permissões baseadas em funções e grupos de segurança.
sidebar:
  label: Visão geral
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/administration/access/index.md
---

Os controles de acesso do PlaidCloud são organizados em torno de alguns conceitos principais:

- **Organização**: o limite de cobrança e identidade de nível superior. Uma organização contém espaços de trabalho e membros.
- **Espaço de trabalho**: um ambiente isolado onde o trabalho realmente acontece. Os membros recebem acesso no nível do espaço de trabalho.
- **Membro**: um usuário com credenciais que pertence a um ou mais espaços de trabalho em uma ou mais organizações.
- **Grupo de segurança**: um conjunto de permissões dentro de um espaço de trabalho. Os membros são atribuídos a grupos de segurança para receber recursos específicos.
- **Logon único (SSO)**: federação opcional baseada em SAML que delega a autenticação ao seu provedor de identidade (Okta, Auth0, Microsoft Entra, Google, AWS).

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 260" role="img" aria-label="Modelo de acesso do PlaidCloud. Uma organização contém um espaço de trabalho. Dentro do espaço de trabalho, os membros são atribuídos a grupos de segurança, e cada um deles reúne um conjunto de permissões. O logon único opcional delega a autenticação a um provedor de identidade externo." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="ac-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="150" y="22" width="522" height="216" rx="12" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="164" y="42" font-size="12" font-weight="700" fill="var(--sl-color-text)">Organização</text>
  <rect x="176" y="56" width="480" height="166" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="190" y="76" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Espaço de trabalho</text>
  <rect x="196" y="104" width="150" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="271" y="130" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Membros</text>
  <text x="271" y="147" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">pessoas com acesso</text>
  <path d="M346 128 L400 128" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#ac-arrow)" />
  <text x="373" y="120" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">atribuídos a</text>
  <rect x="402" y="96" width="238" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="414" y="117" font-size="11" fill="var(--sl-color-text)">Grupo de segurança · Analistas</text>
  <rect x="402" y="136" width="238" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="414" y="157" font-size="11" fill="var(--sl-color-text)">Grupo de segurança · Administradores</text>
  <text x="402" y="192" font-size="10" fill="var(--sl-color-gray-3)">cada grupo = um conjunto de permissões</text>
  <rect x="8" y="104" width="120" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" stroke-dasharray="5 4" />
  <text x="68" y="128" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Provedor de</text>
  <text x="68" y="144" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">identidade (SSO)</text>
  <path d="M128 134 C150 134 240 128 262 122" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#ac-arrow)" />
  <text x="150" y="250" font-size="10" fill="var(--sl-color-gray-3)">O SSO autentica os membros antes que cheguem ao espaço de trabalho</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Uma organização contém espaços de trabalho; os membros pertencem a um espaço de trabalho e são atribuídos a grupos de segurança, cada um deles um conjunto de permissões. O SSO opcional delega o login ao seu provedor de identidade.</figcaption>
</figure>

## Por onde começar

Se você está configurando uma nova organização:

1. **[Organizações e espaços de trabalho explicados](/pt-br/administration/access/overview/organizations-and-workspaces-explained/)**: os limites entre eles e quando usar cada um
2. **[Gerenciar os membros do espaço de trabalho](/pt-br/administration/access/overview/managing-workspace-members/)**: convide usuários, atribua-os a espaços de trabalho e conceda recursos
3. **[Gerenciar grupos de segurança](/pt-br/administration/access/managing-security-groups-and-assignments/)**: agrupe permissões e atribua-as

Se você está integrando com um provedor de identidade existente:

- **[Gerenciar o logon único da organização](/pt-br/administration/access/advanced/managing-single-sign-on-for-organization/)**: visão geral do fluxo de SSO
- Guias específicos de cada fornecedor:
  - [Configuração do SAML do Okta](/pt-br/administration/access/advanced/okta-saml-setup/)
  - [Configuração do SAML do Auth0](/pt-br/administration/access/advanced/auth0-saml-setup/)
  - [Configuração do SAML do Microsoft Entra](/pt-br/administration/access/advanced/entra-saml-setup/)
  - [Configuração do SAML do Google](/pt-br/administration/access/advanced/google-saml-setup/)
  - [Configuração do SAML da AWS](/pt-br/administration/access/advanced/aws-saml-setup/)

## Relacionados

- [Autenticação de membros](/pt-br/administration/access/member-authentication/): opções de senha e MFA para membros que não usam SSO
- [Gerenciamento de membros](/pt-br/administration/access/member-management/): adicionar, remover e atualizar membros
- [Identidade de usuário do membro](/pt-br/administration/access/member-user-identity/): atributos de identidade e como o PlaidCloud os usa
- [Relatórios de uso](/pt-br/administration/access/usage-reports/): quem usa o quê no aplicativo, no Superset, nos aplicativos Panel e no JupyterHub
- [Definir a expiração de membros](/pt-br/administration/access/advanced/setting-member-expiration-period/): políticas de desativação automática
