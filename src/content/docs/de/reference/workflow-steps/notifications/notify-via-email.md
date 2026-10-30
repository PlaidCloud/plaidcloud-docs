---
title: Notify Via Email
description: Senden Sie E-Mail-Benachrichtigungen aus einem PlaidCloud-Workflow-Schritt mit anpassbarem Betreff, Body, Empfängern und Anhangsoptionen.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-email.md
---

## Beschreibung


Senden Sie E-Mail-Benachrichtigungen. Nachrichten werden vom E-Mail-Konto *[info@tartansolutions.com](mailto:info@tartansolutions.com)* gesendet. Es ist keine Einrichtung für ausgehende E-Mails erforderlich.



### E-Mail-Adressen


Geben Sie beliebig viele E-Mail-Empfänger an. Zulässige Trennzeichen sind Semikolon (;) und Komma (,).



### Cc, Bcc und Antwort an

**Cc** (`cc_address`), **Bcc** (`bcc_address`) und **Antwort an** (`reply_to`) erwarten Adressen im selben Format wie die Empfänger und akzeptieren Projekt- und Workflow-Variablen. Cc- und Bcc-Empfänger erhalten dieselbe Nachricht, und Antworten gehen an die Adresse unter „Antwort an". Sie gelten für Klartext- und Jinja-Vorlagen-Bodys. Legen Sie sie unter **Weitere E-Mail-Optionen** auf der Registerkarte **Nachricht** fest.

### Eine E-Mail pro Zeile

Legen Sie unter **Weitere E-Mail-Optionen** **Senden** (`request_source`) auf **Eine E-Mail pro Tabellenzeile** (`table`) fest und wählen Sie eine **Treibertabelle** (`driver_table`), um für jede Zeile einer Tabelle eine E-Mail statt einer einzelnen E-Mail zu senden. **Höchstzahl zu sendender Zeilen** (`row_limit`) begrenzt die verwendeten Zeilen und beträgt standardmäßig 10.000. Der Treiber muss eine Tabelle sein, keine Ansicht.

Verwenden Sie `{{row.column}}` in den Adressen, im Betreff, in der Nachricht und im Anhangspfad, um den Wert der jeweiligen Zeile einzusetzen. Eine Spalte, die die Treibertabelle nicht hat, lässt den Schritt fehlschlagen. Eine Zeile ohne An-Adresse sendet für diese Zeile nichts, und der Schritt endet mit einer Warnung, die sie benennt.

Ein aus einer Zeile befüllter Anhangspfad (`{{row.column}}`) muss eine einzelne vorhandene Datei sein, niemals ein Ordner, damit eine Zeile mit falsch ermitteltem Pfad nicht die Dateien einer anderen Person versenden kann. Eine Zeile, deren Wert für diesen Pfad leer ist, deren Pfad mit `..` aus seinem Ordner herausführt oder deren Datei fehlt, wird ohne den Anhang gesendet, mit einer Warnung, die die Zeile benennt. Der Versand pro Zeile erfordert einen Klartext-Body und ist mit einem Jinja-Vorlagen-Body nicht verfügbar.

### Nachricht


Geben Sie **Betreff** und **Body** nach Wunsch an.



Bitte beachten Sie, dass sowohl Projektvariablen als auch Workflow-Variablen in dieser Transformation verwendet werden können, sowohl in der Betreffzeile als auch im Nachrichtentext.



Zusätzlich ist im Body Standard-HTML-Code zulässig, um das Aussehen der E-Mail-Nachrichten weiter anzupassen.


### Anhänge


Das Anhängen von Dateien an E-Mails ist sehr einfach. Wählen Sie eine Datei oder einen Ordner aus Document zum Anhängen aus. Wird ein Ordner ausgewählt, wird der Inhalt des Ordners als einzelne Dateien angehängt. Die Variablensubstitution funktioniert mit Pfaden, um beim Versand personalisierter E-Mails die Dateianhänge besser zu steuern.



Um mehrere Dokumente anzuhängen, aktivieren Sie **Anhang zur E-Mail hinzufügen** und führen Sie sie unter **Weitere Anhänge** (`attachments`) in **Weitere E-Mail-Optionen** auf, jeweils mit einer **Konto-ID** und einem **Dokumentpfad**; sie werden zusammen mit dem von Ihnen ausgewählten Anhang gesendet, und ein Pfad kann Variablen und Zeilen-Token auf dieselbe Weise verwenden.

### Priorität und Nur-Text

Unter **Weitere E-Mail-Optionen** markiert **Priorität** (`priority`) die Nachricht als **Niedrig**, **Normal** oder **Hoch** (`low`, `normal`, `high`), und **Senden als** (`content_type`), auf **Nur-Text** (`text`) gesetzt, sendet den Body als reinen Text statt als **HTML** (`html`, der Standard).

### Body (Jinja-Vorlage)


Der Body des Schritts wird als **Jinja-Vorlage** verfasst, die über einem oder mehreren **Frames** gerendert wird und eine umfangreiche HTML-E-Mail erzeugt. Jeder Frame ist eine benannte Auswahl aus einer einzelnen Tabelle – ein Frame-Name, eine Workflow-Tabelle sowie optional Spaltenauswahl, ein Where-Filter und Aggregation (keine Joins). Der Editor öffnet sich direkt in dieser Vorlage – mit der Frame-Liste, dem Vorlagen-Body, einer Live-Vorschau und einer Schaltfläche **Test an mich senden** –, ohne Umschalter zwischen Nur-Text und Vorlage. Eine Schaltfläche **Formatieren** und eine Einfügepalette (`render_table(...)` für einen Frame, `{{ cloud }}`, eine for-Schleife sowie die Filter für Währung, Tausendertrennzeichen, Prozent und Datum) helfen beim Gestalten der Vorlage.

Verweisen Sie in der Vorlage auf jeden Frame als `frames['<Frame Name>'].rows` und `frames['<Frame Name>'].columns`; eine Vorlage mit nur einem Frame kann die obersten `rows` / `columns` verwenden, die an den ersten Frame gebunden sind. Die Vorlage ist eine separate Rendering-Engine in einer Sandbox – nur `cloud` wird als Workspace-Wert aufgelöst, und die veralteten Token `{project}` / `{model}` / `{date}` werden darin nicht aufgelöst. Vor der Jinja-Erstellung angelegte Schritte öffnen sich mit ihrem automatisch konvertierten alten Body; ein Body, der sich nicht sicher konvertieren lässt, bleibt in einem Nur-Text-Fallback und wird weiterhin mit der alten `{token}`-Substitution gesendet. Unter [Vorlagenbasierte HTML-E-Mail-Benachrichtigungen senden](/de/guides/workflows/notify-email-templates/) finden Sie die verfügbaren Vorlagenvariablen, den Helfer `render_table`, die HTML-Tags und -Attribute, die den E-Mail-Sanitizer überstehen, und wie vorhandene Bodys migriert werden.



## Beispiele


In diesem Beispiel werden alle Systemvariablen verwendet. Zusätzlich wird ein wenig HTML verwendet, um die erste Zeile des Body zu formatieren. Die Ausführung dieser Transformation sendet die folgende E-Mail:


* AN: [info@tartansolutions.com](mailto:info%40tartansolutions.com)
* VON: [info@tartansolutions.com](mailto:info%40tartansolutions.com) (beachten Sie, dass alle Nachrichten von dieser Adresse kommen)
* Betreff: DEMO – Workflow Analyze Demo Running
