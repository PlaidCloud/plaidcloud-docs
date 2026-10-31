---
title: OAuth-Token
description: Richten Sie OAuth-Token für den PlaidCloud-API-Zugriff ein, um Jupyter-Notebooks, CLI-Tools und benutzerdefinierte Anwendungsverbindungen zu authentifizieren.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/oauth-setup.md
---

PlaidCloud verwendet standardmäßige JSON-RPC-Anfragen und lässt sich mit jeder Anwendung nutzen, die solche Anfragen senden kann.  Anfragen werden mit OAuth-Token abgesichert.


## OAuth-Token abrufen

OAuth-Token werden in der PlaidCloud-App generiert. Um die Liste der Ihnen zugewiesenen OAuth-Token anzuzeigen und neue zu generieren, navigieren Sie zu `Analyze > Tools > Registered Systems`.

Dort können Sie vorhandene Token anzeigen oder ein neues erstellen.

## OAuth-Konfigurationsdatei von PlaidCloud herunterladen
Wählen Sie „Register a New System“.

Füllen Sie das Formular aus und notieren Sie sich den eingegebenen Namen, damit Sie den Eintrag in der Liste wiederfinden.

Öffnen Sie nach der Erstellung den Datensatz des registrierten Systems, indem Sie auf das Zahnradsymbol klicken.  Daraufhin wird der Text der Konfigurationsdatei angezeigt.  

HINWEIS: Wählen Sie oben in der Dropdown-Liste unbedingt das Projekt aus, für das Sie diese Verbindung verwenden möchten.  Dadurch wird die eindeutige Projektkennung zur Konfiguration hinzugefügt.

Kopieren Sie diesen Text in eine Datei plaid.conf auf Ihrem System.  Legen Sie sie im Verzeichnis .plaid ab.

## Konfigurationsdatei lokal erstellen
Erstellen Sie ein Verzeichnis eine Ebene oberhalb Ihres Notebook-Verzeichnisses oder des Verzeichnisses, in dem Sie die Befehlszeile verwenden möchten.  Nennen Sie das Verzeichnis `.plaid`.

Erstellen Sie im Verzeichnis `.plaid` eine Datei namens `plaid.conf` und fügen Sie den oben kopierten Inhalt ein.  Speichern Sie die Datei. Danach können Sie sich mit den PlaidCloud Utilities und den RPC-Methoden verbinden.


## Erweiterte Einsatzmöglichkeiten

Es ist zwar praktisch, den Ordner `.plaid` in der Nähe der Verwendungsstelle abzulegen, er kann aber an jeder beliebigen Stelle im übergeordneten Verzeichnisbaum liegen.  Beim Initialisieren wird der Verzeichnisbaum nach oben durchlaufen, bis das Verzeichnis `.plaid` gefunden wird.

Das Ablegen des Verzeichnisses `.plaid` weiter oben kann sinnvoll sein, wenn mehrere Vorgänge Zugriff benötigen, aber nicht in denselben tiefer liegenden Verzeichnisstrukturen nebeneinander bestehen können.


## Optionale Pfadangaben
Wenn Sie eine lokale Jupyter-Notebook-Installation verwenden oder über die Befehlszeile arbeiten, können Sie mit den Hilfstools Daten, Excel-Dateien und andere Daten exportieren sowie lokale Daten in DataFrames einlesen. Dafür ist eine Datei paths.yaml erforderlich.

Erstellen Sie zusätzlich zur Datei `plaid.conf` eine Datei `paths.yaml`.  Die Datei `paths.yaml` muss sich im Verzeichnis `.plaid` auf derselben Ebene wie die Datei `plaid.conf` befinden.  Sie sollte die folgenden Pfadangaben enthalten:

```yaml
paths:
 PROJECT_ROOT: '{WORKING_USER}/Documents'
 LOCAL_STORAGE: '{PROJECT_ROOT}/local_storage'
 DEBUG: '{PROJECT_ROOT}/local_storage'
 REPORTS: '{PROJECT_ROOT}/reports'
 
 create: []
 local: {}
```
