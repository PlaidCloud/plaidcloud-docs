---
title: Bei PlaidXL anmelden
description: Verbinden Sie PlaidXL mit Ihrem PlaidCloud-Workspace per E-Mail-Adresse und Ihrer gewohnten Anmeldung, auch mit Single Sign-on und Zwei-Faktor-Authentifizierung, und melden Sie sich wieder ab oder wechseln Sie den Workspace.
sidebar:
  label: Anmelden
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL meldet Sie als Sie selbst an, mit derselben Anmeldung, die Sie für PlaidCloud im Browser verwenden. Sie müssen keine Serveradresse eingeben, und in der Arbeitsmappe wird kein Kennwort gespeichert.

## Anmelden

1. Öffnen Sie den Aufgabenbereich: **PlaidCloud → Open PlaidXL** oder **Konto** in der Gruppe **Verbinden**.
2. Geben Sie unter **Enter your email** die E-Mail-Adresse ein, die Sie für PlaidCloud verwenden, und klicken Sie auf **Sign In**. PlaidXL merkt sich die Adresse für das nächste Mal.
3. Wenn Ihre E-Mail-Adresse zu mehr als einem Workspace gehört, wählen Sie unter **Select a workspace** einen aus und klicken Sie auf **Sign In**. PlaidXL merkt sich Ihre Auswahl. Wenn Sie zu einem einzigen Workspace gehören, wählt PlaidXL ihn für Sie aus. Ist der E-Mail-Adresse kein Workspace zugeordnet, weist der Aufgabenbereich darauf hin; prüfen Sie die Adresse und versuchen Sie es erneut.
4. Excel fragt, ob ein Popup-Fenster zugelassen werden soll. Lassen Sie es zu.
5. Melden Sie sich im Popup-Fenster wie gewohnt an:
   - **PlaidCloud-Anmeldung** — Ihre E-Mail-Adresse, Ihr Kennwort und gegebenenfalls ein von Ihnen eingerichteter Zwei-Faktor-Code.
   - **Single Sign-on** — Wenn Sie bereits bei Ihrer Organisation angemeldet sind, läuft dieser Schritt ohne Eingabe durch. Andernfalls öffnet sich zuerst die Anmeldeseite Ihrer Organisation.
6. Wenn das Popup-Fenster **Authenticated successfully** anzeigt, schließen Sie es, falls es sich nicht von selbst geschlossen hat.

Die Kopfzeile des Aufgabenbereichs zeigt nun Ihren Workspace und das mit der Arbeitsmappe verknüpfte Projekt, daneben Ihr Kontomenü. Weiter geht es mit [Mit Tabellen und Dimensionen arbeiten](/de/reference/cli/plaidxl/retrieve/).

Informationen zum Einrichten der Zwei-Faktor-Authentifizierung oder von Single Sign-on für Ihr Konto finden Sie unter [Mitgliederauthentifizierung](/de/administration/access/member-authentication/).

### Mit Ihrem Office-Konto anmelden

Wenn Sie in Office mit einem Geschäftskonto von Microsoft Entra ID angemeldet sind und PlaidXL keine gespeicherte Anmeldung hat, ermittelt es Ihre Workspaces anhand dieses Kontos, sodass Sie Ihre E-Mail-Adresse nicht eingeben müssen:

- **Ein Workspace** — PlaidXL beginnt, Sie bei diesem Workspace anzumelden. Lassen Sie das Popup-Fenster zu, wenn Excel danach fragt; mit Single Sign-on läuft es ohne Eingabe durch. Klicken Sie in Excel im Web zuerst auf **Continue as** und Ihr Konto.
- **Mehrere Workspaces** — Wurde die Arbeitsmappe zuletzt mit einem dieser Workspaces verwendet, meldet PlaidXL Sie dort an. Andernfalls wählen Sie unter **Select a workspace** einen aus.
- **Kein Workspace** — Der E-Mail-Bildschirm öffnet sich mit bereits eingetragener Adresse.

Melden Sie sich mit einer anderen E-Mail-Adresse als der Ihres Office-Kontos an, nennt PlaidXL die Adresse, mit der Sie angemeldet sind. Nachdem Sie sich mit **Log out** abgemeldet haben, wartet PlaidXL darauf, dass Sie sich selbst anmelden.

### Befehle vor der Anmeldung

Sie können jeden PlaidXL-Befehl im Menüband auch vor der Anmeldung anklicken. PlaidXL öffnet den Aufgabenbereich, um Sie anzumelden oder ein Projekt auszuwählen, und führt den Befehl anschließend in der Zelle aus, von der aus Sie gestartet sind.

## Angemeldet bleiben

PlaidXL hält Sie auf diesem Computer angemeldet und erneuert Ihre Anmeldung im Hintergrund, während Sie arbeiten. Wenn Sie den Aufgabenbereich in einer späteren Sitzung öffnen, gelangen Sie direkt zu Ihren Projekten. Ist Ihre Anmeldung vollständig abgelaufen, fragt PlaidXL erneut nach Ihrer E-Mail-Adresse. Ein kurzes Netzwerkproblem beim Erneuern der Anmeldung meldet Sie nicht ab; PlaidXL versucht es erneut.

## Was Sie sehen können

PlaidXL liest mit Ihren Berechtigungen. Sie sehen die Projekte, die Sie in PlaidCloud öffnen können, sowie die darin enthaltenen Tabellen und Dimensionen, und nicht mehr. Fehlt ein Projekt oder eine Tabelle, bitten Sie einen Projektinhaber um Zugriff. Wie die Workspace-Mitgliedschaft funktioniert, erfahren Sie unter [Organisationen und Workspaces erklärt](/de/administration/access/overview/organizations-and-workspaces-explained/).

## Abmelden oder Workspace wechseln

Klicken Sie oben rechts im Aufgabenbereich auf das Kontomenü (die drei Punkte). Es zeigt Ihren Namen und Ihren Workspace sowie drei Befehle:

- **Keyboard shortcuts** listet die PlaidXL-Tastenkombinationen auf, damit Sie sie ändern können. Siehe [Tastenkombinationen](/de/reference/cli/plaidxl/ribbon/#tastenkombinationen).
- **Switch workspace** meldet Sie ab und führt zurück zum E-Mail-Bildschirm, damit Sie unter **Select a workspace** einen anderen Workspace auswählen können.
- **Log out** löscht Ihre Anmeldung und führt zurück zum E-Mail-Bildschirm.

Ihre Anmeldung gilt für alle geöffneten Arbeitsmappen, aber jede Arbeitsmappe behält ihr eigenes Projekt. Das Projekt einer Arbeitsmappe gehört zu einem Workspace. Nach dem Wechsel hat eine Arbeitsmappe, die mit einem Projekt im bisherigen Workspace verknüpft war, kein Projekt, bis Sie eines auswählen. Siehe [Das Projekt gehört zur Arbeitsmappe](/de/reference/cli/plaidxl/retrieve/#das-projekt-gehört-zur-arbeitsmappe).

## Helles und dunkles Design

Der Aufgabenbereich folgt dem Design von Office und ändert sich mit diesem.

## Tastatur und Screenreader

Zeilen in den Listen der Projekte, Tabellen und Dimensionen erhalten den Tastaturfokus und reagieren auf **Enter** und **Leerzeichen**. Eine ausgewählte Zeile wird von einem Screenreader angesagt, und ausgewählte Zustände sowie Warnzustände tragen neben der Farbe auch ein Symbol.

## Verwandte Themen

- [PlaidXL installieren](/de/reference/cli/plaidxl/install/) — das Add-in hinzufügen und den Aufgabenbereich öffnen
- [Fehlerbehebung](/de/reference/cli/plaidxl/troubleshooting/) — wenn sich das Anmelde-Popup nicht öffnet oder ein Workspace fehlt
- [Workspaces anzeigen und verwalten](/de/administration/access/overview/viewing-and-managing-workspaces/) — die Workspaces, zu denen Sie gehören
