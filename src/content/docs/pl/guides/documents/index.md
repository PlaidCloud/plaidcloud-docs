---
title: Zarządzanie plikami
description: Zarządzaj kontami magazynu plików w PlaidCloud, aby importować i eksportować dane w formatach CSV, Excel, Parquet i innych.
sidebar:
  label: Przegląd
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/index.md
---

PlaidCloud Documents — przechowuj, porządkuj, wyszukuj i udostępniaj pliki razem z danymi i przepływami pracy. Dokumenty mogą pochodzić z dowolnego połączonego konta magazynu i być używane w przepływach pracy.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 200" role="img" aria-label="Połączone konta magazynu, takie jak S3, Google Cloud Storage i OneDrive, zasilają moduł PlaidCloud Documents, w którym pliki są przechowywane, porządkowane, wyszukiwane i udostępniane. Kroki przepływu pracy korzystają następnie z tych plików, aby importować i eksportować dane." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="dc-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">konta magazynu</text>
  <rect x="16" y="40" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="60" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">S3</text>
  <rect x="16" y="82" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Cloud Storage</text>
  <rect x="16" y="124" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="144" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">OneDrive</text>
  <path d="M136 55 C186 55 206 92 246 96" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 97 L246 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 139 C186 139 206 108 246 104" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="248" y="70" width="180" height="64" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="338" y="96" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Dokumenty</text>
  <text x="338" y="115" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">przechowuj · porządkuj · szukaj · udostępniaj</text>
  <path d="M428 102 L510 102" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="512" y="76" width="152" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="588" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">kroki przepływu pracy</text>
  <text x="588" y="118" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">import · eksport plików</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Pliki trafiają do modułu Documents z dowolnego połączonego konta magazynu, gdzie można je przechowywać, porządkować, wyszukiwać i udostępniać — a następnie używać ich w krokach przepływu pracy do importowania i eksportowania danych.</figcaption>
</figure>

## Obszar roboczy Dokument

Moduł **Dokument** otwiera się z paskiem bocznym po lewej stronie i wybraną stroną obok niego. Pasek boczny grupuje strony w sekcje **Dokumenty** (**Przegląd** i **Przeglądaj**) oraz **Konta** (**Twoje konta** i **Zarządzanie**). Członkowie, którzy nie mogą otworzyć danej strony, nie widzą jej pozycji. Strony mają tytuł u góry, często z krótkim podtytułem, a ich akcje znajdują się w nagłówku obok niego.

| Pozycja paska bocznego | Co pokazuje |
|---|---|
| **Przegląd** | Kafelki Twoich kont (**Konta** — otwiera **Twoje konta**, **Zarządzane zasobniki**, **Usługi zewnętrzne** i **Wyłączone** — oznaczony jako **Wymaga uwagi** i otwierający **Zarządzanie**, gdy konto, którego jesteś właścicielem, jest wyłączone), **Przypięte** pliki, **Konta według usługi** i **Kto może z nich korzystać**. Wybierz przypięty plik, aby otworzyć widok **Przeglądaj** w jego folderze z zaznaczonym plikiem. |
| **Przeglądaj** | Eksplorator plików. Otwiera Twoje ulubione konto (to, którego folder główny został przypięty) lub domyślne konto obszaru roboczego, a inne konto możesz wybrać z listy w nagłówku strony. Zobacz [Korzystanie z kont dokumentów](/pl/guides/documents/using-document/). |
| **Twoje konta** | Każde konto, z którego możesz korzystać, na jednej liście. Plakietka **Udostępnione** lub **Prywatne** w każdym wierszu informuje, czy konto jest Ci udostępnione, czy należy tylko do Ciebie. Kliknij dwukrotnie wiersz, aby go przeglądać. |
| **Zarządzanie** | Konta, których jesteś właścicielem, z kolumnami **Nazwa**, **Usługa**, **Typ zabezpieczeń**, **Stan** i **Opis**. Administrator obszaru roboczego widzi tu każde konto dokumentów i może zarządzać każdym kontem, którym może zarządzać także w inny sposób; konta zarządzane przez system są odrzucane, a kont zarządzanego zasobnika nie można klonować. |

Pasek boczny pokazuje licznik obok pozycji **Twoje konta**. Widok Przegląd zawiera przyciski **Przeglądaj pliki** i **Nowe konto** umożliwiające szybki start.

### Akcje wiersza w widoku Zarządzanie

Otwórz menu **⋯** wiersza, kliknij wiersz prawym przyciskiem myszy lub użyj menu **Akcje** na pasku narzędzi, aby uzyskać dostęp do następujących opcji:

- **Otwórz** i **Edytuj**, które otwierają stronę konta.
- **Klonuj…**, **Historia wersji** i **Gdzie używane…**. Zobacz [Miejsca użycia i zmiana wskazania](/pl/guides/documents/account-management/document-account-used-by/).
- **Kto może używać**, z pozycjami **Członkowie**, **Grupy**, **Agenci** i **Właściciele**. Zobacz [Kontrola dostępu do konta dokumentów](/pl/guides/documents/account-management/control-document-account-access/).
- **Włącz** lub **Wyłącz** oraz **Usuń**.

### Strona konta

**Nowe konto**, **Otwórz** i **Edytuj** wyświetlają konto jako stronę, z przyciskiem **Zarządzaj kontami** u góry umożliwiającym powrót. Strona zawiera karty:

- **Ogólne**: nazwa konta, usługa, zasobnik i ścieżka początkowa.
- **Dostęp**: model zabezpieczeń i osoby, które mogą korzystać z konta. Pozycje **Członkowie**, **Grupy**, **Agenci** i **Właściciele** mają link **Edytuj**, który otwiera ten sam selektor co menu wiersza.
- **Poświadczenia**: pola tylko do zapisu dla wybranej usługi. Informacja **Poświadczenia zapisane** oznacza, że poświadczenia są ustawione; zapisane wartości nigdy nie są wyświetlane. Pozostaw pole puste, aby zachować zapisaną wartość. Konta SFTP mają też opcję **Testuj połączenie**.
- **SSH**: ustawienia klucza, tylko dla kont SFTP.

Nagłówek zawiera opcje **Przeglądaj**, **Gdzie używane** oraz menu **Akcje** z pozycjami **Klonuj**, **Historia wersji**, **Włącz** lub **Wyłącz** i **Usuń**. Jeśli opuścisz stronę z niezapisanymi zmianami, PlaidCloud zapyta, czy je odrzucić.

Stare linki i zakładki do ekranów dokumentów nadal otwierają odpowiednią stronę.
