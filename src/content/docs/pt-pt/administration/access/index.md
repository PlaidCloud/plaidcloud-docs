---
title: Gestão de identidades e acessos (IAM)
description: Faça a gestão dos controlos de identidade e acesso do PlaidCloud, incluindo a autenticação de utilizadores, as permissões baseadas em funções e os grupos de segurança.
sidebar:
  label: Descrição geral
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/administration/access/index.md
---

Os controlos de acesso do PlaidCloud organizam-se em torno de alguns conceitos essenciais:

- **Organização** — o limite superior de faturação e identidade. Uma organização contém áreas de trabalho e membros.
- **Área de trabalho** — um ambiente isolado onde o trabalho efetivo acontece. Os membros obtêm acesso ao nível da área de trabalho.
- **Membro** — um utilizador com credenciais que pertence a uma ou mais áreas de trabalho, em uma ou mais organizações.
- **Grupo de segurança** — um conjunto de permissões dentro de uma área de trabalho. Os membros são atribuídos a grupos de segurança para lhes conceder capacidades específicas.
- **Início de sessão único (SSO)** — federação opcional baseada em SAML que delega a autenticação no seu fornecedor de identidade (Okta, Auth0, Microsoft Entra, Google, AWS).

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 260" role="img" aria-label="Modelo de acesso do PlaidCloud. Uma organização contém uma área de trabalho. Dentro da área de trabalho, os membros são atribuídos a grupos de segurança, cada um dos quais agrupa um conjunto de permissões. O início de sessão único opcional delega a autenticação num fornecedor de identidade externo." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="ac-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="150" y="22" width="522" height="216" rx="12" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="164" y="42" font-size="12" font-weight="700" fill="var(--sl-color-text)">Organização</text>
  <rect x="176" y="56" width="480" height="166" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="190" y="76" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Área de trabalho</text>
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
  <text x="68" y="128" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Fornecedor de</text>
  <text x="68" y="144" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">identidade (SSO)</text>
  <path d="M128 134 C150 134 240 128 262 122" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#ac-arrow)" />
  <text x="150" y="250" font-size="10" fill="var(--sl-color-gray-3)">o SSO autentica os membros antes de chegarem à área de trabalho</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Uma organização contém áreas de trabalho; os membros pertencem a uma área de trabalho e são atribuídos a grupos de segurança, cada um deles um conjunto de permissões. O SSO opcional delega o início de sessão no seu fornecedor de identidade.</figcaption>
</figure>

## Por Onde Começar

Se está a configurar uma nova organização:

1. **[Organizações e áreas de trabalho explicadas](/pt-pt/administration/access/overview/organizations-and-workspaces-explained/)** — os limites entre elas e quando utilizar cada uma
2. **[Gerir os membros da área de trabalho](/pt-pt/administration/access/overview/managing-workspace-members/)** — convidar utilizadores, atribuí-los a áreas de trabalho e conceder capacidades
3. **[Gerir grupos de segurança](/pt-pt/administration/access/managing-security-groups-and-assignments/)** — agrupar permissões e atribuí-las

Se está a integrar com um fornecedor de identidade existente:

- **[Gerir o início de sessão único da organização](/pt-pt/administration/access/advanced/managing-single-sign-on-for-organization/)** — descrição geral do fluxo de SSO
- Guias específicos de cada fornecedor:
  - [Configuração do SAML do Okta](/pt-pt/administration/access/advanced/okta-saml-setup/)
  - [Configuração do SAML do Auth0](/pt-pt/administration/access/advanced/auth0-saml-setup/)
  - [Configuração do SAML do Microsoft Entra](/pt-pt/administration/access/advanced/entra-saml-setup/)
  - [Configuração do SAML da Google](/pt-pt/administration/access/advanced/google-saml-setup/)
  - [Configuração do SAML da AWS](/pt-pt/administration/access/advanced/aws-saml-setup/)

## Relacionado

- [Autenticação de membros](/pt-pt/administration/access/member-authentication/) — opções de palavra-passe e MFA para membros sem SSO
- [Gestão de membros](/pt-pt/administration/access/member-management/) — adicionar, remover e atualizar membros
- [Identidade de utilizador do membro](/pt-pt/administration/access/member-user-identity/) — atributos de identidade e como o PlaidCloud os utiliza
- [Relatórios de utilização](/pt-pt/administration/access/usage-reports/) — quem utiliza o quê na aplicação, no Superset, nas aplicações Panel e no JupyterHub
- [Definir a expiração de membros](/pt-pt/administration/access/advanced/setting-member-expiration-period/) — políticas de desativação automática
