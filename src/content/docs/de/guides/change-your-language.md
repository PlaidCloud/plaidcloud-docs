---
title: Sprache ändern
description: Zeigen Sie PlaidCloud auf Englisch (US), Englisch (UK), Deutsch, Español, Français, Português (Portugal), Português (Brasil), Polski, 日本語, 한국어 oder 简体中文 an, und Ihre Auswahl folgt Ihnen auf andere Geräte.
sidebar:
  label: Sprache ändern
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/change-your-language.md
---

Die Oberfläche von PlaidCloud ist in elf Sprachen verfügbar:

| Sprache | Menüeintrag |
|---|---|
| Englisch (US) | English (US) |
| Englisch (UK) | English (UK) |
| Deutsch | Deutsch |
| Spanisch | Español |
| Französisch | Français |
| Portugiesisch (Portugal) | Português (Portugal) |
| Portugiesisch (Brasilien) | Português (Brasil) |
| Polnisch | Polski |
| Japanisch | 日本語 |
| Koreanisch | 한국어 |
| Chinesisch (vereinfacht) | 简体中文 |

Alle beginnen mit Englisch (US). Es ändert sich nichts, bis Sie eine Sprache auswählen.

## Sprache ändern

1. Klicken Sie in der oberen Kopfzeile auf die Schaltfläche **Sprache**, neben der Schaltfläche **Darstellung**. Ihr Menü listet jede Sprache unter ihrem eigenen Namen auf, sodass Sie Ihre finden, egal welche Sprache gerade angezeigt wird.
2. Wählen Sie eine Sprache aus.
3. Eine Meldung bestätigt, dass PlaidCloud in dieser Sprache neu geladen wird. Nicht gespeicherte Änderungen gehen verloren, speichern Sie Ihre Arbeit also zuerst. Klicken Sie auf **Neu laden**, um fortzufahren, oder brechen Sie ab, um alles beim Alten zu lassen.

PlaidCloud speichert Ihre Auswahl in Ihrem Profil und lädt in der neuen Sprache neu. Um zurückzuwechseln, wählen Sie auf dieselbe Weise **English (US)**.

## Wo Ihre Auswahl gilt

- **Andere Geräte und Browser.** Ihre Auswahl folgt Ihnen. Wenn Sie sich auf einem anderen Gerät oder in einem anderen Browser beim selben Workspace anmelden, gilt sie ab dem nächsten Laden der Seite.
- **Pro Workspace.** Die Auswahl gehört zu Ihrem Profil in einem Workspace. Wenn Sie mehrere Workspaces verwenden, legen Sie die Sprache in jedem einzeln fest.

## Zahlen und Datumsangaben

Zahlen und Datumsangaben werden im Format der gewählten Sprache angezeigt. Auf Deutsch wird zum Beispiel eintausendzweihundertvierunddreißig und ein halbes als `1.234,5` angezeigt. Auf Polnisch wird 1234567.89 als `1 234 567,89` und der 12. Oktober 2026 als `12.10.2026` angezeigt. Japanisch und Chinesisch zeigen dieses Datum als `2026/10/12`, Koreanisch als `26. 10. 12.`. Englisch (UK) verwendet britische Rechtschreibung und britische Formate.

Nur die Anzeige ändert sich. Werte, die Sie speichern, exportieren oder an Integrationen senden, behalten ihr gewohntes Format.

## Eingabe auf Japanisch, Koreanisch und Chinesisch

Japanische, koreanische und chinesische Eingabemethoden funktionieren in Zahlenfeldern und anderen Feldern, die die Eingabe einschränken. Vollbreite Ziffern werden während der Eingabe umgewandelt, sodass aus `１２３` die Zahl `123` wird.

## Was sonst noch Ihrer Sprache folgt

Auch die Texte, die PlaidCloud Ihnen vom Server sendet, folgen Ihrer Sprache, und zwar in jeder von PlaidCloud angebotenen Sprache:

- **E-Mails.** System-E-Mails wie Einladungen, Passwort-Zurücksetzungen, Benachrichtigungen zu Workflows und Migrationen sowie E-Mails zu Registrierung, Abrechnung und Support.
- **Anmeldebildschirme.** Die Bildschirme für Anmeldung, Passwortvergabe und Abmeldung sowie die E-Mails, die Keycloak von dort aus sendet.
- **Fehlermeldungen.** Die Meldungen, die PlaidCloud anzeigt, wenn eine Anfrage fehlschlägt – in der Oberfläche, über die REST-API und über JSON-RPC.
- **PDF der Projektdokumentation.** Das PDF, das PlaidCloud zur Dokumentation eines Projekts erzeugt.

## Wie PlaidCloud die Sprache auswählt

| Wo | Verwendete Sprache |
|---|---|
| In PlaidCloud | Die Sprache, die Sie mit der Schaltfläche **Sprache** gewählt haben. Ihre Anmeldeseite und Ihre E-Mails folgen derselben Auswahl. |
| Anmeldung und andere Bildschirme vor der Anmeldung | Die Sprache Ihres Browsers. |
| Registrierung | Die Sprache Ihres Browsers. PlaidCloud speichert sie bei Ihrer Organisation, und Abrechnungs- und Konto-E-Mails an die Organisation verwenden sie. |

Wenn Ihr Browser oder Profil eine Sprache verwendet, die PlaidCloud nicht anbietet, erscheint der Text auf Englisch (US). Browser, die auf Traditionelles Chinesisch (zh-TW oder zh-HK) eingestellt sind, greifen bei Servertexten auf Englisch (US) zurück.

## Was auf Englisch bleibt

- Meldungen und Protokolle zu Ausführungen von Workflows und Schritten sowie der Aktivitätsstream. Viele Personen lesen diese, und die Beibehaltung einer Sprache hält sie durchsuchbar und einheitlich.
- Texte des KI-Assistenten und der MCP-Tools.
- E-Mails, die Sie selbst verfassen, einschließlich E-Mail-Vorlagen und E-Mails, die von Berichtsschritten gesendet werden.
- Die OpenAPI-Dokumentation.
- Fehlertexte der SQL- und Ausdruck-Engines.
- Die Registrierungsbildschirme.
- Inhalte, die Sie erstellen, etwa die Namen von Projekten, Tabellen und Schritten.
