---
title: Encrypt File and Decrypt File
description: Verschlüsseln oder entschlüsseln Sie in einem PlaidCloud-Workflow-Schritt eine ganze Dokumentdatei mit AES oder Blowfish oder setzen oder entfernen Sie das Kennwort einer Excel-Arbeitsmappe.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/encrypt-decrypt-file.md
---

## Beschreibung

**Dokument: Datei verschlüsseln** verschlüsselt eine Datei in einem Dokumentenkonto und schreibt das Ergebnis in eine andere Datei. **Dokument: Datei entschlüsseln** macht das Gegenteil. Beide Schritte haben dieselben Einstellungen. Verwenden Sie sie, um verschlüsselte Dateien von einem Partner zu empfangen, sie zu entschlüsseln, bevor ein Import sie liest, und einen Export zu verschlüsseln, bevor er an ein anderes System geht.

## Dateien

| Einstellung | Erforderlich | Funktion |
| --- | --- | --- |
| Quelldatei | Ja | Die Datei, die ver- oder entschlüsselt wird. |
| Zieldatei | Ja | Die Datei, die geschrieben wird. Sie muss eine andere Datei als die Quelle sein, damit eine erneute Ausführung nie mit ihrer eigenen Ausgabe arbeitet. |
| Quelldatei löschen, sobald die Zieldatei geschrieben ist | Nein | Entfernt die Quelldatei, nachdem die Zieldatei sicher geschrieben wurde. |

Eine Quelldatei, die nicht vorhanden ist, ist kein Fehler: Der Schritt endet mit einer Warnung, die den Pfad nennt, schreibt nichts, und der Workflow läuft weiter. Eine leere Quelldatei schreibt eine leere Zieldatei mit einer Warnung; eine Ausnahme ist das Verschlüsseln einer leeren Datei mit AES oder Blowfish, das eine echte verschlüsselte Datei schreibt. Ein Smartsheet-Dokumentenkonto kann nicht verwendet werden, weil sich Dateien daraus nicht zurücklesen lassen.

## Parameter

| Einstellung | Funktion |
| --- | --- |
| Algorithmus | In der Gruppe „Cipher“: **AES-128 (16-Byte-Schlüssel)**, **AES-192 (24-Byte-Schlüssel)**, **AES-256 (32-Byte-Schlüssel)**, **Blowfish (Schlüssel mit 4 bis 56 Byte)** oder **Kennwort der Excel-Arbeitsmappe**. |
| Modus | **CBC** (der Standard), **ECB** oder **GCM**. Blowfish unterstützt nur CBC oder ECB. |
| Schlüsselvariable | Die Workflow- oder Projektvariable, die den Verschlüsselungsschlüssel enthält, etwa `{aes_key}`. Erforderlich für AES und Blowfish. |
| Kodierung von Schlüssel und IV | Wie Schlüssel und IV geschrieben werden: **Text (UTF-8)**, **Hexadezimal** oder **Base64**. |
| Feste IV | Der Initialisierungsvektor. Lassen Sie das Feld leer, dann beginnt die Verschlüsselung die Datei mit einer zufälligen IV, die die Entschlüsselung vom Dateianfang zurückliest. Die GCM-Verschlüsselung verwendet immer eine zufällige IV, lassen Sie das Feld für GCM also leer. |
| Variable für das Arbeitsmappenkennwort | Die Workflow- oder Projektvariable, die das Kennwort enthält, das für eine Excel-Arbeitsmappe gesetzt oder daraus entfernt wird, etwa `{xlsx_password}`. Erforderlich für **Kennwort der Excel-Arbeitsmappe**. |

CBC und ECB füllen mit PKCS7 auf, und GCM hängt nach den verschlüsselten Daten ein 16 Byte langes Authentifizierungs-Tag an. Eine GCM-Datei kann bis zu 256 MB groß sein. Ein falscher Schlüssel oder eine falsche IV stoppt den Schritt mit einem Fehler und hinterlässt keine Teildatei.

## Schlüssel liegen in Variablen

**Schlüsselvariable** und **Variable für das Arbeitsmappenkennwort** nehmen nur einen Variablenverweis wie `{aes_key}` an, niemals den Schlüssel oder das Kennwort selbst: Das Speichern eines Schritts mit etwas anderem darin wird abgelehnt. Legen Sie das Geheimnis in einer [Workflow-Variable](/de/guides/workflows/manage-workflow-variables/) oder einer Projektvariable ab, damit es an einer einzigen Stelle gesetzt wird und nie im Schritt, in seinen Versionen, seinen Kopien oder in dem erscheint, was ein KI-Assistent zurückliest. Der Schritt liest den Wert der Variable, wenn er ausgeführt wird. **Feste IV** ist ein Kennwortfeld, daher ist sein Wert im Formular verborgen.

Bei Schritten, die vor dieser Regel einen eingetippten Schlüssel oder ein eingetipptes Kennwort enthielten, wurde dieser Wert automatisch in eine neue Projektvariable verschoben, die nur für Architects sichtbar ist; die Schritte verweisen jetzt auf diese Variable.

## Verwandte Themen

- [Dokumentschritte](/de/reference/workflow-steps/document/)
- [Workflow-Variablen verwalten](/de/guides/workflows/manage-workflow-variables/)
