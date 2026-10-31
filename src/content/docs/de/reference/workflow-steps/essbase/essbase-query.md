---
title: "Essbase: Cube abfragen"
description: Führen Sie eine Live-MDX-Abfrage gegen einen Oracle-Essbase-Cube aus und legen Sie das Ergebnisraster in einer Workflow-Tabelle ab, mit aus dem Raster abgeleiteten Spalten und auf das Ergebnis angewendetem Zeilenzugriff.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/essbase-query.md
---

## Beschreibung

Der Schritt **Essbase: Cube abfragen** führt ein MDX-`SELECT` gegen einen Oracle-Essbase-Cube aus und schreibt das zurückgegebene Raster in eine Zieltabelle. Er ist eine **echte Live-Abfrage** – der Schritt sendet das MDX und liest das resultierende Raster synchron, sodass jede Ausführung die aktuellen Zahlen des Cubes widerspiegelt. Er ist kein Extrakt und keine Abfrage im Polling-Verfahren: Es gibt keinen Staging-Auftrag, auf den gewartet werden muss, und keinen Snapshot, der zwischen den Ausführungen veraltet.

Verwenden Sie ihn, um einen bestimmten Ausschnitt eines Cubes – eine Reihe von Konten nach Periode, einen Szenariovergleich, einen Treibersatz für eine Umlage – in eine PlaidCloud-Tabelle zu laden, die Sie dann zusammen mit Ihren übrigen Daten transformieren, verknüpfen oder auswerten können.

## Voraussetzungen

- Eine [Oracle-Essbase-Verbindung](/de/reference/connectors/erp/oracle-essbase/), die auf Essbase 21c+ oder Oracle Analytics Cloud (OAC) verweist, mit einem Servicekonto, das die abzufragende Anwendung und den Cube lesen kann.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 720 120" role="img" aria-label="Ablauf von einer Essbase-Verbindung über die gewählte Anwendung und den Cube, eine MDX-Abfrage und das zurückgegebene Raster in eine Zieltabelle." style="width:100%;max-width:720px;height:auto;">
<defs><marker id="eq-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
<rect x="10" y="42" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="70" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Verbindung</text>
<rect x="176" y="42" width="130" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="241" y="63" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Anwendung</text><text x="241" y="78" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">/ Cube</text>
<rect x="352" y="42" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="412" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">MDX SELECT</text>
<rect x="518" y="42" width="80" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="558" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Raster</text>
<rect x="632" y="42" width="80" height="42" rx="8" fill="var(--sl-color-accent)" stroke="var(--sl-color-accent)" /><text x="672" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Tabelle</text>
<path d="M130 63 L172 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M306 63 L348 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M472 63 L514 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M598 63 L628 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" />
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Das MDX läuft live gegen den Cube; das zurückgegebene Raster landet in der Zieltabelle, mit Spalten, die aus dem Raster selbst abgeleitet werden.</figcaption>
</figure>

## Konfiguration

- **Verbindung** – eine Oracle-Essbase-Verbindung. Die Bearbeiten-Verknüpfung neben der Auswahl öffnet den Verbindungseditor zum Ansehen oder Bearbeiten.
- **Anwendung** – die Essbase-Anwendung, die abgefragt wird. Die Auswahl listet die Anwendungen auf, die das Servicekonto der Verbindung sehen kann; legt die Verbindung eine Standardanwendung fest, ist sie vorausgewählt.
- **Cube (Database)** – der Cube innerhalb der gewählten Anwendung, gegen den abgefragt wird.
- **MDX** – das MDX-`SELECT`-Statement, das ausgeführt wird. Erstellen Sie es mit der geführten Mitgliederauswahl oder schreiben Sie es direkt (siehe unten).
- **Zieltabelle** – die Tabelle, in die das zurückgegebene Raster geschrieben wird.

## Die Abfrage erstellen

Das MDX können Sie auf zwei Arten erzeugen:

- **Geführte Mitgliederauswahl.** Durchsuchen Sie die Dimensionen und Mitglieder des Cubes und wählen Sie aus, was in die Spalten und was in die Zeilen kommt; der Schritt stellt das MDX für Sie zusammen. Mitglieder werden beim Aufklappen ebenenweise geladen, sodass eine große Gliederung reaktionsschnell bleibt.
- **Rohes MDX.** Schreiben oder fügen Sie ein MDX-`SELECT` direkt ein – der Ausweg für alles, was die geführte Auswahl nicht abdeckt, etwa berechnete Mitglieder, Funktionen oder Mengenoperatoren.

Beide Wege erzeugen denselben `MDX`-Wert, den der Schritt ausführt; die geführte Auswahl ist ein Ausgangspunkt, den Sie jederzeit von Hand bearbeiten können.

## Optionen

| Feld | Standard | Hinweise |
|---|---|---|
| #Missing-Zellen unterdrücken | Aus | Serverseitig: verwirft `#Missing` und andere strukturell irrelevante Zellen, bevor sie über die Leitung gehen. Sicher – verwirft nie eine gebuchte Null. |
| Auch Nullzellen unterdrücken (verlustbehaftet) | Aus | Ein separater Opt-in-Filter, der nach dem Abruf zusätzlich jede Zelle verwirft, deren Wert bereits genau `0` ist. **Verlustbehaftet**: Eine gebuchte Null ist in einem Planungs-Cube ein echter Fakt, kein fehlender Wert – aktivieren Sie die Option nur, wenn Sie Nullen ausdrücklich aus dem Ergebnis ausschließen wollen. |
| Zeilenlimit | 250.000 | Begrenzt die Anzahl der zurückgegebenen Zeilen. Lassen Sie das Feld leer, um die Standardgrenze von 250.000 zu verwenden; erhöhen oder senken Sie sie ausdrücklich. Eine Abfrage, die das Limit überschreitet, wird abgelehnt, statt stillschweigend abgeschnitten zu werden – grenzen Sie die Abfrage ein (fügen Sie einen Slicer, `NON EMPTY` oder eine engere Mitgliedermenge hinzu) oder erhöhen Sie das Zeilenlimit und versuchen Sie es erneut. |

## Vorschau

Vor dem Speichern führt **Vorschau** das aktuelle MDX gegen den Cube aus und zeigt die zurückgegebenen Spalten und die ersten Zeilen – eine schnelle Kontrolle, ob die Abfrage die erwartete Form hat, unabhängig vom Zeilenlimit, das für den Schritt selbst konfiguriert ist.

## Ergebnisse und Schema-on-Read

Das von Essbase zurückgegebene Raster wird in die Zieltabelle geschrieben, mit **aus dem zurückgegebenen Raster abgeleiteten Spalten** – Schema-on-Read. Sie deklarieren vorab keine Spaltenliste:

- Die Spaltennamen stammen aus den Kopfzeilen des Rasters. Eine Kopfzelle, die nichts umfasst (die Ecke über den Zeilenbeschriftungen), wird zu `column_1`, `column_2` und so weiter; doppelte Namen werden durch ein numerisches Suffix eindeutig gemacht.
- Eine Spalte, deren Datenzellen alle numerisch sind, wird als numerisch typisiert; alles andere als Text. Leere Essbase-Zellen landen als Nullwerte.
- Mitglieds- und Aliasbeschriftungen im Raster stammen aus der in der Verbindung konfigurierten Alias-Tabelle und werden bei jeder Ausführung gleich angewendet – nicht aus dem sitzungsbezogenen Standard von Essbase selbst, der je nachdem, wer bei der Abfrage angemeldet war, unterschiedliche Beschriftungstexte zeigen könnte.

Da die Form der Abfrage folgt, ändert sich mit dem, was das MDX in die Spalten legt, bei der nächsten Ausführung auch die Spalten der Tabelle – beachten Sie das bei nachgelagerten Schritten, die auf bestimmte Spaltennamen verweisen.

## Zeilenzugriff

[Sicherheit auf Zeilenebene](/de/administration/access/managing-security-groups-and-assignments/#zeilenzugriff-verwalten) gilt für die abgelegte Tabelle genau wie für jede andere PlaidCloud-Tabelle. Die Governance wird auf das Ergebnis angewendet, das der Schritt schreibt; ein Leser mit einer Zeilenbeschränkung sieht also nur die Zeilen, die seine Sicherheitsgruppe erlaubt – die Abfrage läuft mit dem Servicekonto der Verbindung, aber die erzeugte Tabelle wird wie der Rest Ihrer Daten gesteuert.

## Beispiel

Dieses MDX legt zwei Kennzahlen in die Spalten und zwei Produkte in die Zeilen:

```mdx
SELECT
  {Sales, COGS} ON COLUMNS,
  {[100-10], [200-10]} ON ROWS
FROM Sample.Basic
```

Die Ausführung gegen einen Cube, der diese vier Zahlen zurückgibt, legt eine Tabelle wie diese ab:

| column_1 | Sales | COGS |
|---|---|---|
| 100-10 | 678.0 | 271.0 |
| 200-10 | 551.0 | 235.0 |

Die Spalte mit den Zeilenbeschriftungen hat im Raster keinen Kopf und wird daher zu `column_1` (Text); `Sales` und `COGS` sind durchgehend numerisch und landen als numerische Spalten.

## Verwandte Themen

- [Mit Oracle Essbase verbinden (Leitfaden)](/de/guides/connections/essbase/) – die Verbindung erstellen und eine Abfrage aufbauen.
- [Oracle Essbase Connector](/de/reference/connectors/erp/oracle-essbase/) – Referenz der Verbindungsfelder.
- [Essbase: Dimension lesen](/de/reference/workflow-steps/essbase/essbase-dimension-read/) – lädt cloud-direkt eine Essbase-Dimensionsgliederung in eine PlaidCloud-Dimension.
- [Oracle-Essbase-Schritte](/de/reference/workflow-steps/essbase/)
- [REST-Anfrage](/de/reference/workflow-steps/general/rest-request/) – der Allzweckschritt für andere Live-HTTP-Anfragen.
