---
title: 집계 함수 (Lakehouse v1)
description: "Lakehouse v1 SQL 집계 함수: 행을 요약합니다 — SUM, AVG, MIN, MAX, COUNT 및 통계 집계 함수."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/index.md
---

집계 함수는 값 집합에 대해 계산을 수행하고 단일 결과를 반환하는 SQL의 핵심 도구입니다.

이 함수를 사용하면 데이터베이스에서 데이터를 추출하고 요약하여 유용한 인사이트를 얻을 수 있습니다.

| 함수 이름                                                    | 기능                                                                 | 
|------------------------------------------------------------------|------------------------------------------------------------------------------|
| [ANY](aggregate-any)                                             | 지정한 조건을 충족하는 행이 있는지 확인합니다                              | 
| [APPROX_COUNT_DISTINCT](aggregate-approx-count-distinct)         | HyperLogLog로 고유 값의 개수를 추정합니다                     | 
| [ARG_MAX](aggregate-arg-max)                                     | val 값이 최대일 때의 arg 값을 찾습니다                                | 
| [ARG_MIN](aggregate-arg-min)                                     | val 값이 최소일 때의 arg 값을 찾습니다                                | 
| [AVG_IF](aggregate-avg-if)                                       | 조건을 충족하는 행의 평균을 계산합니다                          | 
| [ARRAY_AGG](aggregate-array-agg)                                 | 열의 모든 값을 배열로 변환합니다                              |
| [AVG](aggregate-avg)                                             | 특정 열의 평균값을 계산합니다                            | 
| [COUNT_DISTINCT](aggregate-count-distinct)                       | 열에서 고유 값의 개수를 셉니다                             | 
| [COUNT_IF](aggregate-count-if)                                   | 지정한 조건을 충족하는 행의 수를 셉니다                                    | 
| [COUNT](aggregate-count)                                         | 특정 기준을 충족하는 행의 수를 셉니다                         | 
| [COVAR_POP](aggregate-covar-pop)                                 | 숫자 쌍 집합의 모공분산을 반환합니다                   | 
| [COVAR_SAMP](aggregate-covar-samp)                               | 숫자 쌍 집합의 표본 공분산을 반환합니다                       | 
| [GROUP_ARRAY_MOVING_AVG](aggregate-group-array-moving-avg)       | 입력 값의 이동 평균을 계산한 요소로 구성된 배열을 반환합니다 |
| [GROUP_ARRAY_MOVING_SUM](aggregate-group-array-moving-sum)       | 입력 값의 이동 합계를 계산한 요소로 구성된 배열을 반환합니다     |
| [HISTOGRAM](aggregate-histogram)                                | 등높이 버킷 방식으로 데이터 분포 히스토그램을 생성합니다        | 
| [JSON_ARRAY_AGG](aggregate-json-array-agg)                      | NULL을 건너뛰면서 값을 JSON 배열로 변환합니다                           | 
| [JSON_OBJECT_AGG](aggregate-json-object-agg)                    | 키-값 쌍을 JSON 객체로 변환합니다                                 | 
| [KURTOSIS](aggregate-kurtosis)                                   | 값 집합의 초과 첨도를 계산합니다                            | 
| [MAX_IF](aggregate-max-if)                                       | 조건을 충족하는 행의 최댓값을 찾습니다                         | 
| [MAX](aggregate-max)                                             | 특정 열에서 가장 큰 값을 찾습니다                                 | 
| [MEDIAN](aggregate-median)                                       | 특정 열의 중앙값을 계산합니다                             | 
| [MEDIAN_TDIGEST](aggregate-median-tdigest)                       | t-digest 알고리즘으로 특정 열의 중앙값을 계산합니다    | 
| [MIN_IF](aggregate-min-if)                                       | 조건을 충족하는 행의 최솟값을 찾습니다                         | 
| [MIN](aggregate-min)                                             | 특정 열에서 가장 작은 값을 찾습니다                                | 
| [QUANTILE_CONT](aggregate-quantile-cont)                         | 특정 열의 보간된 분위수를 계산합니다                   |
| [QUANTILE_DISC](aggregate-quantile-disc)                         | 특정 열의 분위수를 계산합니다                                | 
| [QUANTILE_TDIGEST](aggregate-quantile-tdigest)                   | t-digest 알고리즘으로 분위수를 계산합니다                             |
| [QUANTILE_TDIGEST_WEIGHTED](aggregate-quantile-tdigest-weighted) | t-digest 알고리즘으로 가중치를 적용한 분위수를 계산합니다               |
| [RETENTION](aggregate-retention)                                 | 이벤트 집합의 리텐션을 계산합니다                                     | 
| [SKEWNESS](aggregate-skewness)                                   | 값 집합의 왜도를 계산합니다                                   | 
| [STDDEV_POP](aggregate-stddev-pop)                               | 열의 모집단 표준 편차를 계산합니다                     | 
| [STDDEV_SAMP](aggregate-stddev-samp)                             | 열의 표본 표준 편차를 계산합니다                         | 
| [STRING_AGG](aggregate-string-agg)                               | NULL이 아닌 모든 값을 문자열로 변환하여 구분자로 구분해 연결합니다       |
| [SUM_IF](aggregate-sum-if)                                       | 특정 열에서 조건을 충족하는 값의 합계를 구합니다                  | 
| [SUM](aggregate-sum)                                             | 특정 열의 값을 모두 더합니다                                      | 
| [WINDOW_FUNNEL](aggregate-windowfunnel)                          | 시간순으로 정렬된 이벤트 시퀀스에서 사용자 행동을 분석합니다                  |
