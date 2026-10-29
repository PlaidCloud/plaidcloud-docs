---
title: Dimensionen laden und entladen
description: Laden und entladen Sie Dimensionsdaten in PlaidCloud, einschließlich Massenimporten, Datenaktualisierung und Synchronisierung mit externen Datenquellen.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dimensions/loading-unloading.md
---

Dimensionen können aus Workflow-Vorgängen heraus durch das Laden von Daten gepflegt werden. Außerdem lassen sich Dimensionsdaten in tabellarische Daten abflachen und in Tabellen speichern. Das ist oft nützlich, um Berichts- und Analysedaten anzureichern.


## Dimensionen laden

Da Dimensionen hierarchische Datenstrukturen darstellen, muss der Ladevorgang die Beziehungen in den Daten vermitteln. PlaidCloud unterstützt zwei verschiedene Datenstrukturen zum Laden von Dimensionen:
 * Eltern-Kind – Die Daten sind vertikal organisiert, wobei eine Spalte *Eltern* und eine Spalte *Kind* jedes Elternelement eines Kindes in der gesamten Struktur festlegen
 * Ebenen – Die Daten sind horizontal organisiert, wobei jede Spalte von links nach rechts eine Ebene der Hierarchie darstellt

 Zusätzlich zur Struktur können weitere Dimensionsinformationen in den Ladevorgang einbezogen werden, etwa Werte, Aliase und Eigenschaften.

 Ein Ebenenladevorgang (flach) verwendet eine Standardkonsolidierung, die jeder vom Ladevorgang erzeugte Zwischenknoten erhält, und kann eine Blattspalte benennen: Wenn er das tut, bestimmt diese Spalte, welcher Knoten die Aliase, Eigenschaften und Werte der Zeile trägt; andernfalls ist die zuletzt gefüllte Ebene das Blatt.

 Der Standard-Konsolidierungstyp eines Eltern-Kind-Ladevorgangs gilt für jede Zeile, deren eigene Konsolidierung leer oder nicht erkannt ist, und muss daher einer der gültigen Typen sein, auch wenn die Tabelle zusätzlich eine Konsolidierungsspalte benennt. Die Hierarchie, auf die ein Ladevorgang zielt, darf nicht denselben Namen tragen wie eine Spalte, die der Ladevorgang zuordnet: Eine Spalte mit diesem Namen wird als die Hierarchie gelesen, zu der jede Zeile gehört. Ein Ladevorgang, der beides benennt, wird daher abgelehnt, statt einer Lesart zu folgen und die andere zu ignorieren.

 Ein Ladevorgang von Aliasen, Eigenschaften oder Werten prüft das Mitglied jeder Zeile, bevor irgendetwas geschrieben wird. Benennt eine Zeile ein Mitglied, das die Dimension nicht enthält, schlägt der Ladevorgang fehl und meldet diese Namen, und nichts aus diesem Ladevorgang wird gespeichert. Laden Sie zuerst die Struktur oder nehmen Sie die fehlenden Mitglieder darin auf und laden Sie dann die Attribute.

 Weitere Informationen finden Sie beim Workflow-Schritt [Dimension Load](/de/reference/workflow-steps/dimensions/dimension-load).


## Dimensionen entladen (exportieren)

Der Export von Dimensionen in Tabellen unterstützt zwei strukturelle Ansätze:
 * Eltern-Kind – Die Daten sind vertikal organisiert, wobei eine Spalte *Eltern* und eine Spalte *Kind* jedes Elternelement eines Kindes in der gesamten Struktur festlegen
 * Ebenen – Die Daten sind horizontal organisiert, wobei jede Spalte von links nach rechts eine Ebene der Hierarchie darstellt

Eigenschaften und Werte können ebenfalls in die abgeflachten tabellarischen Daten aufgenommen werden.

 Weitere Informationen finden Sie beim Workflow-Schritt [Dimension Export](/de/reference/workflow-steps/dimensions/dimension-export).
