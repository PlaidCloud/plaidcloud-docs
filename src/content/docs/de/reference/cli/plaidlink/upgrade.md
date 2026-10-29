---
title: Upgrade
description: Aktualisieren Sie Ihren PlaidLink-Agent auf die neueste Version, um neue Funktionen, Sicherheitspatches und eine bessere Systemkompatibilität zu erhalten.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidlink/upgrade.md
---

Ein manuelles Upgrade von PlaidLink kann erforderlich sein, wenn der Agent nicht über ausreichende Berechtigungen verfügt, um sich bei neuen Versionen selbst zu aktualisieren, oder wenn ein manueller Upgrade-Prozess gewünscht ist.

## Den Agent herunterladen

Suchen Sie auf [PlaidCloud.com](https://plaidcloud.com/) in den Releases nach **PlaidLink**.

## Den aktuellen Agent beenden

Geben Sie **`Services`** in die Windows-Suchleiste ein und öffnen Sie die Dienstverwaltung. Suchen Sie in der Liste der Dienste nach **`PlaidCloud Agent`**.

Klicken Sie mit der rechten Maustaste auf den Dienst **`PlaidCloud Agent`** und wählen Sie *Beenden*. Sobald der Dienst erfolgreich beendet wurde, fahren Sie fort.

## Den Agent entpacken

Navigieren Sie zum aktuellen Speicherort des installierten Agent.

```bash
C:\Users\<Username here>\src\
```

Benennen Sie den aktuellen Installationsordner um, damit er nicht mehr referenziert wird. Beispiel: `Plaidlink_Old_12122022`

Entpacken Sie die heruntergeladene ZIP-Datei an diesem Speicherort und installieren Sie sie dort. In der Regel ist dies:

```bash
C:\Users\<Username here>\src\plaidlink
```

## Den Agent starten

Kehren Sie zum Fenster *Dienste* zurück. Klicken Sie mit der rechten Maustaste auf den Dienst **`PlaidCloud Agent`** und wählen Sie *Starten*.

Geben Sie **`Services`** in die Windows-Suchleiste ein und öffnen Sie die Dienstverwaltung. Suchen Sie in der Liste der Dienste nach **`PlaidCloud Agent`**.

Klicken Sie mit der rechten Maustaste auf den Dienst und wählen Sie **`Start`**, um den Agent zu starten. Sobald der Agent den Status **`Running`** anzeigt, ist er mit der neuen Version wieder betriebsbereit.
