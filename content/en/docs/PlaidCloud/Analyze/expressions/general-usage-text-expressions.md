---
title: General Usage Text Expressions
slug: general-usage-text-expressions
weight: 7.0
description: Commonly Used Text Expressions
date: 2022-01-25T07:39:53
---

## Commonly Used Text Expressions
| Analyze Expression | Return Type | Description | Example | Result |
|--------------------|-------------|-------------|---------|--------|
| func.concat(string, string) | text | String concatenation | concat(‘Post’, ‘greSQL’) | PostgreSQL |
| func.bit_length(stri ng) | int | Number of bits in string | bit_length(‘jose’) | 32 |
| func.char_length(str ing) or func.character_length(string) | int | Number of characters in string | char_leng th(‘jose’) | 4 |
| func.convert(string using conversion_name) | text | Change encoding using specified conversion name. Conversions can be defined by CREATE CONVERSION. Also there are some pre-defined conversion names. SeeTable 9-7for available conversion names. | convert(‘P ostgreSQL’ using iso_8859_1_to_ut f8) | PostgreSQ L’ in UTF8 (Unicode, 8-bit) encoding |
| func.lower(string) | text | Convert string to lower case | lower(‘TOM ‘) | tom |
| func.octet_length(st ring) | int | Number of bytes in string | octet_length(‘jose’ ) | 4 |
| func.overlay(string placing string from int [forint]) | text | Replace substring | overlay(‘Txxxxas’ placing ‘hom’ from 2 for 4) | Thomas |
| func.position(substring in string) | int | Location of specified substring | position(‘om’ in ‘Thomas’) | 3 |
| func.substring(string [from int] [for int]) | text | Extract substring | substring( ‘Thomas’ from 2 for 3) | hom |
| func.substring(string frompattern) | text | Extract substring matching POSIX regular expression. | substring( ‘Thomas’ from ‘…$’) | mas |
| func.substring(string frompatternforescape) | text | Extract substring matching SQL regular expression. | substring( ‘Thomas’ from ‘%#”o_a#” _’ for ‘#’) | oma |
| func.trim([leading, trailing, both] [characters] from string) | text | Remove the longest string containing only the characters (a space by default) from the start/end/both ends of the string | trim(both ‘x’ from ‘xTomxx’) | Tom |
| func.upper(string) | text | Convert string to uppercase | upper(‘tom ‘) | TOM |
| func.ascii(string) | int | ASCII code of the first byte of the argument | ascii(‘x’) | 120 |
| func.btrim(string text [, characters text]) | text | Remove the longest string consisting only of characters in characters (a space by default) from the start and end of string | btrim(‘xyx trimyyx’, ‘xy’) | trim |
| func.chr(int) | text | Character with the given ASCII code | chr(65) | A |
| func.convert(string text, [src_encoding name,]dest_encoding name) | text | Convert string to dest_encoding . The original encoding is specified by src_encoding. If src_encoding is omitted, database encoding is assumed. | convert( ‘text_in_utf8’, ‘UTF8’, ‘LATIN1’) | text_in_utf8 represent ed in ISO 8859-1 encoding |
| func.decode(string text, type text) |  | Decode binary data from string previously encoded with encode. Parameter type is same as in encode. |  |  |
| func.decode(string text, type text) | bytea | Decode binary data from string previously encoded with encode. Parameter type is same as in encode. |  |  |
| func.initcap(string) | text | Convert the first letter of each word to uppercase and the rest to lowercase. Words are sequences of alphanumeric characters separated by non-alphanumer ic characters. | initcap(‘hi THOMAS’) | Hi Thomas |
| func.length(string) | int | Number of characters in string | length(‘jose’) | 4 |
| func.lpad(string text, length int [, fill text]) | text | Fill up the string to length length by prepending the characters fill (a space by default). If the string is already longer than length then it is truncated (on the right). | lpad(‘hi’, 5, ‘xy’) | xyxhi |
| func.ltrim(string text [, characters text]) | text | Remove the longest string containing only characters from characters (a space by default) from the start of string | ltrim(‘zzz ytrim’, ‘xyz’) | trim |
| func.md5(string) | text | Calculates the MD5 hash of string, returning the result in hexadecimal | md5(‘abc’) | 900150983 cd24fb0 d6963f7d2 8e17f72 |
| func.quote_literal(s tring) | text | Return the given string suitably quoted to be used as a string literal in an SQL statement string. Embedded single-quotes and backslashes are properly doubled. | quote_lit eral( ‘O’Reilly’ ) | O’’Reilly ‘ |
| func.regexp_replace( string text, pattern text,replacement text [,flags text]) | text | Replace substring matching POSIX regular expression. SeeSection 9.7for more information on pattern matching. | regexp_re place(‘Tho mas’, ‘.[mN]a.’, ‘M’) | ThM |
| func.repeat(string text, number int) | text | Repeat string the specified number of times | repeat(‘Pg ‘, 4) | PgPgPgPg |
| func.replace(string text, from text, to text) | text | Replace all occurrences in string of substring from with substring to | replace( ‘abcdefabc def’, ‘cd’, ‘XX’) | abXXefabX Xef |
| func.rpad(string text, length int [, fill text]) | text | Fill up the string to length length by appending the characters fill (a space by default). If the string is already longer than length then it is truncated. | rpad(‘hi’, 5, ‘xy’) | hixyx |
| func.rtrim(string text [, characters text]) | text | Remove the longest string containing only characters from characters (a space by default) from the end of string | rtrim(‘trimxxxx’, ‘x’) | trim |
| func.split_part(stri ng text, delimiter text, field int) | text | Split string on delimiter and return the given field (counting from one) | split_par t(‘abc:s ub:@de f@ `ghi’, ‘:sub:`@’ , 2) | def |
| func.strpos(string, substring) | int | Location of specified substring (same as position(subst ring in string), but note the reversed argument order) | strpos(‘hi gh’, ‘ig’) | 2 |
| func.substr(string, from [, count]) | text | Extract substring (same as substring(stri ng from from for count)) | substr(‘al phabet’, 3, 2) | ph |
| func.to_ascii(string text [, encoding text]) | text | Convert string to ASCII from another encoding (only supports conversion from LATIN1, LATIN2, LATIN9, and WIN1250 encodings) | to_ascii( ‘Karel’) | Karel |
| func.to_hex(number int or bigint) | text | Convert number to its equivalent hexadecimal representation | to_hex(21 47483647) | 7fffffff |
| func.translate(string text, from text, to text) | text | Any character in the string that matches a character in the from set is replaced by the corresponding character in the to set | translate( ‘12345’, ‘14’, ‘ax’) | a23x5 |
