---
title: "HFM/FCCS: Daten lesen (Ad-hoc)"
description: Rufen Sie selbst einen Datenausschnitt aus Oracle FCCS ab, indem Sie im Schrittformular einen Betrachtungspunkt aufbauen – das zurückgegebene Raster landet automatisch als Tabelle, wiederholte Abrufe werden zwischengespeichert, die Spalte „Entity" ist bereit für Sicherheit auf Zeilenebene, und ein optionales gebundenes Ziel macht daraus einen geplanten wiederkehrenden Ladevorgang.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-epm/hfm-fccs-read.md
---

## Beschreibung

Liest einen Ad-hoc-Datenausschnitt aus Oracle **FCCS** (Financial Consolidation and Close, EPM Cloud) über Ihre [HFM/FCCS-Verbindung](/de/guides/connections/hfm-fccs/), per **Betrachtungspunkt (Point of View, POV)** statt durch Schreiben einer Abfrage. Ein Finanzbenutzer wählt eine Anwendung, baut aus den FCCS-Dimensionen einen POV auf und führt den Schritt aus; das zurückgegebene Raster landet automatisch als Projekttabelle (Schema-on-Read – die Tabelle wird aus den Spalten des Rasters erstellt). Es fühlt sich wie eine Live-Abfrage an, doch im Hintergrund übermittelt der Schritt einen Exportjob an FCCS, **fragt** ihn bis zum Abschluss **ab** und ruft das Ergebnis dann ab und legt es ab – ein lang laufender Ausschnitt blockiert also nichts, und es ist kein Ticket an das HFM-Team nötig.

Dieser Schritt erscheint im Schrittmenü unter **Oracle EPM (HFM/FCCS)**.

:::note[Entitätsdimension eingrenzen]
Halten Sie die Auswahl der **Entität** begrenzt – ein nicht eingegrenzter Extrakt kann die FCCS-Anwendung für lange Zeit sperren, solange der Exportjob läuft.
:::

## Konfiguration

### Quelle und Ziel

| Feld | Erforderlich | Hinweise |
|---|---|---|
| HFM/FCCS-Verbindung | Ja | Die [HFM/FCCS-Verbindung](/de/guides/connections/hfm-fccs/), über die gelesen wird. |
| Umgebung | Ja | Die Umgebung der Verbindung. |
| Anwendung | Ja | Die FCCS-Anwendung, aus der gelesen wird. Standardmäßig die Standardanwendung der Verbindung, falls eine festgelegt ist. Die Wahl der Anwendung steuert die Live-Erkennung der Member für den POV. |
| Zieltabelle | Ja | Die Projekttabelle, in der das zurückgegebene Raster landet. |

### Betrachtungspunkt

Bauen Sie den Ausschnitt aus den FCCS-Dimensionen auf. Auf unterstützten Pods werden die Member-Listen nach Auswahl von Verbindung und Anwendung automatisch aus der Live-Metadatenerkennung befüllt; auf älteren Pods geben Sie Member-Namen manuell ein.

| Dimension | Erforderlich | Hinweise |
|---|---|---|
| Szenario | Ja | |
| Jahr | Ja | |
| Periode | Ja | |
| Entität | Begrenzt | Muss einen begrenzten Ausschnitt benennen – das Formular lehnt eine leere Auswahl, „all" oder eine Auswahl mit mehr als 500 Membern ab. Halten Sie sie eingegrenzt, damit der Export die Anwendung nicht sperrt. |
| Konto | Nein | |
| Custom1–Custom4 | Nein | Die benutzerdefinierten Dimensionen der Anwendung. |
| ICP | Nein | Intercompany. |
| Ansicht | Nein | |
| Wert | Nein | |

Eine nicht gesetzte optionale Dimension wendet auf dieser Achse keinen Filter an (der Standard-Member von FCCS wird verwendet).

### Gebundenes Ziel

Standardmäßig aus – jede Ausführung legt einen Ad-hoc-Ausschnitt ab, der die Zieltabelle überschreibt.

| Feld | Hinweise |
|---|---|
| Gebundenes Ziel (geplanter wiederkehrender Ladevorgang) | Wenn aktiviert, wird das Ziel zu einer **persistenten** Tabelle: Der Schritt führt per Keyset-Upsert zusammen, statt zu überschreiben, und das Schema wächst additiv, wenn ein späteres Raster neue Spalten mitbringt (eine neue Spalte löst eine Warnung aus, nie einen Fehler). Wird der Schritt in einen geplanten Workflow gestellt, ergibt das einen wiederkehrenden Ladevorgang, der akkumuliert statt zu löschen. |
| Schlüsselspalten | Nur aktiv, wenn „Gebundenes Ziel" aktiviert ist. Kommagetrennte Spalten, die den Merge-Schlüssel bilden (zum Beispiel `Entity, Account`). **Lassen Sie das Feld leer**, um die im abgelegten Raster vorhandenen POV-Dimensionsspalten als Merge-Schlüssel zu verwenden. |

## So funktioniert es

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 720 130" role="img" aria-label="Der Schritt übermittelt einen Exportjob an FCCS, fragt ihn bis zum Abschluss ab, ruft das Raster ab und legt es als Tabelle ab; ein wiederholter Betrachtungspunkt wird stattdessen aus der zwischengespeicherten Tabelle bedient." style="width:100%;max-width:720px;height:auto;">
<defs><marker id="hf-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
<rect x="10" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="58" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Job übermitteln</text>
<rect x="150" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="198" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Abfragen</text>
<rect x="290" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="338" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Raster abrufen</text>
<rect x="430" y="46" width="120" height="40" rx="7" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" /><text x="490" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Tabelle ablegen</text>
<path d="M106 66 L150 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<path d="M246 66 L290 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<path d="M386 66 L430 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<text x="198" y="34" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">solange er läuft …</text>
<rect x="590" y="46" width="120" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="650" y="64" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">Wiederholter POV</text><text x="650" y="78" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">aus dem Cache bedient</text>
<path d="M550 82 C570 100 630 100 650 88" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" stroke-dasharray="4 3" marker-end="url(#hf-arrow)" />
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Eine Ausführung übermittelt einen Exportjob, fragt ihn ab, ruft das Raster ab und legt eine Tabelle ab. Derselbe erneut angeforderte Betrachtungspunkt wird aus der bereits abgelegten Kopie bedient.</figcaption>
</figure>

Während der Job läuft, zeigt der Schritt einen Abfragestatus. Sobald er abgelegt ist, wird die Tabelle aus den Spalten des Rasters erstellt – ein Schema muss nicht vorab definiert werden.

## Caching

Derselbe erneut angeforderte POV wird sofort **aus der bereits abgelegten Tabelle bedient**, statt den Export erneut an FCCS zu übermitteln. Eine Ausführung wird durch Anwendung, Zieltabelle, Betrachtungspunkt und ein **As-of**-Tag (Standard `latest`) identifiziert; eine Wiederholung, die auf einen bereits abgelegten Ausschnitt aufgelöst wird, meldet, dass die Tabelle unverändert gelassen wurde, statt sie neu zu schreiben. Ändern Sie das As-of-Tag, wenn Sie einen frischen Extrakt desselben POV erzwingen möchten.

## Sicherheit auf Zeilenebene

Die Entitätsachse des abgelegten Rasters wird auf eine Spalte mit genau dem Namen **`Entity`** normalisiert, sodass die Tabelle **bereit für Sicherheit auf Zeilenebene** ist – ein Administrator kann sie mit [Zeilenzugriff](/de/administration/access/managing-security-groups-and-assignments/) steuern, sodass Self-Service-Benutzer nur die Entitäten sehen, auf die sie Anspruch haben.

Dies wird **unter Administratorkontrolle gesteuert, nicht automatisch**. Da der Extrakt unter dem Dienstkonto der Verbindung läuft, lässt PlaidCloud nicht zu, dass der Schritt seine eigene Sicherheit deklariert. Ein Administrator folgt dem standardmäßigen Ablauf für den Zeilenzugriff:

1. **Veröffentlichen** Sie die abgelegte Tabelle für Berichte.
2. **Deklarieren** Sie die Spalte `Entity` als steuerndes Attribut (standardmäßig verweigern).
3. **Genehmigen** Sie den ersten gesteuerten Schreibvorgang.
4. **Gleichen Sie ab**, damit Berechtigungen wirksam werden.

Solange ein Administrator dies nicht tut, wird die Tabelle nicht gefiltert. Siehe [Sicherheitsgruppen und Zuweisungen verwalten](/de/administration/access/managing-security-groups-and-assignments/).

## Leistungsgrenzen

| Einschränkung | Bedeutung |
|---|---|
| Nur Lesen | Extrahiert einen Ausschnitt aus FCCS. Es schreibt keine Konsolidierungsdaten, führt keine Konsolidierungen aus und bucht nichts zurück. |
| Begrenzte Entität erforderlich | Das Formular lehnt eine leere Entitätsauswahl, „all" oder eine Auswahl mit mehr als 500 Membern ab, und ein einzelner Aggregat-Member kann serverseitig trotzdem expandieren – halten Sie den Ausschnitt eingegrenzt. |
| Manuelle Member auf älteren Pods | Wenn ein Pod den Metadaten-Endpunkt nicht bereitstellt, werden die Member-Listen nicht automatisch befüllt; geben Sie die Member-Namen von Hand ein. |
| Sicherheit auf Zeilenebene wird vom Administrator gesteuert | Die Spalte `Entity` ist bereit für RLS, doch ein Administrator muss veröffentlichen, deklarieren, den ersten Schreibvorgang genehmigen und abgleichen, bevor die Tabelle gefiltert wird. |

## Verwandte Themen

- [Aus HFM / FCCS extrahieren (Anleitung)](/de/guides/connections/hfm-fccs/) – die vollständige Anleitung.
- [HFM-/FCCS-Konnektor](/de/reference/connectors/rest/hfm-fccs/) – Feldreferenz der Verbindung.
- [Oracle-EPM-Schritte (HFM / FCCS)](/de/reference/workflow-steps/oracle-epm/)
- [Sicherheitsgruppen und Zuweisungen verwalten](/de/administration/access/managing-security-groups-and-assignments/)
