---
title: Salesforce-REST-Konnektor
description: "Richten Sie in PlaidCloud eine Salesforce-REST-API-Verbindung mit dem OAuth-2.0-Client-Credentials-Ablauf ein, testen Sie sie und rufen Sie CRM-Objekte mit dem Schritt Salesforce: Objekt abfragen in Projekttabellen ab."
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/salesforce.md
---

## API-Dokumentation

Die [Salesforce-REST-API-Referenz](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.html) dokumentiert die Datensatz- und Metadatenendpunkte, und das [Bulk API 2.0 Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/bulk_api_2_0.htm) dokumentiert die Abfragejobs, auf denen der Schritt [Salesforce: Objekt abfragen](/de/reference/workflow-steps/salesforce/query-salesforce-object/) läuft.

Eine vollständige Anleitung – die Salesforce-seitige App, der Run-As-Benutzer, das Erstellen der Verbindung und ihr Test – finden Sie in der Anleitung [Mit Salesforce verbinden](/de/guides/connections/salesforce/). Diese Seite ist die Feldreferenz dahinter.

## So funktioniert die Authentifizierung

Der Konnektor meldet sich mit **OAuth 2.0 Client Credentials** an: PlaidCloud tauscht den Consumer Key und das Secret der App am eigenen Token-Endpunkt der Org gegen ein Zugriffstoken und ruft die API als der Benutzer auf, den die App in ihrer Einstellung **Run As** nennt. Es gibt keine interaktive Anmeldung, kein Refresh-Token und kein Zertifikat zu verwalten.

Zwei Eigenschaften dieses Austauschs sind in der Praxis wichtig:

- **Ein Token deckt einen ganzen Extrakt ab.** PlaidCloud speichert das Zugriffstoken pro Verbindung und Umgebung zwischen, bis kurz vor dessen Ablauf, sodass ein großer seitenweiser Lesevorgang nicht bei jeder Seite erneut authentifiziert. Ein Token, das Salesforce vorzeitig nicht mehr akzeptiert – widerrufen, wegen einer IP-Einschränkung oder einer geänderten Sitzungsrichtlinie –, wird verworfen und einmalig automatisch ersetzt.
- **Anfragen gehen dorthin, wohin Salesforce verweist.** Die Token-Antwort nennt die Instanz der Org, und jeder weitere Aufruf geht an diese Instanz statt an den Host, den Sie eingegeben haben. Eine Verbindung funktioniert daher auch nach einer Änderung von My Domain oder der Instanz weiter.

Die Version der REST-API ist pro Verbindung festgelegt und nicht fließend, sodass ein Upgrade der Org die Antwortstrukturen unter einem gespeicherten Schritt nicht unbemerkt ändern kann. Neue Verbindungen verwenden eine aktuell unterstützte Version; eine Verbindung kann über die API für die Verbindungskonfiguration auf eine andere Version festgelegt werden, und wenn eine festgelegte Version das Supportende erreicht, antwortet Salesforce mit HTTP 410 und PlaidCloud meldet, welche Version eingestellt wurde.

## Konfiguration

Diese Felder werden angezeigt, wenn Sie unter **Tools > Connections** eine Salesforce-Verbindung erstellen oder bearbeiten.

### Kontobeschreibung

| Feld | Typ | Beschreibung |
|---|---|---|
| Kontoname | Text | Anzeigename für diese Verbindung. |
| Memo | Text (mehrzeilig) | Optionale Notizen zur Verbindung. |

### Verbindung

| Feld | Typ | Beschreibung |
|---|---|---|
| Host oder IP-Adresse | Text | Der My-Domain-Host der Org – `mycompany.my.salesforce.com` für Production und Developer Edition, `mycompany--uat.sandbox.my.salesforce.com` für eine Sandbox. PlaidCloud ergänzt `https://`, wenn Sie es weglassen. |

### Authentifizierungsdaten

| Feld | Typ | Beschreibung |
|---|---|---|
| Client-ID | Text | Der Consumer Key der App. |
| Client-Secret | Passwort | Das Consumer Secret der App. Wird verschlüsselt gespeichert; geben Sie einen neuen Wert ein, um es zu ändern, oder lassen Sie das Feld leer, um den gespeicherten Wert zu behalten. |

### Verwendung und Sicherheit

| Feld | Typ | Beschreibung |
|---|---|---|
| Aktiv (Zugriff erlauben) | Schalter | Gibt an, ob die Verbindung verwendet werden kann. Deaktivieren Sie sie, um den Zugriff auszusetzen, ohne die Verbindung zu löschen. |
| Sicherheitsmodell | Auswahl | Wer die Verbindung verwenden darf – nur ihre Eigentümer, bestimmte Mitglieder, bestimmte Sicherheitsgruppen oder alle Workspace-Mitglieder. |

Jede Verbindung enthält pro Umgebung einen Satz dieser Werte, sodass eine Verbindung in Ihrer Entwicklungsumgebung auf eine Sandbox und in Ihrer Produktionsumgebung auf Production verweisen kann. Testen Sie die Verbindung und legen Sie die Zugangsdaten pro Umgebung fest.

## Verbindung testen

**Verbindung testen** führt den echten Token-Austausch durch und meldet, als wer sich die Zugangsdaten authentifizieren:

| Gemeldet | Warum es wichtig ist |
|---|---|
| Organisations-ID | Bestätigt, welche Org die Zugangsdaten erreichen – der schnellste Weg, Sandbox-Zugangsdaten zu entdecken, die in einer Produktionsumgebung gespeichert wurden. |
| API-Version | Die höchste Version, die diese Org unterstützt. Lesevorgänge laufen auf der an die Verbindung gebundenen Version – `v61.0`, sofern `salesforce_api_version` nicht gesetzt ist – und nicht auf dieser. |
| Run-As-Benutzer | Der Benutzer, auf den jede Zeile und jedes Feld, die diese Verbindung je zurückgibt, beschränkt ist. Prüfen Sie dies, bevor Sie den Zeilenanzahlen eines Extrakts vertrauen. |

Ein fehlgeschlagener Test nennt die Ursache. Bei Authentifizierungsfehlern werden der HTTP-Status gemeldet und Sie werden aufgefordert, Client-ID und Secret erneut einzugeben, da sich ein gespeichertes Client-Secret nicht zurücklesen lässt.

## Bekannte Einschränkungen

- **Der Run-As-Benutzer beschränkt jeden Lesevorgang, und zwar auf zwei verschiedene Arten.** Zeilen, die dieser Benutzer nicht sehen kann, fehlen einfach, ohne Fehler und ohne Zählung. Ein Feld, das dieser Benutzer nicht lesen kann, lässt die gesamte Abfrage fehlschlagen. Beides wird unter [Der Run-As-Benutzer beschränkt alles](/de/guides/connections/salesforce/#der-run-as-benutzer-bestimmt-den-gesamten-umfang) behandelt.
- **Nur Lesezugriff.** Dieser Konnektor extrahiert Daten; er schreibt keine Datensätze zurück nach Salesforce.
- **Einige Feldtypen lassen sich nicht extrahieren** – zusammengesetzte Adress- und Geolokalisierungsfelder, `base64`-Blobs, `encryptedstring` und `anyType`. Die Feldauswahl des Schritts kennzeichnet jedes dieser Felder und nennt den Grund. Siehe [Felder, die der Schritt ablehnt](/de/reference/workflow-steps/salesforce/query-salesforce-object/#felder-die-der-schritt-ablehnt).
- **Ein Extrakt ist keine Synchronisierung.** Ein in Salesforce gelöschter Datensatz bleibt in der Zieltabelle erhalten.

## Verwandte Themen

- [Mit Salesforce verbinden](/de/guides/connections/salesforce/) – Schritt-für-Schritt-Anleitung
- [Salesforce: Objekt abfragen](/de/reference/workflow-steps/salesforce/query-salesforce-object/)
- [Verbindung erstellen und verwalten](/de/guides/connections/create-connection/)
