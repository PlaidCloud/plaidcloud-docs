---
title: Get Workspace Usage-Schritt
description: Schreiben Sie die Workspace-Nutzung als Aktivität, Mitglieder, Inhalte oder Trends in eine Projekttabelle, um die Akzeptanz auszuwerten oder einen nachgelagerten Schritt zu speisen.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Beschreibung

Schreibt, wie Ihr Workspace genutzt wird, in eine Projekttabelle. Verwenden Sie den Schritt, um die Akzeptanz im Zeitverlauf zu verfolgen, die Nutzung nach Abteilung oder Team auszuwerten, eigene Dashboards zu erstellen oder in einem geplanten Workflow einen Aktivitätsrückgang zu melden. Die Zahlen stammen aus denselben Nutzungsdaten wie die [Nutzungsberichte](/de/administration/access/usage-reports/), und jedes Dataset deckt alle Bereiche ab.

**Aktivität** und **Mitglieder** enthalten Mitgliederidentitäten (Benutzer-ID, Benutzername, E-Mail, Vor- und Nachname sowie Sicherheitsgruppen). Die Zieltabelle ist eine gewöhnliche Projekttabelle, sodass jeder mit Zugriff auf das Projekt sie lesen kann: Behandeln Sie sie wie jede Mitgliederliste. Jede Ausführung, die die Tabelle schreibt, wird im Sicherheitsprotokoll festgehalten.

## Konfiguration

### Usage Data

**Dataset** legt fest, was jede Zeile enthält. Der Text darunter beschreibt die Zeilen und nennt die wichtigsten Spalten des gewählten Datasets.

| Dataset | Wert | Eine Zeile für jeweils | Enthält Identität |
|---|---|---|---|
| **Aktivität** (Standard) | `activity` | Tag, Mitglied, Aktion und Element | Ja |
| **Mitglieder** | `members` | Mitglied, auch Mitglieder ohne Aktivität | Ja |
| **Inhalt** | `content` | Dashboard, App und Notebook, auch Dashboards und Apps, die niemand genutzt hat | Nein |
| **Trends** | `trends` | Tag, Woche und Monat des Zeitraums | Nein |

Die Werte sind das, was ein Schritt enthält, wenn Sie ihn über die API oder einen KI-Assistenten erstellen oder bearbeiten. Ein Schritt, der mit einem Dataset gespeichert wurde, das nicht in dieser Liste steht, schlägt bei der Ausführung fehl und nennt die vier Datasets: Öffnen Sie ihn, wählen Sie ein **Dataset** und speichern Sie ihn. Ein zuvor gespeicherter Schritt mit **Mitglieder** oder **Inhalt** läuft weiter und schreibt die unten stehenden Spalten, und ein Schritt, der auf einen Bereich beschränkt war, deckt nun alle Bereiche ab. In **Inhalt** heißt `subject` jetzt `item_id`, und `type` enthält `Dashboard`, `App` oder `Notebook`.

### Spalten

Daten und Tage landen als Zeitstempel um Mitternacht UTC.

#### Mitgliederspalten

**Aktivität** und **Mitglieder** enthalten diese Spalten:

| Spalte | Enthält |
|---|---|
| `user_id` | Die ID des Mitglieds. |
| `user_name` | Der Benutzername des Mitglieds. |
| `email` | Die E-Mail-Adresse des Mitglieds in Kleinbuchstaben. |
| `first_name` | Vorname. |
| `last_name` | Nachname. |
| `is_active` | Wahr, wenn das Mitglied aktiv ist, falsch, wenn es deaktiviert wurde. |
| `groups` | Die Sicherheitsgruppen des Mitglieds, getrennt durch `; `. |


`groups` listet die Gruppen der obersten Ebene auf, denen das Mitglied direkt angehört.

#### Aktivität

| Spalte | Enthält |
|---|---|
| `day` | Der Tag. |
| Die Mitgliederspalten | Wie oben. |
| `member` | Vor- und Nachname des Mitglieds oder sein Benutzername, wenn keines von beiden gesetzt ist. |
| `area` | `PlaidCloud app`, `Dashboards`, `Apps` oder `Notebooks`. |
| `action` | `Opened app`, `Opened screen`, `Opened step`, `Saved step`, `Used palette action`, `Viewed dashboard`, `Used chart`, `Opened notebook` oder `Saved notebook`. |
| `item_type` | `App area`, `Screen`, `Step`, `Palette action`, `Dashboard`, `Chart`, `App` oder `Notebook`. |
| `item_id` | Die ID des Elements. Bei einem Notebook sein Pfad. |
| `item_name` | Der Name des Elements: ein Bildschirm oder App-Bereich in Worten, etwa `Members List`; der Schritttyp; der Name des Dashboards, des Diagramms oder der App; oder der Pfad des Notebooks. Wenn sich kein Name finden lässt, die ID des Elements. |
| `events` | Wie oft das Mitglied es an diesem Tag getan hat. |
| `source` | Der Schlüssel des Bereichs, wie ihn die Exporte der [Nutzungsberichte](/de/administration/access/usage-reports/) nennen. |
| `event` | Der Schlüssel der Aktion, wie ihn die Exporte nennen. |

`member` und die Mitgliederspalten hängen davon ab, wer die Aktion ausgeführt hat:

- Aktivität, die sich keinem Mitglied zuordnen lässt, hat `Unattributed` in `member` und leere Mitgliederspalten.
- Ein seither gelöschtes Mitglied behält nur die `user_id`, und `member` ist `Deleted user`.
- Jedes andere Konto, etwa ein Servicekonto oder ein Agent, behält nur die `user_id`, und `member` ist sein Benutzername.

`Used chart` zählt einmal pro Mitglied und Diagramm in jedem 5-Minuten-Fenster, misst also die Nutzung, nicht die Abfragen.

#### Mitglieder

| Spalte | Enthält |
|---|---|
| Die Mitgliederspalten | Wie oben. |
| `member` | Vor- und Nachname des Mitglieds oder sein Benutzername, wenn keines von beiden gesetzt ist. |
| `created` | Der Tag, an dem das Mitglied zum Workspace hinzugefügt wurde, sofern bekannt. |
| `status` | `Active`, wenn das Mitglied im Zeitraum aktiv war, `Dormant`, wenn es PlaidCloud zuvor, aber nicht im Zeitraum genutzt hat, `Never active`, wenn bis zum Ende des Zeitraums keine Nutzung verzeichnet ist. |
| `first_seen` | Der erste verzeichnete Tag, an dem das Mitglied PlaidCloud genutzt hat, unabhängig vom Zeitraum. |
| `last_seen` | Der letzte Aktivitätstag des Mitglieds im Zeitraum. |
| `active_days` | Tage mit Aktivität im Zeitraum. |
| `events` | Aktivitätsereignisse im Zeitraum. |
| `active_minutes` | Minuten mit Aktivität im Zeitraum. |
| `session_minutes` | Minuten in Sitzungen im Zeitraum. |
| `app_open_minutes` | Minuten, in denen das Mitglied Panel-Apps im Zeitraum geöffnet hatte. Studio-Vorschauen werden nicht gezählt. |

Jedes Mitglied hat eine Zeile, auch deaktivierte Mitglieder, außer Mitgliedern, deren Nutzungsdaten gelöscht wurden. Servicekonten und Agenten werden nicht aufgeführt. Ein Mitglied ohne Aktivität im Zeitraum hat kein `last_seen`, und seine übrigen Aktivitätsspalten sind leer.

#### Inhalt

| Spalte | Enthält |
|---|---|
| `type` | `Dashboard`, `App` oder `Notebook`. |
| `item_id` | Die ID des Dashboards oder der App oder der Pfad des Notebooks. |
| `name` | Der Name des Dashboards oder der App oder der Pfad des Notebooks. Leer, wenn das Element gelöscht wurde oder Namen nicht gelesen werden können. |
| `deleted` | Wahr, wenn das Dashboard oder die App inzwischen gelöscht wurde. |
| `unused` | Wahr für ein Dashboard oder eine App, die im Zeitraum niemand genutzt hat. |
| `users` | Mitglieder, die es im Zeitraum genutzt haben. |
| `opens` | Anzahl der Öffnungen im Zeitraum, einschließlich Öffnungen, die sich keinem Mitglied zuordnen lassen. |
| `last_used` | Der letzte Tag der Nutzung im Zeitraum. Bei einem ungenutzten Element der letzte Tag, an dem es vor Ende des Zeitraums geöffnet wurde, oder leer. |
| `app_open_minutes` | Minuten, in denen eine Panel-App im Zeitraum geöffnet war. Leer bei Dashboards, Notebooks sowie Dash- und WASM-Apps. |

Jeder Notebook-Pfad hat eine eigene Zeile. Die Zeilen nennen zuerst, was genutzt wurde, mit den meisten Benutzern zuerst, dann die Dashboards und Apps, die niemand genutzt hat. Das sind die veröffentlichten Dashboards und Apps, die zu Beginn des Zeitraums bereits existierten. Sie werden nur aufgeführt, wenn der Zeitraum innerhalb der aufbewahrten Tagesdaten beginnt, die Nutzung dieser Elementart dann bereits erfasst wurde und Namen gelesen werden können. Studio-Vorschauen von Apps bleiben unberücksichtigt.

#### Trends

| Spalte | Enthält |
|---|---|
| `period` | `Day`, `Week` oder `Month`. |
| `period_start` | Der erste Tag des Zeitabschnitts. Wochen beginnen am Montag. |
| `active_members` | Mitglieder, die im Zeitabschnitt aktiv waren, innerhalb des Zeitraums. |
| `events` | Aktivitätsereignisse im Zeitabschnitt. |
| `active_minutes` | Minuten mit Aktivität im Zeitabschnitt. |
| `session_minutes` | Minuten in Sitzungen im Zeitabschnitt. |
| `active_members_7d` | In einer `Day`-Zeile die Mitglieder, die in den 7 Tagen bis zu diesem Tag aktiv waren. |
| `active_members_28d` | In einer `Day`-Zeile die Mitglieder, die in den 28 Tagen bis zu diesem Tag aktiv waren. |
| `stickiness` | In einer `Day`-Zeile `active_members` geteilt durch `active_members_28d`. |
| `complete` | Falsch für heute, für eine Woche oder einen Monat, der heute enthält, und für eine Woche oder einen Monat, die der Zeitraum anschneidet. |

Jeder Tag des Zeitraums, ab dem Beginn der aufbewahrten Tagesdaten, hat eine Zeile, auch ohne Nutzung, ebenso jede Woche und jeder Monat, in die diese Tage fallen. `active_members_7d`, `active_members_28d` und `stickiness` sind in `Week`- und `Month`-Zeilen leer sowie in einer `Day`-Zeile, deren 7 oder 28 Tage vor die aufbewahrten Tagesdaten zurückreichen. `stickiness` ist außerdem leer, wenn `active_members_28d` 0 ist. Ein Monat, der vor den aufbewahrten Tagesdaten beginnt und vollständig im Zeitraum liegt, stammt aus den Monatszusammenfassungen: Er hat `active_members`, aber leere Ereignisse und Minuten, und `complete` gibt an, ob die Zusammenfassung den ganzen Monat abdeckte.

### Beispiel: Aktive Minuten nach Abteilung

**Aktivität** und **Mitglieder** enthalten die `email` des Mitglieds in Kleinbuchstaben. So können Sie sie mit einer eigenen Tabelle verknüpfen, etwa einer HR- oder Organisationsstammtabelle, und nach Abteilung berichten.

1. Fügen Sie einen Schritt **Get Workspace Usage** hinzu, mit **Dataset** auf **Mitglieder** und einer Zieltabelle wie `usage_members`.
2. Fügen Sie einen Schritt **Tabelle: Inner Join** hinzu, der `usage_members` mit Ihrer Organisationstabelle verknüpft, wo die `email`-Spalten in Kleinbuchstaben übereinstimmen. Behalten Sie die Abteilung aus Ihrer Tabelle sowie die Spalten `active_minutes` und `events` aus `usage_members`.
3. Aggregieren Sie im selben Schritt nach Abteilung und summieren Sie `active_minutes`.

Das Ergebnis sind die aktiven Minuten nach Abteilung. Mitglieder, die nicht in Ihrer Organisationstabelle stehen, fallen bei einem Inner Join heraus. Verwenden Sie daher einen Left Join, wenn Sie sie sehen möchten. Wiederholen Sie das mit einem zweiten Schritt auf **Aktivität** und summieren Sie `events` nach Abteilung und `item_name`, um auszuwerten, wer welche Dashboards und Apps nutzt.

### Date Range

**Zeitraum** legt fest, welche Tage gelesen werden:

| Zeitraum | Wert | Liest |
|---|---|---|
| **Letzte Anzahl von Tagen** (Standard 30) | `last_days` | Die letzten Tage, einschließlich heute. |
| **Vormonat** | `previous_month` | Den letzten vollständigen Kalendermonat. |
| **Laufender Monat** | `month_to_date` | Vom Ersten dieses Monats bis heute. |
| **Zwischen Daten** | `dates` | Von **Startdatum** bis **Enddatum**. Lassen Sie **Enddatum** leer, um bis heute zu lesen. |

Tage und Daten sind in UTC. **Tage** nimmt eine ganze Zahl entgegen. **Startdatum** und **Enddatum** nehmen ein Datum im Format `YYYY-MM-DD` oder eine [Variable](/de/guides/workflows/manage-workflow-variables/) wie `{report_start}` entgegen. Der Start darf nicht nach dem Ende liegen.

Tagesdaten werden 180 Tage lang aufbewahrt, Monatszusammenfassungen 25 Monate.

### Usage Target

**Zieltabelle** erhält das Ergebnis. Der Schritt ersetzt den bisherigen Inhalt der Tabelle und schreibt immer die Spalten des Datasets, auch wenn es keine Zeilen gibt.

## Warnungen

Diese lassen den Schritt nicht fehlschlagen. Er endet mit der Warnung und ersetzt die Tabelle trotzdem, mit den Spalten des Datasets:

| Warnung | Bedeutung |
|---|---|
| "Usage data is not available yet: the usage database has not been set up on this workspace." | Die Nutzungserfassung ist für den Workspace noch nicht eingerichtet. |
| "Usage data is not available right now: the usage database could not be reached." | Die Nutzungsdaten konnten nicht gelesen werden. Führen Sie den Schritt später erneut aus. |
| "No usage from *start* to *end*." | Im Zeitraum gab es keine Nutzung. |
| "Usage before *date* isn't kept, so the range was clipped to start there." | Der Zeitraum beginnt vor den aufbewahrten Tagesdaten, daher wird die Aktivität ab *date* gezählt. **Trends** enthält die vollständigen Monate davor weiterhin aus den Monatszusammenfassungen. |
| "This took too long to compute: narrow the date range." | Das Lesen hat zu lange gedauert, daher hat die Tabelle keine Zeilen. Wählen Sie einen kürzeren Zeitraum. |
| "Some names are unavailable right now, so those items are named by their id." | Nur **Aktivität**. Einige Namen von Dashboards, Diagrammen oder Apps konnten nicht gelesen werden, daher enthält `item_name` die ID. |
| "Members could not be read right now, so they are named by their id." | Nur **Aktivität**. Die Mitgliederliste konnte nicht gelesen werden, daher enthält `member` die ID des Mitglieds und von den Mitgliederspalten ist nur `user_id` gefüllt. |
| "Names are unavailable right now, so items nobody used are not listed." | Nur **Inhalt**. Namen von Dashboards oder Apps konnten nicht gelesen werden, daher werden nur genutzte Elemente aufgeführt. |
| "Activity before *date* isn't kept, so items nobody used in this range can't be listed." | Nur **Inhalt**. Der Zeitraum beginnt vor den aufbewahrten Tagesdaten, daher werden nur genutzte Elemente aufgeführt. |

Wenn die Mitgliederliste nicht gelesen werden kann, schlägt stattdessen **Mitglieder** fehl und lässt die Zieltabelle unverändert.

## Sicherheitsprotokoll

Jede Ausführung, die die Tabelle schreibt, fügt dem Sicherheitsprotokoll einen Eintrag hinzu, der das Dataset, den Zeitraum, die Zieltabelle und ihr Projekt, den Workflow, den Schritt und die Ausführung, die Anzahl der geschriebenen Zeilen und, bei **Aktivität** und **Mitglieder**, den Hinweis festhält, dass die Zeilen Mitgliederidentitäten enthalten.

## Verwandte Themen

- [Allgemeine Schritte](/de/reference/workflow-steps/general/)
- [Nutzungsberichte](/de/administration/access/usage-reports/)
- [Get Workspace Members-Schritt](/de/reference/workflow-steps/general/get-workspace-members/)
