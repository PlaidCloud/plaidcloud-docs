---
title: Bei PlaidXL anmelden
description: Verbinden Sie PlaidXL mit Ihrem PlaidCloud-Workspace über Ihre E-Mail-Adresse und Ihre gewohnte Anmeldung, einschließlich Single Sign-on und Zwei-Faktor-Authentifizierung, und melden Sie sich anschließend ab oder wechseln Sie den Workspace.
sidebar:
  label: Anmeldung
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL meldet Sie als Sie selbst an und verwendet dieselbe Anmeldung wie PlaidCloud im Browser. Sie müssen keine Serveradresse eingeben, und in der Arbeitsmappe wird kein Passwort gespeichert.

## Anmelden

1. Öffnen Sie den Aufgabenbereich: **PlaidCloud → Open PlaidXL** oder **Konto** in der Gruppe **Verbinden**.
2. Geben Sie unter **Enter your email** die E-Mail-Adresse ein, die Sie für PlaidCloud verwenden, und klicken Sie auf **Sign In**. PlaidXL merkt sich die Adresse für das nächste Mal.
3. Gehört Ihre E-Mail-Adresse zu mehr als einem Workspace, wählen Sie unter **Select a workspace** einen aus und klicken Sie auf **Sign In**. PlaidXL merkt sich Ihre Auswahl. Gehören Sie zu einem Workspace, wählt PlaidXL ihn für Sie aus. Ist der E-Mail-Adresse kein Workspace zugeordnet, weist der Bereich darauf hin; prüfen Sie die Adresse und versuchen Sie es erneut.
4. Excel fragt, ob ein Pop-up-Fenster zugelassen werden soll. Lassen Sie es zu.
5. Melden Sie sich im Pop-up wie gewohnt an:
   - **PlaidCloud sign-in** – Ihre E-Mail-Adresse, Ihr Passwort und gegebenenfalls ein von Ihnen eingerichteter Zwei-Faktor-Code.
   - **Single sign-on** – wenn Sie bereits bei Ihrer Organisation angemeldet sind, läuft dieser Schritt ohne Eingabe durch. Andernfalls öffnet sich zuerst die Anmeldeseite Ihrer Organisation.
6. Wenn das Pop-up **Authenticated successfully** anzeigt, schließen Sie es, falls es sich nicht von selbst geschlossen hat.

Die Kopfzeile des Aufgabenbereichs zeigt nun Ihren Workspace und das mit der Arbeitsmappe verknüpfte Projekt, daneben Ihr Kontomenü. Fahren Sie fort mit [Mit Tabellen und Dimensionen arbeiten](/de/reference/cli/plaidxl/retrieve/).

Informationen zum Einrichten von Zwei-Faktor-Authentifizierung oder Single Sign-on für Ihr Konto finden Sie unter [Mitgliederauthentifizierung](/de/administration/access/member-authentication/).

### Mit Ihrem Office-Konto anmelden

Sind Sie in Office mit einem Geschäftskonto von Microsoft Entra ID angemeldet und hat PlaidXL keine gespeicherte Anmeldung, findet es Ihre Workspaces über dieses Konto, sodass Sie Ihre E-Mail-Adresse nicht eingeben müssen:

- **One workspace** – PlaidXL beginnt, Sie dort anzumelden. Lassen Sie das Pop-up zu, wenn Excel danach fragt; mit Single Sign-on läuft es ohne Eingabe durch. Klicken Sie in Excel im Web zuerst auf **Continue as** mit Ihrem Konto.
- **Several workspaces** – wählen Sie unter **Select a workspace** einen aus. Der Workspace, mit dem die Arbeitsmappe zuletzt verwendet wurde, ist bereits ausgewählt.
- **No workspace** – der E-Mail-Bildschirm öffnet sich mit bereits ausgefüllter Adresse.

Melden Sie sich mit einer anderen E-Mail-Adresse als der Ihres Office-Kontos an, teilt PlaidXL mit, um welche es sich handelt. Nachdem Sie sich mit **Log out** abgemeldet haben, wartet PlaidXL darauf, dass Sie sich selbst anmelden.

### Befehle vor der Anmeldung

Sie können jeden PlaidXL-Befehl in der Multifunktionsleiste anklicken, bevor Sie angemeldet sind. PlaidXL öffnet den Aufgabenbereich, um Sie anzumelden oder ein Projekt auszuwählen, und führt den Befehl anschließend in der Zelle aus, von der Sie ausgegangen sind.

## Angemeldet bleiben

PlaidXL hält Sie auf diesem Computer angemeldet und erneuert Ihre Anmeldung im Hintergrund, während Sie arbeiten. Öffnen Sie den Aufgabenbereich in einer späteren Sitzung, gelangen Sie direkt zu Ihren Projekten. Ist Ihre Anmeldung vollständig abgelaufen, fragt PlaidXL erneut nach Ihrer E-Mail-Adresse. Ein kurzes Netzwerkproblem beim Erneuern der Anmeldung meldet Sie nicht ab; PlaidXL versucht es erneut.

## Was Sie sehen können

PlaidXL liest mit Ihren Berechtigungen. Sie sehen die Projekte, die Sie in PlaidCloud öffnen können, sowie die Tabellen und Dimensionen darin – nicht mehr. Fehlt ein Projekt oder eine Tabelle, bitten Sie einen Projektinhaber um Zugriff. Wie die Mitgliedschaft in einem Workspace funktioniert, erfahren Sie unter [Organisationen und Workspaces erklärt](/de/administration/access/overview/organizations-and-workspaces-explained/).

## Abmelden oder Workspace wechseln

Klicken Sie oben rechts im Aufgabenbereich auf das Kontomenü (die drei Punkte). Es zeigt Ihren Namen und Ihren Workspace sowie drei Befehle:

- **Keyboard shortcuts** listet die PlaidXL-Tastenkombinationen auf, damit Sie sie ändern können. Siehe [Tastenkombinationen](/de/reference/cli/plaidxl/ribbon/#tastenkombinationen).
- **Switch workspace** meldet Sie ab und führt zurück zum E-Mail-Bildschirm, damit Sie unter **Select a workspace** einen anderen Workspace wählen können.
- **Log out** löscht Ihre Anmeldung und führt zurück zum E-Mail-Bildschirm.

Ihre Anmeldung wird von jeder geöffneten Arbeitsmappe gemeinsam genutzt, aber jede Arbeitsmappe behält ihr eigenes Projekt. Das Projekt einer Arbeitsmappe gehört zu einem Workspace; nach einem Wechsel hat eine Arbeitsmappe, die mit einem Projekt im alten Workspace verknüpft war, daher kein Projekt, bis Sie eines auswählen. Siehe [Das Projekt gehört zur Arbeitsmappe](/de/reference/cli/plaidxl/retrieve/#das-projekt-gehört-zur-arbeitsmappe).

## Helles und dunkles Design

Der Aufgabenbereich folgt Ihrem Office-Design und ändert sich, wenn Sie dieses ändern.

## Tastatur und Screenreader

Zeilen in den Listen der Projekte, Tabellen und Dimensionen erhalten den Tastaturfokus und reagieren auf **Enter** und **Leerzeichen**. Ein Screenreader kündigt eine ausgewählte Zeile an, und ausgewählte Zustände sowie Warnzustände sind außer durch eine Farbe auch durch ein Symbol gekennzeichnet.

## Verwandte Themen

- [PlaidXL installieren](/de/reference/cli/plaidxl/install/) – Add-in hinzufügen und Aufgabenbereich öffnen
- [Fehlerbehebung](/de/reference/cli/plaidxl/troubleshooting/) – wenn das Anmelde-Pop-up nicht erscheint oder ein Workspace fehlt
- [Workspaces anzeigen und verwalten](/de/administration/access/overview/viewing-and-managing-workspaces/) – die Workspaces, denen Sie angehören
