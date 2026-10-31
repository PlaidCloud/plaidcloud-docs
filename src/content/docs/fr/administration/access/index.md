---
title: Gestion des identités et des accès (IAM)
description: Gérez les contrôles d'identité et d'accès de PlaidCloud, notamment l'authentification des utilisateurs, les autorisations basées sur les rôles et les groupes de sécurité.
sidebar:
  label: Vue d'ensemble
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/administration/access/index.md
---

Les contrôles d'accès de PlaidCloud reposent sur quelques concepts de base :

- **Organisation** — la limite de facturation et d'identité de niveau supérieur. Une organisation contient des espaces de travail et des membres.
- **Espace de travail** — un environnement isolé où le travail est réellement effectué. Les membres obtiennent l'accès au niveau de l'espace de travail.
- **Membre** — un utilisateur disposant d'identifiants, qui appartient à un ou plusieurs espaces de travail dans une ou plusieurs organisations.
- **Groupe de sécurité** — un ensemble d'autorisations au sein d'un espace de travail. Les membres sont affectés à des groupes de sécurité pour disposer de capacités précises.
- **Authentification unique (SSO)** — fédération facultative basée sur SAML, qui délègue l'authentification à votre fournisseur d'identité (Okta, Auth0, Microsoft Entra, Google, AWS).

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 260" role="img" aria-label="Modèle d'accès de PlaidCloud. Une organisation contient un espace de travail. Dans l'espace de travail, les membres sont affectés à des groupes de sécurité, chacun regroupant un ensemble d'autorisations. L'authentification unique facultative délègue l'authentification à un fournisseur d'identité externe." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="ac-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="150" y="22" width="522" height="216" rx="12" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="164" y="42" font-size="12" font-weight="700" fill="var(--sl-color-text)">Organisation</text>
  <rect x="176" y="56" width="480" height="166" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="190" y="76" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Espace de travail</text>
  <rect x="196" y="104" width="150" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="271" y="130" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Membres</text>
  <text x="271" y="147" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">personnes ayant accès</text>
  <path d="M346 128 L400 128" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#ac-arrow)" />
  <text x="373" y="120" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">affectés à</text>
  <rect x="402" y="96" width="238" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="414" y="117" font-size="11" fill="var(--sl-color-text)">Groupe de sécurité · Analystes</text>
  <rect x="402" y="136" width="238" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="414" y="157" font-size="11" fill="var(--sl-color-text)">Groupe de sécurité · Administrateurs</text>
  <text x="402" y="192" font-size="10" fill="var(--sl-color-gray-3)">chaque groupe = un ensemble d'autorisations</text>
  <rect x="8" y="104" width="120" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" stroke-dasharray="5 4" />
  <text x="68" y="128" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Fournisseur</text>
  <text x="68" y="144" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">d'identité (SSO)</text>
  <path d="M128 134 C150 134 240 128 262 122" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#ac-arrow)" />
  <text x="150" y="250" font-size="10" fill="var(--sl-color-gray-3)">le SSO authentifie les membres avant leur arrivée dans l'espace de travail</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Une organisation contient des espaces de travail ; les membres appartiennent à un espace de travail et sont affectés à des groupes de sécurité, chacun regroupant un ensemble d'autorisations. Le SSO facultatif délègue la connexion à votre fournisseur d'identité.</figcaption>
</figure>

## Par où commencer

Si vous configurez une nouvelle organisation :

1. **[Organisations et espaces de travail expliqués](/fr/administration/access/overview/organizations-and-workspaces-explained/)** — les limites entre les deux et quand utiliser chacun
2. **[Gérer les membres de l'espace de travail](/fr/administration/access/overview/managing-workspace-members/)** — inviter des utilisateurs, les affecter à des espaces de travail, leur accorder des capacités
3. **[Gérer les groupes de sécurité](/fr/administration/access/managing-security-groups-and-assignments/)** — regrouper des autorisations et les affecter

Si vous vous intégrez à un fournisseur d'identité existant :

- **[Gérer l'authentification unique pour l'organisation](/fr/administration/access/advanced/managing-single-sign-on-for-organization/)** — présentation du flux SSO
- Guides propres à chaque fournisseur :
  - [Configuration SAML d'Okta](/fr/administration/access/advanced/okta-saml-setup/)
  - [Configuration SAML d'Auth0](/fr/administration/access/advanced/auth0-saml-setup/)
  - [Configuration SAML de Microsoft Entra](/fr/administration/access/advanced/entra-saml-setup/)
  - [Configuration SAML de Google](/fr/administration/access/advanced/google-saml-setup/)
  - [Configuration SAML d'AWS](/fr/administration/access/advanced/aws-saml-setup/)

## Voir aussi

- [Authentification des membres](/fr/administration/access/member-authentication/) — options de mot de passe et d'authentification multifacteur pour les membres hors SSO
- [Gestion des membres](/fr/administration/access/member-management/) — ajouter, supprimer et mettre à jour des membres
- [Identité utilisateur des membres](/fr/administration/access/member-user-identity/) — attributs d'identité et usage qu'en fait PlaidCloud
- [Rapports d'utilisation](/fr/administration/access/usage-reports/) — qui utilise quoi dans l'application, Superset, les applications Panel et JupyterHub
- [Définir l'expiration des membres](/fr/administration/access/advanced/setting-member-expiration-period/) — politiques de désactivation automatique
