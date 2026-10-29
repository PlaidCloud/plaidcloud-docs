---
title: Projekt-Branding und App-Projekte
description: Legen Sie Markenfarben und ein Logo einmalig für ein Projekt fest, damit alle Panel-Apps darin einheitlich aussehen, und weisen Sie Panel-Apps beim Veröffentlichen oder später einem Projekt zu.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/branding.md
---

Eine Panel-App gehört zu einem Projekt. Das Projekt erfüllt für die App zwei Aufgaben: Es ist der Ort, an dem die App standardmäßig ihre Tabellen liest, und es enthält die Farben und das Logo, die die App trägt. Legen Sie das Branding einmal fest, und jede App im Projekt übernimmt es.

## Ein Projekt mit Branding versehen

1. Öffnen Sie das Projekt und wechseln Sie zur Registerkarte **Startseite**.
2. Klicken Sie in der Gruppe **Panel App Branding** auf **Edit Branding**.
3. Legen Sie beliebige Farben fest. Klicken Sie auf ein Farbfeld, um eine Farbe auszuwählen, oder geben Sie einen Hex-Wert wie `#0078d4` ein.
4. Wählen Sie optional ein Logo aus.
5. Prüfen Sie die **Vorschau** und klicken Sie dann auf **Speichern**.

Nur Manager und Architects können das Branding speichern. Andere Projektmitglieder sehen das Formular schreibgeschützt.

**Reset to default** löscht alle Farben und das Logo. Beim Speichern wird das gesamte Branding ersetzt, sodass eine Farbe, die Sie leer lassen, auf den PlaidCloud-Standard zurückgeht.

### Farben

| Einstellung | Was sie einfärbt |
|---|---|
| **Brand** | Schaltflächen, die aktive Registerkarte, Schieberegler-Griffe und andere primäre Steuerelemente. |
| **Brand accent** | Sekundäre Akzente. |
| **Brand hover** | Ein primäres Steuerelement, solange der Mauszeiger darüber steht. |
| **Brand pressed** | Ein primäres Steuerelement, solange es gedrückt wird. |
| **Header background** | Die Kopfzeile der App. |
| **Header text** | Der Titel und der Benutzername in der Kopfzeile. |
| **Link** | Links. |
| **Text on brand** | Text, der auf einem Steuerelement in der Markenfarbe steht. |

Diese acht sind die einzigen Einstellungen. Farben müssen 3-stellige oder 6-stellige Hex-Werte sein. Flächen, Fließtext und Rahmen behalten in Hell und Dunkel den PlaidCloud-Look, sodass ein Branding eine App nicht unlesbar machen kann.

### Logo

Das Logo ist ein Bild aus einem [Dokumentenkonto](/de/guides/documents/) im Workspace des Projekts.

1. Laden Sie das Bild in einen Ordner namens `branding` auf oberster Ebene des Dokumentenkontos hoch.
2. Wählen Sie in **Edit Branding** das **Dokumentenkonto** und dann unter **Image in the branding/ folder** das Bild aus.

Das Logo kann eine PNG-, JPEG-, GIF-, WebP- oder SVG-Datei mit bis zu 512 KB sein. Es erscheint auf der rechten Seite der Kopfzeile der App. Das Bild muss direkt in `branding/` oder in einem Ordner darin liegen, und jeder, der das Branding speichert, muss das Konto lesen können.

### Wann Änderungen erscheinen

Eine App liest ihr Branding, wenn die Sitzung eines Betrachters beginnt. Gespeicherte Änderungen werden beim nächsten Öffnen oder Neuladen der App sichtbar.

## Eine App einem Projekt zuweisen

### Beim Veröffentlichen

Der Dialog **Server-Panel-App veröffentlichen** enthält unter **Verzeichniseinstellungen** eine Auswahl **Projekt**. Wählen Sie das Projekt, dem die App gehört. Sie benötigen Zugriff auf das Projekt, um darin zu veröffentlichen. Das Projekt steht fest, sobald die App veröffentlicht ist; um eine App zu verschieben, verwenden Sie wie unten beschrieben **Zuweisen**.

Eine App, die mit einem Projekt veröffentlicht wurde, liest standardmäßig die Tabellen dieses Projekts, sodass `table("sales")` kein Projektargument benötigt.

### Für vorhandene Apps

1. Öffnen Sie **Meine Panel-Apps**.
2. Klicken Sie in der Zeile der App, die Sie verschieben möchten, auf das Symbol **Zuweisen**.
3. Wählen Sie das **Projekt** und klicken Sie auf **Prüfen**.
4. Lesen Sie das Ergebnis. Es listet die Workspace-Mitglieder auf, die die App heute öffnen können, aber keine Mitglieder des Projekts sind.
5. Klicken Sie auf **Zuweisen**.

Prüfen ändert nichts. Die Spalte **Projekt** in **Meine Panel-Apps** zeigt das Projekt jeder App.

### Zugriff

Wer eine App öffnen kann, ändert sich heute durch ihr Projekt nicht: Betrachter, die die App zuvor öffnen konnten, können es weiterhin. Künftig soll sich der Zugriff auf eine App nach der Mitgliedschaft in ihrem Projekt richten. Deshalb listet **Prüfen** die Mitglieder auf, die nicht im Projekt sind, damit Sie sie zuerst hinzufügen können.

## Nächste Schritte

- [Das Panel App Kit](/de/guides/panel-apps/app-kit/) – die Komponenten, die Ihr Branding verwenden.
- [Eine Panel-App erstellen](/de/guides/panel-apps/creating/) – veröffentlichen Sie eine App in einem Projekt.
