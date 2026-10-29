---
title: REST 요청
description: 워크플로 단계에서 REST API를 호출합니다. Postman, OpenAPI 또는 HAR에서 엔드포인트를 가져오고 응답을 테이블이나 워크플로 변수로 보냅니다.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/rest-request.md
---

## 설명

**REST 요청** 단계는 REST API를 호출하고 응답을 대상 테이블이나 워크플로 변수로 보냅니다. 기존의 REST 방식 단계들을 Postman 스타일의 통합 단계 하나로 대체합니다. 엔드포인트(수동, Postman, OpenAPI/Swagger 또는 HAR)를 선택하고, 헤더/쿼리/본문을 편집하고, 테스트 요청을 보낸 다음 저장하면 됩니다.

전체 안내는 [REST 요청 단계 가이드](/ko/guides/workflows/rest-request-step/)를 참조하십시오.

편집하는 동안 브라우저는 단계의 로컬 초안을 보관합니다. 저장하기 전에 닫거나 새로 고치면, 단계를 다시 열 때 저장되지 않은 초안을 복원할지 묻습니다.

## 구성

### 요청

* **엔드포인트 소스** — `Manual`, `From the connection's API definition`, `Postman collection (file/URL)`, `OpenAPI / Swagger (URL/file)`, `HAR archive (file)` 중 하나입니다. **카탈로그 로드**를 사용하여 가져온 소스의 엔드포인트를 나열합니다. 엔드포인트를 선택하면 해당 메서드, URL, 헤더, 쿼리 매개변수, 본문이 채워지며, 요청을 이미 편집한 경우에는 먼저 확인을 요청합니다. 파일 소스 세 가지에는 **붙여넣기…** 도 있어서, 파일을 선택하는 대신 컬렉션이나 사양을 직접 입력할 수 있습니다.
* **연결** *(선택)* — 인증과 기본 URL을 위한 REST 연결입니다. 전체 URL을 직접 호출하려면 생략합니다. 선택기 옆의 편집 바로 가기는 선택한 연결 편집기를 열어 보거나 편집할 수 있게 합니다.
* **메서드** — `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`.
* **엔드포인트** — 경로(연결을 사용하는 경우) 또는 전체 URL입니다.
* **헤더** / **쿼리 매개변수** — 켜기/끄기 토글이 있는 이름/값 행입니다.
* **본문** — 요청 페이로드(JSON, 양식 또는 원시 데이터)입니다.
* **테스트 요청 보내기** / **curl로 복사** / **curl에서 가져오기** — 요청을 보내고 응답을 그 자리에서 확인하거나, 동등한 curl 명령을 복사하거나(비밀 값은 가려짐), curl 명령을 붙여넣어 메서드, URL, 헤더, 본문을 채웁니다.
* **보내기** — `One request`(기본값) 또는 드라이버 테이블 전체로 요청을 분산하는 `One request per table row`입니다.

테스트 요청 보내기가 성공하기 전에 나가는 요청의 변경 사항을 저장하면 확인을 요청합니다. 분산 모드에서는 **1행 테스트**가 성공해야 이 경고가 사라집니다.

**보내기**가 `One request per table row`이면 **드라이버 테이블**을 선택하고(테이블 선택기로 고르거나 이름을 입력) 엔드포인트, 쿼리, 헤더, 본문에 `{{row.column}}` 토큰을 사용하여 각 행의 값을 대입합니다. 엔드포인트와 본문의 변수 삽입 메뉴에는 선택한 드라이버 테이블의 열이 포함됩니다. 선택 사항으로 **드라이버 필터**(SQL `WHERE` 절), **키 열**(각 출력 행에 함께 기록), **행 제한**, **동시성**, **초당 최대 요청 수**(동시성과 별개로 모든 워커에서 요청이 시작되는 속도의 상한이며, 소수를 지원하므로 0.5는 2초마다 요청 하나를 보내고, 0은 제한 없음, 1000을 넘는 값은 경고와 함께 1000으로 제한됨), **Idempotency-Key 헤더 추가**(페이징 없는 단일 POST/PUT/PATCH에 행마다 고정된 `Idempotency-Key`를 보내 다시 실행해도 이중 생성되지 않게 하며, 그 외에는 경고와 함께 건너뜀), **오류 시 계속**(실패한 행을 기록하고 중단하는 대신 경고), **응답**(기본값은 `Parsed records`이고, `Text (one row per request)`는 각 응답을 `DownloadData`와 `DownloadHeaders` 열이 있는 행으로 기록하며, `Raw text, errors as rows`는 서버가 보낸 본문 그대로 같은 방식으로 기록하고 `DownloadStatus` 열을 추가하며 HTTP 또는 전송 오류를 행으로 유지하고 본문, 헤더, 오류 텍스트의 자격 증명은 가려짐)을 설정할 수 있습니다. **1행 테스트**는 첫 번째 드라이버 행에 대한 요청을 보내므로 실행하기 전에 분산 결과를 미리 볼 수 있습니다. 분산은 대상 테이블에 기록하며 변수로 캡처할 수 없습니다.

**응답**을 `Text (one row per request)`로 설정하면 분산 옵션이 두 가지 더 적용됩니다.

* **응답 본문** — `As returned`(기본값), HTML 페이지의 마크업 대신 보이는 텍스트를 `DownloadData`에 기록하는 `Visible page text`, 서버가 보낸 본문의 바이트를 그대로 base64로 인코딩하여 기록하는 `Raw bytes (Base64)`(파일 또는 기타 바이너리 응답용)가 있습니다.
* **응답이 일치하는 동안 폴링 계속** — 작업이 끝날 때까지 "아직 처리 중"이라고 응답하는 API를 위한 옵션입니다. **응답 경로**(전체 응답은 `$`, 이어서 `.name`, `[0]`, `['name']` 또는 `["name"]`), 연산자(`==`, `!=`, `<`, `<=`, `>`, `>=`), 유형이 있는 값(`Text`, `Number`, `True/False`, `Empty`)을 지정합니다. 응답이 일치하는 동안 각 행의 요청을 **N초**(1~600, 기본값 5)마다 **행당 M개 요청**(1~1000, 기본값 60)까지 다시 보내며, 마지막 요청 후에도 일치하는 행은 실패합니다.

base64 텍스트로 열에 저장된 파일이나 오디오 같은 바이너리 콘텐츠를 보내려면 **본문이 base64 텍스트임: 디코딩된 바이트 보내기**(`body_base64`)를 켭니다. 테이블 행마다 요청 하나를 보내는 경우, `{{row.column}}` 토큰을 채운 후의 본문을 base64 텍스트로 읽고 디코딩된 바이트를 보냅니다.

**텍스트 응답 옵션** 및 **로그인, 프록시 및 TLS** 섹션에는 다음 필드가 있습니다. 변환된 KNIME 워크플로도 이 필드를 사용합니다.

테이블 행마다 요청 하나를 보내고 **응답**을 `Text (one row per request)`로 설정한 경우:

* **각 응답의 HTTP 상태를 DownloadStatus 열로 추가**(`include_status`) — 각 응답의 HTTP 상태를 `DownloadStatus` 열로 추가합니다. **상태 열**(`status_column`)은 대신 해당 열의 이름을 지정하며, 이를 설정하면 열이 추가됩니다.
* **실패한 요청의 행을 DownloadStatus와 DownloadError와 함께 유지**(`keep_error_rows`) — 실패한 요청의 행을 유지하되 본문은 비어 있고 `DownloadStatus`와 `DownloadError`가 채워집니다.
* **실패한 요청의 행 유지**(`keep_failed_rows`) — HTTP 400 이상으로 응답한 요청은 상태, 응답 헤더, `DownloadError`의 오류 본문과 함께 행을 유지하고, 응답이 없는 요청은 키 열만 유지합니다. **오류 시 계속**이 꺼져 있으면 실패는 여전히 단계를 중단합니다. **응답 상태에 따라 단계 실패**(`fail_on_status`)는 단계를 실패시키는 `5xx` 같은 상태 계열을 나열하며, 그 밖의 계열의 응답은 행으로 유지됩니다.
* `document` *(AI 어시스턴트 또는 REST API로 설정)* — 각 응답을 이 문서 폴더 `{account, path, file_name}`에 파일로 저장합니다. `file_name`의 기본값은 URL의 마지막 세그먼트입니다. 행에는 본문 대신 `FilePath`가 들어갑니다.
* **본문을 웹 페이지 문서로 기록**(`html_document`) — 각 본문을 정규화된 HTML 문서(`html`) 또는 XML 형태(`xml`)로 기록합니다. **상대 href 및 src 값을 절대 값으로 변환**(`html_absolute_urls`, 기본값 true)은 상대 `href` 및 `src` 값을 요청 URL을 기준으로 한 절대 값으로 만듭니다.
* **첫 번째 성공한 응답으로 본문 열의 형식 지정**(`typed_body`) — 첫 번째 성공한 응답의 `Content-Type`에 따라 본문 열을 JSON, 텍스트 또는 바이너리로 지정합니다. 다른 종류의 이후 응답, 구문 분석되지 않는 JSON, 빈 본문은 누락 값이 됩니다.
* **응답 헤더마다 열 추가**(`all_headers`) — 응답 헤더마다 상태 열 뒤에 텍스트 열을 추가합니다. 응답이 보내지 않은 헤더는 누락 값이 됩니다.
* **응답 쿠키 추가(DownloadCookies)**(`cookies`) — 각 응답의 쿠키인 `DownloadCookies`를 추가합니다.

테이블 행마다 요청 하나를 보내는 경우:

* **URL이 절대 http(s) URL이 아닌 행 건너뛰기**(`skip_invalid_urls`) — URL이 절대 HTTP 또는 HTTPS URL이 아닌 행은 요청을 보내지 않고 행도 기록하지 않습니다. **행의 URL이 절대 http(s) URL이 아니면 단계 실패**(`fail_invalid_urls`)는 이런 행에서 대신 단계를 실패시킵니다.
* **행 값이 NULL인 헤더는 보내지 않음**(`skip_null_headers`) — `{{row.column}}` 값이 NULL인 헤더는 보내지 않습니다. **헤더의 행 값이 NULL이면 단계 실패**(`fail_null_headers`)는 대신 단계를 실패시킵니다.
* **SOAP 작업**(`soap`) — 엔드포인트가 지정한 WSDL의 작업을 행마다 한 번씩 호출합니다. `service`, `port`, `operation`(비어 있으면 각각 첫 번째 항목), 각 매개변수를 열이나 상수에 매핑하는 `inputs`, 열로 기록할 응답 요소를 지정하는 `outputs`(비어 있으면 리프 요소마다 열 하나), 응답 요소를 XML로 추가하는 `xml`을 사용합니다. WSDL과 서비스 주소는 공개 HTTP 또는 HTTPS URL이어야 합니다.

모든 요청에 해당하는 항목:

* **HTTP Digest 챌린지에 응답**(`digest_auth`) — 연결의 Basic Auth 사용자 이름과 암호로 HTTP Digest 챌린지에 응답합니다. **NTLM 챌린지에 응답**(`ntlm_auth`)은 같은 방식으로 NTLM 챌린지에 응답하며, 도메인을 지정하려면 사용자 이름을 `DOMAIN\user`로 작성합니다.
* `proxy` — HTTP 또는 SOCKS 프록시를 통해 요청을 보내며, **프록시 프로토콜**(`protocol`: `http`, `https`, `socks`, `socks4` 또는 `socks5`), **프록시 호스트**(`host`), **프록시 포트**(`port`), **직접 보낼 호스트**(`excluded` 호스트 패턴), **프록시 사용자 이름**(`username`)으로 설정합니다. 암호는 연결의 `proxy_password`이며, 연결의 `proxy_host`가 이 호스트일 때만 사용됩니다.

워크플로 변수를 가리키는 `{{name}}` 참조(`{{var.name}}` / `{{project_var.name}}`도 가능)는 실행 시 엔드포인트, 헤더, 쿼리 값, 본문에서 대입됩니다. 이중 중괄호만 대입되므로 JSON 본문의 단일 중괄호는 그대로 유지됩니다. 센서/웹훅 실행에서는 `{{trigger_sensor_id}}`, `{{trigger_sensor_type}}`, `{{trigger_fired_at}}`, `{{trigger_payload_json}}`도 사용할 수 있습니다(트리거되지 않은 실행에서는 비어 있음).

편집기는 엔드포인트, 헤더 및 쿼리 테이블, 본문 편집기에서 감지된 `{{...}}` 토큰을 강조 표시합니다.

**재시도 횟수**는 멱등 메서드(GET/HEAD/OPTIONS/DELETE)에만 적용됩니다. POST/PUT/PATCH는 멱등이 아닌 본문이 다시 전송되지 않도록 항상 한 번만 보냅니다. **재시도 횟수**는 0~100을 지정할 수 있습니다. **제한 시간(초)** 은 요청당 제한으로 1~600초이며, 테스트 요청은 최대 300초까지 기다립니다. 카탈로그 필터, 붙여넣기 및 끌어놓기, JSON 도구, 요청 경고, 테스트 결과는 [REST 요청 단계](/ko/guides/workflows/rest-request-step/)를 참조하십시오.

### 응답 대상

* **테이블** *(기본값)* — 응답을 **대상 테이블**(필수, 뷰는 안 되고 테이블만 가능)로 구문 분석합니다. 제어 항목: 행 형식(`Object` 또는 `Array`, 테이블 행마다 요청 하나를 보내려면 `Object` 필요), 항목 경로, 페이징 모드(`No Paging`, `Offset Paging`, `Page Number Paging`, `Next Page URL Paging`, `Cursor Paging` 또는 `Link Header Paging (RFC 5988)`), 모드 매개변수, 모드 경로, "행을 구문 분석하는 대신 원시 JSON 덤프", 재시도 횟수, 제한 시간. **테이블 데이터 선택** 탭은 응답 필드를 열에 매핑합니다. **소스 검사 → 채우기**는 실제 응답으로 이를 채우며, 연결이 필요하고 GET, HEAD, OPTIONS 이외의 메서드를 보내기 전에 먼저 확인을 요청합니다. 요약 및 고유는 제공되지 않습니다.
* **워크플로 변수** — 요청 하나를 보내고 `{prefix}_status`, `{prefix}_body`, `{prefix}_headers`, `{prefix}_elapsed_ms`를 설정합니다. **변수 접두사**는 일반 식별자여야 하며 `cloud`, `project`, `model`, `date` 중 하나일 수 없습니다.

## 동작

* 변수 모드에서는 단계가 요청을 한 번만 보내며, 페이징과 행 구문 분석은 적용되지 않습니다.
* 캡처된 변수는 다운스트림에서 `{my_call_status}`처럼 이름으로 참조합니다.
