---
title: Alteryx 변환 매트릭스
description: PlaidCloud가 Alteryx 도구를 네이티브 고급 워크플로 단계, 매크로, 변수, 관리형 실행기로 변환하는 방법과 도구별 지원 상태를 설명합니다.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/alteryx-conversion-matrix.md
---

PlaidCloud는 Alteryx 워크플로, 앱, 매크로를 네이티브 고급 워크플로로 변환합니다. 가져오기 도구는 각 Alteryx 도구를
워크플로 단계, 매크로 구성 요소, 제어 변수, 문서 기반 파일 작업 또는 관리형 작업 실행기에 매핑하므로,
변환된 워크플로는 에뮬레이션이 아니라 클라우드 네이티브로 실행됩니다.

**거의 모든 표준 Alteryx 도구가 완전히 변환됩니다.** 아래의 지원 상태는 도구별로 표시됩니다.

- **전체** — 네이티브 PlaidCloud 단계, 매크로, 변수, 아티팩트 또는 관리형 실행기로 변환되어 도구의 기능을 실행합니다.
  대부분의 도구가 여기에 해당합니다.
- **부분** — 일반적인 사용에서는 변환되어 실행되지만, 도구의 서로 구분되는 *기능 모드* 하나는 아직 재현되지 않습니다. 드뭅니다.
- **지원되지 않음** — 변환되지 않으며, 해당 기능은 대신 네이티브로 다시 구성합니다.

외부 시스템 커넥터(Salesforce, HTTP, Google Analytics, Cassandra, 이메일, Hadoop, Spark 등)는
**변환되지 않고 연결됩니다**. [외부 시스템에 연결](#외부-시스템에-연결)을 참조하십시오.

## 도구 지원

| Alteryx 도구 | 상태 | PlaidCloud 대응 항목 | 변환 내용 |
| --- | --- | --- | --- |
| Action | 전체 | 변수 바인딩 및 조건부 단계 구성 | 변환된 앱 입력으로부터 다운스트림 단계 설정을 업데이트합니다. |
| Analytic App interface (`.yxwz`) | 부분 | 게시된 Panel "App Runner" 프런트엔드 | 앱의 `<Questions>` 레이아웃이 사용자 입력을 수집하고 변환된 워크플로를 구동하는 작동하는 Panel 앱으로 구체화되며, 변환의 일부로 자동 게시됩니다(입력 위젯이 없는 앱은 건너뜁니다). 일반적인 질문 유형인 텍스트, 숫자(Numeric Up Down), 날짜, 확인란, 라디오 버튼, 드롭다운, 목록 상자, 트리, 파일 찾아보기, 폴더 찾아보기는 App Runner 위젯이 됩니다. 어떤 워크플로 변수에도 바인딩되지 않는 질문은 아무 쓸모 없는 값을 조용히 수집하는 대신 눈에 띄는 안내와 함께 표시되며, 덜 일반적인 질문 유형은 구체화되지 않고 검토 대상으로 표시됩니다. [변환된 Alteryx 앱 사용](/ko/guides/workflows/use-converted-alteryx-apps/#app-runner-프런트엔드)을 참조하십시오. |
| Append Fields | 전체 | 필드 추가 변환 | 한 스트림의 필드를 다른 스트림에 추가합니다. |
| Auto Field | 전체 | 자동 필드 크기 조정 변환 | 추론된 필드 크기를 유지합니다. |
| AutoML | 전체 | [ML: Train Model](/ko/reference/workflow-steps/machine-learning/ml-train/) 단계 | 모델 방법, 대상, 후보 알고리즘 선택을 Classification 및 Regression과 마찬가지로 ML Train 단계로 통합합니다. AutoML은 Alteryx 실행 시 실제로 어떤 후보 알고리즘이 선택되었는지 기록하지 않으므로, 변환 시 ML Train이 지원하는 첫 번째 선택된 알고리즘을 고르고 그 선택을 안내로 남깁니다. 변환된 AutoML 단계를 사용자의 Alteryx 결과와 비교하십시오. |
| Barcode | 전체 | 바코드 실행기 | 구성된 심볼로지로 바코드를 읽거나 씁니다. |
| Batch Macro | 부분 | 제어 앵커 테이블에 대해 팬아웃되는 매크로 | 호출자가 제어 입력의 레코드마다 전체 매크로를 한 번씩 실행하며, 매 패스마다 내부의 제어 매개변수를 바인딩합니다. 여기에는 정확히 하나만 사용 중일 때 호출자가 표시 레이블로 이름을 바꾼 제어 매개변수와, 변수로 Select의 필드 목록을 다시 쓰는 `UpdateRawXml` Action이 포함됩니다. 패스별 값을 안전하게 재현할 수 없는 형태는 잘못 변환되지 않고 이름과 함께 닫힌 상태로 실패합니다. 해당 형태는 Select의 필드 목록 이외의 것을 다시 쓰는 `UpdateRawXml`, 그리고 Filter의 전체 식을 변수로 대체하는 Action입니다(원시 패스별 구문이 잘못 평가될 수 있기 때문입니다). |
| Browse | 전체 | Browse / 통과 | 실행 비용 없이 검사용으로 보존됩니다. |
| Buffer | 전체 | [Spatial Buffer](/ko/reference/workflow-steps/spatial/spatial-buffer/) 단계 | 각 지오메트리를 고정 거리만큼 확장합니다. |
| Build Features | 부분 | [Build Features](/ko/reference/workflow-steps/tables/table-build-features/) 단계 | 산술 및 상호작용 기본 요소, 날짜 부분 추출, 명시적 임계값 구간화, z-점수 및 최소-최대 스케일링, 원-핫 인코딩을 변환합니다. 테이블 간 집계(Manage Relationships 탭 전반의 Deep Feature Synthesis), PCA, 타깃 인코딩, 데이터 기반 자동 구간화는 대응 기능이 없으며, 각각 조용히 버려지지 않고 변환 보고서에 이름과 함께 표시됩니다. |
| Calgary Cross Count | 전체 | [Calgary 데이터베이스](/ko/guides/workflows/migrate-alteryx-workflows/#calgary-데이터베이스) 집계 | 인덱싱된 필드를 그룹화하고 각 사용자 지정 필드의 명명된 값을 집계합니다. |
| Calgary Cross Count Append | 전체 | [Calgary Cross Count Append](/ko/guides/workflows/migrate-alteryx-workflows/#calgary-join-및-cross-count-append) | 각 입력 레코드를 값 인덱스와 매칭한 다음, 매칭된 데이터베이스 레코드 수를 셉니다. |
| Calgary Input | 전체 | [Calgary 데이터베이스](/ko/guides/workflows/migrate-alteryx-workflows/#calgary-데이터베이스) 입력 | 저장된 쿼리를 필터로 적용하여 데이터베이스를 읽습니다. |
| Calgary Join | 전체 | [Calgary Join](/ko/guides/workflows/migrate-alteryx-workflows/#calgary-join-및-cross-count-append) | 각 레코드를 데이터베이스의 값 인덱스와 매칭하고 매칭된 레코드를 유지합니다. |
| Calgary Loader | 전체 | [Calgary 데이터베이스](/ko/guides/workflows/migrate-alteryx-workflows/#calgary-데이터베이스) 작성기 | 모든 Calgary 리더가 바인딩되는 대체 테이블을 작성합니다. |
| Centroid | 전체 | Centroid 실행기 작업 | 각 지오메트리를 중심점으로 줄여 `Centroid` 열로 추가합니다. |
| Check Box | 전체 | 제어 워크플로 변수 | 앱 확인란 선택을 제어 입력으로 변환합니다. |
| Classification | 전체 | [ML: Train Model](/ko/reference/workflow-steps/machine-learning/ml-train/) 단계 | Assisted Modeling 체인을 알고리즘, 대상, 특징, 하이퍼파라미터가 포함된 하나의 ML Train 단계로 통합합니다. |
| Comment / Annotation / Link | 전체 | 캔버스 주석 | 워크플로 컨텍스트로 보존됩니다. |
| Condition | 전체 | 단계 조건 | 식에 따라 경고, 오류 또는 분기를 트리거합니다. |
| Control Parameter | 전체 | 매크로 제어 매개변수 | PlaidCloud 매크로 매개변수에 매핑됩니다. |
| Convex Hull | 전체 | Convex Hull 실행기 작업 | 각 지오메트리를 둘러싸는 가장 작은 볼록 다각형을 만들어 `ConvexHull` 열로 추가합니다. |
| Create Points | 전체 | `geom_point`를 사용하는 [Table Extract](/ko/reference/workflow-steps/spatial/spatial-sql-recipes/) 단계 | 경도/위도 열에서 SQL로 점 지오메트리를 만듭니다. |
| Create Samples | 전체 | 출력마다 하나씩 Table Extract 단계 | 입력을 구성된 비율로 Estimation, Validation, Holdout으로 분할합니다. |
| Cross Tab | 전체 | 피벗 / 교차표 변환 | 모든 집계 방법과 파생 합계에 걸쳐 행을 열로 피벗합니다. |
| Data Cleansing | 전체 | 데이터 정제 변환 | 공백, null, 문장 부호, 대소문자를 정리합니다. |
| Date | 전체 | 워크플로 변수(날짜) | 단계와 조건에 사용할 ISO 날짜 값을 내보냅니다. |
| DateTime | 전체 | 날짜/시간 변환 | 날짜 및 시간 구문 분석과 서식 지정을 변환합니다. |
| Detour | 전체 | 조건부 분기 라우팅 | 경로 선택을 DAG 조건으로 변환합니다. |
| Detour End | 전체 | 조건부 분기 병합 | 조건에 따라 선택된 분기를 다시 합칩니다. |
| Directory | 전체 | 문서 디렉터리 목록 | 문서 경로의 파일을 나열합니다. |
| Distance | 전체 | `ST_DISTANCE_SPHERE`를 사용하는 [Table Extract](/ko/reference/workflow-steps/spatial/spatial-sql-recipes/) 단계 | SQL로 계산하는 측지 점 간 거리와 방위입니다. |
| Download | 전체 | REST 연결에 대한 [REST Request](/ko/reference/workflow-steps/general/rest-request/) 단계 | 외부 데이터나 아티팩트를 다운로드합니다. 실행하기 전에 변환된 단계에 REST 연결을 할당하십시오. |
| Drop Down | 전체 | 제어 워크플로 변수 | 앱 드롭다운 선택을 제어 입력으로 변환합니다. |
| Dynamic Input | 부분 | 동적 문서 입력 | 실행 시점에 파일 패턴과 변수 기반 입력을 확인합니다. Directory 도구가 나열한 모든 통합 문서에서 하나의 워크시트를 읽은 다음 합치는 Excel *ReadList*는, 상위 Filter가 정확히 일치하는 단일 이름으로 시트를 고정한 경우 폴더 glob 시트 읽기로 변환됩니다. Contains, 부등식, OR 필터로 선택된 시트나 둘 이상의 시트에 걸친 읽기는 잘못된 시트를 읽는 대신 변환을 거부합니다. |
| Dynamic Rename | 전체 | 동적 이름 바꾸기 변환 | 메타데이터나 규칙에 따라 필드 이름을 바꿉니다. |
| Dynamic Replace | 전체 | 동적 바꾸기 변환 | 두 번째 스트림의 바꾸기 규칙을 적용합니다. |
| Dynamic Select | 전체 | 동적 필드 선택 변환 | 유형, 이름 또는 규칙으로 필드를 선택합니다. |
| Error | 전체 | 단계 조건(오류) | 구성된 오류 동작을 단계 조건으로 변환합니다. |
| Feature Types | 전체 | [ML: Train Model](/ko/reference/workflow-steps/machine-learning/ml-train/) 단계 특징 구성 | 각 필드에 지정된 모델 역할을 통합된 ML Train 단계로 전달합니다. |
| File Browse | 전체 | 제어 문서 파일 변수 | 변환된 앱을 실행할 때 사용자가 파일을 선택할 수 있게 합니다. |
| Filter | 전체 | 필터 변환 | 식에 따라 레코드를 참과 거짓 경로로 분할합니다. |
| Fit | 전체 | [ML: Train Model](/ko/reference/workflow-steps/machine-learning/ml-train/) 단계 | 통합된 ML Train 단계로 합쳐집니다. |
| Folder Browse | 전체 | 제어 문서 폴더 변수 | 변환된 앱을 실행할 때 사용자가 폴더를 선택할 수 있게 합니다. |
| Formatted Excel output into a styled template | 부분 | 템플릿 인식 Excel 작성기(여러 시트는 [Export to Excel Sheets](/ko/reference/workflow-steps/export/export-to-excel-sheets/) 단계) | 스타일이 적용된 템플릿에 쓰면 템플릿의 서식이 보존됩니다. 값, 숫자 형식, 글꼴, 채우기, 테두리, 병합된 셀, 열 너비가 지정된 시트와 범위로 그대로 전달됩니다. 이는 단일 시트와, 한 통합 문서의 서로 다른 시트에 조립된 여러 출력을 한 번에 채우는 경우를 모두 포함하므로 시트끼리 더 이상 서로 덮어쓰지 않습니다. 한 가지 경우는 부분 지원으로 남습니다. 피벗 테이블이나 차트가 있는 템플릿은 시트를 쓸 때 해당 개체가 삭제됩니다. 스타일이 없는 일반 Excel 출력은 전체 지원입니다. Output Data를 참조하십시오. |
| Formula | 전체 | 수식 변환 | 필드 식을 PlaidCloud 식이나 SQL로 변환합니다. |
| Fuzzy Match | 전체 | 퍼지 매칭 실행기 | 키, 임계값, 후보 검토를 기준으로 매칭합니다. |
| Generalize | 전체 | [Spatial Generalize](/ko/reference/workflow-steps/spatial/spatial-generalize/) 단계 | 위상을 유지하면서 허용 오차까지 지오메트리를 단순화합니다. |
| HTML | 전체 | 보고서 텍스트 / HTML 아티팩트 | 콘텐츠를 보고서 또는 아티팩트 출력으로 보존합니다. |
| Image Processing | 전체 | 이미지 변환 실행기 | 캔버스 순서대로 회색조, 크기 조정, 자르기, 회전을 적용합니다. |
| Image Profile | 전체 | 이미지 프로필 실행기 | 크기, 모드, 형식, 채널, 휘도 통계를 보고합니다. |
| Image to Text | 전체 | OCR 실행기 | 관리형 OCR로 이미지에서 텍스트를 추출합니다. |
| Input Data | 전체 | 문서 기반 파일 입력 | `.yxdb`, `.dbf`, Excel, 고정 너비 `.flat` 소스 파일을 워크플로 데이터로 로드합니다. |
| Insights | 전체 | 대시보드 / 아티팩트 출력 | 클라우드 네이티브 검토 아티팩트를 만듭니다. |
| Interactive Chart | 전체 | 차트 아티팩트 | 변환된 데이터로 차트 아티팩트를 만듭니다. |
| Join | 전체 | 조인 변환 | 단일 또는 다중 필드 키나 위치를 기준으로 조인된 스트림, 왼쪽 전용 스트림, 오른쪽 전용 스트림을 생성합니다. |
| Join Multiple | 전체 | 다중 조인 변환 | 여러 입력 스트림을 조인합니다. |
| Key/Value Pairs | 전체 | [Text: NLP AI](/ko/reference/workflow-steps/text-documents/nlp-ai/) 단계(keyvalue 작업) | LLM 기반 NLP AI 단계를 통해 텍스트 열에서 키/값 쌍을 추출하며, 후보 키와 퍼지 또는 정확 일치를 선택적으로 지정할 수 있습니다. |
| Line To Polygon | 전체 | Line To Polygon 실행기 작업 | 각 선을 다각형 고리로 닫아 `Polygon` 열로 추가합니다. |
| List Box | 전체 | 제어 워크플로 변수 | 앱 목록 선택을 제어 입력으로 변환합니다. |
| Location Optimizer | 부분 | [Location Optimizer](/ko/reference/workflow-steps/optimization/location-optimizer/) 단계 | 수요까지의 총 거리 또는 가중 거리를 최소화하는 K개 지점을 선택하는 선형 거리 최소화 사례를 네이티브 p-median MIP 단계로 변환합니다. 중력 커널 점수, 맞춤형 점수 계산 매크로 또는 기타 후보 탐색 목적 함수는 여전히 변환을 거부합니다. [Alteryx 워크플로 마이그레이션](/ko/guides/workflows/migrate-alteryx-workflows/#변환된-워크플로의-매크로)을 참조하십시오. |
| Macro calls | 전체 | 매크로 호출 | 알려진 매크로 소스를 가져오고 매크로 호출을 PlaidCloud 매크로 단계에 매핑합니다. |
| Macro Input / Macro Output | 전체 | 매크로 입력 / 출력 포트 | PlaidCloud 매크로 포트에 직접 매핑됩니다. |
| Make Grid | 전체 | [Spatial Make Grid](/ko/reference/workflow-steps/spatial/spatial-make-grid/) 단계 | 범위를 정사각형 셀로 타일링하여 셀마다 한 행씩 만듭니다. |
| Map | 전체 | 지도 아티팩트 | PlaidCloud 지도 아티팩트를 만듭니다. |
| Map Input | 전체 | [Spatial File Import](/ko/reference/workflow-steps/spatial/spatial-file-import/) 단계 | MapInfo, ESRI, KML, GeoJSON 파일을 보조 파일과 함께 읽습니다. |
| Master Selector | 부분 | 제어 워크플로 변수 및 조건부 단계 표시 | 인터페이스 요소에 대한 도구의 표시/숨김 가시성 조건을 조건부 단계 표시로 변환합니다. 선택이 실행하는 하위 워크플로는 최선의 노력으로 변환합니다. 실제 테넌트 앱에 대한 검증은 아직 진행 중이므로, 운영 환경에서 사용하기 전에 선택된 실행 대상을 검토하십시오. |
| Message | 전체 | 단계 조건(메시지) | 조건에 따라 워크플로 경고, 메시지 또는 오류를 내보냅니다. |
| Modeling | 전체 | [ML: Train Model](/ko/reference/workflow-steps/machine-learning/ml-train/) 단계 | 파이프라인의 모델 선택과 함께 ML Train 단계로 통합됩니다. |
| Multi-Field Formula | 전체 | 다중 필드 수식 변환 | 선택한 필드 전체에 수식을 적용합니다. |
| Multi-Row Formula | 전체 | 윈도 / 행 인식 수식 변환 | 행 상대 로직을 Group By로 파티션된 윈도 동작으로 변환합니다. |
| Named Entity Recognition (NER) | 전체 | [Text: NLP AI](/ko/reference/workflow-steps/text-documents/nlp-ai/) 단계(ner 작업) | LLM 기반 NLP AI 단계를 통해 텍스트 열에서 엔터티(사람, 조직, 위치, 날짜, 수량 또는 사용자 지정 유형 목록)를 추출합니다. |
| Numeric Up Down | 전체 | 제어 숫자 변수 | 앱 숫자 입력을 형식이 지정된 변수로 변환합니다. |
| Output Data | 전체 | 문서 / 테이블 출력 | Parquet 및 Avro 파일을 포함하여 출력을 문서나 PlaidCloud 테이블에 씁니다. `.yxdb`, `.hyper`, `.dbf` 출력은 Parquet로 기록됩니다. |
| Overlay | 전체 | [Spatial Process](/ko/reference/workflow-steps/spatial/spatial-process/) 단계 | 두 지오메트리 열의 교차, 합집합 또는 잘라내기를 수행합니다. |
| PDF Input | 전체 | PDF 추출 실행기 | PDF에서 텍스트나 표를 추출합니다. |
| Point To Line | 전체 | Point To Line 실행기 작업 | 시퀀스 필드 순서에 따라 각 그룹의 점을 그룹당 하나의 `SequenceLine`으로 연결합니다. |
| Poly-Build | 전체 | [Spatial Poly-Build](/ko/reference/workflow-steps/spatial/spatial-poly-build/) 단계 | 점 그룹마다 다각형 또는 볼록 껍질을 만듭니다. |
| Poly-Split | 전체 | [Spatial Poly-Split](/ko/reference/workflow-steps/spatial/spatial-poly-split/) 단계 | 꼭짓점, 구성 다각형 또는 구멍마다 한 행을 만듭니다. |
| Portfolio Composer (Text / Table / Image / Layout / Render) | 전체 | 보고서 아티팩트 | 보고서 콘텐츠, 레이아웃, 렌더링을 PlaidCloud 보고서 출력으로 변환합니다. |
| POS Tagger | 전체 | [Text: NLP AI](/ko/reference/workflow-steps/text-documents/nlp-ai/) 단계(pos 작업) | LLM 기반 NLP AI 단계를 통해 텍스트 열에서 각 토큰의 품사를 태깅합니다. |
| Predict | 전체 | [ML: Score](/ko/reference/workflow-steps/machine-learning/ml-score/) 단계 | 학습된 모델 테이블로 데이터를 점수화하고 예측 열을 추가합니다. |
| Radio Button | 전체 | 제어 워크플로 변수 | 앱 라디오 선택을 제어 입력으로 변환합니다. |
| Random % Sample | 전체 | Table Extract 단계(무작위) | 요청한 정확한 개수 또는 비율의 레코드를 반환합니다. |
| Record ID | 전체 | 행 식별자 변환 | 구성된 유형과 시작 값으로 결정적 레코드 식별자를 추가하며, 그룹마다 다시 시작합니다. |
| Redistribute | 전체 | Redistribute 실행기 작업 | 겹치는 면적에 따라 한 지리 집합의 측정값을 다른 집합으로 재배분하여 `Redistributed` 열로 추가합니다. |
| RegEx | 전체 | 정규식 변환 | 텍스트를 구문 분석하거나, 일치시키거나, 바꿉니다. |
| Regression | 전체 | [ML: Train Model](/ko/reference/workflow-steps/machine-learning/ml-train/) 단계 | Assisted Modeling 체인을 하나의 ML Train 단계로 통합합니다. |
| Report Map | 전체 | 지도 보고서 아티팩트 | 클라우드 네이티브 지도/보고서 아티팩트를 생성합니다. |
| Run Command | 부분 | REST 연결에 대한 [REST Request](/ko/reference/workflow-steps/general/rest-request/) 단계(`curl`/`wget`만 해당) | `curl` 또는 `wget` 명령줄을 REST Request 단계로 변환합니다. 인터프리터 및 스크립트 명령(`cscript`, PowerShell, Python 등), Excel-COM 자동화, 파일 시스템 작업, 불투명하거나 워크플로를 시작하는 명령은 자동 변환되지 않고 수동 검토 대상으로 이름과 함께 표시됩니다. |
| Sample | 전체 | 샘플 변환 | 개수, 비율 또는 그룹화로 레코드를 유지합니다. |
| Select | 전체 | 선택 및 스키마 프로젝션 단계 | 필드를 선택하고, 이름을 바꾸고, 순서를 바꾸고, 유형을 다시 지정합니다. |
| Smooth | 전체 | [Spatial Smooth](/ko/reference/workflow-steps/spatial/spatial-smooth/) 단계 | 여러 패스에 걸쳐 각 지오메트리를 평활화합니다. |
| Sort | 전체 | 정렬 변환 | 구성된 필드와 방향으로 레코드를 정렬합니다. |
| Spatial Info | 전체 | [Spatial Info](/ko/reference/workflow-steps/spatial/spatial-info/) 단계 | 측지 측정값으로서의 면적, 길이, 중심점, 경계 사각형입니다. |
| Spatial Match | 전체 | [Spatial Match](/ko/reference/workflow-steps/spatial/spatial-match/) 단계 / [Spatial Match (Intersect / Unmatched)](/ko/reference/workflow-steps/spatial/spatial-match-executor/) 단계 | Within, Contains, Intersects, Touches, Crosses, Overlaps, Centroid-In 등 모든 관계를 데이터베이스나 워크플로 엔진에서 매칭하여 변환합니다. |
| Spatial Process | 전체 | [Spatial Process](/ko/reference/workflow-steps/spatial/spatial-process/) 단계 | 지오메트리 열의 교차, 합집합 또는 잘라내기를 수행합니다. |
| Summarize | 전체 | 집계 변환 | 합계, 개수, 평균, 최소, 최대, 중앙값, 최빈값, 표준 편차, 분산, 고유 개수로 그룹화하고 집계합니다. |
| Tab | 전체 | 앱 탭 그룹화 | 변환된 앱 구조로 보존됩니다. |
| Test | 전체 | 단계 조건 | 테스트 어서션을 단계 조건으로 변환합니다. |
| Text Box | 전체 | 제어 텍스트 변수 | 앱 텍스트 입력을 형식이 지정된 변수로 변환합니다. |
| Text Input | 전체 | 인라인 테이블 입력 | 워크플로용 인라인 데이터를 만듭니다. |
| Text Pre-processing | 전체 | NLP 전처리 실행기 | 텍스트를 정규화하고 전처리합니다. |
| Text Summary | 전체 | [Text: NLP AI](/ko/reference/workflow-steps/text-documents/nlp-ai/) 단계(summary 작업) | LLM 기반 NLP AI 단계를 통해 텍스트 열을 구성된 최대 문장 수로 요약합니다. |
| Text To Columns | 전체 | 열 분할 변환 | 텍스트를 필드나 행으로 분할합니다. |
| Tile | 전체 | 타일 / 그룹화 변환 | 구성된 규칙에 따라 타일 그룹을 할당합니다. |
| Tool Container | 전체 | 캔버스 컨테이너 / 실행 그룹 | 워크플로 구성으로 보존됩니다. |
| Topic Modeling | 전체 | 토픽 모델링 실행기 | 관리형 NLP를 통해 토픽 모델링을 실행합니다. |
| Transformation | 전체 | 변환 단계 | 변환 로직을 PlaidCloud 식이나 SQL로 변환합니다. |
| Transpose | 전체 | 언피벗 변환 | 열을 Name/Value 쌍의 행으로 변환합니다. |
| Tree | 전체 | 제어 워크플로 변수 | 앱 트리 선택을 제어 입력으로 변환합니다. |
| Union | 전체 | 유니온 변환 | 이름, 위치 또는 구성된 규칙으로 스트림을 결합합니다. |
| Unique | 전체 | 고유 / 중복 분리 변환 | 처음 나온 고유 레코드와 중복을 분리합니다. |
| Visual Layout | 전체 | 캔버스 레이아웃 메타데이터 | 디자인 컨텍스트로 보존됩니다. |
| Word Cloud | 전체 | 텍스트 시각화 아티팩트 | 텍스트 분석으로 시각화 아티팩트를 만듭니다. |
| XML Parse | 전체 | XML 구문 분석 변환 | XML 필드를 워크플로 데이터로 추출합니다. |
| Zero-shot Text Classification | 전체 | [Text: NLP AI](/ko/reference/workflow-steps/text-documents/nlp-ai/) 단계(zeroshot 작업) | LLM 기반 NLP AI 단계를 통해 행별 후보 레이블 목록에 대해 텍스트 열을 단일 레이블 또는 다중 레이블로 분류합니다. |
| Find Nearest | 전체 | [Spatial Find Nearest](/ko/reference/workflow-steps/spatial/spatial-find-nearest/) 단계 | 거리순 최근접 이웃 조인입니다. 직선 거리 방식과, PlaidCloud의 자체 호스팅 라우팅 엔진을 통한 주행 시간 최근접(도로망의 소요 시간(분) 기준 순위) 방식을 지원합니다. 주행 시간은 워크스페이스별로 사용 설정됩니다. |
| Trade Area | 전체 | [Spatial Trade Area](/ko/reference/workflow-steps/spatial/spatial-trade-area/) 단계 | 실제 단위로 크기를 지정한 동심 버퍼입니다. 고정 반경 방식과, 자체 호스팅 라우팅 엔진을 통한 주행 시간 상권(도로망의 소요 시간(분)) 방식을 지원합니다. 주행 시간은 워크스페이스별로 사용 설정됩니다. |
| Image Template | 전체 | Image Template 실행기 작업 | 수동 모드에서는 템플릿에 그린 각 영역에 맞게 이미지를 자릅니다. 자동 모드에서는 개방형 표준 레이아웃 모델로 페이지 영역을 감지하고, 감지된 경계와 검토용 신뢰도를 담은 행을 영역마다 하나씩 내보냅니다. 모델이 확실하게 읽을 수 없는 페이지는 잘리지 않고 이름과 함께 표시됩니다. 개방형 표준 감지는 Alteryx 자체 감지와 다를 수 있으므로, 감지된 영역을 검토하거나 정밀한 제어가 필요하면 수동 모드를 사용하십시오. |
| Image Recognition | 전체 | 이미지 인식 실행기 | 워크플로 안에서 이미지 분류기를 학습시키고 새 이미지를 그 자리에서 점수화합니다. 외부 계정이 필요 없으며 데이터가 PlaidCloud 밖으로 나가지 않습니다. 분류기는 Alteryx에서 복사하지 않고 다시 학습시키므로, 결과는 비트 단위로 일치하는 것이 아니라 충실한 근사치이며 학습은 CPU에서 실행됩니다. 워크스페이스별로 사용 설정됩니다. |
| Geocoder | 전체 | 자체 호스팅 지오코더 | PlaidCloud 자체 지오코더로 주소를 좌표로 지오코딩하고 좌표를 주소로 역지오코딩합니다. 외부 계정이 필요 없으며 데이터가 PlaidCloud 밖으로 나가지 않습니다. 워크스페이스별로 사용 설정됩니다. |

인터페이스 위젯(드롭다운, 목록 상자, 확인란, 텍스트/숫자/날짜 입력, 파일 및 폴더 선택기), 캔버스 개체(주석, 링크,
컨테이너), 매크로 포트는 모두 네이티브 제어 변수나 캔버스 개체로 변환됩니다. Alteryx 앱의 전체 인터페이스 레이아웃,
즉 `.yxwz` 파일의 `<Questions>` 정의도 게시된 Panel "App Runner" 프런트엔드로 구체화되므로, 앱을 변환하면 개별 제어 변수뿐
아니라 동일한 값을 수집하고 변환된 워크플로를 구동하는 작동하는 입력 양식이 만들어집니다. 위의 Analytic App interface 행과
[변환된 Alteryx 앱 사용](/ko/guides/workflows/use-converted-alteryx-apps/#app-runner-프런트엔드)을 참조하십시오.

**Excel 출력에 대한 참고.** 기본 서식으로 데이터를 쓰는 일반 새 통합 문서는 완전히 변환됩니다. 서식을 보존하면서 이름이 지정된
시트와 범위를 채우는 *스타일이 적용된 템플릿*에 쓰는 경우는 단일 시트와, 한 통합 문서의 서로 다른 시트에 조립된 여러 출력에서
변환됩니다([Export to Excel Sheets](/ko/reference/workflow-steps/export/export-to-excel-sheets/) 단계가 모든 시트를 한 번에 채웁니다).
피벗 테이블이나 차트가 있는 템플릿은 시트를 쓸 때 해당 개체가 삭제되며, Run Command(Excel COM/VBS)로 구동되는 시트 수준 파일 조작은
자동 변환되지 않고 수동 검토 대상으로 이름과 함께 표시됩니다.

## 공간 도구 지원 범위

Alteryx **Spatial** 팔레트의 모든 도구에는 PlaidCloud 경로가 있으며, 그 경로는 모두 직접 만들 수도 있는 단계입니다. 변환은
편의 기능일 뿐 유일한 진입 방법이 아닙니다. 전체 참조는 [지리 공간 단계](/ko/reference/workflow-steps/spatial/)를, 이들이 어떻게
함께 작동하는지는 [지리 공간 분석](/ko/guides/workflows/geospatial-analytics/)을 참조하십시오.

| Alteryx 공간 도구 | PlaidCloud 경로 | 실행 위치 |
| --- | --- | --- |
| Buffer | [Spatial Buffer](/ko/reference/workflow-steps/spatial/spatial-buffer/) 단계 | 워크플로 엔진 |
| Centroid | Centroid 실행기 작업 | 워크플로 엔진 |
| Convex Hull | Convex Hull 실행기 작업 | 워크플로 엔진 |
| Create Points | [Table Extract 식](/ko/reference/workflow-steps/spatial/spatial-sql-recipes/) | 데이터베이스 |
| Distance | [Table Extract 식](/ko/reference/workflow-steps/spatial/spatial-sql-recipes/) | 데이터베이스 |
| Find Nearest | [Spatial Find Nearest](/ko/reference/workflow-steps/spatial/spatial-find-nearest/) 단계 | 데이터베이스, 주행 시간은 라우팅 서비스 |
| Generalize | [Spatial Generalize](/ko/reference/workflow-steps/spatial/spatial-generalize/) 단계 | 워크플로 엔진 |
| Heat Map | [Heat Map (macro)](/ko/reference/workflow-steps/macros/macro-heat-map/) | 워크플로 엔진 |
| Line To Polygon | Line To Polygon 실행기 작업 | 워크플로 엔진 |
| Make Grid | [Spatial Make Grid](/ko/reference/workflow-steps/spatial/spatial-make-grid/) 단계 | 워크플로 엔진 |
| Point To Line | Point To Line 실행기 작업 | 워크플로 엔진 |
| Poly-Build | [Spatial Poly-Build](/ko/reference/workflow-steps/spatial/spatial-poly-build/) 단계 | 워크플로 엔진 |
| Poly-Split | [Spatial Poly-Split](/ko/reference/workflow-steps/spatial/spatial-poly-split/) 단계 | 워크플로 엔진 |
| Redistribute | Redistribute 실행기 작업 | 워크플로 엔진 |
| Smooth | [Spatial Smooth](/ko/reference/workflow-steps/spatial/spatial-smooth/) 단계 | 워크플로 엔진 |
| Spatial Info | [Spatial Info](/ko/reference/workflow-steps/spatial/spatial-info/) 단계 | 워크플로 엔진 |
| Spatial Match | [Spatial Match](/ko/reference/workflow-steps/spatial/spatial-match/) 단계 | 데이터베이스 |
| Spatial Match — intersection object, Unmatched | [Spatial Match (Intersect / Unmatched)](/ko/reference/workflow-steps/spatial/spatial-match-executor/) 단계 | 워크플로 엔진 |
| Spatial Process | [Spatial Process](/ko/reference/workflow-steps/spatial/spatial-process/) 단계 | 워크플로 엔진 |
| Trade Area (fixed-radius + drive-time) | [Spatial Trade Area](/ko/reference/workflow-steps/spatial/spatial-trade-area/) 단계 | 워크플로 엔진, 주행 시간은 라우팅 서비스 |
| Pie Wedge Trade Area | [Pie Wedge Trade Area (macro)](/ko/reference/workflow-steps/macros/macro-pie-wedge-trade-area/) | 워크플로 엔진 |
| Spatial file input | [Spatial File Import](/ko/reference/workflow-steps/spatial/spatial-file-import/) 단계 | 워크플로 엔진 |
| Summarize — SpatialObjCombine, SpatialObjConvexHull | [Spatial Combine](/ko/reference/workflow-steps/spatial/spatial-combine/) 단계 | 워크플로 엔진 |
| Report Map | [Report Map](/ko/reference/workflow-steps/reports/report-map/) 단계 | 워크플로 엔진 |

**주행 시간 상권과 최근접** — Trade Area 주행 시간 링과 Find Nearest 주행 시간 순위는 호스팅된 서드파티 API가 아니라
PlaidCloud의 자체 호스팅 라우팅 엔진(도로망 등시선과 이동 시간 행렬)에서 실행되므로 출발지 좌표가 플랫폼 밖으로 나가지 않습니다.
주행 시간은 워크스페이스별로 사용 설정됩니다. 라우팅과 주행 시간 영역은 OpenStreetMap 데이터를 사용합니다.
© OpenStreetMap contributors, [Open Database License
(ODbL)](https://www.openstreetmap.org/copyright)에 따라 제공됩니다.

### 알려진 공간 사전 요구 사항

공간 도구 자체는 변환되며, 아래는 입력에 대한 사전 요구 사항입니다.

- **`.geo` GeoFile 형식.** Alteryx의 독점 바이너리 GeoFile에는 공개 리더가 없으므로, 이를 가져오면 실행 시점에 충돌하는 대신
  닫힌 상태로 실패합니다. Alteryx에서 레이어를 표준 공간 형식(shapefile 또는 GeoJSON)으로 다시 내보낸 다음 이를 가져오십시오.
  다른 공간 형식은 영향을 받지 않습니다.
  [공간 Alteryx 워크플로 마이그레이션](/ko/guides/workflows/migrate-spatial-alteryx-workflows/#공간-입력-패키징)을 참조하십시오.
- **Peano key Spatial Info 측정값.** Peano key는 공개 사양이 없는 독점 Alteryx 공간 인덱스이므로, 이를 요청하는 Spatial Info는
  해당 열 하나를 건너뛰고 안내에 그 이름을 밝힙니다. 면적, 길이, 중심점, 경계 사각형, 개체 유형, 부분 및 점 개수, 끝점 등
  다른 모든 Spatial Info 측정값은 변환됩니다.
- **투영된 Create Points 좌표.** Create Points는 부동 소수점 및 정수(×1,000,000) 경도/위도 좌표를 직접 변환합니다.
  이미 투영 좌표계에 있는 좌표는 워크플로가 어떤 투영을 사용하는지 기록하지 않으므로, 먼저 상위에서 WGS84 경도/위도로
  재투영해야 합니다.

## Calgary 도구 지원 범위

Alteryx Calgary 데이터베이스(`.cydb`)는 PlaidCloud가 열 수 없는 독점 인덱스 저장소입니다. 변환은 각 데이터베이스를 `calgary_<database name>`이라는 이름의 일반 PlaidCloud 테이블 하나로 간주하므로, 이를 중심으로 만들어진 도구들은 아예 거부되지 않고 일반 테이블 작업으로 변환됩니다. 대체 테이블의 작동 방식은 [Calgary 데이터베이스](/ko/guides/workflows/migrate-alteryx-workflows/#calgary-데이터베이스)를, 인덱스 매칭 도구는 [Calgary Join 및 Cross Count Append](/ko/guides/workflows/migrate-alteryx-workflows/#calgary-join-및-cross-count-append)를 참조하십시오.

| Alteryx Calgary 도구 | PlaidCloud 경로 | 변환 여부 |
| --- | --- | --- |
| Calgary Loader | `calgary_<database>`에 쓰는 Table Extract 단계 | 데이터베이스 이름이 지정되고 데이터 필드가 하나 이상 저장되는 경우 변환됩니다. |
| Calgary Input | 저장된 쿼리를 필터로 사용하여 `calgary_<database>`를 읽는 동적 문서 입력 | 변환됩니다. Or로 구성되거나 Not으로 감싼 쿼리, contains 또는 starts-with 필터(SQL LIKE로 다시 구성됨)도 포함합니다. 공간 조회 쿼리와 Skip Records/Max Records 제한에서는 변환을 거부합니다. |
| Calgary Input (Count Only) / Calgary Cross Count | `calgary_<database>`에 대한 집계 변환 | 변환됩니다. Or로 구성되거나 Not으로 감싼 버킷도 포함합니다. 사용자 지정 필드가 둘 이상인 교차와, 집계할 열을 지정하지 않은 개수 전용 읽기에서는 변환을 거부합니다. |
| Calgary Join | 입력의 각 레코드를 `calgary_<database>`와 매칭하는 동적 문서 입력 | 들어오는 필드가 값 인덱스에 매칭되는 일반 값인 경우 변환됩니다. 입력 레코드마다 매칭된 데이터베이스 레코드 수를 세고 매칭되지 않은 레코드는 0으로 세는 Count Only 모드도 포함합니다. 필드가 공간 유형인 경우(Spatial Match로 다시 구성하십시오)나 유형이 확인되지 않은 경우, 범위 인덱스 또는 매칭되지 않은 출력이 연결된 Join, 매칭 필드를 지정하지 않은 Join, 입력에 아무것도 연결되지 않은 Join에서는 변환을 거부합니다. |
| Calgary Cross Count Append | 각 레코드를 매칭하는 동적 문서 입력 다음에 `calgary_<database>`에 대한 개수 조인 | 들어오는 필드가 값 인덱스에 매칭되는 일반 값인 경우 변환됩니다. 입력 레코드마다 매칭된 데이터베이스 레코드 수를 세며, 아무것도 매칭되지 않은 레코드는 0으로 셉니다. 공간 또는 확인되지 않은 인덱스(Spatial Match로 다시 구성하십시오), 사용자 지정 값 교차 집계 그리드, 범위 인덱스, 필드를 지정하지 않은 매칭에서는 변환을 거부합니다. |

### 알려진 Calgary 사전 요구 사항

대부분은 변환 제한이 아니라 입력에 대한 사전 요구 사항입니다.

- **공간 인덱스 매칭은 Spatial Match로 다시 구성해야 합니다.** 공간 인덱스에 매칭된 Calgary Join 또는 Cross Count Append는 대체 테이블의 이름을 밝히며 변환을 거부합니다. 워크플로는 인덱스의 이름은 기록하지만 일반 값을 담고 있는지 공간 지오메트리를 담고 있는지는 기록하지 않으며, 값 매칭(동등 조인)과 공간 매칭(점이 다각형 안에 있는지)은 서로 다른 작업입니다. 데이터베이스를 테이블로 내보내고 매칭을 Join(값 인덱스) 또는 Spatial Match(공간 인덱스)로 다시 구성하십시오.
- **Skip Records 또는 Max Records로 제한된 읽기에는 명시적인 순서가 필요합니다.** 내보낸 대체 테이블에는 레코드 순서가 없으므로, 위치를 기준으로 처음 또는 마지막 N개 레코드를 가져와야 한다면 내보낼 때 순서 열을 추가하십시오.
- **인구 통계 또는 참조 데이터베이스를 먼저 로드해야 합니다.** 데이터베이스가 로드되기 전의 Calgary 읽기는 만들어야 할 테이블의 이름을 밝히며 중단됩니다. `.cydb` 파일 자체에는 공개 리더가 없으므로 Alteryx에서 다시 내보낸 다음(Calgary Input을 CSV 또는 Parquet를 쓰는 Output Data 도구에 연결) 이를 해당 이름의 테이블로 가져오십시오. [읽을 수 없는 .cydb(Calgary) 데이터베이스](/ko/guides/workflows/troubleshoot-alteryx-imports/#읽을-수-없는-cydbcalgary-데이터베이스)를 참조하십시오. 이는 Alteryx가 제공하는 라이선스 인구 통계 및 참조 `.cydb` 파일(Experian, Census 등)의 일반적인 경우입니다. 어떤 변환기도 해당 서드파티 데이터를 재현할 수 없으므로, 라이선스를 보유한 참조 데이터를 직접 가져와 해당 이름의 테이블에 로드하십시오. Geocoder 참조 데이터도 마찬가지입니다.
- **데이터 필드를 저장하지 않는 Calgary Loader는 변환되지 않습니다.** 이 도구가 쓰는 테이블에 열이 없기 때문입니다.
- **사용자 지정 값 교차 집계 그리드는 아직 변환되지 않습니다.** 단일 일반 교차 집계 필드는 변환되어 입력 레코드마다 일치하는 데이터베이스 레코드를 세지만, *명명된* 사용자 지정 값의 그리드는 값마다 개수 열을 하나씩 추가하게 되며 Alteryx는 열이 몇 개인지, 어떤 이름을 붙이는지 문서화하지 않습니다. 열 규약을 역설계할 참조 내보내기를 기다리는 중이며 향후 릴리스에서 추적합니다.

값, 범위, contains, starts-with 쿼리는 모두 필터로 변환됩니다. 열 수준의 대응 항목이 없는 인덱스 작업인 공간 조회 쿼리만 변환되지 않습니다.

## 외부 시스템에 연결

Salesforce, HTTP, Google Analytics, Cassandra, 이메일, Hadoop, Spark 등 Alteryx의 커넥터 엔드포인트는 양방향 모두 변환되지 않습니다.
PlaidCloud는 캔버스의 도구가 아니라 연결을 통해 이러한 시스템에 접근하기 때문입니다. 각 항목은 이름과 함께 변환을 거부하며
작업을 어디로 옮겨야 하는지 알려 줍니다.

| Alteryx 도구 | PlaidCloud에서의 위치 |
| --- | --- |
| Salesforce Input / Output | **Salesforce** 연결 |
| Anaplan | **Anaplan** 연결 |
| HTTP Input | **REST** 연결에 대한 **REST Request** 단계 |
| Google Analytics Input | Google Analytics 탭을 사용하는 **Import: Singer Source** 단계 |
| Cassandra Input | Cassandra 탭을 사용하는 **Import: Singer Source** 단계 |
| Email Input | GMail 탭을 사용하는 **Import: Singer Source** 단계 |
| Hadoop Input / Output | Hive, Impala 또는 Presto 연결을 통한 **Import: SQL** / **Export: SQL** 단계 |
| Spark Input / Output | Databricks 연결을 통한 **Import: SQL** / **Export: SQL** 단계 |

이 중 네 가지는 쓰기 경로가 전혀 없습니다. PlaidCloud는 Google Analytics와 Cassandra에서 읽기만 하고 쓰지는 않으므로,
Google Analytics Output 또는 Cassandra Output 도구는 대신 지원되는 대상으로 가는 **Export: SQL** 단계가 됩니다. 이메일도 데이터 대상이
아닙니다. **Notify: Email** 단계는 사람들에게 알림을 보내므로, Email Output 도구는 Export 단계와 별도의 알림이 됩니다.
**Anaplan** 연결도 같은 방식으로 읽기 전용입니다. 저장된 뷰를 읽거나, 기존 내보내기 작업을 실행하거나, 목록을 PlaidCloud 차원으로
로드하지만, Anaplan에 다시 쓰는 PlaidCloud 단계는 없습니다.

## 변환된 워크플로 검증

운영 워크플로의 경우 변환된 출력을 신뢰할 수 있는 Alteryx 출력과 비교하여 검증하십시오. PlaidCloud 검증은 스키마, 행 수, 행 값에
초점을 맞추며, 워크플로가 행 순서에 의존하지 않는 한 행 순서는 무시합니다. 특수 작업(공간, 퍼지 매칭, OCR, NLP, 보고)은 워크플로를
클라우드 네이티브로 유지하는 관리형 작업 실행기를 통해 실행되며, 머신 러닝 파이프라인은 네이티브
[ML: Train Model](/ko/reference/workflow-steps/machine-learning/ml-train/) 및
[ML: Score](/ko/reference/workflow-steps/machine-learning/ml-score/) 단계로 변환됩니다. 가져오기부터 검증까지의 전체 안내는
[Alteryx 워크플로 마이그레이션](/ko/guides/workflows/migrate-alteryx-workflows/)을 참조하십시오.
