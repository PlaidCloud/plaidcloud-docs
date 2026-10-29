---
title: PlaidXL installieren
description: Fügen Sie das PlaidXL-Add-in unter Windows oder Mac zu Excel hinzu, finden Sie die Registerkarte „PlaidCloud“ im Menüband und öffnen Sie den PlaidXL-Aufgabenbereich.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/install.md
---

Sie installieren PlaidXL einmal pro Computer, nicht einmal pro Arbeitsmappe. Danach ist die Registerkarte **PlaidCloud** in jeder von Ihnen geöffneten Arbeitsmappe im Excel-Menüband vorhanden.

## Vor dem Start

- Verwenden Sie Excel für Microsoft 365 oder Excel 2021 oder höher unter Windows oder Mac.
- Wenn Ihre Organisation Office-Add-ins zentral verwaltet, muss PlaidXL möglicherweise Ihr Microsoft-365-Administrator für Sie bereitstellen. Wenn Sie selbst keine Add-ins installieren können, bitten Sie ihn, das Add-in **PlaidCloud** hinzuzufügen.

## Unter Windows installieren

1. Öffnen Sie in Excel **Insert → Add-ins** (in einigen Versionen **Home → Add-ins**).
2. Geben Sie `PlaidCloud` in das Suchfeld für Add-ins ein.
3. Wählen Sie das Add-in **PlaidCloud** aus und klicken Sie auf **Hinzufügen**.

## Auf dem Mac installieren

1. Öffnen Sie in Excel für Mac **Insert → Add-ins**. In älteren Versionen lautet das Menü **Insert → Store**.
2. Geben Sie `PlaidCloud` in das Suchfeld für Add-ins ein.
3. Wählen Sie das Add-in **PlaidCloud** aus und klicken Sie auf **Hinzufügen**.

## Aufgabenbereich öffnen

1. Klicken Sie im Menüband auf die Registerkarte **PlaidCloud**.
2. Klicken Sie in der Gruppe **PlaidXL Controls** auf **Show Taskpane**.

Der PlaidXL-Aufgabenbereich öffnet sich auf der rechten Seite des Fensters und fordert Sie zur Anmeldung auf. Fahren Sie mit [Anmelden](/de/reference/cli/plaidxl/connect/) fort.

Der Aufgabenbereich bleibt zwischen Sitzungen angemeldet, sodass Sie sich in der Regel einmal anmelden und den Aufgabenbereich danach nur noch bei Bedarf öffnen.

## Wenn PlaidXL nicht angezeigt wird

- Schließen Sie alle Excel-Fenster und öffnen Sie Excel erneut. Ein Add-in erscheint im Menüband oft erst nach einem Neustart von Excel.
- Suchen Sie unter **Insert → My Add-ins** (Windows) bzw. **Insert → Add-ins → My Add-ins** (Mac) und wählen Sie dort **PlaidCloud** aus.
- Wenn Ihre Organisation Add-ins aus dem Store blockiert, bitten Sie Ihren Microsoft-365-Administrator, es bereitzustellen.

Weitere Lösungen finden Sie auf der Seite [Fehlerbehebung](/de/reference/cli/plaidxl/troubleshooting/).

## Verwandte Themen

- [Anmelden](/de/reference/cli/plaidxl/connect/) — das Add-in mit Ihrem Workspace verbinden
- [Das PlaidCloud-Menüband](/de/reference/cli/plaidxl/ribbon/) — jeder Befehl auf der Registerkarte **PlaidCloud**
