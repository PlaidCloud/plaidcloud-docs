---
title: ODBC
description: Richten Sie in PlaidCloud eine ODBC-Verbindung über einen System-DSN oder einen ODBC-Treiber auf dem Rechner eines PlaidLink-Agents ein, unter Windows oder Linux.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/odbc.md
---

**ODBC (Open Database Connectivity)** erreicht eine Datenbank über die ODBC-Einrichtung auf dem Rechner, auf dem ein [PlaidLink-Agent](/de/reference/cli/plaidlink/) läuft. Verwenden Sie ODBC für eine Datenbank ohne dedizierten PlaidCloud-Connector, aus Agent-Schritten wie [Agent Remote Export of SQL Result](/de/reference/workflow-steps/agent/agent-remote-export-of-sql-result/). Wählen Sie zum Erstellen **ODBC** als Verbindungstyp.

:::note
Eine ODBC-Verbindung erfordert PlaidLink 1.2.31 oder höher auf dem Agent. Siehe [Upgrade](/de/reference/cli/plaidlink/upgrade/).
:::

Eine ODBC-Verbindung funktioniert auf eine von zwei Arten:

- **Über einen DSN.** Lassen Sie **ODBC-Treiber** leer und geben Sie eine auf dem Rechner des Agents eingerichtete Datenquelle (DSN) an. Der DSN enthält den Treiber, den Server, die Datenbank und alle weiteren Treibereinstellungen; **Verbindungsattribute** können sie überschreiben. Das funktioniert mit jedem ODBC-Treiber.
- **Über einen Treiber.** Wählen Sie einen auf dem Rechner des Agents installierten **ODBC-Treiber** aus oder geben Sie ihn ein und geben Sie dann Server und Datenbank an. PlaidCloud übergibt dem Treiber eine `Server`- und eine `Database`-Einstellung, gefolgt von allen **Verbindungsattributen**. Das funktioniert mit den SQL-Server-Treibern von Microsoft. Verwenden Sie für jeden anderen Treiber, auch für die übrigen in der Liste vorgeschlagenen, einen DSN.

## Dokumentation des Herstellers
Der ODBC-Treiber jeder Datenbank hat eigene Einstellungen. Welche Schlüsselwörter er akzeptiert, entnehmen Sie der Dokumentation des Treiberherstellers, sowohl beim Erstellen eines DSN als auch beim Schreiben von Verbindungsattributen.

## DSN auf dem Rechner des Agents erstellen

Richten Sie den DSN auf dem Rechner, auf dem der Agent läuft, als System-DSN ein, damit der Agent ihn unabhängig vom verwendeten Konto findet.

### Unter Windows

1. Öffnen Sie **ODBC Data Sources (64-bit)**.
2. Fügen Sie auf der Registerkarte **System DSN** eine Datenquelle hinzu, die den ODBC-Treiber der Datenbank verwendet, und geben Sie Server, Datenbank und alle weiteren vom Treiber verlangten Einstellungen ein.
3. Notieren Sie den **Namen der Datenquelle**. Sie geben ihn in der Verbindung ein.

:::caution
Der DSN muss ein 64-Bit-**System-DSN** sein. Unter Windows läuft der Agent als Dienst und kann weder einen Benutzer-DSN noch einen im 32-Bit-ODBC-Administrator erstellten DSN sehen. Der Schritt schlägt dann mit `ODBC data source '<name>' is not defined on the agent machine` fehl.
:::

### Unter Linux

Unter Linux erreicht der Agent ODBC über unixODBC.

1. Installieren Sie unixODBC und den ODBC-Treiber der Datenbank.
2. Prüfen Sie, ob der Treiber in `odbcinst.ini` unter seinem Namen in eckigen Klammern registriert ist. Die meisten Treiberpakete registrieren sich bei der Installation selbst; `odbcinst -q -d` listet die registrierten Treiber auf.
3. Fügen Sie die Datenquelle der System-`odbc.ini` hinzu, als Abschnitt mit dem Namen des DSN. Setzen Sie `Driver` auf den registrierten Treibernamen und ergänzen Sie Server, Datenbank und alle weiteren vom Treiber verlangten Einstellungen:

   ```ini
   [Sales]
   Driver=ODBC Driver 18 for SQL Server
   Server=sales-db.example.com
   Database=Sales
   ```

4. Notieren Sie den Abschnittsnamen, hier `Sales`. Sie geben ihn in der Verbindung ein.

`odbcinst -j` zeigt, wo die System-`odbcinst.ini` und die System-`odbc.ini` liegen, in der Regel unter `/etc`. Ein DSN in der eigenen `~/.odbc.ini` eines Benutzers wird nur gefunden, wenn der Agent als dieser Benutzer läuft.

### In einem Container

Das PlaidLink-Container-Image enthält unixODBC, aber keinen ODBC-Treiber. Um ODBC aus einem Agent zu verwenden, der in Docker oder Kubernetes läuft, erstellen Sie auf dieser Grundlage ein Image, das den Treiber installiert, und fügen Sie die System-`odbc.ini` mit dem DSN dem Image hinzu oder binden Sie sie in den Container ein. Das Image läuft als Benutzer `plaid`; wechseln Sie daher zum Installieren des Treibers zu `root` und anschließend wieder zu `plaid`.

## Konfiguration

### Datenbankverbindung

| Feld | Erforderlich | Beschreibung |
|---|---|---|
| ODBC-Treiber | Nein | Leer lassen, um eine Verbindung über einen DSN herzustellen. Andernfalls der Name eines auf dem Rechner des Agents installierten ODBC-Treibers, genau so, wie dieser Rechner ihn registriert: unter Windows so, wie **ODBC Data Sources (64-bit)** ihn auf der Registerkarte **Drivers** auflistet, und unter Linux als sein Abschnittsname in `odbcinst.ini`. Die Liste bietet gängige Treiber an, und Sie können jeden anderen eingeben. Nur die SQL-Server-Treiber von Microsoft funktionieren hier. Lassen Sie das Feld für jeden anderen Treiber, auch für die übrigen in der Liste angebotenen, leer und verwenden Sie einen DSN. Ein Treibername darf keine geschweiften Klammern und keine Semikolons enthalten. |
| Name der Datenquelle (DSN) oder Server | Ja | Ohne Treiber der Name des System-DSN auf dem Rechner des Agents. Mit Treiber der Hostname des Datenbankservers oder `host,port` für SQL Server an einem nicht standardmäßigen Port. |
| Datenbank | Mit Treiber | Die zu öffnende Datenbank. Sie ist ohne Treiber nicht verfügbar, weil der DSN seine eigene angibt, und das Speichern lehnt eine Datenbank ohne Treiber ab. |
| Verbindungsattribute | Nein | Weitere Einstellungen für den Treiber als durch `;` getrennte `KEY=value`-Paare. Siehe [Verbindungsattribute](#verbindungsattribute). |

Die Verbindung hat kein Portfeld. Für SQL Server an einem nicht standardmäßigen Port fügen Sie ihn dem Server als `host,port` hinzu, da die SQL-Server-Treiber von Microsoft kein Port-Schlüsselwort kennen. Legen Sie bei einem DSN den Port im DSN fest oder überschreiben Sie ihn für einen Treiber, der einen Port akzeptiert, mit einem Attribut wie `PORT=5433`.

### Verbindungsattribute

**Verbindungsattribute** übergibt ODBC-Einstellungen in beiden Modi an den Treiber, so geschrieben, wie ODBC sie schreibt:

- Mit einem Treiber werden sie hinter den eigenen Einstellungen der Verbindung angefügt. Verwenden Sie sie für alles Weitere, was der Treiber benötigt, etwa `ApplicationIntent=ReadOnly`, um eine Verbindung zu einem schreibgeschützten Replikat herzustellen.
- Mit einem DSN überschreiben sie die eigenen Einstellungen des DSN, etwa `PORT=5433`, oder `DBQ=MYLIB` für die Standardbibliothek von IBM i.

Trennen Sie Paare mit `;`, wie in `Encrypt=yes;ApplicationIntent=ReadOnly`. Setzen Sie einen Wert, der `;` enthält, in geschweifte Klammern, wie in `KEY={first;second}`, und schreiben Sie `}` innerhalb der Klammern als `}}`. Die Schlüsselwörter erreichen den Treiber in Großbuchstaben; ODBC-Schlüsselwörter sind nicht von der Groß- und Kleinschreibung abhängig.

Das Speichern lehnt Folgendes ab:

- Text, der keine `KEY=value`-Paare enthält, einschließlich einer geschweiften Klammer, die nie geschlossen wird, und eines Schlüsselworts ohne Wert;
- ein Schlüsselwort, das mehrfach angegeben ist, in beliebiger Schreibweise;
- ein Schlüsselwort, das die Verbindung aus ihren eigenen Feldern setzt: `DRIVER`, `DSN`, `SERVER`, `DATABASE`, `UID`, `PWD`, `USER`, `USERID`, `USERNAME` und `PASSWORD`;
- `FILEDSN` und `SAVEFILE`, durch die der Agent die Einstellungen der Verbindung aus einer Datei auf seinem Rechner lesen oder in eine solche schreiben würde.

Verbindungslisten maskieren die Attribute, weil ein Treiber dort sein eigenes Anmeldedaten-Schlüsselwort akzeptieren kann; das eigene Formular der Verbindung zeigt sie an. Leeren Sie das Feld, um sie zu entfernen. Geben Sie Benutzer und Passwort unter **Authentifizierungsdaten** ein.

:::note
**ODBC Driver 18 for SQL Server** verschlüsselt die Verbindung und überprüft standardmäßig das Zertifikat des Servers. Fügen Sie für einen Server mit selbstsigniertem Zertifikat `TrustServerCertificate=yes` zu den Attributen hinzu.
:::

### Authentifizierungsdaten

| Feld | Beschreibung |
|---|---|
| User | Der Benutzer, mit dem die Verbindung hergestellt wird. Lassen Sie das Feld bei einem DSN leer, um sich so anzumelden, wie der DSN eingerichtet ist, oder fügen Sie für SQL Server `TRUSTED_CONNECTION=Yes` zu den Attributen hinzu, um sich mit dem eigenen Konto des Agents anzumelden. Mit einem SQL-Server-Treiber und ohne Benutzer meldet sich die Verbindung mit dem eigenen Konto des Agents an: seinem Windows-Konto oder unter Linux seinem Kerberos-Ticket. |
| Use Single Sign-On Authentication (No Password, Optional User) | Verbindung ohne gespeichertes Passwort herstellen. |
| Password | Das Passwort des Benutzers (nur schreibbar). Lassen Sie das Feld beim Bearbeiten leer, um das gespeicherte Passwort beizubehalten. |

### SSL-Konfiguration und SSH-Konfiguration

Diese Registerkarten gelten nicht für eine ODBC-Verbindung. Legen Sie Verschlüsselung und weitere Treiberoptionen im DSN oder in den Verbindungsattributen fest.

## Von einer früheren Version gespeicherte Verbindungen

Frühere Versionen dieses Formulars verlangten eine **Datenbank** und einen aus einer festen Liste gewählten Treiber und füllten einen **Port** aus, gaben den Treiber aber nie weiter, sodass diese Verbindungen keine Verbindung herstellen konnten. Öffnen Sie die Verbindung und gehen Sie auf eine der folgenden Arten vor:

- **Verbindung über einen DSN:** Leeren Sie **ODBC-Treiber**, geben Sie den DSN ein und speichern Sie. Beim Speichern wird die alte Datenbank gelöscht.
- **Verbindung über einen SQL-Server-Treiber:** Prüfen Sie, ob **ODBC-Treiber** einem auf dem Rechner des Agents installierten SQL-Server-Treiber entspricht. Viele Namen in der alten Liste waren nicht die Namen, unter denen Treiber sich registrieren.

Eine Verbindung, die einen Treiber aus der alten Liste behält, wird als Treiberverbindung geöffnet. Sie kann keine Verbindung herstellen, bis der Treiber ein auf dem Rechner des Agents installierter SQL-Server-Treiber ist; für jede andere Datenbank stellen Sie die Verbindung über einen DSN her.

Beim Speichern wird auch der alte Port gelöscht. Eine Verbindung, die nur einen DSN und keine Datenbank hatte, wird mit leerem **ODBC-Treiber** geöffnet.
