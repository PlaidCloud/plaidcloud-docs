---
title: Document Text Substitution (krok)
description: Wykonuj podstawienia tekstu typu znajdź i zamień w dokumentach w kroku przepływu pracy PlaidCloud, aby automatycznie przekształcać treść.
sidebar:
  order: 15
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/document-text-substitution.md
---

## Opis

Znajdź i zamień wewnątrz pliku tekstowego. Zastępuj określone ciągi lub symbole zastępcze nowymi wartościami — przydatne w szablonowaniu (zastąpienie symbolu zastępczego, takiego jak `CUSTOMER_NAME`, rzeczywistą nazwą) lub w oczyszczaniu tekstu (usuwanie lub zaciemnianie określonych ciągów).

Działa na plikach tekstowych UTF-8 (TXT, CSV, JSON, XML, HTML, RML) o dowolnym rozmiarze. Plik, który nie jest tekstem UTF-8, taki jak PDF lub dokument pakietu Office, powoduje niepowodzenie kroku.

## Dane wejściowe

- **Plik lub katalog wejściowy** — plik lub folder z plikami do zmiany.
- **Plik lub katalog docelowy** — miejsce zapisu wyniku. Wynik jest zawsze zapisywany na koncie dokumentów danych wejściowych; miejsce docelowe określa ścieżkę.
- **Kompresja** — Bez kompresji, Zip, GZip, BZip2, Zstandard, LZ4, Snappy, LZO lub Deflate (zlib) dla danych wyjściowych. Snappy i LZ4 są zapisywane w formacie blokowym odczytywanym przez Spark i Hadoop, a LZO jako plik `lzop`.
- **Kolejność operacji zamiany tekstu** — jeden wiersz na zamianę, z oryginalnym tekstem i jego zamiennikiem. W zamienniku można używać zmiennych.

## Jak to działa

- Zamiany są wykonywane od góry do dołu, a każda działa na wyniku poprzednich — dlatego zamiana może zmienić tekst, który wstawił wcześniejszy wiersz.
- Dopasowanie jest dokładne i uwzględnia wielkość liter, a zamieniane jest każde wystąpienie.
- Wiersz z pustym oryginalnym tekstem jest ignorowany.
- Dla folderu każdy plik jest zapisywany w folderze nazwanym jak miejsce docelowe, bez jego rozszerzenia, pod własną nazwą pliku.
- Jeśli ścieżka wejściowa nie istnieje lub nie zawiera plików, krok kończy się ostrzeżeniem ze wskazaniem ścieżki, niczego nie przetwarza, a przepływ pracy jest kontynuowany.

## Przykłady

| Oryginał | Zamiennik | `Dear CUSTOMER_NAME,` zmienia się w |
|---|---|---|
| `CUSTOMER_NAME` | `Acme Ltd` | `Dear Acme Ltd,` |
