---
title: Bei PlaidXL anmelden
description: Verbinden Sie PlaidXL mit Ihrem PlaidCloud-Workspace über Ihre E-Mail-Adresse und Ihre gewohnte Anmeldung, einschließlich Single Sign-on und Zwei-Faktor-Authentifizierung, und melden Sie sich ab oder wechseln Sie den Workspace.
sidebar:
  label: Anmelden
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL meldet Sie unter Ihrer eigenen Identität an, mit derselben Anmeldung, die Sie für PlaidCloud im Browser verwenden. Sie müssen keine Serveradresse eingeben, und in der Arbeitsmappe wird kein Passwort gespeichert.

## Anmelden

1. Öffnen Sie den Aufgabenbereich: **PlaidCloud → Show Taskpane**.
2. Geben Sie unter **Enter your email** die E-Mail-Adresse ein, die Sie für PlaidCloud verwenden, und klicken Sie auf **Sign In**.
3. Wenn Ihre E-Mail-Adresse zu mehr als einem Workspace gehört, wählen Sie unter **Select a tenant** einen aus und klicken Sie auf **Sign In**. (Ein *Tenant* ist in PlaidXL Ihr PlaidCloud-Workspace.) Gehören Sie nur einem Workspace an, wählt PlaidXL ihn automatisch aus.
4. Excel fragt, ob ein Popup-Fenster zugelassen werden soll. Lassen Sie es zu.
5. Melden Sie sich im Popup wie gewohnt an:
   - **PlaidCloud-Anmeldung** — Ihre E-Mail-Adresse, Ihr Passwort und gegebenenfalls ein von Ihnen eingerichteter Zwei-Faktor-Code.
   - **Single Sign-on** — Wenn Sie bereits in Ihrer Organisation angemeldet sind, wird dieser Schritt direkt durchlaufen. Andernfalls öffnet sich zuerst die Anmeldeseite Ihrer Organisation.
6. Wenn das Popup **Authenticated successfully** anzeigt, schließen Sie es, falls es sich nicht von selbst geschlossen hat.

Der Aufgabenbereich zeigt nun **Connected to** mit Ihrer Workspace-ID **as** Ihrem Benutzernamen an, darunter die Liste Ihrer Projekte. Fahren Sie mit [Mit Tabellen und Dimensionen arbeiten](/de/reference/cli/plaidxl/retrieve/) fort.

Informationen zum Einrichten der Zwei-Faktor-Authentifizierung oder von Single Sign-on für Ihr Konto finden Sie unter [Mitgliederauthentifizierung](/de/administration/access/member-authentication/).

## Angemeldet bleiben

PlaidXL hält Sie auf diesem Computer angemeldet und erneuert Ihre Anmeldung im Hintergrund, während Sie arbeiten. Wenn Sie den Aufgabenbereich in einer späteren Sitzung öffnen, gelangen Sie direkt zu Ihren Projekten. Ist Ihre Anmeldung vollständig abgelaufen, fragt PlaidXL erneut nach Ihrer E-Mail-Adresse.

## Was Sie sehen können

PlaidXL liest mit Ihren Berechtigungen. Sie sehen die Projekte, die Sie in PlaidCloud öffnen können, sowie die darin enthaltenen Tabellen und Dimensionen, und nicht mehr. Wenn ein Projekt oder eine Tabelle fehlt, bitten Sie einen Projekteigentümer um Zugriff. Wie die Workspace-Mitgliedschaft funktioniert, erfahren Sie unter [Organisationen und Workspaces erklärt](/de/administration/access/overview/organizations-and-workspaces-explained/).

## Abmelden oder Workspace wechseln

Klicken Sie oben im Aufgabenbereich auf **Logout**. PlaidXL löscht Ihre Anmeldung und kehrt zum E-Mail-Bildschirm zurück.

Um in einem anderen Workspace zu arbeiten, melden Sie sich ab, melden Sie sich erneut an und wählen Sie unter **Select a tenant** den anderen Workspace. PlaidXL arbeitet immer mit einem Workspace gleichzeitig, für alle geöffneten Arbeitsmappen.

## Helles und dunkles Design

Der Aufgabenbereich folgt Ihrem Office-Design. Um ihn auf hell oder dunkel festzulegen, klicken Sie oben links im Aufgabenbereich auf die Schaltfläche mit der Sonne oder dem Mond.

## Verwandte Themen

- [PlaidXL installieren](/de/reference/cli/plaidxl/install/) — das Add-in hinzufügen und den Aufgabenbereich öffnen
- [Fehlerbehebung](/de/reference/cli/plaidxl/troubleshooting/) — wenn das Anmelde-Popup nicht erscheint oder ein Workspace fehlt
- [Workspaces anzeigen und verwalten](/de/administration/access/overview/viewing-and-managing-workspaces/) — die Workspaces, denen Sie angehören
