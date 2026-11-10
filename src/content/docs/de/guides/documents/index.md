---
title: Dateiverwaltung
description: Verwalten Sie Dateispeicherkonten in PlaidCloud, um Daten über CSV, Excel, Parquet und andere Dateiformate zu importieren und zu exportieren.
sidebar:
  label: Übersicht
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/index.md
---

PlaidCloud Documents: Speichern, organisieren, durchsuchen und teilen Sie Dateien zusammen mit Ihren Daten und Workflows. Dokumente können aus jedem verbundenen Speicherkonto stammen und in Workflows referenziert werden.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 200" role="img" aria-label="Verbundene Speicherkonten wie S3, Google Cloud Storage und OneDrive speisen PlaidCloud Documents, wo Dateien gespeichert, organisiert, durchsucht und geteilt werden. Workflow-Schritte referenzieren diese Dateien anschließend, um Daten zu importieren und zu exportieren." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="dc-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">Speicherkonten</text>
  <rect x="16" y="40" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="60" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">S3</text>
  <rect x="16" y="82" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Cloud Storage</text>
  <rect x="16" y="124" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="144" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">OneDrive</text>
  <path d="M136 55 C186 55 206 92 246 96" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 97 L246 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 139 C186 139 206 108 246 104" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="248" y="70" width="180" height="64" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="338" y="96" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Dokumente</text>
  <text x="338" y="115" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">speichern · organisieren · suchen · teilen</text>
  <path d="M428 102 L510 102" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="512" y="76" width="152" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="588" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Workflow-Schritte</text>
  <text x="588" y="118" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">Dateien importieren · exportieren</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Dateien gelangen aus jedem verbundenen Speicherkonto in Documents, wo Sie sie speichern, organisieren, durchsuchen und teilen – und referenzieren sie dann aus Workflow-Schritten, um Daten zu importieren und zu exportieren.</figcaption>
</figure>

## Der Arbeitsbereich „Documents“

**Dokument** öffnet sich mit einer Navigationsleiste auf der linken Seite und der ausgewählten Seite daneben. Mitglieder, die eine Seite nicht öffnen können, sehen deren Eintrag nicht.

| Eintrag der Navigationsleiste | Was er zeigt |
|---|---|
| **Übersicht** | Kacheln für Ihre Konten (**Konten**, **Freigegeben**, **Nur für Sie**, **Verwaltete Buckets**, **Externe Dienste** und **Deaktiviert**, wenn ein Konto Aufmerksamkeit erfordert), **Angeheftete** Dateien, **Konten nach Dienst** und **Wer sie verwenden kann**. Wählen Sie eine angeheftete Datei aus, um **Durchsuchen** in ihrem Ordner mit ausgewählter Datei zu öffnen. |
| **Durchsuchen** | Der Datei-Explorer. Wählen Sie das Konto aus der Liste in der Kopfzeile der Seite. Siehe [Dokumentenkonten verwenden](/de/guides/documents/using-document/). |
| **Freigegeben** | Konten, die für Sie freigegeben sind. Doppelklicken Sie auf eine Zeile, um sie zu durchsuchen. |
| **Meine privaten** | Konten, die nur Sie verwenden können. Doppelklicken Sie auf eine Zeile, um sie zu durchsuchen. |
| **Verwalten** | Konten, deren Eigentümer Sie sind, mit **Name**, **Dienst**, **Sicherheitstyp**, **Status** und **Beschreibung**. Ein Workspace-Administrator sieht hier jedes Dokumentenkonto und kann jedes davon verwalten. |

Die Navigationsleiste zeigt neben **Freigegeben**, **Meine privaten** und **Verwalten** einen Zähler an. Die Übersicht bietet für einen schnellen Einstieg die Schaltflächen **Dateien durchsuchen** und **Neues Konto**.

### Zeilenaktionen unter „Verwalten“

Öffnen Sie das Menü **⋯** einer Zeile, klicken Sie mit der rechten Maustaste auf die Zeile oder verwenden Sie das Menü **Aktionen** in der Symbolleiste für:

- **Öffnen** und **Bearbeiten**, die die Kontoseite öffnen.
- **Klonen…**, **Versionsverlauf** und **Verwendungsnachweis…**. Siehe [Verwendungsnachweis und Umstellung](/de/guides/documents/account-management/document-account-used-by/).
- **Who can use it**, mit **Mitglieder**, **Gruppen**, **Agenten** und **Eigentümer**. Siehe [Zugriff auf Dokumentenkonten steuern](/de/guides/documents/account-management/control-document-account-access/).
- **Aktivieren** oder **Deaktivieren** sowie **Löschen**.

### Die Kontoseite

**Neues Konto**, **Öffnen** und **Bearbeiten** zeigen das Konto als Seite an, mit **Konten verwalten** oben, um zurückzukehren. Sie enthält Karten für:

- **Allgemein**: Name, Dienst, Bucket und Startpfad des Kontos.
- **Zugriff**: das Sicherheitsmodell und wer das Konto verwenden kann. **Mitglieder**, **Gruppen**, **Agenten** und **Eigentümer** haben jeweils einen Link **Bearbeiten**, der dieselbe Auswahl öffnet wie das Zeilenmenü.
- **Anmeldedaten**: nur beschreibbare Felder für den gewählten Dienst. Ein Hinweis **Anmeldedaten gespeichert** zeigt, dass die Anmeldedaten festgelegt sind; gespeicherte Werte werden nie angezeigt. Lassen Sie ein Feld leer, um den gespeicherten Wert beizubehalten. SFTP-Konten bieten außerdem **Verbindung testen**.
- **SSH**: die Schlüsseleinstellungen, nur für SFTP-Konten.

Die Kopfzeile enthält **Durchsuchen**, **Verwendungsnachweis** und ein Menü **Aktionen** mit **Klonen**, **Versionsverlauf**, **Aktivieren** oder **Deaktivieren** und **Löschen**. Wenn Sie eine Seite mit nicht gespeicherten Änderungen verlassen, fragt PlaidCloud, ob diese verworfen werden sollen.

Alte Links und Lesezeichen zu Document-Bildschirmen öffnen weiterhin die entsprechende Seite.
