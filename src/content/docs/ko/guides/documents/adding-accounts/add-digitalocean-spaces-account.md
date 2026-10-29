---
title: DigitalOcean Spaces 계정 추가
description: DigitalOcean의 S3 호환 객체 스토리지를 사용해 데이터 파일을 가져오고 내보낼 수 있도록 PlaidCloud에 DigitalOcean Spaces 스토리지 계정을 추가합니다.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-digitalocean-spaces-account.md
---

## DigitalOcean Spaces 설정

다음 단계는 DigitalOcean 제어판에서 완료해야 합니다.

1. [DigitalOcean 제어판](https://cloud.digitalocean.com)에 로그인합니다
2. 왼쪽 사이드바에서 **Spaces Object Storage**로 이동합니다
3. Space가 아직 없으면 만듭니다. Space 이름과 리전(예: `nyc3`)을 기록해 둡니다.
4. (Tokens 섹션 아래의) **API > Spaces Keys**로 이동합니다
5. **Generate New Key**를 선택합니다
6. 키 이름을 지정합니다
7. **Key**(액세스 키)와 **Secret**을 복사합니다. 아래 PlaidCloud Document 설정에 사용할 수 있도록 둘 다 저장합니다. 비밀 키는 한 번만 표시됩니다.
8. Space 리전의 엔드포인트 URL을 기록해 둡니다. `https://{region}.digitaloceanspaces.com`(예: `https://nyc3.digitaloceanspaces.com`) 형식을 따릅니다

이제 PlaidCloud Document에 DigitalOcean Spaces 계정을 추가하는 데 필요한 모든 것을 갖추었습니다.


## PlaidCloud Document 설정

1. PlaidCloud에 로그인합니다
2. 새 문서 계정을 둘 워크스페이스를 선택합니다
3. `Document > Manage Accounts`로 이동합니다
4. `+ New Account` 버튼을 선택합니다
5. 서비스 유형으로 `DigitalOcean Spaces`를 선택합니다
6. 이름과 설명을 입력합니다
7. **시작 경로**에 엔드포인트 URL 뒤에 Space 이름을 붙여 입력합니다: `https://nyc3.digitaloceanspaces.com/my-space`
8. **리전**을 입력합니다(예: `nyc3`, `sfo3`, `ams3`)
9. 사용 목적에 맞는 **보안 모델**을 선택합니다. 잘 모르겠으면 `Private`로 둡니다.
10. **Key**를 인증 자격 증명 아래의 액세스 키 ID 필드에 붙여넣습니다
11. **Secret**을 인증 자격 증명 아래의 비밀 액세스 키 필드에 붙여넣습니다
12. 저장 버튼을 선택하면 새 문서 계정이 활성화됩니다
