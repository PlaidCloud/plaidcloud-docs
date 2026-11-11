---
title: Zarządzanie plikami
description: Zarządzaj kontami magazynu plików w PlaidCloud na potrzeby importowania i eksportowania danych w formatach CSV, Excel, Parquet i innych.
sidebar:
  label: Przegląd
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/index.md
---

PlaidCloud Dokumenty — przechowuj, porządkuj, przeszukuj i udostępniaj pliki razem z danymi i przepływami pracy. Dokumenty mogą pochodzić z dowolnego podłączonego konta magazynu i być przywoływane w przepływach pracy.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 200" role="img" aria-label="Podłączone konta magazynu, takie jak S3, Google Cloud Storage i OneDrive, zasilają PlaidCloud Dokumenty, gdzie pliki są przechowywane, porządkowane, przeszukiwane i udostępniane. Kroki przepływu pracy odwołują się następnie do tych plików, aby importować i eksportować dane." style="width:100%;max-width:680px;height:auto;">
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
  <text x="338" y="115" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">przechowuj · porządkuj · przeszukuj · udostępniaj</text>
  <path d="M428 102 L510 102" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="512" y="76" width="152" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="588" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">kroki przepływu pracy</text>
  <text x="588" y="118" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">import · eksport plików</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Pliki trafiają do Dokumentów z dowolnego podłączonego konta magazynu, gdzie je przechowujesz, porządkujesz, przeszukujesz i udostępniasz — a następnie odwołujesz się do nich z kroków przepływu pracy, aby importować i eksportować dane.</figcaption>
</figure>

## Obszar roboczy Dokumenty

**Dokument** otwiera się z paskiem bocznym po lewej stronie i wybraną obok niego stroną. Pasek boczny grupuje swoje strony w sekcjach **Dokumenty** (**Przegląd** i **Przeglądaj**) oraz **Konta** (**Your accounts** i **Zarządzanie**). Członkowie, którzy nie mogą otworzyć danej strony, nie widzą jej pozycji. Każda strona ma u góry tytuł i krótki podtytuł, a jej akcje znajdują się w nagłówku obok nich.

| Pozycja paska bocznego | Co pokazuje |
|---|---|
| **Przegląd** | Kafelki dla Twoich kont (**Konta**, **Shared**, **Private to you**, **Managed buckets**, **External services** oraz **Wyłączone**, gdy konto wymaga uwagi), **Pinned** pliki, **Accounts by service** i **Who can use them**. Wybierz przypięty plik, aby otworzyć **Przeglądaj** w jego folderze z zaznaczonym plikiem. |
| **Przeglądaj** | Eksplorator plików. Otwiera Twoje ulubione konto (to, którego folder główny został przypięty), lub domyślne konto obszaru roboczego, a inne konto możesz wybrać z listy w nagłówku strony. Zobacz [Korzystanie z kont dokumentów](/pl/guides/documents/using-document/). |
| **Your accounts** | Wszystkie konta, z których możesz korzystać, na jednej liście. Etykieta **Shared** lub **Prywatne** w każdym wierszu informuje, czy konto jest Ci udostępnione, czy jest tylko Twoje. Kliknij wiersz dwukrotnie, aby je przeglądać. |
| **Zarządzanie** | Konta, których jesteś właścicielem, z kolumnami **Nazwa**, **Usługa**, **Security type**, **Stan** i **Opis**. Administrator obszaru roboczego widzi tu każde konto dokumentów i może zarządzać każdym kontem, którym mógłby zarządzać w inny sposób; konta zarządzane przez system są odrzucane, a kont z zarządzanymi zasobnikami nie można klonować. |

Pasek boczny pokazuje licznik obok **Your accounts** i **Zarządzanie**. Dla administratora obszaru roboczego, który ma konta, których nie jest właścicielem, **Zarządzanie** pokazuje **admin** zamiast licznika. Strona Przegląd ma przyciski **Przeglądaj pliki** i **Nowe konto** do szybkiego startu.

### Akcje wiersza w sekcji Zarządzanie

Otwórz menu **⋯** wiersza, kliknij wiersz prawym przyciskiem myszy lub użyj menu **Akcje** na pasku narzędzi, aby uzyskać:

- **Otwórz** i **Edytuj**, które otwierają stronę konta.
- **Klonuj…**, **Version history** i **Gdzie używane…**. Zobacz [Gdzie używane i zmiana wskazania](/pl/guides/documents/account-management/document-account-used-by/).
- **Who can use it**, z opcjami **Członkowie**, **Grupy**, **Agenci** i **Właściciele**. Zobacz [Kontrola dostępu do konta dokumentów](/pl/guides/documents/account-management/control-document-account-access/).
- **Włącz** lub **Disable**, oraz **Usuń**.

### Strona konta

**Nowe konto**, **Otwórz** i **Edytuj** pokazują konto jako stronę, z opcją **Zarządzaj kontami** u góry, aby wrócić. Zawiera ona karty:

- **Ogólne**: nazwa konta, usługa, zasobnik i ścieżka początkowa.
- **Dostęp**: model zabezpieczeń i osoby, które mogą korzystać z konta. **Członkowie**, **Grupy**, **Agenci** i **Właściciele** mają każdy łącze **Edytuj**, które otwiera ten sam selektor co menu wiersza.
- **Credentials**: pola tylko do zapisu dla wybranej usługi. Informacja **Credentials saved** pokazuje, że poświadczenia są ustawione, a zapisane wartości nigdy nie są wyświetlane. Pozostaw pole puste, aby zachować zapisaną wartość. Konta SFTP mają także **Testuj połączenie**.
- **SSH**: ustawienia kluczy tylko dla kont SFTP.

W nagłówku znajdują się **Przeglądaj**, **Gdzie używane** oraz menu **Akcje** z opcjami **Klonuj**, **Version history**, **Włącz** lub **Disable** oraz **Usuń**. Jeśli opuścisz stronę z niezapisanymi zmianami, PlaidCloud zapyta, czy je odrzucić.

Stare łącza i zakładki do ekranów dokumentów nadal otwierają odpowiednią stronę.
