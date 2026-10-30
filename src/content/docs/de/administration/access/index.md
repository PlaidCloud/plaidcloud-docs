---
title: Identitäts- und Zugriffsverwaltung (IAM)
description: Verwalten Sie PlaidCloud-Identitäts- und Zugriffskontrollen, darunter Benutzerauthentifizierung, rollenbasierte Berechtigungen und Sicherheitsgruppen.
sidebar:
  label: Überblick
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/administration/access/index.md
---

Die Zugriffskontrollen von PlaidCloud sind um einige zentrale Konzepte herum organisiert:

- **Organisation** – die oberste Abrechnungs- und Identitätsgrenze. Eine Organisation enthält Workspaces und Mitglieder.
- **Workspace** – eine isolierte Umgebung, in der die eigentliche Arbeit stattfindet. Mitglieder erhalten Zugriff auf Workspace-Ebene.
- **Mitglied** – ein Benutzer mit Anmeldedaten, der zu einem oder mehreren Workspaces in einer oder mehreren Organisationen gehört.
- **Sicherheitsgruppe** – ein Bündel von Berechtigungen innerhalb eines Workspace. Mitglieder werden Sicherheitsgruppen zugewiesen, um ihnen bestimmte Fähigkeiten zu gewähren.
- **Single Sign-On (SSO)** – optionale SAML-basierte Föderation, die die Authentifizierung an Ihren Identitätsanbieter delegiert (Okta, Auth0, Microsoft Entra, Google, AWS).

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 260" role="img" aria-label="Das PlaidCloud-Zugriffsmodell. Eine Organisation enthält einen Workspace. Innerhalb des Workspace werden Mitglieder Sicherheitsgruppen zugewiesen, die jeweils ein Bündel von Berechtigungen enthalten. Optionales Single Sign-On delegiert die Authentifizierung an einen externen Identitätsanbieter." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="ac-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="150" y="22" width="522" height="216" rx="12" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="164" y="42" font-size="12" font-weight="700" fill="var(--sl-color-text)">Organisation</text>
  <rect x="176" y="56" width="480" height="166" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="190" y="76" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Workspace</text>
  <rect x="196" y="104" width="150" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="271" y="130" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Mitglieder</text>
  <text x="271" y="147" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">Personen mit Zugriff</text>
  <path d="M346 128 L400 128" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#ac-arrow)" />
  <text x="373" y="120" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">zugewiesen zu</text>
  <rect x="402" y="96" width="238" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="414" y="117" font-size="11" fill="var(--sl-color-text)">Sicherheitsgruppe · Analysten</text>
  <rect x="402" y="136" width="238" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="414" y="157" font-size="11" fill="var(--sl-color-text)">Sicherheitsgruppe · Administratoren</text>
  <text x="402" y="192" font-size="10" fill="var(--sl-color-gray-3)">jede Gruppe = ein Bündel von Berechtigungen</text>
  <rect x="8" y="104" width="120" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" stroke-dasharray="5 4" />
  <text x="68" y="128" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Identitäts-</text>
  <text x="68" y="144" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">anbieter (SSO)</text>
  <path d="M128 134 C150 134 240 128 262 122" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#ac-arrow)" />
  <text x="150" y="250" font-size="10" fill="var(--sl-color-gray-3)">SSO authentifiziert Mitglieder, bevor sie den Workspace erreichen</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Eine Organisation enthält Workspaces; Mitglieder gehören zu einem Workspace und werden Sicherheitsgruppen zugewiesen, die jeweils ein Bündel von Berechtigungen darstellen. Optionales SSO delegiert die Anmeldung an Ihren Identitätsanbieter.</figcaption>
</figure>

## Wo Sie beginnen

Wenn Sie eine neue Organisation einrichten:

1. **[Organisationen und Workspaces erklärt](/de/administration/access/overview/organizations-and-workspaces-explained/)** – die Abgrenzung zwischen beiden und wann Sie welche verwenden
2. **[Workspace-Mitglieder verwalten](/de/administration/access/overview/managing-workspace-members/)** – Benutzer einladen, Workspaces zuweisen, Fähigkeiten gewähren
3. **[Sicherheitsgruppen verwalten](/de/administration/access/managing-security-groups-and-assignments/)** – Berechtigungen bündeln und zuweisen

Wenn Sie einen bestehenden Identitätsanbieter integrieren:

- **[Single Sign-On für die Organisation verwalten](/de/administration/access/advanced/managing-single-sign-on-for-organization/)** – Überblick über den SSO-Ablauf
- Anbieterspezifische Leitfäden:
  - [Okta-SAML-Einrichtung](/de/administration/access/advanced/okta-saml-setup/)
  - [Auth0-SAML-Einrichtung](/de/administration/access/advanced/auth0-saml-setup/)
  - [Microsoft-Entra-SAML-Einrichtung](/de/administration/access/advanced/entra-saml-setup/)
  - [Google-SAML-Einrichtung](/de/administration/access/advanced/google-saml-setup/)
  - [AWS-SAML-Einrichtung](/de/administration/access/advanced/aws-saml-setup/)

## Verwandte Themen

- [Mitgliederauthentifizierung](/de/administration/access/member-authentication/) – Kennwort- und MFA-Optionen für Mitglieder ohne SSO
- [Mitgliederverwaltung](/de/administration/access/member-management/) – Mitglieder hinzufügen, entfernen und aktualisieren
- [Benutzeridentität von Mitgliedern](/de/administration/access/member-user-identity/) – Identitätsattribute und wie PlaidCloud sie verwendet
- [Nutzungsberichte](/de/administration/access/usage-reports/) – wer was in der App, in Superset, in Panel-Apps und in JupyterHub nutzt
- [Ablauf von Mitgliedern festlegen](/de/administration/access/advanced/setting-member-expiration-period/) – Richtlinien für die automatische Deaktivierung
