---
title: Die App-Galerie
description: Fügen Sie eine Studio-App zur Galerie hinzu oder nehmen Sie sie heraus und erstellen Sie aus einer aufgeführten App eine neue App.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/gallery.md
---

Die App-Galerie ist das Regal, in dem Ihr Workspace fertige Panel-Apps bereithält. Jeder, der das Projekt einer aufgeführten App ansehen kann, kann eine eigene Kopie erstellen und ändern, sodass eine gute App zum Ausgangspunkt wird, statt dass jeder sie neu baut.

## Eine App aus der Galerie erstellen

1. Wählen Sie in **Meine Panel-Apps** die Option **Neue Studio-App**.
2. Wählen Sie unter **Starten mit** die Option **Aus der Galerie**.
3. Wählen Sie unter **Galerie-App** eine App aus. Ihre Beschreibung erscheint unter der Auswahl.
4. Benennen Sie Ihre App, wählen Sie ihr **Projekt** und wählen Sie **Erstellen**.

Sie können auch **Galerie** in der Symbolleiste von **Meine Panel-Apps** wählen, um die Galerie für sich zu durchsuchen. Jede Karte zeigt Name, Beschreibung und Projekt der App mit **App daraus erstellen…**. Die Galerie führt nur Apps in Projekten auf, die Sie ansehen können.

Die neue App ist eine Kopie der Dateien der aufgeführten App. Ihre Kopie und das Original sind getrennt: Eine Änderung an der einen ändert nie die andere.

## Ihre App aufführen

Sie benötigen Bearbeitungszugriff auf das Projekt der App. Nur Apps, die in [Panel Studio](/de/guides/panel-apps/studio/) erstellt wurden und zu einem Projekt gehören, lassen sich aufführen; Server-, WASM- und Dash-Apps nicht.

1. Öffnen Sie die App in Studio und wählen Sie **Galerie…**. Die Schaltfläche ist nur für eine App verfügbar, die zu einem Projekt gehört.
2. Geben Sie eine **Beschreibung** ein, die auf der Galeriekarte angezeigt wird.
3. Wählen Sie **In Galerie aufnehmen** und bestätigen Sie.

Um die Beschreibung zu ändern, wählen Sie **Eintrag aktualisieren**. Um die App aus der Galerie zu entfernen, öffnen Sie **Galerie…** und wählen Sie **Aus der Galerie entfernen**. Auch das Verschieben der App in ein anderes Projekt nimmt sie aus der Galerie.

## Wer was sehen kann

Jeder, der das Projekt ansehen kann, kann den Quellcode der aufgeführten App lesen, einschließlich Änderungen, die Sie später veröffentlichen. Legen Sie keine Kennwörter oder privaten Notizen in den Dateien einer aufgeführten App ab. Beim Aufführen einer App werden Sie zuvor um Bestätigung gebeten, und das Aufführen wird im Überwachungsprotokoll festgehalten.

Wer aus der Galerie erstellt, erhält nur eine Kopie der Dateien im eigenen Ordner der App. Repository-Details, Verbindungen oder Webhook-Einstellungen der App sehen diese Personen nie.

## Nächste Schritte

- [Panel Studio](/de/guides/panel-apps/studio/) – bearbeiten und veröffentlichen Sie die Kopie, die Sie erstellen.
- [Das Panel-App-Kit](/de/guides/panel-apps/app-kit/) – die Komponenten, aus denen die meisten Galerie-Apps bestehen.
