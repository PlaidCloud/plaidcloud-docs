---
title: Administración de identidades y accesos (IAM)
description: Administre los controles de identidad y acceso de PlaidCloud, incluidos la autenticación de usuarios, los permisos basados en roles y los grupos de seguridad.
sidebar:
  label: Descripción general
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/administration/access/index.md
---

Los controles de acceso de PlaidCloud se organizan en torno a unos pocos conceptos fundamentales:

- **Organización**: el límite superior de facturación e identidad. Una organización contiene espacios de trabajo y miembros.
- **Espacio de trabajo**: un entorno aislado donde se realiza el trabajo. Los miembros obtienen acceso a nivel del espacio de trabajo.
- **Miembro**: un usuario con credenciales que pertenece a uno o más espacios de trabajo en una o más organizaciones.
- **Grupo de seguridad**: un conjunto de permisos dentro de un espacio de trabajo. Los miembros se asignan a grupos de seguridad para otorgarles capacidades específicas.
- **Inicio de sesión único (SSO)**: federación opcional basada en SAML que delega la autenticación en su proveedor de identidad (Okta, Auth0, Microsoft Entra, Google, AWS).

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 260" role="img" aria-label="Modelo de acceso de PlaidCloud. Una organización contiene un espacio de trabajo. Dentro del espacio de trabajo, los miembros se asignan a grupos de seguridad, cada uno de los cuales agrupa un conjunto de permisos. El inicio de sesión único opcional delega la autenticación en un proveedor de identidad externo." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="ac-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="150" y="22" width="522" height="216" rx="12" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="164" y="42" font-size="12" font-weight="700" fill="var(--sl-color-text)">Organización</text>
  <rect x="176" y="56" width="480" height="166" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="190" y="76" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Espacio de trabajo</text>
  <rect x="196" y="104" width="150" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="271" y="130" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Miembros</text>
  <text x="271" y="147" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">personas con acceso</text>
  <path d="M346 128 L400 128" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#ac-arrow)" />
  <text x="373" y="120" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">asignados a</text>
  <rect x="402" y="96" width="238" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="414" y="117" font-size="11" fill="var(--sl-color-text)">Grupo de seguridad · Analistas</text>
  <rect x="402" y="136" width="238" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="414" y="157" font-size="11" fill="var(--sl-color-text)">Grupo de seguridad · Administradores</text>
  <text x="402" y="192" font-size="10" fill="var(--sl-color-gray-3)">cada grupo = un conjunto de permisos</text>
  <rect x="8" y="104" width="120" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" stroke-dasharray="5 4" />
  <text x="68" y="128" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Proveedor de</text>
  <text x="68" y="144" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">identidad (SSO)</text>
  <path d="M128 134 C150 134 240 128 262 122" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#ac-arrow)" />
  <text x="150" y="250" font-size="10" fill="var(--sl-color-gray-3)">El SSO autentica a los miembros antes de que lleguen al espacio de trabajo</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Una organización contiene espacios de trabajo; los miembros pertenecen a un espacio de trabajo y se asignan a grupos de seguridad, cada uno un conjunto de permisos. El SSO opcional delega el inicio de sesión en su proveedor de identidad.</figcaption>
</figure>

## Por dónde empezar

Si está configurando una organización nueva:

1. **[Organizaciones y espacios de trabajo explicados](/es/administration/access/overview/organizations-and-workspaces-explained/)**: los límites entre ellos y cuándo usar cada uno
2. **[Administración de los miembros del espacio de trabajo](/es/administration/access/overview/managing-workspace-members/)**: invite a usuarios, asígnelos a espacios de trabajo y otorgue capacidades
3. **[Administración de grupos de seguridad](/es/administration/access/managing-security-groups-and-assignments/)**: agrupe permisos y asígnelos

Si va a realizar la integración con un proveedor de identidad existente:

- **[Administrar el inicio de sesión único de la organización](/es/administration/access/advanced/managing-single-sign-on-for-organization/)**: descripción general del flujo de SSO
- Guías específicas de cada proveedor:
  - [Configuración de SAML con Okta](/es/administration/access/advanced/okta-saml-setup/)
  - [Configuración de SAML con Auth0](/es/administration/access/advanced/auth0-saml-setup/)
  - [Configuración de SAML con Microsoft Entra](/es/administration/access/advanced/entra-saml-setup/)
  - [Configuración de SAML con Google](/es/administration/access/advanced/google-saml-setup/)
  - [Configuración de SAML con AWS](/es/administration/access/advanced/aws-saml-setup/)

## Temas relacionados

- [Autenticación de miembros](/es/administration/access/member-authentication/): opciones de contraseña y MFA para los miembros que no usan SSO
- [Administración de miembros](/es/administration/access/member-management/): agregar, quitar y actualizar miembros
- [Identidad de usuario del miembro](/es/administration/access/member-user-identity/): atributos de identidad y cómo los usa PlaidCloud
- [Informes de uso](/es/administration/access/usage-reports/): quién usa qué en la aplicación, Superset, las aplicaciones de Panel y JupyterHub
- [Establecer la expiración de miembros](/es/administration/access/advanced/setting-member-expiration-period/): políticas de desactivación automática
