---
title: PlaidXL
description: Nutzen Sie das Excel-Add-in PlaidXL, um sich bei Ihrem PlaidCloud-Workspace anzumelden, Projekttabellen und Dimensionshierarchien in Arbeitsblätter zu holen, Live-Berichte zu erstellen, Zahlen per Drilldown aufzuschlüsseln und zu erklären, governte Kennzahlen zu lesen, durch Zurückschreiben von Werten nach PlaidCloud zu planen und Weave zu fragen.
sidebar:
  label: PlaidXL
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/index.md
---

PlaidXL ist das PlaidCloud-Add-in für Microsoft Excel. Es verbindet eine Arbeitsmappe mit Ihrem PlaidCloud-Workspace, sodass Ihre Modelle und Berichte aus maßgeblichen Projekttabellen und Dimensionen lesen und nicht aus einer Kopie, die veraltet, sobald ein Workflow das nächste Mal ausgeführt wird.

Sie können mit PlaidXL auf drei Arten arbeiten, und die meisten Arbeitsmappen nutzen alle drei:

- **Der Aufgabenbereich** – durchsuchen Sie Ihre Projekte, wählen Sie eine Tabelle oder Dimension aus, legen Sie Spalten und Filter fest und rufen Sie die Daten in ein Arbeitsblatt ab. Mit der Aktualisierung bleiben sie aktuell, und **Save to PlaidCloud** schreibt eine bearbeitete Tabelle zurück. Weitere Registerkarten erstellen für Sie eine Formel oder einen ganzen Bericht, erklären, woher eine Zahl stammt, und lassen Sie Weave in einfachen Worten fragen.
- **Benutzerdefinierte Funktionen** – Formeln wie `=PLAIDXL.TABLE.GET_TABLE("Sales")`, `=PLAIDXL.CELL(...)` und `=PLAIDXL.METRIC("Net Revenue")`, die PlaidCloud-Daten direkt in Zellen lesen. Verwenden Sie sie, um Tabellen und Dimensionen aufzulisten, eine Hierarchie anzulegen, aggregierte Werte für einen Bericht zu berechnen und governte Kennzahlen zu lesen.
- **Die Multifunktionsleiste und das Kontextmenü** – führen Sie von jeder Zelle aus einen Drilldown einer Dimension aus, wählen Sie Elemente aus, aktualisieren Sie, erklären Sie eine Zahl oder zeigen Sie die zugrunde liegenden Zeilen an, jeweils mit einer Tastenkombination.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 230" role="img" aria-label="Excel enthält den PlaidXL-Aufgabenbereich und die benutzerdefinierten PlaidXL-Funktionen. Beide senden Anfragen, als Sie angemeldet, an ein Projekt in Ihrem PlaidCloud-Workspace, das Tabellenzeilen, Dimensionshierarchien und aggregierte Werte in Zellen des Arbeitsblatts zurückgibt." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="px-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="20" y="20" width="250" height="190" rx="10" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="44" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Excel-Arbeitsmappe</text>
  <rect x="40" y="62" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="84" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">PlaidXL-Aufgabenbereich</text>
  <text x="145" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">durchsuchen, filtern, abrufen, aktualisieren</text>
  <rect x="40" y="130" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="152" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">PLAIDXL.*-Funktionen</text>
  <text x="145" y="170" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">Tabellen, Hierarchien, Werte in Zellen</text>
  <rect x="410" y="40" width="230" height="150" rx="10" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="66" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">PlaidCloud-Workspace</text>
  <rect x="430" y="80" width="190" height="94" rx="8" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="102" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Projekt</text>
  <text x="525" y="124" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">Tabellen</text>
  <text x="525" y="142" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">Dimensionen und Hierarchien</text>
  <path d="M252 98 L405 98" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="90" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">als Sie angemeldet</text>
  <path d="M405 150 L254 150" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="168" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">Zeilen, Knoten, Werte</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Der Aufgabenbereich und die benutzerdefinierten Funktionen lesen beide aus dem Projekt, das Sie auswählen, mit Ihren eigenen PlaidCloud-Berechtigungen.</figcaption>
</figure>

PlaidXL liest aus PlaidCloud und ändert eine Projekttabelle nur, wenn Sie selbst darauf schreiben: indem Sie eine Zahl über einen `CELL`-Wert eingeben oder ein abgerufenes Blatt mit **Save to PlaidCloud** speichern. Beides wird sofort geschrieben, und **Undo last write** macht es rückgängig. Siehe [Werte in PlaidCloud eingeben](/de/reference/cli/plaidxl/write-values/).

## Anforderungen

- Excel für Microsoft 365 oder Excel 2021 oder neuer, unter Windows oder Mac. Die Registerkarte PlaidCloud der Multifunktionsleiste, das Kontextmenü und der Aufgabenbereich laufen in Excel für den Desktop.
- Ein PlaidCloud-Konto in mindestens einem Workspace sowie Zugriff auf die Projekte, die Sie lesen möchten. PlaidXL zeigt nur die Projekte, Tabellen und Dimensionen, die Ihr Konto in PlaidCloud bereits sehen kann.

## Themen

- [Installation](/de/reference/cli/plaidxl/install/) – PlaidXL zu Excel hinzufügen und den Aufgabenbereich öffnen
- [Anmeldung](/de/reference/cli/plaidxl/connect/) – mit Ihrem Workspace verbinden, abmelden und Workspaces wechseln
- [Mit Tabellen und Dimensionen arbeiten](/de/reference/cli/plaidxl/retrieve/) – ein Projekt auswählen, eine Tabelle filtern, in ein Blatt abrufen, aktualisieren und zurückspeichern
- [Benutzerdefinierte Funktionen](/de/reference/cli/plaidxl/functions/) – jede `PLAIDXL`-Funktion, ihre Argumente und ihre Rückgabe
- [Einen Bericht erstellen](/de/reference/cli/plaidxl/build-a-report/) – einen Live-Bericht über den Aufgabenbereich oder mit Formeln anlegen
- [Drilldown, Elemente auswählen und Zahlen erklären](/de/reference/cli/plaidxl/drill/) – von einer Zelle aus Drilldown ausführen, Elemente auswählen, eine Zahl erklären und ihre Detailzeilen anzeigen
- [Werte in PlaidCloud eingeben](/de/reference/cli/plaidxl/write-values/) – durch Überschreiben von Berichtswerten planen und jeden Schreibvorgang rückgängig machen
- [Weave fragen in Excel](/de/reference/cli/plaidxl/weave/) – aus Anfragen in einfacher Sprache erstellen, Drilldown ausführen und korrigieren
- [Die PlaidCloud-Multifunktionsleiste](/de/reference/cli/plaidxl/ribbon/) – jeder Befehl, das Kontextmenü und die Tastenkombinationen
- [Fehlerbehebung](/de/reference/cli/plaidxl/troubleshooting/) – Lösungen für die häufigsten Probleme

Neu bei PlaidXL? Das Tutorial [In Excel mit PlaidXL arbeiten](/de/get-started/tutorials/excel-with-plaidxl/) führt Sie in etwa 20 Minuten von der Installation des Add-ins bis zu einem ersten Bericht.

## Verwandte Themen

- [Projekte](/de/guides/projects/) – was ein Projekt enthält und wie Sie eines finden
- [Tabellen und Ansichten](/de/guides/data/tables-views/) – die Tabellen, die PlaidXL abruft
- [Dimensionen verwenden](/de/guides/dimensions/dimensions/) – die Hierarchien, die PlaidXL anlegt und aggregiert
