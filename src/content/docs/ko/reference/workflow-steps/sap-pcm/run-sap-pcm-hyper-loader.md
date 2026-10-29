---
title: Run SAP PCM Hyper Loader 단계
description: PlaidCloud 워크플로 단계에서 SAP PCM Hyper Loader를 실행하여 PCM 모델에 데이터를 고속으로 대량 로드합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/run-sap-pcm-hyper-loader.md
---

## 설명


직접 테이블 로드를 사용하여 SAP Profitability and Cost Management(PCM) 모델을 로드합니다. 이 프로세스는 Databridge보다 훨씬 빠릅니다. Hyper Loader는 현재 PCM의 거의 모든 데이터, 할당 및 구조 테이블을 지원합니다.


현재 사용할 수 있는 로드 대상 목록은 다음과 같습니다.


* 활동 별칭
* 활동 차원 계층
* 활동 드라이버 별칭
* 활동 드라이버 차원 계층
* 활동 드라이버 값
* BOM 기본 구성
* BOM 외부 단위 비율
* BOM 구성
* BOM 생산량
* BOM 판매 수량
* 비용 개체 1 별칭
* 비용 개체 1 차원 계층
* 비용 개체 2 별칭
* 비용 개체 2 차원 계층
* 비용 개체 3 별칭
* 비용 개체 3 차원 계층
* 비용 개체 4 별칭
* 비용 개체 4 차원 계층
* 비용 개체 5 별칭
* 비용 개체 5 차원 계층
* 비용 개체 할당
* 비용 개체 드라이버
* 라인 항목 별칭
* 라인 항목 세부 정보 별칭
* 라인 항목 세부 정보 차원 계층
* 라인 항목 세부 정보 값
* 라인 항목 차원 계층
* 라인 항목 직접 활동 할당
* 라인 항목 리소스 드라이버 할당
* 라인 항목 값
* 기간 별칭
* 기간 차원 계층
* 리소스 드라이버 별칭
* 리소스 드라이버 차원 계층
* 리소스 드라이버 분할
* 리소스 드라이버 값
* 책임 센터 별칭
* 책임 센터 차원 계층
* 수익
* 수익 별칭
* 수익 차원 계층
* 서비스 별칭
* 서비스 차원 계층
* 분산 별칭
* 분산 차원 계층
* 분산 값
* 버전 별칭
* 버전 차원 계층
* 워크시트 1 별칭
* 워크시트 1 차원 계층
* 워크시트 2 별칭
* 워크시트 2 차원 계층
* 워크시트 값

## 당사의 자격


PlaidCloud는 SAP 공식 파트너이며, SAP PCM 모델 설계 및 구현 관련 서비스의 우선 공급업체입니다.


## 저장 시 검사 항목

**로드 단계** 탭의 각 소스는 **대상 로드 테이블**로 선택한 로더 테이블에 열 이름을 기준으로 매칭되어 스테이징됩니다. 다음과 같은 경우 소스 이름과 함께 저장이 거부됩니다.

- 소스에 대상 로드 테이블이 없거나 PCM 로더 테이블이 아닌 테이블이 지정된 경우 — *Source 'activity_aliases' loads into 'ACTIVITY', which isn't a PCM loader table.*
- 소스의 열이 로더 테이블과 일치하지 않는 경우: 로더 테이블 열이 없거나, 로더 테이블의 유형과 다르거나, 소스, 식 또는 상수가 없는 경우 — *Source 'activity_aliases' doesn't match loader table PPLOAD_ACTIVITY_AL: missing DEFAULTALIAS; no source, expression or constant for ALIAS.* **대상 열을 스키마로 재설정**을 선택하면 로더 테이블을 기준으로 소스의 대상 열이 다시 채워집니다.
- 두 소스의 이름이 같은 경우. 각 소스는 자신의 이름으로 된 파일로 내보내지므로 하나가 다른 하나를 덮어쓰게 됩니다 — *Source name 'activity_aliases' is used more than once; each source needs its own, or one overwrites the other.*


## 예제


드롭다운에서 사용할 에이전트를 선택합니다. 모델 이름을 입력하고 로드 패키지 저장 경로 위치를 선택한 다음, 그 안에서 원하는 하위 폴더를 선택합니다. 아래의 테이블 데이터 선택을 사용하여 소스 테이블 모델과 대상 로드 테이블을 선택합니다. 소스를 검사하고 >> 전파하면 테이블 양쪽의 데이터가 표시됩니다. 데이터를 입력하고 필요한 식을 추가했으면 “저장 및 실행”을 클릭합니다.
