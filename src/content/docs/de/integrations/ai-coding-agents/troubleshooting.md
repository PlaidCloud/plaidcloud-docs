---
title: Fehlerbehebung
description: Häufige Probleme bei der Verbindung von KI-Agents mit dem PlaidCloud-MCP-Server und ihre Lösungen.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/troubleshooting.md
---

## Cursor (oder ein anderer strenger Client) verbindet sich überhaupt nicht

Symptom: Der Server baut in Cursor und ähnlichen strengen Clients nie eine Sitzung auf, während derselbe Workspace in Claude Code funktioniert.

Ursache: ein **abschließender Schrägstrich** in der Server-URL. Verwenden Sie `https://<your-workspace>.plaid.cloud/mcp` – nicht `.../mcp/`. Strenge Clients lehnen eine URL mit abschließendem Schrägstrich ab (oder folgen der Weiterleitung nicht, die der ältere Pfad ausgestellt hat), während nachsichtige Clients wie Claude Code sie tolerieren.

Lösung: Entfernen Sie den abschließenden Schrägstrich aus der `url` in Ihrer Konfiguration und verbinden Sie sich erneut. Alle Beispiele in diesen Anleitungen verwenden die Form ohne Schrägstrich.

## „Failed to Connect“ / „Session Not Found“

Symptom: Die Client-Konfiguration sieht korrekt aus, aber der Server wird im MCP-Statusbereich des Clients als fehlgeschlagen angezeigt. In den Server-Protokollen erscheinen 404-Fehler `Session not found`.

Ursache: ein bekannter Fehler in einigen MCP-Clients (vor allem Claude Code 2.1.111 mit statischen `Authorization`-Headern), bei dem der Client `mcp-session-id` zwischen aufeinanderfolgenden HTTP-Anfragen nicht beibehält. Der MCP-Server von PlaidCloud läuft im zustandslosen HTTP-Modus, um dies zu umgehen. Wenn Sie den Fehler auf einem Tenant sehen, der seit der Korrektur nicht neu bereitgestellt wurde, bitten Sie Ihren Administrator um eine erneute Bereitstellung.

Bis die erneute Bereitstellung erfolgt ist, funktioniert der OAuth-Ablauf (ohne statische `Authorization`-Header) weiterhin, da er im Client einen anderen Codepfad verwendet.

## Die Seite „Application Access Request“

Symptom: Nach der Anmeldung bei PlaidCloud während einer OAuth-Autorisierung landen Sie auf einer Seite mit dem Titel **Application Access Request**, die eine Anwendung und einen Redirect-URI nennt, und müssen auf „Approve“ klicken, bevor der Ablauf fortgesetzt wird.

Ursache: Das ist erwartetes Verhalten. Jede OAuth-Autorisierung über den MCP-Server von PlaidCloud zeigt diese Seite an, damit Sie bestätigen können, womit Sie sich verbinden, bevor ein Token ausgestellt wird. Sie nennt die anfragende Anwendung und den Redirect-URI, an den die Anmeldedaten gesendet werden. Prüfen Sie, ob beide zu dem Client passen, mit dem Sie sich tatsächlich verbinden, und genehmigen Sie keine Anfrage, die Sie nicht selbst gestartet haben.

Ein bereits verbundener Client sieht diese Seite bei der Token-Erneuerung nicht erneut – nur eine neue Autorisierung (erste Verbindung oder nach Ablauf oder Widerruf des Refresh-Tokens) führt wieder dorthin.

Lösung: Es gibt nichts zu beheben – genehmigen Sie die Seite, um fortzufahren. Wenn Sie die Autorisierung in einem Browser (oder Profil) gestartet haben und die Seite in einem anderen angezeigt wird, kann sie nicht abgeschlossen werden: Die Zustimmung ist an den Browser gebunden, der den Ablauf gestartet hat. Starten Sie die Autorisierung erneut in dem Browser, in dem Sie bei PlaidCloud angemeldet sind.

## „OAuth Flow Is Not in Progress“ bei der Anmeldung in Claude Code

Symptom: Sie autorisieren im Browser, fügen die Callback-URL in Claude Code ein, und es meldet, dass kein Ablauf aktiv ist.

Ursache: Der OAuth-Zustand der Bridge liegt im Arbeitsspeicher, gilt pro Port und kann zwischen den Tool-Aufrufen `authenticate` und `complete_authentication` verloren gehen – besonders in Remote-/SSH-Sitzungen, in denen der Browser-Callback `localhost` nicht erreichen kann.

Lösung: Wechseln Sie zum statischen Bearer-Ablauf. Öffnen Sie `https://<your-workspace>.plaid.cloud/mcp/setup/token` in einem Browser, in dem Sie bei PlaidCloud angemeldet sind, kopieren Sie das Snippet in Ihre `.mcp.json` und starten Sie Claude Code neu.

## Token abgelaufen

Symptom: Tools, die gestern funktionierten, liefern jetzt 401 Unauthorized.

Ursache: Statische Bearer-Tokens folgen der Richtlinie zur Lebensdauer von Access-Tokens in Ihrem Keycloak-Realm (typischerweise einige Stunden bis ein Tag).

Lösung: Laden Sie `https://<your-workspace>.plaid.cloud/mcp/setup/token` neu, um ein frisches Token zu erzeugen, und fügen Sie es in Ihre Konfiguration ein. Für langlebige Sitzungen bevorzugen Sie OAuth – Clients, die es unterstützen, erneuern Tokens automatisch.

## „No `access_token` in Session“

Symptom: Das Öffnen von `/mcp/setup/token` zeigt „Sign-in required“ oder „No access_token in session“, obwohl Sie bei PlaidCloud angemeldet sind.

Ursache: Ihre Sitzung wurde über einen Anmeldepfad aufgebaut, der das Keycloak-Token nicht zwischengespeichert hat (ungewöhnlich, aber möglich).

Lösung: Melden Sie sich bei PlaidCloud ab und über die Standard-Anmeldeseite wieder an. Die neue Sitzung enthält das Access-Token.

## Fehlende Tools oder unvollständiger Katalog

Symptom: `mcp_introspect` liefert weniger Tools als erwartet, oder bestimmte benötigte Tools fehlen.

Ursache 1 – Scopes: Tools erfordern bestimmte PlaidCloud-Scopes (z. B. `analyze.workflow.write`). Fehlt Ihrem Konto der Scope, verweigert das Tool die Ausführung. Führen Sie `mcp_introspect(name='<tool>')` aus, um die `required_scopes` zu sehen. Bitten Sie Ihren Workspace-Administrator, den Scope zu erteilen, oder führen Sie den Vorgang über ein Konto aus, das ihn besitzt.

Ursache 2 – Versionskonflikt: Eine ältere Bereitstellung enthält möglicherweise nicht alle Tools, die in der aktuellen Dokumentation beschrieben sind. Vergleichen Sie die Tool-Anzahl von `mcp_introspect()` mit den Versionshinweisen Ihrer aktuellen Version und fordern Sie bei Bedarf eine erneute Bereitstellung an.

## Mehrere Tenants: Welchen Tenant hat der Agent gerade angesprochen?

Symptom: Sie haben mehrere PlaidCloud-Tenants konfiguriert, und die Antwort des Agents könnte von jedem davon stammen.

Lösung: Nennen Sie den Tenant ausdrücklich in Ihrem Prompt („im **dev**-Tenant, liste die Workflows auf …“). Die MCP-Servernamen, die Sie in Ihrer Konfiguration gewählt haben (z. B. `plaidcloud-prod`, `plaidcloud-dev`), dienen zugleich als Bezeichner, anhand derer das Modell unterscheiden kann. Lassen Sie bei kritischen Vorgängen die Produktion in der Connector-Auswahl ausgeschaltet, bis Sie sie wirklich brauchen.

## Ratenbegrenzung und Kontingent

Die REST-Schnittstelle von PlaidCloud ist pro Minute ratenbegrenzt, über dieselbe Middleware, die auch der Benutzeroberfläche vorgeschaltet ist. MCP-Aufrufe teilen sich dieses Limit. Wenn ein Agent eine lange Folge von `find`-Aufrufen absetzt (z. B. um jedes Projekt, jeden Workflow und jeden Schritt aufzulisten), können Sie das Limit erreichen. Verwenden Sie Paginierung (`cursor`, `limit`) und `count_only=True` für Größenprüfungen, statt die vollständige Ergebnismenge abzurufen.

Beachten Sie, dass ein Find standardmäßig 25 Zeilen pro Seite liefert (`step_find` liefert 50). Das Auflisten einer großen Menge kostet daher mehr Aufrufe als früher – erhöhen Sie bei einer gezielten Vollabfrage `limit`, statt mit dem Standardwert zu blättern. Wenn Sie umgekehrt immer wieder an das Limit stoßen, bedeuten `count_only=True` und eine engere `fields=[...]`-Projektion meist, dass Sie die Vollabfrage gar nicht gebraucht hätten.

## Eine Liste wirkt zu kurz, oder ein Agent sagt „Das sind alle“

Symptom: Ein Find lieferte weniger Zeilen als erwartet, oder der Agent kam zu dem Schluss, ein Projekt habe 25 Tabellen, obwohl es 300 hat.

Lösung: Prüfen Sie den Envelope. Eine gekappte Seite setzt `next_cursor`, und ein Find-Tool nennt die gekürzte Liste außerdem in `truncated` – beides bedeutet, dass noch mehr abzurufen ist. `total` meldet unabhängig davon die vollständige Anzahl; vergleichen Sie sie mit den erhaltenen Zeilen. Bitten Sie den Agent, mit dem Cursor zu blättern oder die Abfrage mit höherem `limit` zu wiederholen.

## Ein Ergebnis sieht aus wie `{"_fmt": "cols", ...}`

Symptom: Ein Tool lieferte `{"_fmt": "cols", "cols": [...], "rows": [[...]]}` statt der erwarteten Liste von Objekten.

Das ist die vorgesehene Form für ein großes Ergebnis, dessen Zeilen alle dieselben Felder tragen – die Feldnamen werden einmal gesendet, statt in jeder Zeile wiederholt zu werden. Zeile *i* ist `dict(zip(cols, rows[i]))`. Agents werden beim Verbinden darüber informiert und verarbeiten dies ohne Aufforderung; wenn Sie diese Antworten in Ihrem eigenen Code lesen, dekodieren Sie beide Formen, da kleine und unregelmäßige Ergebnisse weiterhin als gewöhnliche Arrays von Objekten ankommen. Am Envelope ändert sich sonst nichts, und kein Wert wird verändert. Siehe [Erste Schritte mit KI-Coding-Agents](/de/integrations/ai-coding-agents/getting-started/#spaltenorientierte-ergebnisse).

## Hilfe erhalten

Prüfen Sie bei serverseitigen Problemen – Authentifizierungsfehlern, Tools, die ohne erkennbare Ursache Fehler liefern, fehlenden Tools – zuerst den `error`-Envelope der Antwort. Jeder Fehler enthält `code`, `retryable`, `message` und oft einen `hint`. Reicht der Hinweis nicht aus, wenden Sie sich an Ihren PlaidCloud-Administrator oder eröffnen Sie ein Support-Ticket mit der Request-ID (zurückgegeben im Antwort-Header `X-Request-Id`).
