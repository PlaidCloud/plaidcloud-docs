---
title: 지리 공간 단계
description: PlaidCloud의 모든 지리 공간 워크플로 단계입니다. 공간 파일 가져오기, 버퍼, 매치, 측정, 지오메트리 구성을 지원하며 Alteryx 공간 도구를 모두 포괄합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/spatial/index.md
---

지오메트리를 읽고, 구성하고, 변환하고, 매치하는 워크플로 단계입니다. [지오메트리 식](/ko/reference/workflow-steps/spatial/spatial-sql-recipes/)과 함께 사용하면
Alteryx 공간 도구 전체를 포괄합니다. 도구별 매핑은
[Alteryx 변환 매트릭스](/ko/reference/alteryx-conversion-matrix/)를 참조하십시오.

## 지오메트리는 WKT입니다

모든 공간 단계는 지오메트리를 일반 텍스트 열의 **WKT**(well-known text)로 읽고 씁니다.
선언해야 하는 별도의 지오메트리 유형이 없으며 단계 간 변환도 필요하지 않습니다.
[공간 파일 가져오기](/ko/reference/workflow-steps/spatial/spatial-file-import/)가 생성한 지오메트리 열은
[Spatial Buffer 단계](/ko/reference/workflow-steps/spatial/spatial-buffer/),
[공간 매치](/ko/reference/workflow-steps/spatial/spatial-match/) 또는 SQL
식에서 순서에 관계없이 바로 사용할 수 있습니다.

## 두 가지 실행 경로

각 단계는 올바른 결과를 내는 가장 간단한 경로로 실행됩니다.

| 경로 | 실행되는 항목 | 이유 |
|---|---|---|
| **SQL** — 데이터베이스 내부 | 가장 가까운 항목 찾기, 매치 및 [지오메트리 식](/ko/reference/workflow-steps/spatial/spatial-sql-recipes/) | 조건자 조인과 열 식은 테이블 크기에 맞게 확장되며 행이 웨어하우스 밖으로 나가지 않습니다 |
| **워크플로 엔진** — Shapely 및 GDAL | 지오메트리 형태를 바꾸는 모든 작업 | 버퍼링, 평활화, 디졸브는 데이터베이스 SQL로 표현할 수 없습니다 |

경로는 직접 선택하지 않으며 각 단계 유형마다 하나로 정해져 있습니다. 이 구분은 작업 규모를 산정할 때 중요합니다.
SQL 경로 단계는 웨어하우스에 맞게 확장되고 엔진 경로 단계는 워크플로 파드에 맞게 확장됩니다.

## 지오메트리 로드 및 쓰기

- [공간 파일 가져오기](/ko/reference/workflow-steps/spatial/spatial-file-import/) — MapInfo `.TAB`, ESRI `.shp`, `.kml` 또는 `.geojson` 파일과 그 사이드카 파일을 읽습니다
- [공간 파일 내보내기](/ko/reference/workflow-steps/spatial/spatial-file-export/) — WKT 지오메트리와 속성을 shapefile, GeoJSON, GeoPackage, KML, GML 또는 MapInfo 파일로 기록합니다
- [Geometry in SQL 단계](/ko/reference/workflow-steps/spatial/spatial-sql-recipes/) — 경도/위도 열에서 점을 만듭니다

## 매치 및 측정

- [Spatial Find Nearest 단계](/ko/reference/workflow-steps/spatial/spatial-find-nearest/) — 한 테이블의 각 행에 대해 다른 테이블에서 가장 가까운 N개 행을 거리와 함께 찾습니다
- [공간 매치](/ko/reference/workflow-steps/spatial/spatial-match/) — 지오메트리가 교차하거나, 내부에 있거나, 포함하는 행을 짝짓습니다
- [Spatial Match (Intersect / Unmatched) 단계](/ko/reference/workflow-steps/spatial/spatial-match-executor/) — 동일한 매치를 수행하되 겹치는 지오메트리 또는 일치하지 않은 행을 출력합니다
- [Spatial Info 단계](/ko/reference/workflow-steps/spatial/spatial-info/) — 면적, 길이, 중심점, 경계 사각형을 측지 방식으로 측정합니다
- [공간 다시 투영](/ko/reference/workflow-steps/spatial/spatial-reproject/) — 지오메트리를 한 좌표 참조 시스템에서 다른 시스템으로 변환합니다

## 지오메트리 형태 변경

- [Spatial Buffer 단계](/ko/reference/workflow-steps/spatial/spatial-buffer/) — 각 지오메트리를 고정 거리만큼 확장합니다
- [Spatial Trade Area 단계](/ko/reference/workflow-steps/spatial/spatial-trade-area/) — 실제 단위로 크기를 지정한 동심 버퍼입니다
- [Spatial Generalize 단계](/ko/reference/workflow-steps/spatial/spatial-generalize/) — 허용 오차에 맞게 단순화합니다
- [Spatial Smooth 단계](/ko/reference/workflow-steps/spatial/spatial-smooth/) — 지정한 패스 수만큼 평활화합니다
- [공간 처리](/ko/reference/workflow-steps/spatial/spatial-process/) — 두 지오메트리 열의 교집합, 합집합을 구하거나 한쪽에서 다른 쪽을 제거합니다

## 구성 및 분해

- [Spatial Poly-Build 단계](/ko/reference/workflow-steps/spatial/spatial-poly-build/) — 점 그룹마다 폴리곤 또는 볼록 껍질을 만듭니다
- [Spatial Poly-Split 단계](/ko/reference/workflow-steps/spatial/spatial-poly-split/) — 꼭짓점, 구성 폴리곤 또는 구멍마다 한 행씩 만듭니다
- [공간 결합](/ko/reference/workflow-steps/spatial/spatial-combine/) — 각 그룹의 지오메트리를 하나로 디졸브합니다
- [Spatial Centroid 단계](/ko/reference/workflow-steps/spatial/spatial-centroid/) — 각 지오메트리의 중심점을 추가합니다
- [Spatial Point to Line 단계](/ko/reference/workflow-steps/spatial/spatial-point-to-line/) — 각 그룹의 점을 이어 선으로 만듭니다
- [Spatial Line to Polygon 단계](/ko/reference/workflow-steps/spatial/spatial-line-to-polygon/) — 각 선을 닫아 폴리곤으로 만듭니다
- [Spatial Make Grid 단계](/ko/reference/workflow-steps/spatial/spatial-make-grid/) — 범위를 정사각형 셀로 나눕니다

## 식 참조

- [지오메트리 함수(Lakehouse v1)](/ko/reference/expressions/lakehouse-v1/09-geometry-functions/) — `ST_*` 계열
- [지리 함수(Lakehouse v1)](/ko/reference/expressions/lakehouse-v1/09-geo-functions/) — H3 육각형 인덱싱 및 지오해시
- [공간 함수(Lakehouse v2)](/ko/reference/expressions/lakehouse-v2/17-spatial-functions/)

## 관련 항목

- [지리 공간 분석](/ko/guides/workflows/geospatial-analytics/) — 소스 파일에서 게시된 지도까지의 실제 사례 경로
- [공간 Alteryx 워크플로 마이그레이션](/ko/guides/workflows/migrate-spatial-alteryx-workflows/)
- [Report Map](/ko/reference/workflow-steps/reports/report-map/) — 보고서에 지오메트리를 렌더링합니다
- [패키지 매크로 단계](/ko/reference/workflow-steps/macros/) — Heat Map 및 Pie Wedge Trade Area
