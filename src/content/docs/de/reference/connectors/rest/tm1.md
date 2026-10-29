---
title: TM1-Connector
description: Verbinden Sie PlaidCloud über die REST-API mit einem IBM TM1 / Planning Analytics-Server – mit nativer Basic-Authentifizierung oder CAM-Namespace-Authentifizierung – direkt aus der Cloud oder über einen lokalen PlaidLink-Agent für einen Server, den die Cloud nicht direkt erreichen kann.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/tm1.md
---

Verbinden Sie PlaidCloud über die veröffentlichte OData-v4-REST-API mit einem IBM **TM1 / Planning Analytics**-Server – ohne JVM-Bridge und ohne PAOlap-Treiber. Lesen Sie Cube-Daten mit [TM1: Cube abfragen](/de/reference/workflow-steps/ibm-planning-analytics/tm1-query/) oder eine TM1-Dimensionshierarchie mit [TM1: Dimension lesen](/de/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/); beide Schritte arbeiten direkt aus der Cloud. Für einen TM1-Server, der nur aus Ihrem eigenen Netzwerk erreichbar ist, leitet [TM1: Cube abfragen (Agent)](/de/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) dieselbe Leseabfrage stattdessen über einen installierten PlaidLink-Agent weiter.

Der Verbindungstyp erscheint in der Verbindungsauswahl als **IBM Planning Analytics (TM1)**.

## So funktioniert die Authentifizierung

Es gibt zwei Authentifizierungsmodi, die den eigenen REST-Anmeldeverfahren von TM1 entsprechen:

- **Native** – HTTP-Basic-Authentifizierung mit einem TM1-Benutzernamen und -Passwort.
- **CAM** – Single Sign-on über IBM Cognos Access Manager, begrenzt auf einen Namespace. Die Anfrage enthält einen `Authorization: CAMNamespace`-Header, der aus Benutzername, Passwort und Namespace zusammen gebildet wird und sich von einfachem Basic unterscheidet.

Eine Anmeldung per Bearer-Token für PlanningAnalytics-as-a-Service (PAaaS) gibt es noch nicht – nur die beiden oben genannten REST-Anmeldeverfahren.

## Konfiguration

| Feld | Erforderlich | Beschreibung |
|---|---|---|
| Name | Ja | Anzeigename dieser Verbindung. |
| Host | Ja | Der Host der TM1-REST-API, z. B. `https://tm1-prod.example.com:8010` oder eine PAaaS-URL. |
| Standarddatenbank | Nein | Eine Vorbelegung für das Feld „Datenbank“ eines Schritts „TM1: Cube abfragen“. Jeder Schritt kann sie überschreiben. |
| Authentifizierungsmodus | Ja | `Native` (TM1-Benutzer/Passwort) oder `CAM` (Cognos-Access-Manager-SSO). Standardmäßig Native. |
| Benutzername | Ja | Das TM1-Konto, mit dem die Authentifizierung erfolgt. |
| Passwort | Ja | Wird verschlüsselt gespeichert. |
| CAM-Namespace | Nur mit CAM | Der Cognos-Access-Manager-Namespace, gegen den authentifiziert wird. Im Modus Native nicht verwendet. |
| SSL-Zertifikat prüfen | Nein | Standardmäßig aktiviert. Deaktivieren Sie die Option nur für ein bekanntes selbstsigniertes Zertifikat auf einem Testserver. |
| Timeout (Sekunden) | Nein | Standardwert ist 30. |

## Die Verbindung testen

**Verbindung testen** fragt das Singleton `Configuration` des Servers ab (`GET {host}/api/v1/Configuration`) – der günstigste authentifizierte Aufruf, den TM1 bietet, und einer, der weder Datenbank- noch Cube-Kontext benötigt. Ein erfolgreicher Test meldet die **`ProductVersion`** des Servers und bestätigt damit sowohl, dass der Host erreichbar ist, als auch, dass die Zugangsdaten authentifiziert werden.

## Nur lesend

Dieser Connector arbeitet nur lesend. Er liest Cube-Daten und Dimensionshierarchien aus TM1; er schreibt, bucht oder führt keine TI-Prozesse in TM1 zurück aus.

## Was Sie mit der Verbindung tun können

- **Cube-Daten über eine gespeicherte Ansicht oder MDX lesen.** Der Schritt [TM1: Cube abfragen](/de/reference/workflow-steps/ibm-planning-analytics/tm1-query/) führt eine benannte Cube-Ansicht oder eine MDX-Rohabfrage aus, wendet optional einen Point-of-View-Ausschnitt an und legt das Ergebnis als Tabelle ab.
- **Eine TM1-Hierarchie als PlaidCloud-Dimension laden.** Der Schritt [TM1: Dimension lesen](/de/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) liest die Elemente, Eltern-Kind-Beziehungen und Attribute einer Dimension und erstellt daraus eine PlaidCloud-Dimension.
- **Für einen inkrementellen Extrakt nach Periode eingrenzen.** TM1 hat keine integrierte Änderungsverfolgung. Ein Workflow, der nur neue Daten benötigt, grenzt die Abfrage daher nach Periode oder Version ein – das Muster dazu finden Sie in der Schrittreferenz.
- **Cubes, Ansichten und Dimensionen live ermitteln**, direkt aus der Cloud. Die Auswahllisten für Cube, Ansicht und Dimension im Schrittformular fragen den verbundenen Server direkt ab, sodass Sie echte Namen auswählen, statt sie blind einzutippen.
- **Einen TM1-Server lesen, den die Cloud nicht erreichen kann, über einen lokalen Agent.** Siehe [TM1 hinter einer Firewall lesen](#tm1-hinter-einer-firewall-lesen) weiter unten.

## TM1 hinter einer Firewall lesen

Ein TM1-Server, der nur aus Ihrem eigenen Netzwerk erreichbar ist – ohne öffentlichen Endpunkt, ohne freigegebene IP-Adresse und ohne VPN zu PlaidCloud –, wird nicht direkt aus der Cloud, sondern über einen installierten **PlaidLink-Agent** erreicht. Der Workflow-Schritt [TM1: Cube abfragen (Agent)](/de/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) führt dieselbe Abfrage mit Ansicht, MDX und Point of View aus wie TM1: Cube abfragen, leitet sie aber an den Agent weiter, der TM1 in Ihrem Netzwerk erreicht und das Ergebnis zurückliefert.

Dieser Weg setzt Folgendes voraus:

- **Ein installierter PlaidLink-Agent** auf einem Rechner mit Netzwerkzugriff auf den TM1-Server. Siehe [PlaidLink installieren](/de/reference/cli/plaidlink/install/).
- **Ein Build dieses Agents, der den TM1-Handler enthält.** PlaidCloud prüft die vom Agent gemeldeten Fähigkeiten, bevor es eine Abfrage an ihn weiterleitet. Ein älterer Agent-Build kann TM1-Anfragen daher erst bedienen, nachdem er neu erstellt und neu installiert wurde – PlaidLink aktualisiert sich nicht automatisch. Siehe [PlaidLink aktualisieren](/de/reference/cli/plaidlink/upgrade/).
- **Diese TM1-Verbindung, die mit diesem Agent geteilt ist**, zusätzlich zum bereits bestehenden Zugriff für Mitglieder und Gruppen, über die Liste `Actions > Agents` der Verbindung. Siehe [Sicherheitsmodell](/de/guides/connections/create-connection/#sicherheitsmodell).

TM1: Cube abfragen (Agent) bietet keine Live-Ermittlung – ein Agent ist nur während einer Ausführung erreichbar, nicht solange das Formular des Schritts geöffnet ist –, daher werden Cube, Ansicht und MDX von Hand eingegeben und erst bei der Ausführung des Schritts validiert. TM1: Dimension lesen arbeitet nur direkt aus der Cloud und bietet noch keinen lokalen Weg.

## Bekannte Einschränkungen

| Einschränkung | Bedeutung |
|---|---|
| Nur lesend | Kein Zurückschreiben, keine Ausführung von TI-Prozessen. |
| Lokale Reichweite nur für Abfragen | Der Weg über den lokalen PlaidLink-Agent deckt Cube-Lesezugriffe ab (TM1: Cube abfragen (Agent)). TM1: Dimension lesen hat noch keinen lokalen Weg – es benötigt einen Netzwerkpfad, den PlaidCloud direkt erreichen kann. |
| Dimensionslesen ist auf eine Hierarchie und einen Elternknoten beschränkt | Eine TM1-Hierarchie, in der ein Element unter mehr als einem Elternknoten steht, kann nicht als PlaidCloud-Dimension geladen werden, und der Betrag einer Konsolidierungsgewichtung (0,5; 2,0) lässt sich nicht abbilden – nur ihr Vorzeichen. Siehe [TM1: Dimension lesen](/de/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/#was-dieser-schritt-nicht-abbilden-kann). |
| Keine PAaaS-Bearer-Authentifizierung | Unterstützt werden nur die Authentifizierung Native (Basic) und CAM. |

## Verwandte Themen

- [Mit TM1 verbinden (Anleitung)](/de/guides/connections/tm1/) – erstellen Sie die Verbindung und bauen Sie eine Abfrage.
- [TM1: Cube abfragen](/de/reference/workflow-steps/ibm-planning-analytics/tm1-query/) – Cube-Lesezugriffe, direkt aus der Cloud.
- [TM1: Cube abfragen (Agent)](/de/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) – Cube-Lesezugriffe über einen lokalen Agent.
- [TM1: Dimension lesen](/de/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) – eine TM1-Hierarchie als PlaidCloud-Dimension laden.
- [Eine Verbindung erstellen und verwalten](/de/guides/connections/create-connection/)
