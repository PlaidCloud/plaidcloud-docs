---
title: Datenverwaltung – Dimensionen
description: Verwalten Sie hierarchische Datendimensionen in PlaidCloud, einschließlich Attributen, Alternativhierarchien, Eigenschaften und berechneten Werten.
sidebar:
  label: Übersicht
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dimensions/index.md
---

Dimensionen sind Hierarchien, mit denen Sie Daten aufteilen und aggregieren – Kostenstellen, Produkte, Geografie, Zeiträume. Dieser Abschnitt behandelt die Verwaltung von Attributen, Alternativhierarchien, Eigenschaften und berechneten Werten.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 640 250" role="img" aria-label="Eine Geografiedimension als Baum dargestellt. Die Wurzel Gesamt hat zwei Kindknoten, Nord und Süd. Nord hat die Blattmitglieder NY und MA; Süd hat die Blattmitglieder TX und FL. Blattwerte werden über die Eltern bis zur Wurzel aggregiert." style="width:100%;max-width:640px;height:auto;">
  <defs><marker id="dm-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <path d="M320 54 L175 96" stroke="var(--sl-color-gray-5)" stroke-width="1.4" fill="none" />
  <path d="M320 54 L465 96" stroke="var(--sl-color-gray-5)" stroke-width="1.4" fill="none" />
  <path d="M175 132 L90 176" stroke="var(--sl-color-gray-5)" stroke-width="1.4" fill="none" />
  <path d="M175 132 L260 176" stroke="var(--sl-color-gray-5)" stroke-width="1.4" fill="none" />
  <path d="M465 132 L380 176" stroke="var(--sl-color-gray-5)" stroke-width="1.4" fill="none" />
  <path d="M465 132 L550 176" stroke="var(--sl-color-gray-5)" stroke-width="1.4" fill="none" />
  <rect x="270" y="20" width="100" height="36" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="320" y="43" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">Gesamt</text>
  <rect x="125" y="96" width="100" height="36" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="175" y="119" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Nord</text>
  <rect x="415" y="96" width="100" height="36" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="465" y="119" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Süd</text>
  <rect x="50" y="176" width="80" height="32" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="90" y="197" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">NY</text>
  <rect x="220" y="176" width="80" height="32" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="260" y="197" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">MA</text>
  <rect x="340" y="176" width="80" height="32" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="380" y="197" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">TX</text>
  <rect x="510" y="176" width="80" height="32" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="550" y="197" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">FL</text>
  <path d="M615 200 L615 40" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" marker-end="url(#dm-arrow)" />
  <text x="628" y="124" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)" transform="rotate(-90 628 124)">Werte werden aggregiert</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Eine Dimension ist eine Hierarchie. Blattwerte werden über die Elternknoten bis zur Wurzel aggregiert – derselbe Baum dient sowohl der Aufteilung als auch der Aggregation. Alternativhierarchien gruppieren dieselben Blätter auf andere Weise.</figcaption>
</figure>
