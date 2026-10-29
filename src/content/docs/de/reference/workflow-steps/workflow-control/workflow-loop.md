---
title: Workflow Loop-Schritt
description: Erstellt in einem PlaidCloud-Workflow-Schritt eine Schleife, die eine Menge von Werten durchläuft und Schritte für jedes Element der Sammlung wiederholt.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/workflow-loop.md
---

## Beschreibung

Führt einen Ziel-Workflow einmal pro Zeile eines Datensatzes aus und setzt vor jeder Iteration die Spaltenwerte der jeweiligen Zeile als Projektvariablen. Verwenden Sie dies, wenn ein parametrisierter Prozess mehrfach mit unterschiedlichen Eingaben ausgeführt werden soll – zum Beispiel „den Monatsabschluss für jede Geschäftseinheit in dieser Tabelle ausführen“ oder „diesen Bericht für jedes aufgeführte Quartal laden“.

Jede Schleifeniteration sieht die Variablen so, als wären sie manuell gesetzt worden. Der aufgerufene Workflow kann sie daher mit der Standardsyntax `\{variable_name}` in Ausdrücken, Filtern, Dateipfaden und Tabellennamen verwenden. Die Schleife läuft standardmäßig sequenziell; Iterationen werden nicht parallel ausgeführt.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 690 170" role="img" aria-label="Ein Workflow Loop über einen Datensatz mit den Zeilen Q1, Q2 und Q3. Die Spaltenwerte jeder Zeile werden zu Projektvariablen, dann wird der Ziel-Workflow ausgeführt – ein Durchlauf pro Zeile, nacheinander, nicht parallel." style="width:100%;max-width:690px;height:auto;">
  <defs><marker id="wl-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="50" width="120" height="74" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="74" y="44" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">Datensatz</text>
  <text x="74" y="76" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q1</text>
  <text x="74" y="96" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q2</text>
  <text x="74" y="116" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q3</text>
  <path d="M134 87 L178 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="180" y="63" width="140" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="250" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q1</text>
  <text x="250" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">Durchlauf 1</text>
  <path d="M320 87 L360 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="362" y="63" width="140" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="432" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q2</text>
  <text x="432" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">Durchlauf 2</text>
  <path d="M502 87 L542 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="544" y="63" width="138" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="613" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q3</text>
  <text x="613" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">Durchlauf 3</text>
  <text x="408" y="142" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">sequenziell – ein Durchlauf nach dem anderen, nicht parallel</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Die Spalten jeder Zeile werden zu Projektvariablen, dann wird der Ziel-Workflow ausgeführt – ein Durchlauf pro Zeile, nacheinander. Für eine isolierte, parallele Auffächerung verwenden Sie stattdessen ein <a href="/de/guides/workflows/create-a-macro/">Makro</a>.</figcaption>
</figure>



## Zu beendender Workflow


Wählen Sie zunächst im Dropdown-Menü **Projekt** das Projekt aus, das den Workflow enthält, der bei jedem Schleifendurchlauf ausgeführt wird.



Wählen Sie anschließend im Dropdown-Menü **Workflow** den Workflow aus, der ausgeführt werden soll.

## Wenn eine Iteration fehlschlägt

Standardmäßig hält die Schleife bei der ersten Iteration an, deren Workflow fehlschlägt, und der Schritt schlägt fehl. Wählen Sie unter **Fehlerbehandlung** die Option **Nach fehlgeschlagener Iteration fortfahren**, um jede Iteration auszuführen, auch wenn eine fehlschlägt. Jeder Fehler wird zusammen mit dem Ergebnis jeder Iteration in **Schleifenausführungsstatus** festgehalten, und der Schritt endet mit einer Warnung, die angibt, wie viele Iterationen fehlgeschlagen sind. Ist die Option deaktiviert, hält die Schleife beim ersten Fehler an.

## Beispiele

Beispiele folgen in Kürze
