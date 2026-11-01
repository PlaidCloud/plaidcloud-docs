---
title: Bei PlaidXL anmelden
description: Verbinden Sie PlaidXL mit Ihrem PlaidCloud-Workspace über Ihre E-Mail-Adresse und Ihre übliche Anmeldung, einschließlich Single Sign-on und Zwei-Faktor-Authentifizierung, und melden Sie sich ab oder wechseln Sie den Workspace.
sidebar:
  label: Anmelden
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL meldet Sie als Sie selbst an, mit derselben Anmeldung, die Sie für PlaidCloud in einem Browser verwenden. Sie müssen keine Serveradresse eingeben, und in der Arbeitsmappe wird kein Passwort gespeichert.

## Anmelden

1. Öffnen Sie den Aufgabenbereich: **PlaidCloud → Open PlaidXL**.
2. Geben Sie unter **Enter your email** die E-Mail-Adresse ein, die Sie für PlaidCloud verwenden, und klicken Sie auf **Sign In**. PlaidXL merkt sich die Adresse für das nächste Mal.
3. Wenn Ihre E-Mail-Adresse zu mehreren Workspaces gehört, wählen Sie unter **Select a workspace** einen aus und klicken Sie auf **Sign In**. PlaidXL merkt sich Ihre Auswahl. Wenn Sie einem einzigen Workspace angehören, wählt PlaidXL ihn für Sie aus. Wenn der E-Mail-Adresse kein Workspace zugeordnet ist, teilt der Aufgabenbereich dies mit; prüfen Sie die Adresse und versuchen Sie es erneut.
4. Excel fragt, ob ein Pop-up-Fenster zugelassen werden soll. Lassen Sie es zu.
5. Melden Sie sich im Pop-up wie gewohnt an:
   - **PlaidCloud-Anmeldung** – Ihre E-Mail-Adresse, Ihr Passwort und gegebenenfalls ein von Ihnen eingerichteter Zwei-Faktor-Code.
   - **Single Sign-on** – wenn Sie bereits bei Ihrer Organisation angemeldet sind, wird dieser Schritt direkt durchlaufen. Andernfalls öffnet sich zuerst die Anmeldeseite Ihrer Organisation.
6. Wenn das Pop-up **Authenticated successfully** anzeigt, schließen Sie es, falls es sich nicht selbst geschlossen hat.

Die Kopfzeile des Aufgabenbereichs zeigt nun Ihren Workspace und das mit der Arbeitsmappe verknüpfte Projekt an, daneben Ihr Kontomenü. Weiter geht es mit [Mit Tabellen und Dimensionen arbeiten](/de/reference/cli/plaidxl/retrieve/).

Informationen zum Einrichten der Zwei-Faktor-Authentifizierung oder von Single Sign-on für Ihr Konto finden Sie unter [Mitgliederauthentifizierung](/de/administration/access/member-authentication/).

## Angemeldet bleiben

PlaidXL hält Sie auf diesem Computer angemeldet und erneuert Ihre Anmeldung im Hintergrund, während Sie arbeiten. Wenn Sie den Aufgabenbereich in einer späteren Sitzung öffnen, gelangt er direkt zu Ihren Projekten. Wenn Ihre Anmeldung vollständig abgelaufen ist, fragt PlaidXL erneut nach Ihrer E-Mail-Adresse. Ein kurzes Netzwerkproblem beim Erneuern Ihrer Anmeldung meldet Sie nicht ab; PlaidXL versucht es erneut.

## Was Sie sehen können

PlaidXL liest mit Ihren Berechtigungen. Sie sehen die Projekte, die Sie in PlaidCloud öffnen können, sowie die darin enthaltenen Tabellen und Dimensionen, und nicht mehr. Wenn ein Projekt oder eine Tabelle fehlt, bitten Sie einen Projektinhaber um Zugriff. Wie die Workspace-Mitgliedschaft funktioniert, erfahren Sie unter [Organisationen und Workspaces erklärt](/de/administration/access/overview/organizations-and-workspaces-explained/).

## Abmelden oder Workspace wechseln

Klicken Sie oben rechts im Aufgabenbereich auf das Kontomenü (die drei Punkte). Es zeigt Ihren Namen und Workspace mit zwei Befehlen:

- **Log out** löscht Ihre Anmeldung und kehrt zum E-Mail-Bildschirm zurück.
- **Switch workspace** meldet Sie ab und kehrt zum E-Mail-Bildschirm zurück, sodass Sie unter **Select a workspace** einen anderen Workspace auswählen können.

Ihre Anmeldung wird von jeder geöffneten Arbeitsmappe gemeinsam genutzt, aber jede Arbeitsmappe behält ihr eigenes Projekt. Das Projekt einer Arbeitsmappe gehört zu einem Workspace. Nach dem Wechsel hat eine Arbeitsmappe, die mit einem Projekt im alten Workspace verknüpft ist, daher kein Projekt, bis Sie eines auswählen. Siehe [Das Projekt gehört zur Arbeitsmappe](/de/reference/cli/plaidxl/retrieve/#das-projekt-gehört-zur-arbeitsmappe).

## Helles und dunkles Design

Der Aufgabenbereich folgt Ihrem Office-Design und ändert sich, wenn Sie es ändern.

## Tastatur und Screenreader

Zeilen in den Listen der Projekte, Tabellen und Dimensionen erhalten den Tastaturfokus und reagieren auf **Enter** und **Leerzeichen**. Eine ausgewählte Zeile wird von einem Screenreader angesagt, und ausgewählte Zustände und Warnzustände tragen neben einer Farbe auch ein Symbol.

## Verwandte Themen

- [PlaidXL installieren](/de/reference/cli/plaidxl/install/) – das Add-in hinzufügen und den Aufgabenbereich öffnen
- [Fehlerbehebung](/de/reference/cli/plaidxl/troubleshooting/) – wenn das Anmelde-Pop-up nicht geöffnet wird oder ein Workspace fehlt
- [Workspaces anzeigen und verwalten](/de/administration/access/overview/viewing-and-managing-workspaces/) – die Workspaces, denen Sie angehören
