---
title: Bei PlaidXL anmelden
description: Verbinden Sie PlaidXL mit Ihrem PlaidCloud-Workspace über Ihre E-Mail-Adresse und Ihre gewohnte Anmeldung, einschließlich Single Sign-on und Zwei-Faktor-Authentifizierung, und melden Sie sich ab oder wechseln Sie den Workspace.
sidebar:
  label: Anmelden
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL meldet Sie als Sie selbst an und verwendet dieselbe Anmeldung wie PlaidCloud im Browser. Sie müssen keine Serveradresse eingeben, und in der Arbeitsmappe wird kein Kennwort gespeichert.

## Anmelden

1. Öffnen Sie den Aufgabenbereich über **PlaidCloud → Open PlaidXL** oder über **Konto** in der Gruppe **Verbinden**.
2. Geben Sie unter **Enter your email** die E-Mail-Adresse ein, die Sie für PlaidCloud verwenden, und klicken Sie auf **Sign In**. PlaidXL merkt sich die Adresse für das nächste Mal.
3. Gehört Ihre E-Mail-Adresse zu mehr als einem Workspace, wählen Sie unter **Select a workspace** einen aus und klicken Sie auf **Sign In**. PlaidXL merkt sich Ihre Auswahl. Gehören Sie nur zu einem Workspace, wählt PlaidXL ihn automatisch aus. Ist mit der E-Mail-Adresse kein Workspace verknüpft, weist der Aufgabenbereich darauf hin; prüfen Sie die Adresse und versuchen Sie es erneut.
4. Excel fragt, ob ein Popup-Fenster zugelassen werden soll. Lassen Sie es zu.
5. Melden Sie sich im Popup wie gewohnt an:
   - **PlaidCloud sign-in** — Ihre E-Mail-Adresse, Ihr Kennwort und gegebenenfalls der eingerichtete Zwei-Faktor-Code.
   - **Single sign-on** — Sind Sie bereits bei Ihrer Organisation angemeldet, wird dieser Schritt automatisch durchlaufen. Andernfalls öffnet sich zuerst die Anmeldeseite Ihrer Organisation.
6. Sobald im Popup **Authenticated successfully** angezeigt wird, schließen Sie es, falls es sich nicht von selbst geschlossen hat.

Die Kopfzeile des Aufgabenbereichs zeigt nun Ihren Workspace und das mit der Arbeitsmappe verknüpfte Projekt, daneben Ihr Kontomenü. Weiter geht es mit [Mit Tabellen und Dimensionen arbeiten](/de/reference/cli/plaidxl/retrieve/).

Informationen zum Einrichten der Zwei-Faktor-Authentifizierung oder des Single Sign-on für Ihr Konto finden Sie unter [Authentifizierung von Mitgliedern](/de/administration/access/member-authentication/).

### Mit Ihrem Office-Konto anmelden

Wenn Sie in Office mit einem Geschäftskonto von Microsoft Entra ID angemeldet sind und PlaidXL keine gespeicherte Anmeldung hat, ermittelt PlaidXL Ihre Workspaces anhand dieses Kontos, sodass Sie Ihre E-Mail-Adresse nicht eingeben müssen:

- **Ein Workspace** — PlaidXL beginnt, Sie dort anzumelden. Lassen Sie das Popup zu, wenn Excel danach fragt; mit Single Sign-on wird es automatisch durchlaufen. Klicken Sie in Excel im Web zuerst auf **Continue as** und Ihr Konto.
- **Mehrere Workspaces** — Wurde die Arbeitsmappe zuletzt mit einem davon verwendet, meldet PlaidXL Sie dort an. Andernfalls wählen Sie unter **Select a workspace** einen aus.
- **Kein Workspace** — Der E-Mail-Bildschirm öffnet sich mit bereits ausgefüllter Adresse.

Melden Sie sich mit einer anderen E-Mail-Adresse als Ihrem Office-Konto an, nennt PlaidXL Ihnen die verwendete Adresse. Nachdem Sie sich mit **Log out** abgemeldet haben, wartet PlaidXL darauf, dass Sie sich selbst anmelden.

### Befehle vor der Anmeldung

Sie können in der Multifunktionsleiste jeden PlaidXL-Befehl anklicken, bevor Sie angemeldet sind. PlaidXL öffnet den Aufgabenbereich, um Sie anzumelden oder ein Projekt auszuwählen, und führt den Befehl anschließend in der Zelle aus, von der aus Sie gestartet haben.

## Angemeldet bleiben

PlaidXL hält Sie auf diesem Computer angemeldet und erneuert Ihre Anmeldung im Hintergrund, während Sie arbeiten. Öffnen Sie den Aufgabenbereich in einer späteren Sitzung, gelangen Sie direkt zu Ihren Projekten. Ist Ihre Anmeldung vollständig abgelaufen, fragt PlaidXL erneut nach Ihrer E-Mail-Adresse. Ein kurzes Netzwerkproblem während der Erneuerung meldet Sie nicht ab; PlaidXL versucht es erneut.

## Was Sie sehen können

PlaidXL liest mit Ihren Berechtigungen. Sie sehen die Projekte, die Sie in PlaidCloud öffnen können, sowie die darin enthaltenen Tabellen und Dimensionen, und nichts darüber hinaus. Fehlt ein Projekt oder eine Tabelle, bitten Sie einen Projektinhaber um Zugriff. Wie die Workspace-Mitgliedschaft funktioniert, erfahren Sie unter [Organisationen und Workspaces erklärt](/de/administration/access/overview/organizations-and-workspaces-explained/).

## Abmelden oder Workspace wechseln

Klicken Sie oben rechts im Aufgabenbereich auf das Kontomenü (die drei Punkte). Es zeigt Ihren Namen und Workspace mit drei Befehlen:

- **Keyboard shortcuts** listet die PlaidXL-Tastenkombinationen auf, damit Sie sie ändern können. Siehe [Tastenkombinationen](/de/reference/cli/plaidxl/ribbon/#tastenkombinationen).
- **Switch workspace** meldet Sie ab und kehrt zum E-Mail-Bildschirm zurück, damit Sie unter **Select a workspace** einen anderen Workspace auswählen können. Melden Sie sich auf Aufforderung beim neuen Workspace an. Der Wechsel zurück zu einem Workspace, bei dem Sie bereits angemeldet waren, erfordert keine neue Anmeldung, und wenn Sie die Anmeldung abbrechen, bleiben Sie im bisherigen Workspace.
- **Log out** löscht Ihre Anmeldung und kehrt zum E-Mail-Bildschirm zurück.

Jede Anmeldung gilt nur für den Workspace, in dem sie erfolgt ist. Nach dieser Änderung melden sich alle einmalig neu an. Sind Sie abgemeldet, zeigt **Speichern** den Hinweis **Sign in to PlaidCloud to save.**, und beim Abrufen einer Dimension erscheint **Sign in to PlaidCloud to retrieve a dimension.**

Ihre Anmeldung wird von allen geöffneten Arbeitsmappen gemeinsam genutzt, aber jede Arbeitsmappe behält ihr eigenes Projekt. Das Projekt einer Arbeitsmappe gehört zu einem Workspace. Nach einem Wechsel hat eine Arbeitsmappe, die mit einem Projekt im bisherigen Workspace verknüpft war, daher kein Projekt, bis Sie eines auswählen. Siehe [Das Projekt gehört zur Arbeitsmappe](/de/reference/cli/plaidxl/retrieve/#das-projekt-gehört-zur-arbeitsmappe).

## Helles und dunkles Design

Der Aufgabenbereich folgt Ihrem Office-Design und ändert sich, wenn Sie es ändern.

## Tastatur und Screenreader

Zeilen in den Listen der Projekte, Tabellen und Dimensionen erhalten den Tastaturfokus und reagieren auf **Enter** und **Leerzeichen**. Ein Screenreader kündigt eine ausgewählte Zeile an, und ausgewählte Zustände und Warnzustände werden zusätzlich zur Farbe durch ein Symbol gekennzeichnet.

## Verwandte Themen

- [PlaidXL installieren](/de/reference/cli/plaidxl/install/) — das Add-in hinzufügen und den Aufgabenbereich öffnen
- [Fehlerbehebung](/de/reference/cli/plaidxl/troubleshooting/) — wenn sich das Anmelde-Popup nicht öffnet oder ein Workspace fehlt
- [Workspaces anzeigen und verwalten](/de/administration/access/overview/viewing-and-managing-workspaces/) — die Workspaces, denen Sie angehören
