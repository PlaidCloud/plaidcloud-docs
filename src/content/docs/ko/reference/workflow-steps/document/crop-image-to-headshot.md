---
title: Crop Image to Headshot 단계
description: PlaidCloud 워크플로 단계에서 이미지를 정사각형 프로필 사진으로 잘라 디렉터리와 배지에 사용할 표준화된 인물 사진을 만듭니다.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/crop-image-to-headshot.md
---

이미지를 가운데 기준 정사각형으로 자르고 500 × 500 픽셀 JPEG로 크기를 조정합니다. 원본 사진의 가로세로 비율이 제각각인 직원 또는 멤버 디렉터리를 표준화하는 데 유용합니다.

## 입력

- **입력 파일 또는 디렉터리** — 문서 계정에 있는 이미지 또는 이미지가 들어 있는 폴더입니다.
- **출력 파일 또는 디렉터리** — 프로필 사진을 쓸 위치입니다.

## 출력

원본의 가운데에서 잘라 낸 500 × 500 JPEG입니다. 폴더의 경우 각 파일의 프로필 사진은 출력 경로에서 확장자를 뺀 이름의 폴더 안에 쓰입니다.

## 참고

- 이미지의 가운데를 기준으로 잘라 내며 얼굴을 찾지는 않으므로, 원본 사진은 피사체가 가운데에 오도록 구도를 잡으십시오.
- 이미지로 읽을 수 없는 파일은 단계가 실패하지 않고 출력으로 변경 없이 복사됩니다.
- 입력 경로가 없거나 그 안에 파일이 없으면 단계는 경로를 알려 주는 경고와 함께 아무것도 처리하지 않고 완료되며, 워크플로는 계속 진행됩니다.
- 출력 경로는 입력 경로와 같을 수 없습니다.

## 일반적인 용도

- 직원 디렉터리 사진 표준화
- 내부 포털용 일관된 아바타 이미지 생성
- 사원증과 자격 증명용 사진 다듬기

## 관련 항목

- [Convert PDF or Image to JPEG 단계](/ko/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Fix File Extension 단계](/ko/reference/workflow-steps/document/fix-file-extension/)
