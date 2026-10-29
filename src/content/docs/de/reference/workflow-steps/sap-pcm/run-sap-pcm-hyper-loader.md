---
title: Run SAP PCM Hyper Loader (Schritt)
description: Führen Sie den SAP PCM Hyper Loader aus einem PlaidCloud-Workflow-Schritt aus, um Daten per Hochgeschwindigkeits-Bulk-Load in PCM-Modelle zu laden.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/run-sap-pcm-hyper-loader.md
---

## Beschreibung


Lädt ein SAP-PCM-Modell (Profitability and Cost Management) über direkte Tabellenladevorgänge. Dieser Vorgang ist deutlich schneller als Databridge. Der Hyper Loader unterstützt praktisch alle aktuellen PCM-Daten-, Zuordnungs- und Strukturtabellen.


Dies ist die aktuelle Liste der verfügbaren Ladeziele:


* Aktivitäts-Aliase
* Aktivitäts-Dimensionshierarchie
* Aktivitätstreiber-Aliase
* Aktivitätstreiber-Dimensionshierarchie
* Aktivitätstreiberwert
* Standardzusammensetzung der Stückliste
* Externer Einheitensatz der Stückliste
* Zusammensetzung der Stückliste
* Produktionsvolumen der Stückliste
* Verkaufte Einheiten der Stückliste
* Kostenobjekt-1-Aliase
* Kostenobjekt-1-Dimensionshierarchie
* Kostenobjekt-2-Aliase
* Kostenobjekt-2-Dimensionshierarchie
* Kostenobjekt-3-Aliase
* Kostenobjekt-3-Dimensionshierarchie
* Kostenobjekt-4-Aliase
* Kostenobjekt-4-Dimensionshierarchie
* Kostenobjekt-5-Aliase
* Kostenobjekt-5-Dimensionshierarchie
* Kostenobjektzuordnung
* Kostenobjekttreiber
* Positions-Aliase
* Positionsdetail-Aliase
* Positionsdetail-Dimensionshierarchie
* Positionsdetailwert
* Positions-Dimensionshierarchie
* Direkte Aktivitätszuordnung der Position
* Ressourcentreiber-Zuordnung der Position
* Positionswert
* Perioden-Aliase
* Perioden-Dimensionshierarchie
* Ressourcentreiber-Aliase
* Ressourcentreiber-Dimensionshierarchie
* Ressourcentreiber-Aufteilung
* Ressourcentreiberwert
* Verantwortungsbereich-Aliase
* Verantwortungsbereich-Dimensionshierarchie
* Umsatz
* Umsatz-Aliase
* Umsatz-Dimensionshierarchie
* Service-Aliase
* Service-Dimensionshierarchie
* Verteilungs-Aliase
* Verteilungs-Dimensionshierarchie
* Verteilungswert
* Versions-Aliase
* Versions-Dimensionshierarchie
* Arbeitsblatt-1-Aliase
* Arbeitsblatt-1-Dimensionshierarchie
* Arbeitsblatt-2-Aliase
* Arbeitsblatt-2-Dimensionshierarchie
* Arbeitsblattwert

## Unsere Zertifizierungen


PlaidCloud ist ein offizieller SAP-Partner und ein bevorzugter Anbieter von Services rund um Design und Implementierung von SAP-PCM-Modellen.


## Was beim Speichern geprüft wird

Jede Quelle auf der Registerkarte **Ladeschritte** wird in die Ladertabelle geladen, die als ihre **Zielladetabelle** gewählt ist; die Zuordnung erfolgt über den Spaltennamen. Das Speichern wird unter Nennung der Quelle verweigert, wenn:

- Eine Quelle keine Zielladetabelle hat oder eine, die keine PCM-Ladertabelle ist — *Source 'activity_aliases' loads into 'ACTIVITY', which isn't a PCM loader table.*
- Die Spalten einer Quelle nicht zu ihrer Ladertabelle passen: Eine Spalte der Ladertabelle fehlt, hat einen anderen Typ als in der Ladertabelle oder hat weder Quelle noch Ausdruck noch Konstante — *Source 'activity_aliases' doesn't match loader table PPLOAD_ACTIVITY_AL: missing DEFAULTALIAS; no source, expression or constant for ALIAS.* Mit **Zielspalten auf Schema zurücksetzen** werden die Zielspalten einer Quelle aus ihrer Ladertabelle neu befüllt.
- Zwei Quellen denselben Namen haben. Jede Quelle wird in eine nach ihr benannte Datei exportiert, sodass eine die andere überschreiben würde — *Source name 'activity_aliases' is used more than once; each source needs its own, or one overwrites the other.*


## Beispiele


Wählen Sie in der Dropdown-Liste den **Zu verwendender Agent** aus. Geben Sie den Modellnamen ein, wählen Sie den Speicherpfad des Ladepakets und anschließend den gewünschten untergeordneten Ordner darin. Wählen Sie in der **Tabellendatenauswahl** weiter unten die Quelltabelle des Modells und die Zielladetabelle aus. Mit „Inspect source >> propagate“ werden die Daten auf beiden Seiten der Tabelle sichtbar. Klicken Sie auf „Speichern und ausführen“, sobald die Daten eingegeben sind und Sie alle Ausdrücke hinzugefügt haben.
