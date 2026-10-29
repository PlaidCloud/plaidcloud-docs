---
title: Deactivate Workspace Members
description: Deaktivieren Sie Workspace-Mitglieder, die in einer Projekttabelle aufgeführt sind, abgeglichen über E-Mail-Adresse oder Benutzername.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/deactivate-workspace-members.md
---

import { Aside } from '@astrojs/starlight/components';

## Beschreibung

Deaktiviert die Workspace-Mitglieder, die in einer Quelltabelle genannt sind. Verwenden Sie den Schritt, um das Offboarding anhand einer maßgeblichen Liste zu automatisieren — etwa einem HR-Extrakt oder einer Zugriffsprüfung —, anstatt Personen von Hand zu deaktivieren.

Kombinieren Sie ihn mit [Get Workspace Members](/de/reference/workflow-steps/general/get-workspace-members/), um die Liste derjenigen zu erstellen, die keinen Zugriff mehr haben sollen.

<Aside type="caution" title="Dies entzieht den Zugriff">
  Jedes übereinstimmende Mitglied verliert den Zugriff, sobald der Schritt
  ausgeführt wird. Prüfen Sie vor dem Planen dieses Schritts, dass die
  Quelltabelle nur die Personen enthält, die Sie beabsichtigen.
</Aside>

## Workspace-Admins in der Liste

[Nur ein Workspace-Admin kann einen Workspace-Admin deaktivieren](/de/administration/access/member-management/#einen-workspace-administrator-ändern). Wenn der Schritt ohne Workspace-Admin-Rechte ausgeführt wird und seine Liste Admins enthält, lässt er diese Admins aktiv, deaktiviert alle anderen und endet dann mit einem Fehler. Die Fehlermeldung nennt, wie viele Mitglieder er deaktiviert hat, und führt jeden Admin auf, den er aktiv gelassen hat. Die deaktivierten Mitglieder bleiben deaktiviert. Um einen Admin zu deaktivieren, lassen Sie dies von einem Workspace-Admin in Identity vornehmen.

## Konfiguration

### Suchparameter für Mitglieder

Legt fest, wie Zeilen in der Quelltabelle Mitgliedern zugeordnet werden. Wählen Sie eine Option:

- **E-Mail** (Standard)
- **Benutzername**

## Verwandte Themen

- [Allgemeine Schritte](/de/reference/workflow-steps/general/)
- [Get Workspace Members](/de/reference/workflow-steps/general/get-workspace-members/)
- [Mitgliederverwaltung](/de/administration/access/)
