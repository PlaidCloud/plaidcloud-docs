---
title: Zarządzanie tożsamością i dostępem (IAM)
description: Zarządzaj tożsamością i kontrolą dostępu w PlaidCloud, w tym uwierzytelnianiem użytkowników, uprawnieniami opartymi na rolach i grupami zabezpieczeń.
sidebar:
  label: Przegląd
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/administration/access/index.md
---

Kontrola dostępu w PlaidCloud opiera się na kilku podstawowych pojęciach:

- **Organizacja** — nadrzędna granica rozliczeń i tożsamości. Organizacja zawiera obszary robocze i członków.
- **Obszar roboczy** — izolowane środowisko, w którym odbywa się faktyczna praca. Członkowie uzyskują dostęp na poziomie obszaru roboczego.
- **Członek** — użytkownik z poświadczeniami, który należy do jednego lub wielu obszarów roboczych w jednej lub wielu organizacjach.
- **Grupa zabezpieczeń** — zestaw uprawnień w obszarze roboczym. Członkowie są przypisywani do grup zabezpieczeń, aby uzyskać określone możliwości.
- **Jednokrotne logowanie (SSO)** — opcjonalna federacja oparta na SAML, która deleguje uwierzytelnianie do Twojego dostawcy tożsamości (Okta, Auth0, Microsoft Entra, Google, AWS).

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 260" role="img" aria-label="Model dostępu PlaidCloud. Organizacja zawiera obszar roboczy. W obszarze roboczym członkowie są przypisani do grup zabezpieczeń, z których każda grupuje zestaw uprawnień. Opcjonalne jednokrotne logowanie deleguje uwierzytelnianie do zewnętrznego dostawcy tożsamości." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="ac-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="150" y="22" width="522" height="216" rx="12" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="164" y="42" font-size="12" font-weight="700" fill="var(--sl-color-text)">Organizacja</text>
  <rect x="176" y="56" width="480" height="166" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="190" y="76" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Obszar roboczy</text>
  <rect x="196" y="104" width="150" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="271" y="130" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Członkowie</text>
  <text x="271" y="147" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">osoby z dostępem</text>
  <path d="M346 128 L400 128" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#ac-arrow)" />
  <text x="373" y="120" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">przypisani do</text>
  <rect x="402" y="96" width="238" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="414" y="117" font-size="11" fill="var(--sl-color-text)">Grupa zabezpieczeń · Analitycy</text>
  <rect x="402" y="136" width="238" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="414" y="157" font-size="11" fill="var(--sl-color-text)">Grupa zabezpieczeń · Administratorzy</text>
  <text x="402" y="192" font-size="10" fill="var(--sl-color-gray-3)">każda grupa = zestaw uprawnień</text>
  <rect x="8" y="104" width="120" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" stroke-dasharray="5 4" />
  <text x="68" y="128" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Dostawca</text>
  <text x="68" y="144" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">tożsamości (SSO)</text>
  <path d="M128 134 C150 134 240 128 262 122" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#ac-arrow)" />
  <text x="150" y="250" font-size="10" fill="var(--sl-color-gray-3)">SSO uwierzytelnia członków, zanim uzyskają dostęp do obszaru roboczego</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Organizacja zawiera obszary robocze; członkowie należą do obszaru roboczego i są przypisywani do grup zabezpieczeń, z których każda jest zestawem uprawnień. Opcjonalne SSO deleguje logowanie do Twojego dostawcy tożsamości.</figcaption>
</figure>

## Od czego zacząć

Jeśli konfigurujesz nową organizację:

1. **[Wyjaśnienie organizacji i obszarów roboczych](/pl/administration/access/overview/organizations-and-workspaces-explained/)** — granice między nimi i kiedy używać każdego z nich
2. **[Zarządzanie członkami obszaru roboczego](/pl/administration/access/overview/managing-workspace-members/)** — zapraszanie użytkowników, przypisywanie ich do obszarów roboczych, nadawanie możliwości
3. **[Zarządzanie grupami zabezpieczeń](/pl/administration/access/managing-security-groups-and-assignments/)** — grupowanie uprawnień i ich przypisywanie

Jeśli integrujesz się z istniejącym dostawcą tożsamości:

- **[Zarządzanie jednokrotnym logowaniem dla organizacji](/pl/administration/access/advanced/managing-single-sign-on-for-organization/)** — przegląd przebiegu SSO
- Przewodniki dla poszczególnych dostawców:
  - [Konfiguracja SAML w Okta](/pl/administration/access/advanced/okta-saml-setup/)
  - [Konfiguracja SAML w Auth0](/pl/administration/access/advanced/auth0-saml-setup/)
  - [Konfiguracja SAML w Microsoft Entra](/pl/administration/access/advanced/entra-saml-setup/)
  - [Konfiguracja SAML w Google](/pl/administration/access/advanced/google-saml-setup/)
  - [Konfiguracja SAML w AWS](/pl/administration/access/advanced/aws-saml-setup/)

## Powiązane

- [Uwierzytelnianie członków](/pl/administration/access/member-authentication/) — opcje hasła i MFA dla członków niekorzystających z SSO
- [Zarządzanie członkami](/pl/administration/access/member-management/) — dodawanie, usuwanie i aktualizowanie członków
- [Tożsamość użytkownika członka](/pl/administration/access/member-user-identity/) — atrybuty tożsamości i sposób ich wykorzystania przez PlaidCloud
- [Raporty użycia](/pl/administration/access/usage-reports/) — kto z czego korzysta w aplikacji, Superset, aplikacjach Panel i JupyterHub
- [Ustawianie wygasania członkostwa](/pl/administration/access/advanced/setting-member-expiration-period/) — zasady automatycznej dezaktywacji
