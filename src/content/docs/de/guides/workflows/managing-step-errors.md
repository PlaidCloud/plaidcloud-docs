---
title: Schrittfehler verwalten
description: Behandeln und verwalten Sie Schrittfehler in PlaidCloud-Workflows, einschließlich Fehlerbenachrichtigungen, Wiederholungslogik und Optionen zur Fehlerbehebung.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/managing-step-errors.md
---

Tritt bei der Verarbeitung eines Workflows ein Fehler auf, wird sowohl am Workflow als auch am fehlerhaften Schritt eine Fehleranzeige dargestellt. PlaidCloud kann einen fehlgeschlagenen Schritt mehrmals wiederholen. Das ist oft hilfreich, wenn der Schritt auf Remote-Systeme oder Daten zugreift, die nicht durchgehend verfügbar sind oder aus unbekannten Gründen sporadisch ausfallen. Die Wiederholung lässt sich auf viele Versuche einstellen, und zwischen den Versuchen kann eine Pause von Sekunden bis zu Stunden eingefügt werden.



Ein Schritt, dessen Server mitten in der Ausführung verloren geht, wird getrennt von Wiederholungen behandelt: Ein Schritt, der sich gefahrlos wiederholen lässt, wird automatisch erneut ausgeführt, und ein Schritt, bei dem das nicht der Fall ist, schlägt einmalig mit der Meldung **Unterbrochen** fehl. Siehe [Unterbrochene Schritte](/de/guides/workflows/run-a-workflow/#unterbrochene-schritte).

Lehnt PlaidCloud einen Schritt aus einem Grund ab, den Sie beheben können, etwa wegen einer fehlenden Berechtigung oder einer ungültigen Einstellung, zeigt das Schrittprotokoll diese Meldung in verständlichen Worten an statt eines Serverfehlers mit Stacktrace. Schlägt bei einem Schritt Model Loop, Model Run oder Macro Run der untergeordnete Workflow fehl, zeigt der Schritt die eigene Fehlermeldung des untergeordneten Workflows an, und zwar als „Child workflow run failed:“, gefolgt von der Meldung.

Wenn keine Wiederholung ausgewählt ist oder die maximale Anzahl an Wiederholungen überschritten wird, wird der Schritt als fehlerhaft markiert. PlaidCloud bietet für diesen Fall drei Ebenen der Fehlerbehandlung:


* Den Workflow bei einem Fehler anhalten
* Den Schritt als fehlerhaft markieren, die Verarbeitung des Workflows aber fortsetzen
* Den Schritt als fehlerhaft markieren und stattdessen einen Korrektur-Workflow-Prozess auslösen, statt den aktuellen Workflow fortzusetzen

## Den Workflow anhalten


Den Workflow bei einem Schrittfehler anzuhalten ist die gängigste Vorgehensweise, da Workflows in der Regel fehlerfrei laufen sollten. Dadurch wird der Workflow angehalten, und die Fehleranzeige erscheint sowohl am Schritt als auch am Workflow. Der Fehler wird außerdem im Aktivitätsmonitor angezeigt, es erfolgt jedoch keine weitere Aktion.



## Weiterverarbeiten


Jeder Schritt kann im Schrittformular so eingestellt werden, dass er bei einem Fehler fortfährt. Ist dieses Kontrollkästchen aktiviert, wird jeder Schritt bei einem Fehler zwar als fehlerhaft markiert, der Workflow behandelt den Fehler aber wie einen Abschluss des Schritts und fährt fort. Das ist oft nützlich, wenn es Schritte gibt, die Aufgaben ausführen, bei denen bei fehlenden Daten ein Fehler auftreten kann, die für die Gesamtprozesse aber unschädlich sind.



Da der Workflow in diesem Szenario trotz Fehler fortfährt, zeigt er keine Fehleranzeige an und zeigt weiterhin eine Anzeige für „Wird ausgeführt“.



## Korrektur-Workflow auslösen


Wenn bei der Einrichtung des Workflows ein Korrektur-Workflow festgelegt wurde, stoppt ein Workflow-Fehler sofort die Verarbeitung des aktuellen Workflows und startet die Verarbeitung des Korrektur-Workflows. Beachten Sie: Ist ein Schritt so markiert, dass er bei einem Fehler fortfährt, löst ein Fehlschlag den Korrektur-Workflow nicht aus. Nur Schritte, deren Fehlschlag auch den gesamten Workflow anhalten würde, lösen den Korrekturprozess aus.



Ein Korrektur-Workflow kann nützlich sein, um Personen einfach darüber zu informieren, dass ein Fehler aufgetreten ist, oder um andere komplexe Verarbeitungen auszuführen und die zugrunde liegenden Ursachen des Fehlschlags des ursprünglichen Workflows automatisch zu beheben.
