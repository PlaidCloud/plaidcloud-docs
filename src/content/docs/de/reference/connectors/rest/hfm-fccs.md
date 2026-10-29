---
title: HFM-/FCCS-Konnektor
description: Richten Sie in PlaidCloud eine Verbindung zu Oracle FCCS (Financial Consolidation and Close, EPM Cloud) ein, um mit einer Point-of-View-Auswahl selbstständig einen Ad-hoc-Datenausschnitt abzurufen, optional mit Caching und einem geplanten wiederkehrenden Ladevorgang.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/hfm-fccs.md
---

Verbinden Sie PlaidCloud mit Oracle **FCCS** (Financial Consolidation and Close, Teil von Oracle EPM Cloud), damit ein Finanzanwender einen Datenausschnitt selbstständig abrufen kann, ohne ein Ticket beim HFM-Team zu erstellen. Der Schritt [HFM/FCCS: Daten lesen (Ad-hoc)](/de/reference/workflow-steps/oracle-epm/hfm-fccs-read/) fühlt sich an wie eine Live-Abfrage, ist intern aber eine asynchrone Abfolge aus Anfrage, Abfragen des Status und Abruf über die Datenexport-Job-API von FCCS.

Die Verbindungsart erscheint in der Verbindungsauswahl als **REST – HFM/FCCS**.

:::note[Entitätsdimension eingrenzen]
Halten Sie jeden Point of View eingegrenzt. Ein Extrakt ohne Eingrenzung kann die FCCS-Anwendung für lange Zeit sperren, solange der Exportjob läuft.
:::

## API-Dokumentation

Der Konnektor verwendet die [REST-API](https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/index.html) von Oracle EPM Cloud: die Endpunkte für Anwendungsmetadaten (zum Ermitteln von Dimensionen und Mitgliedern) und die Endpunkte für Datenexportjobs (zum Anfordern, Abfragen und Abrufen eines Rasters).

## So funktioniert die Authentifizierung

Die Verbindung verwendet **HTTP-Basic-Authentifizierung mit einem Dienstkonto** auf einem klassischen EPM-Cloud-Pod. Es gibt keinen OAuth- oder Token-Ablauf (OCI-/Gen-2-Pods mit Bearer-Token werden nicht unterstützt). Ist eine **Identitätsdomäne** festgelegt, setzt PlaidCloud den Login als `identitydomain.username` zusammen (die Domäne, ein Punkt, dann der Benutzername). Lassen Sie die Identitätsdomäne leer oder enthält Ihr Benutzername bereits einen Punkt, wird der Benutzername unverändert gesendet. Verweisen Sie die Verbindung auf ein dediziertes Integrations-Dienstkonto mit Lesezugriff auf die Anwendungen und Point-of-View-Ausschnitte, die Ihre Self-Service-Benutzer abrufen.

## Konfiguration

| Feld | Erforderlich | Beschreibung |
|---|---|---|
| Name | Ja | Anzeigename für diese Verbindung. |
| EPM-Cloud-URL | Ja | Die URL Ihres EPM-Cloud-Pods bzw. -Dienstes, z. B. `https://planning-test-yourdomain.epm.us2.oraclecloud.com`. |
| Identitätsdomäne | Nein | Ihre EPM-Cloud-Identitätsdomäne. Wenn sie festgelegt ist, stellt PlaidCloud sie beim Login als `identitydomain.username` dem Benutzernamen voran. |
| Benutzername | Ja | Der Benutzername des Integrations-Dienstkontos. |
| Passwort | Ja | Das Passwort des Dienstkontos. Wird verschlüsselt gespeichert. |
| Standardanwendung | Nein | Eine FCCS-Standardanwendung, die in der Point-of-View-Auswahl des Schritts vorbelegt wird. Jeder Schritt kann sie überschreiben. |

## Was Sie mit der Verbindung tun können

- **Einen Ad-hoc-Ausschnitt selbst abrufen.** Erstellen Sie im Schrittformular einen Point of View (POV), bestehend aus der Anwendung und den FCCS-Dimensionen, klicken Sie auf „Ausführen“, und eine Ergebnistabelle wird automatisch angelegt. Siehe [HFM/FCCS: Daten lesen (Ad-hoc)](/de/reference/workflow-steps/oracle-epm/hfm-fccs-read/).
- **Ohne Ticket auskommen.** Der Ausschnitt läuft unter dem Dienstkonto der Verbindung, sodass ein Finanzanwender die Daten selbst abruft, statt auf einen HFM-Administrator zu warten.
- **Wiederholte Abrufe zwischenspeichern.** Wird derselbe POV mit demselben Stichtag erneut angefordert, erhalten Sie sofort die bereits geladene Kopie, ohne FCCS erneut abzufragen.
- **Steuern, wer welche Entitäten sieht.** Die geladene Tabelle ist **bereit für Sicherheit auf Zeilenebene**: Ein Administrator kann für die Spalte `Entity` einen Zeilenzugriff festlegen, sodass Self-Service-Benutzer nur die Entitäten sehen, auf die sie Anspruch haben. Das wird unter Kontrolle des Administrators gesteuert und erfolgt nicht automatisch – siehe die Schrittreferenz.
- **Einen wiederkehrenden Ladevorgang planen.** Aktivieren Sie **Gebundenes Ziel**, um einen Ad-hoc-Ausschnitt in eine persistente Tabelle zu überführen, die additiv wächst und Daten zusammenführt statt sie zu überschreiben. Derselbe Schritt in einem geplanten Workflow wird so zu einem nächtlichen wiederkehrenden Ladevorgang.

## Metadatenermittlung

Auf unterstützten FCCS-Pods ermittelt das Schrittformular die Mitgliederliste jeder Dimension live aus den Anwendungsmetadaten, sobald Sie eine Verbindung und eine Anwendung gewählt haben. Die POV-Auswahl bietet dann echte Mitglieder zur Auswahl an (die Ermittlung wird bei jeder Änderung der Auswahl neu ausgeführt). Auf älteren Pods, die den Metadatenendpunkt nicht bereitstellen, liefert die Ermittlung nichts und die Auswahl wechselt zur manuellen Eingabe: Sie geben Mitgliedsnamen von Hand ein, und ein gespeicherter Point of View lässt sich immer wieder korrekt laden. Der Abruf funktioniert in beiden Fällen gleich.

## Bekannte Einschränkungen

| Einschränkung | Bedeutung |
|---|---|
| Schreibgeschützt | Der Konnektor extrahiert Daten aus FCCS. Er schreibt keine Konsolidierungsdaten, führt keine Konsolidierungen aus und bucht nichts zurück. |
| Entitätsdimension eingrenzen | Ein Extrakt ohne Eingrenzung (ohne `Entity`-Auswahl) kann die FCCS-Anwendung für lange Zeit sperren, solange der Exportjob läuft. Halten Sie die Entitätsauswahl eingegrenzt. |
| Manuelle Mitglieder auf älteren Pods | Wenn ein Pod den Metadatenendpunkt nicht bereitstellt, werden die Mitgliederlisten nicht automatisch gefüllt – geben Sie die Mitgliedsnamen von Hand ein. |
| Sicherheit auf Zeilenebene wird vom Administrator gesteuert, nicht automatisch | Die geladene Tabelle lässt sich mit Zeilenzugriff steuern, aber ein Administrator muss veröffentlichen, die Spalte `Entity` deklarieren, den ersten gesteuerten Schreibvorgang genehmigen und abgleichen. Bis dahin wird die Tabelle nicht gefiltert. |

## Verwandte Themen

- [Aus HFM / FCCS extrahieren (Anleitung)](/de/guides/connections/hfm-fccs/) – Verbindung erstellen, einen POV aufbauen, ausführen, zwischenspeichern, steuern und planen.
- [HFM/FCCS: Daten lesen (Ad-hoc)](/de/reference/workflow-steps/oracle-epm/hfm-fccs-read/) – die Feldreferenz des Schritts.
- [Sicherheitsgruppen und Zuweisungen verwalten](/de/administration/access/managing-security-groups-and-assignments/) – wie der Zeilenzugriff die geladene Tabelle steuert.
- [Verbindung erstellen und verwalten](/de/guides/connections/create-connection/)
