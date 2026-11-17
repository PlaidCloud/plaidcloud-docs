---
title: Convert Document Encoding
description: Konvertiert die Kodierung einer Dokumentdatei in einem PlaidCloud-Workflow-Schritt zwischen Zeichensätzen, um Kompatibilitätsprobleme bei der Kodierung zu beheben.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding.md
---

## Beschreibung



Kodiert eine Textdatei von einer Zeichenkodierung in eine andere um. Nützlich, wenn Quelldateien in Legacy-Kodierungen (Windows-1252, ISO-8859-1) eintreffen, nachgelagerte Tools aber UTF-8 benötigen, oder umgekehrt.

Wenn die Quelldatei nicht UTF-8 ist, wird ihre Kodierung aus dem Inhalt der Datei ermittelt. Eine sehr kurze oder stark repetitive Datei liefert zu wenig Anhaltspunkte und kann falsch gelesen werden; prüfen Sie daher bei einer solchen Datei die konvertierte Ausgabe.

Ein Zeichen, das die Zielkodierung nicht darstellen kann, lässt den Schritt standardmäßig fehlschlagen. Wählen Sie **Zeichen, die die Zielkodierung nicht darstellen kann, durch ? ersetzen**, um stattdessen ein `?` an seine Stelle zu schreiben, wie es ein Java-Writer tut, und der Schritt wird beendet.

Eine komprimierte Datei wird zuerst entpackt, und jede darin enthaltene Datei wird konvertiert. Bei einem Ordner wird jede Datei unter ihrem eigenen Namen in das Ziel geschrieben. Aktivieren Sie **Unterordner beibehalten**, um stattdessen eine Datei aus einem Unterordner in den entsprechenden Unterordner des Ziels zu schreiben; der Inhalt einer komprimierten Datei geht dann in den Unterordner, in dem die komprimierte Datei lag. Würden zwei Dateien an dieselbe Stelle geschrieben, schlägt der Schritt fehl, bevor er die zweite schreibt, statt sie die erste ersetzen zu lassen, und gibt an, ob das Aktivieren von **Unterordner beibehalten** sie auseinanderhalten würde.

Wählen Sie die Zielkodierung in der Schrittkonfiguration. Für bestimmte Kodierungskürzel siehe die Varianten [UTF-8](/de/reference/workflow-steps/document/convert-document-encoding-to-utf-8/), [UTF-16](/de/reference/workflow-steps/document/convert-document-encoding-to-utf-16/) und [ASCII](/de/reference/workflow-steps/document/convert-document-encoding-to-ascii/).


## Beispiele


Legen Sie eine Quelleingabe an, wählen Sie die Eingabedatei aus und navigieren Sie an ihrem Speicherort zur Datei. Wählen Sie den gewünschten Ausgabeort und navigieren Sie zum gewünschten Speicherort der Datei. Speichern und ausführen.
