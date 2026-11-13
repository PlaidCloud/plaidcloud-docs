---
title: Die App-Galerie
description: Nehmen Sie eine Studio-App in die Galerie auf oder entfernen Sie sie, und erstellen Sie aus einer aufgelisteten App eine neue App.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/gallery.md
---

Die App-Galerie ist das Regal, in dem Ihr Workspace fertige Panel-Apps bereithält. Jeder, der das Projekt einer aufgelisteten App ansehen kann, kann in einem Projekt, das er bearbeiten kann, seine eigene Kopie erstellen und ändern, sodass eine gute App zum Ausgangspunkt wird, anstatt dass Leute sie neu aufbauen.

## Eine App aus der Galerie erstellen

1. Wählen Sie in **Apps** **New app** > **Studio**.
2. Wählen Sie unter **Starten mit** **Aus der Galerie**.
3. Wählen Sie unter **Galerie-App** eine App aus. Ihre Beschreibung erscheint unter der Auswahl.
4. Benennen Sie Ihre App, wählen Sie ihr **Projekt** und wählen Sie **Erstellen**.

Sie können auch **New app** > **From gallery…** wählen, um die Galerie für sich allein zu durchsuchen. Sie listet jede App mit ihrem Namen, ihrem Projekt und ihrer Beschreibung auf, dazu **App daraus erstellen…**. Die Galerie listet nur Apps in Projekten auf, die Sie ansehen können.

Die neue App ist eine Kopie der Dateien der aufgelisteten App. Ihre Kopie und das Original sind getrennt: Eine Änderung an einer ändert nie die andere.

## Ihre App auflisten

Sie benötigen Bearbeitungszugriff auf das Projekt der App. Nur Apps, die in [Panel Studio](/de/guides/panel-apps/studio/) erstellt wurden und zu einem Projekt gehören, können aufgelistet werden; Server-, WASM- und Dash-Apps nicht.

1. Öffnen Sie die App in Studio und wählen Sie **Galerie…**. Die Schaltfläche ist nur für eine App verfügbar, die zu einem Projekt gehört.
2. Geben Sie eine **Beschreibung** ein, die auf der Galeriekarte angezeigt wird.
3. Wählen Sie **In Galerie aufnehmen** und bestätigen Sie.

Um die Beschreibung zu ändern, wählen Sie **Eintrag aktualisieren**. Um die App aus der Galerie zu entfernen, öffnen Sie **Galerie…** und wählen Sie **Aus der Galerie entfernen**. Auch das Verschieben der App in ein anderes Projekt nimmt sie aus der Galerie.

## Wer was sehen kann

Jeder, der das Projekt ansehen kann, kann den Quellcode der aufgelisteten App lesen, einschließlich später von Ihnen veröffentlichter Änderungen. Legen Sie in den Dateien einer aufgelisteten App keine Passwörter oder privaten Notizen ab. Wenn Sie eine App auflisten, werden Sie zuvor um Bestätigung gebeten, und das Auflisten wird im Audit-Protokoll aufgezeichnet.

Wer aus der Galerie erstellt, erhält nur eine Kopie der Dateien im eigenen Ordner der App. Repository-Details, Verbindungen oder Webhook-Einstellungen der App sehen diese Personen nie.

## Nächste Schritte

- [Panel Studio](/de/guides/panel-apps/studio/) – bearbeiten und veröffentlichen Sie die Kopie, die Sie erstellen.
- [Das Panel-App-Kit](/de/guides/panel-apps/app-kit/) – die Komponenten, aus denen die meisten Galerie-Apps bestehen.
