---
title: Pulpity
description: Twórz i dostosowuj pulpity PlaidCloud, aby wizualizować dane za pomocą interaktywnych wykresów, diagramów i dynamicznych wyświetlaczy metryk.
sidebar:
  label: Pulpity
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dashboards/index.md
---

Buduj interaktywne pulpity na danych projektów PlaidCloud — wykresy, metryki, kolumny obliczeniowe, dynamiczne filtry i osadzona eksploracja danych.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 200" role="img" aria-label="Opublikowane tabele i widoki projektu zasilają elementy składowe pulpitu — wykresy, kafelki metryk i dynamiczne filtry — które składają się w jeden interaktywny pulpit do eksploracji przez członków obszaru roboczego." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="db-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="16" y="74" width="140" height="56" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="86" y="98" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">opublikowane dane</text>
  <text x="86" y="116" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">tabele i widoki</text>
  <path d="M156 102 C196 102 206 66 244 66" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#db-arrow)" />
  <path d="M156 102 L244 102" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#db-arrow)" />
  <path d="M156 102 C196 102 206 138 244 138" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#db-arrow)" />
  <rect x="246" y="48" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="311" y="69" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">wykresy</text>
  <rect x="246" y="86" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="311" y="107" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">kafelki metryk</text>
  <rect x="246" y="124" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="311" y="145" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">dynamiczne filtry</text>
  <path d="M376 103 L436 103" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#db-arrow)" />
  <rect x="438" y="60" width="150" height="86" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="513" y="98" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Pulpit</text>
  <text x="513" y="116" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">interaktywny</text>
  <path d="M588 103 L636 103" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#db-arrow)" />
  <text x="654" y="99" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">członkowie</text>
  <text x="654" y="114" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">eksplorują</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Opublikowane tabele i widoki zasilają wykresy, kafelki metryk i dynamiczne filtry, które składają się w jeden interaktywny pulpit do eksploracji przez członków.</figcaption>
</figure>
