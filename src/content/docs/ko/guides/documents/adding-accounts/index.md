---
title: 새 문서 계정 추가
description: S3, GCS, Azure Blob, Google Drive, OneDrive, SFTP, WebDAV 등 클라우드 및 온프레미스 문서 스토리지를 PlaidCloud에 연결합니다.
sidebar:
  label: 새 문서 계정 추가
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/index.md
---

S3, Google Cloud Storage, Azure Blob, Google Drive, OneDrive, SFTP, WebDAV 등 클라우드 및 온프레미스 문서 스토리지를 PlaidCloud에 연결합니다. 제공업체마다 자격 증명과 연결 방식이 다릅니다.

가장 빠른 방법은 **PlaidCloud 관리형 버킷**입니다. PlaidCloud가 스토리지를 설정하고 운영하므로 이름만 정하면 되고 다른 구성은 필요하지 않습니다. 이미 보유한 스토리지를 연결하려면 아래에서 해당 제공업체를 선택하십시오.

## 저장된 시크릿은 쓰기 전용입니다

계정의 시크릿은 **개인 키 / 비밀번호** 필드이며, 계정 유형에 따라 **비밀 액세스 키**, **계정 키**, **클라이언트 시크릿**, **액세스 토큰**, **암호**, **시스템 사용자 JSON 키** 또는 **OAuth2 자격 증명 JSON**으로 표시되기도 합니다. 이 시크릿은 쓰기 전용이며, SFTP 계정의 **RSA 개인 키**도 마찬가지입니다. 한 번 저장하면 양식, API, AI 어시스턴트 어디에서도 다시 표시되지 않습니다. 계정을 편집할 때 해당 필드는 비어 있고 *Paste the value; leave blank on edit to keep the saved one.*라는 힌트가 표시됩니다. 저장된 시크릿을 유지하려면 비워 두고, 교체하려면 새 값을 붙여넣으십시오.

계정의 연결 대상을 변경하려면 시크릿을 다시 입력해야 합니다. **시작 경로**의 첫 부분(클라우드 스토리지의 경우 버킷 또는 컨테이너), SFTP 계정의 **호스트 또는 IP 주소**나 **SSH 연결 포트**, OneDrive 계정의 **OneDrive 테넌트 ID**를 변경하는 경우에도 시크릿을 함께 붙여넣어야 하며, 그렇지 않으면 *Changing where the account connects needs its secret entered again*라는 메시지와 함께 저장이 거부됩니다. 이는 계정을 편집할 수 있지만 시크릿을 본 적이 없는 사용자가 그 시크릿을 임의로 지정한 서버로 보내지 못하게 합니다.

PlaidCloud MCP 커넥터를 통해 연결된 AI 어시스턴트도 스토리지 유형, 자격 증명, 시작 경로를 지정하여 계정을 만들고 업데이트할 수 있습니다. 자격 증명은 쓰기 전용이며 계정을 다시 읽을 때 숨겨집니다. 작업 예시는 [OneDrive / SharePoint 계정 추가](/ko/guides/documents/adding-accounts/add-onedrive-account/#ai-어시스턴트로-계정-만들기)를 참조하십시오.
