---
title: Bei PlaidXL anmelden
description: Verbinden Sie PlaidXL mit Ihrem PlaidCloud-Workspace über Ihre E-Mail-Adresse und Ihre gewohnte Anmeldung, einschließlich Single Sign-on und Zwei-Faktor-Authentifizierung, und melden Sie sich ab oder wechseln Sie den Workspace.
sidebar:
  label: Anmelden
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL meldet Sie als Sie selbst an, mit derselben Anmeldung, die Sie für PlaidCloud im Browser verwenden. Sie müssen keine Serveradresse eingeben, und in der Arbeitsmappe wird kein Passwort gespeichert.

## Anmelden

1. Öffnen Sie den Aufgabenbereich: **PlaidCloud → Open PlaidXL** oder **Konto** in der Gruppe **Verbinden**.
2. Geben Sie unter **Enter your email** die E-Mail-Adresse ein, die Sie für PlaidCloud verwenden, und klicken Sie auf **Sign In**. PlaidXL merkt sich die Adresse für das nächste Mal.
3. Wenn Ihre E-Mail-Adresse zu mehreren Workspaces gehört, wählen Sie unter **Select a workspace** einen aus und klicken Sie auf **Sign In**. PlaidXL merkt sich Ihre Auswahl. Wenn Sie zu einem einzigen Workspace gehören, wählt PlaidXL ihn für Sie aus. Wenn der E-Mail-Adresse kein Workspace zugeordnet ist, weist der Aufgabenbereich darauf hin; prüfen Sie die Adresse und versuchen Sie es erneut.
4. Excel fragt, ob ein Pop-up-Fenster zugelassen werden soll. Lassen Sie es zu.
5. Melden Sie sich im Pop-up so an, wie Sie es gewohnt sind:
   - **PlaidCloud-Anmeldung** – Ihre E-Mail-Adresse, Ihr Passwort und gegebenenfalls ein von Ihnen eingerichteter Zwei-Faktor-Code.
   - **Single Sign-on** – Wenn Sie bereits bei Ihrer Organisation angemeldet sind, wird dieser Schritt ohne Eingabe durchlaufen. Andernfalls öffnet sich zuerst die Anmeldeseite Ihrer Organisation.
6. Wenn das Pop-up **Authenticated successfully** anzeigt, schließen Sie es, falls es sich nicht von selbst geschlossen hat.

Die Kopfzeile des Aufgabenbereichs zeigt jetzt Ihren Workspace und das mit der Arbeitsmappe verknüpfte Projekt an, daneben Ihr Kontomenü. Weiter geht es mit [Mit Tabellen und Dimensionen arbeiten](/de/reference/cli/plaidxl/retrieve/).

Informationen zum Einrichten der Zwei-Faktor-Authentifizierung oder von Single Sign-on für Ihr Konto finden Sie unter [Mitgliederauthentifizierung](/de/administration/access/member-authentication/).

### Mit Ihrem Office-Konto anmelden

Wenn Sie in Office mit einem Geschäftskonto von Microsoft Entra ID angemeldet sind und PlaidXL keine gespeicherte Anmeldung hat, ermittelt PlaidXL Ihre Workspaces anhand dieses Kontos, sodass Sie Ihre E-Mail-Adresse nicht eingeben müssen:

- **Ein Workspace** – PlaidXL beginnt, Sie dort anzumelden. Lassen Sie das Pop-up zu, wenn Excel danach fragt; mit Single Sign-on wird es ohne Eingabe durchlaufen. Klicken Sie in Excel im Web zuerst auf **Continue as** und Ihr Konto.
- **Mehrere Workspaces** – Wurde die Arbeitsmappe zuletzt mit einem davon verwendet, meldet PlaidXL Sie dort an. Andernfalls wählen Sie unter **Select a workspace** einen aus.
- **Kein Workspace** – Der E-Mail-Bildschirm öffnet sich mit bereits eingetragener Adresse.

Wenn Sie sich mit einer anderen E-Mail-Adresse als der Ihres Office-Kontos anmelden, teilt PlaidXL mit, um welche Adresse es sich handelt. Nachdem Sie sich mit **Log out** abgemeldet haben, wartet PlaidXL darauf, dass Sie sich selbst anmelden.

### Befehle vor der Anmeldung

Sie können auf jeden PlaidXL-Befehl im Menüband klicken, bevor Sie angemeldet sind. PlaidXL öffnet den Aufgabenbereich, um Sie anzumelden oder ein Projekt auszuwählen, und führt den Befehl anschließend auf der Zelle aus, in der Sie begonnen haben.

## Angemeldet bleiben

PlaidXL hält Sie auf diesem Computer angemeldet und erneuert Ihre Anmeldung im Hintergrund, während Sie arbeiten. Wenn Sie den Aufgabenbereich in einer späteren Sitzung öffnen, gelangen Sie direkt zu Ihren Projekten. Ist Ihre Anmeldung vollständig abgelaufen, fragt PlaidXL erneut nach Ihrer E-Mail-Adresse. Ein kurzes Netzwerkproblem beim Erneuern Ihrer Anmeldung meldet Sie nicht ab; PlaidXL versucht es erneut.

## Was Sie sehen können

PlaidXL liest mit Ihren Berechtigungen. Sie sehen die Projekte, die Sie in PlaidCloud öffnen können, und die darin enthaltenen Tabellen und Dimensionen, nicht mehr. Fehlt ein Projekt oder eine Tabelle, bitten Sie einen Projekteigentümer um Zugriff. Wie die Mitgliedschaft in einem Workspace funktioniert, erfahren Sie unter [Organisationen und Workspaces erklärt](/de/administration/access/overview/organizations-and-workspaces-explained/).

## Abmelden oder Workspace wechseln

Klicken Sie oben rechts im Aufgabenbereich auf das Kontomenü (die drei Punkte). Es zeigt Ihren Namen und Ihren Workspace sowie drei Befehle:

- **Keyboard shortcuts** listet die PlaidXL-Tastenkombinationen auf, damit Sie sie ändern können. Siehe [Tastenkombinationen](/de/reference/cli/plaidxl/ribbon/#tastenkombinationen).
- **Switch workspace** meldet Sie ab und führt zurück zum E-Mail-Bildschirm, sodass Sie unter **Select a workspace** einen anderen Workspace auswählen können. Melden Sie sich auf Nachfrage beim neuen Workspace an. Der Wechsel zurück zu einem Workspace, bei dem Sie bereits angemeldet waren, erfordert keine neue Anmeldung, und wenn Sie die Anmeldung abbrechen, bleiben Sie im bisherigen Workspace.
- **Log out** löscht Ihre Anmeldung und führt zurück zum E-Mail-Bildschirm.

Jede Anmeldung gilt nur für den Workspace, in dem sie erfolgt ist. Nach dieser Änderung meldet sich jeder einmal neu an. Wenn Sie abgemeldet sind, lautet die Meldung bei **Speichern** **Sign in to PlaidCloud to save.**, und beim Abrufen einer Dimension lautet sie **Sign in to PlaidCloud to retrieve a dimension.**

Ihre Anmeldung wird von allen geöffneten Arbeitsmappen gemeinsam genutzt, aber jede Arbeitsmappe behält ihr eigenes Projekt. Das Projekt einer Arbeitsmappe gehört zu einem Workspace. Nach einem Wechsel hat eine Arbeitsmappe, die mit einem Projekt im alten Workspace verknüpft war, daher kein Projekt, bis Sie eines auswählen. Siehe [Das Projekt gehört zur Arbeitsmappe](/de/reference/cli/plaidxl/retrieve/#das-projekt-gehört-zur-arbeitsmappe).

## Helles und dunkles Design

Der Aufgabenbereich entspricht der PlaidCloud-Webanwendung, mit Markenblau, Registerkarten und Listen im Seitenleistenstil sowie Tabellen, Dimensionen, Projekten und Spalten in begrenzten, scrollbaren Karten. Er folgt Ihrem Office-Design und ändert sich, wenn Sie es ändern. In einem schmalen Aufgabenbereich stehen die Registerkarten in zwei Zeilen zu je drei nebeneinander; ab einer Breite von 560 Pixeln stehen sie in einer Zeile.

## Tastatur und Screenreader

Zeilen in den Listen der Projekte, Tabellen und Dimensionen können den Tastaturfokus erhalten und reagieren auf die **Eingabetaste** und die **Leertaste**. Eine ausgewählte Zeile wird von einem Screenreader angesagt. Ausgewählte Zustände und Warnzustände werden zusätzlich zur Farbe durch ein Symbol gekennzeichnet, und das Steuerelement mit dem Tastaturfokus hat einen deutlichen Fokusrahmen.

## Zahlen

Jede Zahl, die der Aufgabenbereich anzeigt, etwa Zeilen- und Spaltenanzahlen sowie Meldungen zu Aktualisierung, Neuberechnung, Explain, Formeln, Bericht und Planung, folgt der Anzeigesprache von Excel. Das deutsche Excel zeigt beispielsweise 4.812.233. In Zellen geschriebene Werte ändern sich nicht.

## Verwandte Themen

- [PlaidXL installieren](/de/reference/cli/plaidxl/install/) – das Add-in hinzufügen und den Aufgabenbereich öffnen
- [Fehlerbehebung](/de/reference/cli/plaidxl/troubleshooting/) – wenn sich das Anmelde-Pop-up nicht öffnet oder ein Workspace fehlt
- [Workspaces anzeigen und verwalten](/de/administration/access/overview/viewing-and-managing-workspaces/) – die Workspaces, denen Sie angehören
