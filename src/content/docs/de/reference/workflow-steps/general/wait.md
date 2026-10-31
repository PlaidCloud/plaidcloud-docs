---
title: Warten
description: Fügen Sie in einem PlaidCloud-Workflow-Schritt eine zeitgesteuerte Verzögerung hinzu, um die Ausführung für eine bestimmte Dauer anzuhalten, bevor mit dem nächsten Schritt fortgefahren wird.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/wait.md
---

## Beschreibung


Die Transformation „Warten" hält die Verarbeitung für eine bestimmte Dauer an. Das kann besonders hilfreich sein, wenn auf E/A-Vorgänge anderer Systeme gewartet wird oder um Workflows während der Entwicklung zu debuggen.



## Dauerparameter


Geben Sie mit dem Drehfeld **Dauer** einen nicht negativen ganzzahligen Wert an.



Legen Sie als Nächstes im Dropdown-Menü die Zeiteinheit fest. Die folgenden Einheiten stehen zur Auswahl:


* Sekunden
* Minuten
* Stunden

## Auf eine Uhrzeit oder eine Datei warten

Der Abschnitt **Weitere Wartebedingungen** hat diese Felder. Der Schritt wartet nach der Dauer in dieser Reihenfolge auf sie:

* **Millisekunden** (`milliseconds`) — Millisekunden, die zusätzlich zur Dauer gewartet werden.
* **Bis Uhrzeit** (`until_time`) — wartet dann, bis die Uhr das nächste Mal diese Uhrzeit in UTC anzeigt, als `HH:MM:SS`.
* **Auf Datei warten** (`file`) — wartet dann darauf, dass sich diese Document-Datei, `{account, path}`, ändert. **Dateiänderung** (`file_event`) ist die Änderung, auf die gewartet wird: `modified` (Standard), `created` oder `deleted`. Der Schritt prüft die Datei alle **Datei alle (Sekunden) prüfen** (`poll_seconds`, Standard 5) höchstens **Längste Dateiwartezeit (Sekunden)** (`max_wait_seconds`, Standard 3600, höchstens einen Tag) lang, endet dann mit einer Warnung, und der Workflow wird fortgesetzt. Eine Datei, die beim Warten auf `created` bereits vorhanden ist, beendet das Warten sofort, und eine fehlende Datei beim Warten auf `modified` oder `deleted` endet mit einer Warnung, die den Pfad nennt, ohne zu warten.
