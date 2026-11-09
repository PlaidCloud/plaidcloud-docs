---
title: Get Workspace Usage (Schritt)
description: Schreiben Sie die Workspace-Nutzungssummen aus den Nutzungsberichten tages- oder monatsweise in eine Projekttabelle, um die Akzeptanz darzustellen oder einen nachgelagerten Schritt zu speisen.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Beschreibung

Schreibt, wie Ihr Workspace genutzt wird, in eine Projekttabelle. Verwenden Sie den Schritt, um die Akzeptanz im Zeitverlauf zu verfolgen, die Nutzung nach Abteilung oder Team zu berichten, eigene Dashboards zu erstellen oder in einem geplanten Workflow einen Aktivitätsrückgang zu melden. Die Zahlen sind dieselben, die [Nutzungsberichte](/de/administration/access/usage-reports/) anzeigt.

Drei Datasets enthalten nur Summen: Keine Zeile nennt ein Mitglied, und Notebook-Pfade werden durch `*` ersetzt. Die anderen vier (**Mitglieder**, **Daily per member**, **Inhalt** und **Content per member**) sind für Berichte gedacht. **Mitglieder**, **Daily per member** und **Content per member** enthalten die Identität der Mitglieder (Benutzer-ID, Benutzername, E-Mail, Vor- und Nachname sowie Sicherheitsgruppen). Behandeln Sie die Zieltabelle daher wie jede Mitgliederliste. Jede Ausführung des Schritts wird im Sicherheitsprotokoll aufgezeichnet.

## Konfiguration

### Nutzungsdaten

**Dataset** legt fest, was jede Zeile enthält:

| Dataset | Eine Zeile für jeden/jede | Enthält Identität |
|---|---|---|
| **Daily per item** | Tag, Bereich, Ereignis und Gegenstand | Nein |
| **Monthly per item** | Monat, Bereich, Ereignis und Gegenstand | Nein |
| **Monthly totals** (Standard) | Monat und Bereich | Nein |
| **Mitglieder** | Person im Workspace | Ja |
| **Daily per member** | Person, Tag und Bereich | Ja |
| **Inhalt** | Dashboard, App oder Notebook | Nein |
| **Content per member** | Person und Element | Ja |

**Area** beschränkt die Zeilen auf einen Bereich: **PlaidCloud-App**, **Dashboards**, **Apps**, **App visits** oder **Notebooks**. Belassen Sie die Einstellung auf **All areas**, um alle einzubeziehen.

### Spalten

#### Daily per item

`day`, `source`, `event`, `subject`, `events`.

#### Monthly per item

`month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial`.

#### Monthly totals

`month`, `source`, `active_users`, `coverage_start`, `partial`.

`partial` ist wahr für einen Monat, den der Verlauf nicht vollständig abdeckt, und `coverage_start` ist das Datum, an dem die Erfassung begann. Ein Monat wird einbezogen, sobald er abgeschlossen und ausgeglichen ist, was 3 Tage dauert.

#### Mitgliederspalten

**Mitglieder**, **Daily per member** und **Content per member** beginnen mit denselben sieben Spalten:

| Spalte | Enthält |
|---|---|
| `user_id` | Die ID des Mitglieds. |
| `user_name` | Der Benutzername des Mitglieds. |
| `email` | Die E-Mail-Adresse des Mitglieds in Kleinbuchstaben. |
| `first_name` | Vorname. |
| `last_name` | Nachname. |
| `is_active` | Wahr, wenn das Mitglied aktiv ist, falsch, wenn es deaktiviert wurde. |
| `groups` | Die Sicherheitsgruppen des Mitglieds, getrennt durch `; `. |

`groups` listet nur Gruppen der obersten Ebene auf. Untergruppen werden nicht aufgelöst.

#### Mitglieder

Die Mitgliederspalten, danach:

| Spalte | Enthält |
|---|---|
| `first_seen` | Der erste Tag, an dem das Mitglied PlaidCloud je verwendet hat, unabhängig vom Datumsbereich. |
| `last_seen` | Der letzte Aktivitätstag des Mitglieds innerhalb des Bereichs. |
| `active_days` | Tage mit Aktivität im Bereich. |
| `events` | Aktivitätsereignisse im Bereich. |
| `active_minutes` | Minuten mit Aktivität. Sich überschneidende Minuten über mehrere Bereiche hinweg werden einmal gezählt. |
| `session_minutes` | Minuten in Sitzungen. |
| `app_open_minutes` | Minuten, in denen das Mitglied Panel-Apps geöffnet hatte. |

Jede Person im Workspace hat eine Zeile. Ein Mitglied ohne Aktivität im Bereich hat nach `groups` leere Werte. Die Summen stimmen mit den [Nutzungsberichten](/de/administration/access/usage-reports/) überein, mit Ausnahme von Mitgliedern, die seitdem gelöscht wurden.

#### Daily per member

Die Mitgliederspalten, danach `day`, `source` (der Bereich), `events`, `active_minutes`, `session_minutes`, `first_at` und `last_at` (die Zeitpunkte der ersten und der letzten Aktivität an diesem Tag).

#### Inhalt

| Spalte | Enthält |
|---|---|
| `type` | `dashboard`, `panel_app`, `wasm_app` oder `notebook`. |
| `subject` | Die ID des Elements. Alle Notebooks teilen sich eine Zeile mit `*` an dieser Stelle. |
| `name` | Der Name des Elements oder `*` bei Notebooks. |
| `deleted` | Wahr, wenn das Element inzwischen gelöscht wurde. |
| `users` | Mitglieder, die es geöffnet haben. |
| `opens` | Wie oft es geöffnet wurde. |
| `last_used` | Wann es zuletzt verwendet wurde. |
| `app_open_minutes` | Minuten, in denen Panel-Apps geöffnet waren. |

#### Content by member

Die Mitgliederspalten, danach `type`, `subject`, `name` (wie bei **Inhalt**), `opens` (wie oft dieses Mitglied das Element geöffnet hat) und `last_day` (der letzte Nutzungstag des Mitglieds).

### Hinweise zu den Mitglieder-Datasets

- Aktivität von Agenten, Dienstkonten und seitdem gelöschten Mitgliedern hat leere Identitätsspalten. Ein gelöschtes Mitglied behält die `user_id` und nichts weiter.
- Die Öffnungen in **Inhalt** können die Summe der Öffnungen in **Content per member** übersteigen. Die Differenz sind Öffnungen, die sich keinem Mitglied zuordnen lassen, etwa eingebettete Ansichten oder Gastansichten eines Dashboards. **Inhalt** zählt sie, **Content per member** kann das nicht.

### Beispiel: Aktive Minuten nach Abteilung

**Mitglieder** und **Content per member** enthalten die `email` des Mitglieds in Kleinbuchstaben, sodass Sie sie mit einer eigenen Tabelle verknüpfen können, etwa einer HR- oder Organisationsstammtabelle, und nach Abteilung berichten.

1. Fügen Sie einen Schritt **Get Workspace Usage** hinzu, bei dem **Dataset** auf **Mitglieder** gesetzt ist, mit einer Zieltabelle wie `usage_members`.
2. Fügen Sie einen Schritt **Tabelle: Inner Join** hinzu, der `usage_members` mit Ihrer Organisationstabelle verknüpft, wo die `email`-Spalten in Kleinbuchstaben übereinstimmen. Behalten Sie die Abteilung aus Ihrer Tabelle sowie die Spalten `active_minutes` und `events` aus `usage_members`.
3. Aggregieren Sie im selben Schritt nach Abteilung und summieren Sie `active_minutes`.

Das Ergebnis sind die aktiven Minuten nach Abteilung. Mitglieder, die nicht in Ihrer Organisationstabelle stehen, fallen bei einem Inner Join heraus. Verwenden Sie daher einen Left Join, wenn Sie sie sehen möchten. Wiederholen Sie dies mit einem zweiten Schritt für **Content per member** und summieren Sie `opens` nach Abteilung, um zu berichten, wer welche Dashboards und Apps nutzt.

### Datumsbereich

**Range** legt die zu lesenden Tage fest:

- **Last number of days** (Standard 30) liest die letzten Tage einschließlich heute.
- **Previous month** liest den letzten vollen Kalendermonat.
- **Laufender Monat** liest vom Ersten dieses Monats bis heute.
- **Between dates** liest von **Startdatum** bis **Enddatum**. Lassen Sie **Enddatum** leer, um bis heute zu lesen.

Tage und Datumsangaben sind in UTC. **Tage**, **Startdatum** und **Enddatum** akzeptieren eine [Variable](/de/guides/workflows/manage-workflow-variables/) wie `{report_start}` sowie eine Zahl oder ein Datum im Format `YYYY-MM-DD`. Der Beginn darf nicht nach dem Ende liegen.

### Nutzungsziel

**Zieltabelle** nimmt das Ergebnis auf. Der Schritt ersetzt alles, was die Tabelle enthielt, und schreibt immer die Spalten des Datasets, auch wenn es keine Zeilen gibt.

## Warnungen

Diese lassen den Schritt nicht fehlschlagen. Er endet mit einer Warnung, die beschreibt, was geschehen ist, und schreibt die Tabelle trotzdem:

- Die Nutzungserfassung ist für den Workspace noch nicht eingerichtet.
- Im Bereich gab es keine Nutzung.
- Der Bereich beginnt vor dem aufbewahrten Zeitraum und wurde daher so gekürzt, dass er dort beginnt, wo der Verlauf einsetzt. Tagesdaten werden 180 Tage und Monatsdaten 25 Monate aufbewahrt.

## Sicherheitsprotokoll

Jede Ausführung schreibt einen Eintrag ins Sicherheitsprotokoll, der das Dataset, den Bereich, die Zieltabelle, den Workflow, den Schritt und die Ausführung sowie die Anzahl der geschriebenen Zeilen festhält.

## Verwandte Themen

- [Allgemeine Schritte](/de/reference/workflow-steps/general/)
- [Nutzungsberichte](/de/administration/access/usage-reports/)
- [Schritt Get Workspace Members](/de/reference/workflow-steps/general/get-workspace-members/)
