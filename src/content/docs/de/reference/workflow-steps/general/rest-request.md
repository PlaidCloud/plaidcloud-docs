---
title: REST-Anfrage
description: Rufen Sie in einem Workflow-Schritt eine REST-API auf — importieren Sie Endpunkte aus Postman, OpenAPI oder HAR und leiten Sie die Antwort in eine Tabelle oder in Workflow-Variablen.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/rest-request.md
---

## Beschreibung

Der Schritt **REST-Anfrage** ruft eine REST-API auf und leitet die Antwort in eine Zieltabelle oder in Workflow-Variablen. Er ersetzt die älteren REST-Schritte durch einen einheitlichen Schritt im Postman-Stil: Wählen Sie einen Endpunkt (manuell, Postman, OpenAPI/Swagger oder HAR), bearbeiten Sie Header, Abfrage und Body, senden Sie eine Testanfrage und speichern Sie.

Eine vollständige Anleitung finden Sie im [Leitfaden zum Schritt REST-Anfrage](/de/guides/workflows/rest-request-step/).

Während Sie bearbeiten, speichert der Browser einen lokalen Entwurf für den Schritt. Wenn Sie vor dem Speichern schließen oder neu laden, bietet der Schritt beim erneuten Öffnen an, diesen ungespeicherten Entwurf wiederherzustellen.

## Konfiguration

### Anfrage

* **Endpunktquelle** — `Manual`, `From the connection's API definition`, `Postman collection (file/URL)`, `OpenAPI / Swagger (URL/file)` oder `HAR archive (file)`. Mit **Katalog laden** listen Sie die Endpunkte einer importierten Quelle auf. Beim Auswählen eines Endpunkts werden Methode, URL, Header, Abfrageparameter und Body ausgefüllt, wobei zuvor nachgefragt wird, wenn Sie die Anfrage bearbeitet haben. Die drei Dateiquellen bieten außerdem **Einfügen…**, womit Sie die Collection oder Spezifikation direkt angeben können, statt eine Datei auszuwählen.
* **Verbindung** *(optional)* — eine REST-Verbindung für Authentifizierung und Basis-URL. Lassen Sie sie weg, um direkt eine vollständige URL aufzurufen. Die Bearbeitungsverknüpfung neben der Auswahl öffnet den Editor der ausgewählten Verbindung zum Anzeigen oder Bearbeiten.
* **Methode** — `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`.
* **Endpunkt** — Pfad (mit einer Verbindung) oder vollständige URL.
* **Header** / **Abfrageparameter** — Name-Wert-Zeilen mit einem Ein/Aus-Schalter.
* **Body** — Anfrage-Payload (JSON, Formular oder Rohdaten).
* **Testanfrage senden** / **Als curl kopieren** / **Aus curl importieren** — senden die Anfrage und zeigen die Antwort direkt an, kopieren einen äquivalenten curl-Befehl (Geheimnisse maskiert) oder füllen Methode, URL, Header und Body aus einem eingefügten curl-Befehl.
* **Senden** — `One request` (Standard) oder `One request per table row`, um die Anfrage über eine Treibertabelle aufzufächern.

Das Speichern von Änderungen an ausgehenden Anfragen vor einer erfolgreichen **Testanfrage senden** fordert zur Bestätigung auf. Im Auffächerungsmodus ist **Zeile 1 testen** der erfolgreiche Test, der die Warnung aufhebt.

Wenn **Senden** auf `One request per table row` steht, wählen Sie eine **Treibertabelle** (über die Tabellenauswahl oder durch Eingabe eines Namens) und verwenden Sie `{{row.column}}`-Token im Endpunkt, in der Abfrage, in den Headern oder im Body, um die Werte jeder Zeile einzusetzen. Die Einfügemenüs für Variablen im Endpunkt und im Body enthalten die Spalten der ausgewählten Treibertabelle. Optional: **Treiberfilter** (eine SQL-`WHERE`-Klausel), **Schlüsselspalten** (werden in jede Ausgabezeile übernommen), **Zeilenlimit**, **Parallelität**, **Max. Anfr./Sek.** (Obergrenze, wie schnell Anfragen über alle Worker hinweg gestartet werden, unabhängig von der Parallelität; akzeptiert Bruchwerte, 0,5 sendet also eine Anfrage alle zwei Sekunden; 0 = kein Limit; ein Wert über 1000 wird mit einer Warnung auf 1000 begrenzt), **Add Idempotency-Key header** (sendet bei einem einzelnen POST/PUT/PATCH ohne Paginierung einen stabilen `Idempotency-Key` pro Zeile, damit erneute Ausführungen nichts doppelt anlegen; andernfalls mit einer Warnung übersprungen) und **Continue on error** (hält eine fehlgeschlagene Zeile fest und warnt, statt abzubrechen) sowie **Antwort** (standardmäßig `Parsed records`; `Text (one row per request)` schreibt jede Antwort als Zeile mit den Spalten `DownloadData` und `DownloadHeaders`; `Raw text, errors as rows` tut dasselbe mit dem Body exakt so, wie ihn der Server gesendet hat, fügt eine Spalte `DownloadStatus` hinzu und behält einen HTTP- oder Transportfehler als Zeile, wobei Anmeldedaten in Body, Headern und Fehlertext maskiert werden). **Zeile 1 testen** sendet die Anfrage für die erste Treiberzeile, damit Sie die Auffächerung vor der Ausführung in der Vorschau sehen können. Die Auffächerung schreibt in die Zieltabelle; sie kann nicht in Variablen erfassen.

Wenn **Antwort** auf `Text (one row per request)` steht, gelten zwei weitere Auffächerungsoptionen:

* **Antworttext** — `As returned` (Standard); `Visible page text` schreibt statt des Markups den sichtbaren Text einer HTML-Seite in `DownloadData`; `Raw bytes (Base64)` schreibt die Bytes des Bodys exakt so, wie sie der Server gesendet hat, Base64-codiert, für eine Datei oder eine andere binäre Antwort.
* **Weiter abfragen, solange die Antwort übereinstimmt** — für eine API, die „noch in Arbeit" antwortet, bis ein Job abgeschlossen ist. Geben Sie einen **Antwortpfad** an (`$` für die gesamte Antwort, dann `.name`, `[0]`, `['name']` oder `["name"]`), einen Operator (`==`, `!=`, `<`, `<=`, `>` oder `>=`) und einen Wert mit seinem Typ (`Text`, `Number`, `True/False` oder `Empty`). Die Anfrage jeder Zeile wird erneut gesendet, solange ihre Antwort übereinstimmt, alle **N seconds** (1 bis 600, standardmäßig 5) und für bis zu **M requests per row** (1 bis 1000, standardmäßig 60). Eine Zeile, die nach der letzten Anfrage noch übereinstimmt, schlägt fehl.

Um binäre Inhalte zu senden, etwa eine Datei oder Audio, die als Base64-Text in einer Spalte gespeichert sind, aktivieren Sie **Der Body ist Base64-Text: die dekodierten Bytes senden** (`body_base64`). Bei einer Anfrage pro Tabellenzeile wird der Body, nachdem seine `{{row.column}}`-Token ausgefüllt wurden, als Base64-Text gelesen und die dekodierten Bytes werden gesendet.

Die Abschnitte **Optionen für Textantworten** und **Anmeldung, Proxy und TLS** haben diese Felder. Auch konvertierte KNIME-Workflows verwenden sie.

Bei einer Anfrage pro Tabellenzeile und **Antwort** auf `Text (one row per request)`:

* **Den HTTP-Status jeder Antwort als Spalte DownloadStatus hinzufügen** (`include_status`) — fügt den HTTP-Status jeder Antwort als Spalte `DownloadStatus` hinzu. **Statusspalte** (`status_column`) benennt stattdessen diese Spalte, und ihr Festlegen fügt die Spalte hinzu.
* **Die Zeile einer fehlgeschlagenen Anfrage behalten, mit DownloadStatus und DownloadError** (`keep_error_rows`) — eine fehlgeschlagene Anfrage behält ihre Zeile, wobei der Body fehlt und `DownloadStatus` und `DownloadError` gefüllt sind.
* **Die Zeile einer fehlgeschlagenen Anfrage behalten** (`keep_failed_rows`) — eine Anfrage, die mit HTTP 400 oder höher geantwortet hat, behält ihre Zeile mit dem Status, den Antwort-Headern und dem Fehler-Body in `DownloadError`. Eine Anfrage ohne Antwort behält nur ihre Schlüsselspalten. Ein Fehler beendet den Schritt weiterhin, wenn **Continue on error** deaktiviert ist. **Schritt bei einem Antwortstatus fehlschlagen lassen** (`fail_on_status`) listet die Statusfamilien, etwa `5xx`, auf, die den Schritt fehlschlagen lassen; eine Antwort jeder anderen Familie wird als Zeile behalten.
* `document` *(festgelegt mit einem KI-Assistenten oder der REST-API)* — speichert jede Antwort als Datei in diesem Dokumentordner, `{account, path, file_name}`, wobei `file_name` standardmäßig das letzte Segment der URL ist. Die Zeile enthält `FilePath` statt des Bodys.
* **Den Body als Webseitendokument schreiben** (`html_document`) — schreibt jeden Body als normalisiertes HTML-Dokument (`html`) oder dessen XML-Form (`xml`). **Relative href- und src-Werte absolut machen** (`html_absolute_urls`, Standard true) macht relative `href`- und `src`-Werte gegenüber der Anfrage-URL absolut.
* **Die Body-Spalte nach der ersten erfolgreichen Antwort typisieren** (`typed_body`) — typisiert die Body-Spalte nach der ersten erfolgreichen Antwort: JSON, Text oder binär anhand ihres `Content-Type`. Eine spätere Antwort anderer Art, JSON, das nicht geparst werden kann, und ein leerer Body fehlen.
* **Eine Spalte pro Antwort-Header hinzufügen** (`all_headers`) — fügt nach der Statusspalte für jeden Antwort-Header eine Textspalte hinzu. Ein Header, den eine Antwort nicht gesendet hat, fehlt.
* **Die Antwort-Cookies hinzufügen (DownloadCookies)** (`cookies`) — fügt `DownloadCookies` hinzu, die Cookies jeder Antwort.

Bei einer Anfrage pro Tabellenzeile:

* **Eine Zeile überspringen, deren URL keine absolute http(s)-URL ist** (`skip_invalid_urls`) — eine Zeile, deren URL keine absolute HTTP- oder HTTPS-URL ist, sendet keine Anfrage und schreibt keine Zeile. **Schritt fehlschlagen lassen, wenn die URL einer Zeile keine absolute http(s)-URL ist** (`fail_invalid_urls`) lässt den Schritt für eine solche Zeile stattdessen fehlschlagen.
* **Keinen Header senden, dessen Zeilenwert NULL ist** (`skip_null_headers`) — ein Header, dessen `{{row.column}}`-Wert NULL ist, wird nicht gesendet. **Schritt fehlschlagen lassen, wenn der Zeilenwert eines Headers NULL ist** (`fail_null_headers`) lässt den Schritt stattdessen fehlschlagen.
* **SOAP-Operation** (`soap`) — ruft eine Operation des WSDL auf, das der Endpunkt benennt, einmal pro Zeile: `service`, `port` und `operation` (jeweils der erste, wenn leer), `inputs`, das jeden Parameter einer Spalte oder einer Konstanten zuordnet, `outputs`, das die als Spalten zu schreibenden Antwortelemente benennt (eine Spalte pro Blattelement, wenn leer), und `xml`, um das Antwortelement als XML hinzuzufügen. Das WSDL und die Dienstadresse müssen öffentliche HTTP- oder HTTPS-URLs sein.

Für jede Anfrage:

* **Eine HTTP-Digest-Abfrage beantworten** (`digest_auth`) — beantwortet eine HTTP-Digest-Abfrage mit dem Basic-Auth-Benutzernamen und -Kennwort der Verbindung. **Eine NTLM-Abfrage beantworten** (`ntlm_auth`) beantwortet eine NTLM-Abfrage auf dieselbe Weise. Schreiben Sie den Benutzernamen als `DOMAIN\user`, um eine Domäne anzugeben.
* `proxy` — sendet Anfragen über einen HTTP- oder SOCKS-Proxy, festgelegt mit **Proxy-Protokoll** (`protocol`: `http`, `https`, `socks`, `socks4` oder `socks5`), **Proxy-Host** (`host`), **Proxy-Port** (`port`), **Direkt angesprochene Hosts** (`excluded`-Hostmuster) und **Proxy-Benutzername** (`username`). Das Kennwort ist das `proxy_password` der Verbindung und wird nur verwendet, wenn der `proxy_host` der Verbindung dieser Host ist.

`{{name}}`-Verweise auf Workflow-Variablen (auch `{{var.name}}` / `{{project_var.name}}`) werden zur Laufzeit im Endpunkt, in den Headern, den Abfragewerten und im Body ersetzt. Nur doppelte geschweifte Klammern werden ersetzt, einfache geschweifte Klammern in einem JSON-Body bleiben also unverändert. Sensor-/Webhook-Ausführungen stellen außerdem `{{trigger_sensor_id}}`, `{{trigger_sensor_type}}`, `{{trigger_fired_at}}` und `{{trigger_payload_json}}` bereit (bei nicht ausgelösten Ausführungen leer).

Der Editor hebt erkannte `{{...}}`-Token im Endpunkt, in den Header- und Abfragetabellen und im Body-Editor hervor.

**Wiederholungen** gelten nur für idempotente Methoden (GET/HEAD/OPTIONS/DELETE). Ein POST/PUT/PATCH wird immer nur einmal gesendet, damit ein nicht idempotenter Body nie erneut gesendet wird. **Wiederholungen** akzeptiert 0 bis 100. **Timeout (s)** ist das Limit pro Anfrage, 1 bis 600 s. Testanfragen warten höchstens 300 s. Informationen zum Katalogfilter, zum Einfügen und Ablegen, zu JSON-Werkzeugen, Anfragewarnungen und Testergebnissen finden Sie unter [REST-Anfrage-Schritt](/de/guides/workflows/rest-request-step/).

### Antwortziel

* **Tabelle** *(Standard)* — parst die Antwort in die **Zieltabelle** (erforderlich; nur Tabellen, keine Ansichten). Steuerelemente: Zeilenformat (`Object` oder `Array`; eine Anfrage pro Tabellenzeile erfordert `Object`), Elementpfad, Paginierungsmodus (`No Paging`, `Offset Paging`, `Page Number Paging`, `Next Page URL Paging`, `Cursor Paging` oder `Link Header Paging (RFC 5988)`), Modusparameter, Modus-Pfade, „Dump raw JSON instead of parsing rows", Wiederholungen, Timeout. Die Registerkarte **Tabellendatenauswahl** ordnet Antwortfelder Spalten zu. **Quelle untersuchen → Populate** füllt sie aus einer Live-Antwort, was eine Verbindung erfordert und vor dem Senden einer anderen Methode als GET, HEAD oder OPTIONS nachfragt. Zusammenfassen und Eindeutig werden nicht angeboten.
* **Workflow-Variablen** — sendet eine Anfrage und setzt `{prefix}_status`, `{prefix}_body`, `{prefix}_headers` und `{prefix}_elapsed_ms`. Das **Variablenpräfix** muss ein einfacher Bezeichner sein und darf keines von `cloud`, `project`, `model`, `date` sein.

## Verhalten

* Im Variablenmodus sendet der Schritt eine einzelne Anfrage. Paginierung und Zeilen-Parsing gelten nicht.
* Erfasste Variablen werden nachgelagert über ihren Namen referenziert, z. B. `{my_call_status}`.
