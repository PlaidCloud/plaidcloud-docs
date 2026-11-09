---
title: Get Workspace Usage-Schritt
description: Schreiben Sie Workspace-Nutzungssummen aus den Nutzungsberichten tages- oder monatsweise in eine Projekttabelle, um die Akzeptanz darzustellen oder einen nachgelagerten Schritt zu speisen.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Beschreibung

Schreibt, wie Ihr Workspace genutzt wird, in eine Projekttabelle. Verwenden Sie den Schritt, um die Akzeptanz im Zeitverlauf zu verfolgen, die Nutzung nach Abteilung oder Team auszuwerten, eigene Dashboards zu erstellen oder in einem geplanten Workflow einen Aktivitätsrückgang zu melden. Die Zahlen entsprechen denen in den [Nutzungsberichten](/de/administration/access/usage-reports/).

Drei Datasets enthalten nur Summen: Keine Zeile nennt ein Mitglied, und Notebook-Pfade sind durch `*` ersetzt. Die anderen vier (**Mitglieder**, **Täglich pro Mitglied**, **Inhalt** und **Inhalte pro Mitglied**) sind für Berichte gedacht. **Mitglieder**, **Täglich pro Mitglied** und **Inhalte pro Mitglied** enthalten Mitgliederidentitäten (Benutzer-ID, Benutzername, E-Mail, Vor- und Nachname sowie Sicherheitsgruppen). Behandeln Sie die Zieltabelle daher wie jede Mitgliederliste. Jede Ausführung des Schritts wird im Sicherheitsprotokoll festgehalten.

## Konfiguration

### Usage Data

**Dataset** legt fest, was jede Zeile enthält:

| Dataset | Wert | Eine Zeile für jeweils | Enthält Identität |
|---|---|---|---|
| **Täglich pro Element** | `daily_item` | Tag, Bereich, Ereignis und Subjekt | Nein |
| **Monatlich pro Element** | `monthly_item` | Monat, Bereich, Ereignis und Subjekt | Nein |
| **Monatssummen** (Standard) | `monthly_tenant` | Monat und Bereich | Nein |
| **Mitglieder** | `members` | Person im Workspace | Ja |
| **Täglich pro Mitglied** | `daily_user` | Person, Tag und Bereich | Ja |
| **Inhalt** | `content` | Dashboard, App oder Notebook | Nein |
| **Inhalte pro Mitglied** | `content_user` | Person und Element | Ja |

**Bereich** beschränkt die Zeilen auf einen Bereich. Belassen Sie die Einstellung auf **Alle Bereiche**, um alle einzubeziehen.

| Bereich | Wert |
|---|---|
| **Alle Bereiche** (Standard) | `""` |
| **PlaidCloud-App** | `plaidclient` |
| **Dashboards** | `superset` |
| **Apps** | `panel` |
| **App-Besuche** | `panel_visit` |
| **Notebook-Server** | `jupyterhub` |
| **Notebooks** | `jupyter` |

Die Werte sind das, was ein Schritt enthält, wenn Sie ihn über die API oder einen KI-Assistenten erstellen oder bearbeiten.

### Spalten

#### Daily Per Item

`day`, `source`, `event`, `subject`, `events`.

#### Monthly Per Item

`month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial`.

#### Monthly Totals

`month`, `source`, `active_users`, `coverage_start`, `partial`.

`partial` ist wahr für einen Monat, den der Verlauf nicht vollständig abdeckt, und `coverage_start` ist das Datum, an dem die Erfassung begann. Ein Monat wird 3 Tage nach seinem Abschluss aufgenommen, sobald sich seine Zahlen stabilisiert haben.

#### Mitgliederspalten

**Mitglieder**, **Täglich pro Mitglied** und **Inhalte pro Mitglied** beginnen mit denselben sieben Spalten:

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

Die Mitgliederspalten, dann:

| Spalte | Enthält |
|---|---|
| `first_seen` | Der erste Tag, an dem das Mitglied PlaidCloud überhaupt genutzt hat, unabhängig vom Zeitraum. Wenn Sie einen **Bereich** festlegen, ist es der erste Tag in diesem Bereich. |
| `last_seen` | Der letzte Aktivitätstag des Mitglieds innerhalb des Zeitraums. |
| `active_days` | Tage mit Aktivität im Zeitraum. |
| `events` | Aktivitätsereignisse im Zeitraum. |
| `active_minutes` | Minuten mit Aktivität. Sich überschneidende Minuten über mehrere Bereiche hinweg werden einmal gezählt. |
| `session_minutes` | Minuten in Sitzungen. |
| `app_open_minutes` | Minuten, in denen das Mitglied Panel-Apps geöffnet hatte. |

Jedes Mitglied hat eine Zeile, außer Mitgliedern, deren Nutzungsdaten gelöscht wurden. Servicekonten und Agenten werden nicht aufgeführt. Ein Mitglied ohne Aktivität im Zeitraum hat nach `groups` leere Werte. Die Summen stimmen mit den [Nutzungsberichten](/de/administration/access/usage-reports/) überein, mit Ausnahme von Mitgliedern, die seither gelöscht wurden.

#### Täglich pro Mitglied

Die Mitgliederspalten, dann `day`, `source` (der Bereich), `events`, `active_minutes`, `session_minutes`, `first_at` und `last_at` (die Zeiten der ersten und der letzten Aktivität an diesem Tag).

#### Inhalt

| Spalte | Enthält |
|---|---|
| `type` | `dashboard`, `panel_app`, `wasm_app` oder `notebook`. |
| `subject` | Die ID des Elements. Alle Notebooks teilen sich eine Zeile mit `*` an dieser Stelle. |
| `name` | Der Name des Elements oder `*` für Notebooks. |
| `deleted` | Wahr, wenn das Element inzwischen gelöscht wurde. |
| `users` | Mitglieder, die es geöffnet haben. |
| `opens` | Anzahl der Öffnungen. |
| `last_used` | Zeitpunkt der letzten Nutzung. |
| `app_open_minutes` | Minuten, in denen Panel-Apps geöffnet waren. |

#### Inhalte pro Mitglied

Die Mitgliederspalten, dann `type`, `subject`, `name` (wie bei **Inhalt**), `opens` (wie oft dieses Mitglied das Element geöffnet hat) und `last_day` (der letzte Nutzungstag des Mitglieds).

### Hinweise zu den Mitglieder-Datasets

- Aktivität von Agenten, Servicekonten und seither gelöschten Mitgliedern hat leere Identitätsspalten. Ein gelöschtes Mitglied behält nur die `user_id`.
- Die Öffnungen in **Inhalt** können die Summe der Öffnungen in **Inhalte pro Mitglied** übersteigen. Der Unterschied sind Öffnungen, die sich keinem Mitglied zuordnen lassen, etwa eingebettete oder Gastansichten eines Dashboards. **Inhalt** zählt sie, **Inhalte pro Mitglied** kann das nicht.

### Beispiel: Aktive Minuten nach Abteilung

**Mitglieder** und **Inhalte pro Mitglied** enthalten die `email` des Mitglieds in Kleinbuchstaben. So können Sie sie mit einer eigenen Tabelle verknüpfen, etwa einer HR- oder Organisationsstammtabelle, und nach Abteilung berichten.

1. Fügen Sie einen Schritt **Get Workspace Usage** hinzu, mit **Dataset** auf **Mitglieder** und einer Zieltabelle wie `usage_members`.
2. Fügen Sie einen Schritt **Tabelle: Inner Join** hinzu, der `usage_members` mit Ihrer Organisationstabelle verknüpft, wo die `email`-Spalten in Kleinbuchstaben übereinstimmen. Behalten Sie die Abteilung aus Ihrer Tabelle sowie die Spalten `active_minutes` und `events` aus `usage_members`.
3. Aggregieren Sie im selben Schritt nach Abteilung und summieren Sie `active_minutes`.

Das Ergebnis sind die aktiven Minuten nach Abteilung. Mitglieder, die nicht in Ihrer Organisationstabelle stehen, fallen bei einem Inner Join heraus. Verwenden Sie daher einen Left Join, wenn Sie sie sehen möchten. Wiederholen Sie das mit einem zweiten Schritt auf **Inhalte pro Mitglied** und summieren Sie `opens` nach Abteilung, um auszuwerten, wer welche Dashboards und Apps nutzt.

### Date Range

**Zeitraum** legt fest, welche Tage gelesen werden:

| Zeitraum | Wert | Liest |
|---|---|---|
| **Letzte Anzahl von Tagen** (Standard 30) | `last_days` | Die letzten Tage, einschließlich heute. |
| **Vormonat** | `previous_month` | Den letzten vollständigen Kalendermonat. |
| **Laufender Monat** | `month_to_date` | Vom Ersten dieses Monats bis heute. |
| **Zwischen Daten** | `dates` | Von **Startdatum** bis **Enddatum**. Lassen Sie **Enddatum** leer, um bis heute zu lesen. |

Tage und Daten sind in UTC. **Tage**, **Startdatum** und **Enddatum** akzeptieren eine [Variable](/de/guides/workflows/manage-workflow-variables/) wie `{report_start}` sowie eine Zahl oder ein Datum im Format `YYYY-MM-DD`. Der Start darf nicht nach dem Ende liegen.

### Usage Target

**Zieltabelle** erhält das Ergebnis. Der Schritt ersetzt den bisherigen Inhalt der Tabelle und schreibt immer die Spalten des Datasets, auch wenn es keine Zeilen gibt.

## Warnungen

Diese lassen den Schritt nicht fehlschlagen. Er endet mit einer Warnung, die beschreibt, was passiert ist, und schreibt die Tabelle trotzdem:

- Die Nutzungserfassung ist für den Workspace noch nicht eingerichtet.
- Im Zeitraum gab es keine Nutzung.
- Der Zeitraum beginnt vor dem aufbewahrten Bestand und wurde daher so gekürzt, dass er dort beginnt, wo der Verlauf beginnt. Tagesdaten werden 180 Tage lang aufbewahrt, Monatsdaten 25 Monate.

## Sicherheitsprotokoll

Jede Ausführung schreibt einen Eintrag in das Sicherheitsprotokoll, der das Dataset, den Zeitraum, die Zieltabelle, den Workflow, den Schritt und die Ausführung sowie die Anzahl der geschriebenen Zeilen festhält.

## Verwandte Themen

- [Allgemeine Schritte](/de/reference/workflow-steps/general/)
- [Nutzungsberichte](/de/administration/access/usage-reports/)
- [Get Workspace Members-Schritt](/de/reference/workflow-steps/general/get-workspace-members/)
