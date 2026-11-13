---
title: Google Drive 계정 추가
description: Google Drive 클라우드 스토리지를 사용해 데이터 파일을 가져오고 내보낼 수 있도록 PlaidCloud에 Google Drive 스토리지 계정을 추가합니다.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-drive-account.md
---

## Google Drive 설정

다음 단계는 PlaidCloud가 Google Drive에 액세스하는 데 사용할 수 있는 서비스 계정을 만들기 위해 Google Cloud Console에서 완료해야 합니다.

### Google Cloud 프로젝트 만들기

1. [Google Cloud Console](https://console.cloud.google.com)에 로그인합니다
2. 새 프로젝트를 만들거나 기존 프로젝트를 선택합니다

### Google Drive API 사용 설정

1. **APIs & Services > Library**로 이동합니다
2. **Google Drive API**를 검색합니다
3. 이를 선택하고 **사용**을 클릭합니다

### 서비스 계정 만들기

1. **APIs & Services > Credentials**로 이동합니다
2. **+ Create Credentials > Service account**를 선택합니다
3. 서비스 계정의 이름을 입력합니다(예: `plaidcloud-drive`)
4. **Create and Continue**를 선택합니다
5. 필요한 경우 역할을 부여합니다(읽기 전용은 **뷰어**, 읽기/쓰기는 **Editor** 등). **계속**을 선택합니다.
6. **완료**를 선택합니다

### 서비스 계정 키 생성

1. **Service Accounts** 목록에서 방금 만든 서비스 계정을 선택합니다
2. **Keys** 탭으로 이동합니다
3. **키 추가 > 새로 만들기**를 선택합니다
4. **JSON** 형식을 선택하고 **만들기**를 선택합니다
5. JSON 키 파일이 다운로드됩니다. 이 파일에는 PlaidCloud가 사용할 자격 증명이 들어 있으므로 안전하게 보관하십시오.

### 서비스 계정과 Drive 콘텐츠 공유

1. 서비스 계정의 이메일 주소를 복사합니다(예: `plaidcloud-drive@your-project.iam.gserviceaccount.com`)
2. Google Drive에서 PlaidCloud가 액세스하도록 하려는 폴더를 이 이메일 주소와 공유하고 **Editor** 액세스를 부여합니다. 공유 드라이브를 사용하려면 대신 서비스 계정을 해당 공유 드라이브의 멤버로 추가합니다.

이제 PlaidCloud Document에 Google Drive 계정을 추가하는 데 필요한 모든 것을 갖추었습니다.


## PlaidCloud Document 설정

1. PlaidCloud에 로그인합니다
2. 새 문서 계정을 둘 워크스페이스를 선택합니다
3. `Document > Manage`로 이동합니다
4. **새 계정** 버튼을 선택합니다
5. 서비스 유형으로 `Google Drive`를 선택합니다
6. 이름과 설명을 입력합니다
7. **시작 경로** 필드에 공유 폴더 경로를 입력하거나, 공유된 모든 콘텐츠에 액세스하려면 비워 둡니다
8. 사용 목적에 맞는 **보안 모델**을 선택합니다. 잘 모르겠으면 `Private`로 둡니다.
9. 인증 자격 증명 아래의 계정 개인 키 필드에 서비스 계정 JSON 키 파일의 전체 내용을 붙여넣습니다
10. 저장 버튼을 선택하면 새 문서 계정이 활성화됩니다

## 워크플로에서 계정 사용

Google Drive 계정은 Document 브라우저뿐 아니라 워크플로에서도 사용할 수 있습니다. 단계에서 파일을 나열, 가져오기, 내보내기, 복사, 이동, 이름 바꾸기, 삭제할 수 있으며 폴더를 만들 수도 있습니다.

- **위치.** 계정의 최상위 위치는 서비스 계정과 공유된 폴더와 서비스 계정이 멤버로 속한 공유 드라이브입니다. 경로는 `Finance/Reports/2026`처럼 폴더 이름입니다. 공유 폴더나 공유 드라이브 두 개 이상의 이름이 같으면 계정이 해당 이름을 열지 않습니다. 하나만 남기고 나머지의 이름을 바꾸거나 공유를 해제하십시오.
- **Google Sheets.** Google 스프레드시트는 `.xlsx` 내보내기로 읽히며 `Name.xlsx`로 표시됩니다. Docs, Slides 같은 다른 Google Workspace 파일은 읽을 수 없습니다.
- **내 드라이브의 새 파일.** 서비스 계정에는 자체 스토리지가 없으므로, 개인의 내 드라이브에 있는 폴더에서는 기존 파일을 덮어쓸 수는 있지만 새 파일을 만들 수는 없습니다. 먼저 해당 위치에 파일을 만들거나, 새 파일과 폴더를 허용하는 공유 드라이브의 폴더를 사용하십시오.
- **없는 폴더.** 존재하지 않는 폴더는 오류가 발생하지 않고 빈 폴더로 나열됩니다.
- **제한.** Google이 요청을 제한하거나 일시적인 오류를 반환하면 PlaidCloud가 자동으로 다시 시도합니다.
