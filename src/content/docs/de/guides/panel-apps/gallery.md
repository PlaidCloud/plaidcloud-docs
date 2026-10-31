---
title: Die App-Galerie
description: Nehmen Sie eine Studio-App in die Galerie auf oder entfernen Sie sie wieder, und erstellen Sie aus einer aufgelisteten App eine neue App.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/gallery.md
---

Die App-Galerie ist das Regal, in dem Ihr Workspace fertige Panel-Apps bereithält. Jeder, der das Projekt einer aufgelisteten App ansehen kann, kann in einem Projekt, das er bearbeiten kann, eine eigene Kopie erstellen und ändern. So wird eine gute App zu einem Ausgangspunkt, statt dass jeder sie neu aufbaut.

## Eine App aus der Galerie erstellen

1. Wählen Sie in **Meine Panel-Apps** die Option **Neue Studio-App**.
2. Wählen Sie unter **Starten mit** die Option **Aus der Galerie**.
3. Wählen Sie unter **Galerie-App** eine App aus. Ihre Beschreibung erscheint unter der Auswahl.
4. Benennen Sie Ihre App, wählen Sie ihr **Projekt** und wählen Sie **Erstellen**.

Sie können auch in der Symbolleiste von **Meine Panel-Apps** die Option **Galerie** wählen, um die Galerie für sich allein zu durchsuchen. Sie listet jede App mit Namen, Projekt und Beschreibung auf, dazu **App daraus erstellen…**. Die Galerie listet nur Apps in Projekten auf, die Sie ansehen können.

Die neue App ist eine Kopie der Dateien der aufgelisteten App. Ihre Kopie und das Original sind voneinander getrennt: Eine Änderung an der einen wirkt sich nie auf die andere aus.

## Ihre App aufnehmen

Sie benötigen Bearbeitungszugriff auf das Projekt der App. Nur Apps, die in [Panel Studio](/de/guides/panel-apps/studio/) erstellt wurden und zu einem Projekt gehören, können aufgenommen werden; Server-, WASM- und Dash-Apps nicht.

1. Öffnen Sie die App in Studio und wählen Sie **Galerie…**. Die Schaltfläche ist nur für eine App verfügbar, die zu einem Projekt gehört.
2. Geben Sie eine **Beschreibung** ein, die auf der Galeriekarte angezeigt wird.
3. Wählen Sie **In Galerie aufnehmen** und bestätigen Sie.

Um die Beschreibung zu ändern, wählen Sie **Eintrag aktualisieren**. Um die App aus der Galerie zu entfernen, öffnen Sie **Galerie…** und wählen Sie **Aus der Galerie entfernen**. Auch wenn Sie die App in ein anderes Projekt verschieben, wird sie aus der Galerie entfernt.

## Wer was sehen kann

Jeder, der das Projekt ansehen kann, kann den Quellcode der aufgelisteten App lesen, einschließlich Änderungen, die Sie später veröffentlichen. Legen Sie in den Dateien einer aufgelisteten App keine Passwörter oder privaten Notizen ab. Wenn Sie eine App aufnehmen, werden Sie zuvor aufgefordert, dies zu bestätigen, und die Aufnahme wird im Audit-Protokoll aufgezeichnet.

Wer aus der Galerie eine App erstellt, erhält nur eine Kopie der Dateien im eigenen Ordner der App. Die Repository-Details, Verbindungen oder Webhook-Einstellungen der App bekommt er nie zu sehen.

## Nächste Schritte

- [Panel Studio](/de/guides/panel-apps/studio/) – bearbeiten und veröffentlichen Sie die Kopie, die Sie erstellen.
- [Das Panel-App-Kit](/de/guides/panel-apps/app-kit/) – die Komponenten, aus denen die meisten Galerie-Apps bestehen.
