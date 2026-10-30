---
title: Die App-Galerie
description: Stellen Sie eine Panel-App als Vorlage bereit, von der Ihr Workspace ausgehen kann, und erstellen Sie aus einer aufgelisteten App eine neue App.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/gallery.md
---

Die App-Galerie ist das Regal, in dem Ihr Workspace fertige Panel-Apps bereithält. Jeder, der das Projekt einer aufgelisteten App ansehen kann, kann eine eigene Kopie erstellen und ändern, sodass eine gute App zum Ausgangspunkt wird, statt dass Personen sie neu aufbauen.

## Eine App aus der Galerie erstellen

1. Wählen Sie unter **Meine Panel-Apps** die Option **Create app**.
2. Wählen Sie unter **Starten mit** die Option **Aus der Galerie**.
3. Wählen Sie eine App aus. Ihre Beschreibung erscheint unter der Auswahl.
4. Benennen Sie Ihre App, wählen Sie ihr **Projekt** und wählen Sie **Erstellen**.

Sie können die Galerie auch eigenständig öffnen. Dort zeigt jede Karte Name, Beschreibung und Projekt der App mit **Create app from this…**. Die Galerie listet nur Apps in Projekten auf, die Sie ansehen können.

Die neue App ist eine Kopie der Dateien der aufgelisteten App. Ihre Kopie und das Original sind voneinander getrennt: Die Änderung des einen ändert nie das andere.

## Ihre App auflisten

Sie benötigen Bearbeitungsrechte für das Projekt der App, und die App muss in [Panel Studio](/de/guides/panel-apps/studio/) erstellt und einem Projekt zugewiesen worden sein.

1. Öffnen Sie die App in Studio und wählen Sie **Gallery…**.
2. Geben Sie eine **Beschreibung** ein, die auf der Galerie-Karte angezeigt wird.
3. Wählen Sie **List in gallery** und bestätigen Sie.

Um die Beschreibung zu ändern, wählen Sie **Update listing**. Um die App zu entfernen, wählen Sie **Take out of gallery**. Wenn Sie die App in ein anderes Projekt verschieben, wird sie ebenfalls aus der Galerie genommen.

## Wer was sehen kann

Jeder, der das Projekt ansehen kann, kann den Quellcode der aufgelisteten App lesen, einschließlich später von Ihnen veröffentlichter Änderungen. Legen Sie keine Kennwörter oder privaten Notizen in den Dateien einer aufgelisteten App ab. Beim Auflisten einer App werden Sie zunächst um Bestätigung gebeten, und das Auflisten wird im Auditprotokoll festgehalten.

Wer aus der Galerie erstellt, erhält nur eine Kopie der Dateien im eigenen Ordner der App. Repository-Details, Verbindungen und Webhook-Einstellungen der App sehen diese Personen nie.

## Nächste Schritte

- [Panel Studio](/de/guides/panel-apps/studio/) – bearbeiten und veröffentlichen Sie die Kopie, die Sie erstellen.
- [Das Panel App Kit](/de/guides/panel-apps/app-kit/) – die Komponenten, aus denen die meisten Galerie-Apps bestehen.
