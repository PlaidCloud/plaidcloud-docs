---
title: Panel-Apps mit Weave erstellen
description: Beschreiben Sie die gewünschte App, lassen Sie Weave sie in Panel Studio schreiben und genehmigen Sie die genaue Änderung, bevor etwas gespeichert wird.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/build-with-weave.md
---

Weave kann Panel-Apps für Sie schreiben und ändern. Es arbeitet in [Panel Studio](/de/guides/panel-apps/studio/) an der App, die Sie geöffnet haben, und nichts, was es vorschlägt, ändert die App, bevor Sie es genehmigen.

## Weave fragen

1. Öffnen Sie die App in Panel Studio.
2. Wählen Sie **Ask Weave** und beschreiben Sie, was Sie möchten, zum Beispiel „Füge einen Regionsfilter und ein Diagramm des Umsatzes nach Monat hinzu.“

Weave kennt die App, an der es arbeitet, bereits: ihre Dateien, ihren Build-Status und etwaige Build-Fehler sowie die Tabelle oder Ansicht, auf der sie basiert. Sie müssen weder Code noch Fehler in die Unterhaltung einfügen. Wenn ein Build fehlschlägt, bitten Sie Weave, ihn zu beheben.

## Die Änderung genehmigen

Wenn Weave den Code der App ändern möchte, zeigt es eine Genehmigungskarte mit dem vollständigen Unterschied: jede Zeile, die es hinzufügt und entfernt, Datei für Datei.

1. Lesen Sie den Unterschied.
2. Wählen Sie **Genehmigen**, um die Änderung im Entwurf der App zu speichern, oder **Ablehnen**, um sie zu verwerfen.

Beim Genehmigen wird ein Entwurf gespeichert. Es wird nicht veröffentlicht. Sehen Sie sich das Ergebnis in der Vorschau an und [veröffentlichen Sie](/de/guides/panel-apps/studio/#veröffentlichen) dann, wenn Sie zufrieden sind.

### Genehmigungen nur im Web

Eine Codeänderung können Sie nur in PlaidCloud im Web genehmigen. In der mobilen PlaidCloud-App können Sie eine vorgeschlagene Codeänderung ablehnen, aber nicht genehmigen. Andere Änderungen von Weave können Sie weiterhin auf Ihrem Smartphone genehmigen. Siehe [Weave auf dem Smartphone](/de/guides/mobile-app/weave-on-mobile/).

## Nächste Schritte

- [Panel Studio](/de/guides/panel-apps/studio/) – speichern, in der Vorschau ansehen und veröffentlichen.
- [Das Panel App Kit](/de/guides/panel-apps/app-kit/) – die Komponenten, mit denen Weave baut.
