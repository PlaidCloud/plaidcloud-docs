---
title: User Defined Transform 단계
description: PlaidCloud 워크플로 단계에서 Python 코드로 사용자 지정 데이터 변환을 만들어 유연하고 강력한 데이터 처리 로직을 구현합니다.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/user-defined-transform.md
---

## 설명

PlaidCloud에 포함된 **표준 워크플로 변환**으로 대개 필요한 거의 모든 작업을 수행할 수 있습니다. 또한 이러한 표준 변환은 성능 면에서 지속적으로 최적화되며 가장 견고한 데이터를 제공합니다. 그러나 표준 옵션을 단독으로 또는 조합하여 사용해도 목표를 달성할 수 없는 경우에는 필요에 맞는 **사용자 정의 변환**을 만들 수 있습니다. PlaidCloud에서는 많은 고급 패키지를 포함한 표준 Python 코드를 사용할 수 있습니다.

사용자 정의 변환을 만들려면 Python 코딩이 필요하며, Python 3.14에서 실행됩니다. 자세한 내용은 [Python 웹사이트](https://www.python.org/)를 참조하십시오.



## 사용자 정의 변환

사용자 정의 함수(UDF)를 만드는 방법은 두 가지입니다.
 - PlaidCloud에서 직접 로직을 작성하고 유지 관리
 - Git 리포지토리에 연결하여 파일을 지정

표준 Python을 사용하는 것 외에도 모든 PlaidCloud API 함수를 바로 사용하여 PlaidCloud와 기본적으로 상호 작용할 수 있습니다. SciPy, PySpark, Pandas 같은 고급 분석 패키지도 가져와 사용할 수 있습니다.

### PlaidCloud에 저장되는 UDF 작성 및 유지 관리
새 사용자 정의 함수(UDF)를 만들려면 사용자 지정 변환이 필요한 워크플로를 열고 **사용자 정의** 탭을 선택한 다음 **사용자 정의 함수 추가** 버튼을 클릭합니다. UDF의 ID를 지정합니다. 만든 후에는 맨 왼쪽의 함수 로직 편집 아이콘을 선택하여 “사용자 정의 함수 편집” 창을 엽니다.

또는 **사용자 정의** 탭에서 **가져오기** 버튼을 사용하여 이전에 만든 사용자 정의 함수를 가져올 수도 있습니다. 이 버튼을 누른 다음 드롭다운 메뉴(현재 워크스페이스의 모든 워크플로가 들어 있음)에서 해당 워크플로를 선택하기만 하면 됩니다. 이어서 가져올 함수를 선택하고 **선택한 함수 가져오기** 버튼을 누릅니다.

함수를 만들거나 가져왔으면 워크플로의 **Analyze 단계** 탭으로 이동하여 **표준 변환**을 추가할 때와 마찬가지로 적절한 위치에 **User Defined Transform** 단계를 추가합니다. 구성 창에서 유형으로 UDF 분석을 선택한 다음 드롭다운 메뉴에서 적절한 **사용자 정의 함수**를 선택합니다.

### Git 리포지토리의 UDF 참조

먼저 **외부 데이터 연결** 영역에서 Git 리포지토리(예: Github, Gitlab 등)에 대한 연결을 만들어야 합니다.

Git 리포지토리 연결을 사용할 수 있게 되면 워크플로의 **Analyze 단계** 탭으로 이동하여 **표준 변환**을 추가할 때와 마찬가지로 적절한 위치에 **User Defined Transform** 단계를 추가합니다. 구성 창에서 유형으로 외부 소스 코드 리포지토리를 선택한 다음 UDF의 연결, 브랜치, 파일 경로를 선택합니다. 브랜치 선택에서는 표준 릴리스 프로세스를 지원하도록 태그도 선택할 수 있습니다.

Git에 있는 파일을 변경하면 UDF가 다음에 실행될 때 자동으로 반영됩니다.

## 소스 및 대상 테이블 구성
UDF 변환 구성에서 정의하지 않고도 UDF에서 테이블에 직접 액세스할 수 있지만, 이 경우 테이블 종속성을 사용할 수 없습니다. 따라서 UDF에서 사용하는 모든 소스 테이블과 대상 테이블을 구성에서 정의할 것을 권장합니다. 구성에서 테이블을 정의하면 UDF 안에서 더 간단한 방식으로 바로 사용할 수도 있습니다(아래 참조).

## 추가 변수 지정
프로젝트 수준과 워크플로 수준의 변수는 모두 표준 API 메서드를 사용하여 UDF 안에서 사용할 수 있지만, 단계에 한정된 추가 변수가 유용한 경우가 많습니다. 이러한 변수는 구성의 **기타 변수** 섹션에서 정의할 수 있습니다.

변수 값은 직접 설정하거나 프로젝트 변수와 워크플로 변수의 조합을 사용하여 동적으로 정의할 수 있습니다.

## Python UDF 예제

### PlaidCloud API 연결 설정이 포함된 일반적인 가져오기

```python
### COMMON PYTHON IMPORTS
# import os
# import pandas as pd
# import numpy as np

### COMMON PLAIDCLOUD IMPORTS
from plaidcloud.utilities.connect import PlaidConnection
from plaidcloud.utilities import frame_manager as fm
# from plaidcloud.utilities import data_helpers as dh

conn = PlaidConnection()
```

### 애플리케이션 로그에 로그 메시지 설정
```python
conn.logger.info('Sample Info Log Message')
conn.logger.warn('Sample Warning Log Message')
conn.logger.error('Sample Error Log Message')
```

### 프로젝트 변수 및 워크플로 변수 액세스
```python
workflow_vars = conn.analyze.workflow.variable_values(project_id=conn.project_id, workflow_id=conn.workflow_id)
variable_1 = workflow_vars.get('my_wf_var_1')

project_vars = conn.analyze.project.variable_values(project_id=conn.project_id)
variable_2 = project_vars.get('my_prj_var_2')
```

### 테이블에 데이터 저장
이 예제는 데이터가 Pandas 데이터프레임에 있다고 가정합니다.

```python
fm.save(dfImport, name='/path_to_table/OUTBOUND_TABLE_NAME', append=False)
```

### 테이블에서 데이터 읽기

테이블을 사용하려면 먼저 테이블 객체를 가져와야 합니다. 객체를 가져온 후에는 `get_data()` 메서드로 쿼리할 수 있습니다. `get_data()` 메서드는 SQLAlchemy 구문도 지원하여 고급 쿼리 작성이 가능합니다. 쿼리 결과는 Pandas 데이터프레임 객체입니다.

```python
tbl_object = conn.get_table('INBOUND_TABLE_NAME')
dfImport = conn.get_data(tbl_object)
dfImportQuery = conn.get_data(
    tblImport.select().with_only_columns(
        [tblImport.c.Col1, tblImport.c.Col2]
    ).where(
        tblImport.c.Col1 == 'FilterValue'
    )
)
```

### 정의된 소스 및 대상 테이블의 데이터 액세스
단계 구성에서 구성한 소스 테이블과 대상 테이블을 사용하는 경우 초기 객체 가져오기(예: `get_table()`)가 자동으로 수행됩니다. 미리 구성된 테이블은 다음 절차로 사용합니다.

```python
# Source Tables as a dict
my_source = conn.udf.source_by_name('my_table')

# All sources as a list
my_sources = conn.udf.sources()

# Target Tables as a dict
my_target = conn.udf.target_by_name('my_table')

# All targets as a list
my_targets = conn.udf.targets()
```

### 단계 변수 액세스
단계 구성에서 정의한 변수는 다음 절차로 액세스합니다.

```python
# Access variables by name
my_var = conn.udf.variable_by_name('my_var')

# All variables as a list
my_vars = conn.udf.variables()
```

### Document에서 파일 읽기
PlaidCloud 연결을 사용하면 Document의 파일에도 간단히 액세스할 수 있습니다. 다음은 파일 내용을 가져와 런타임 컨테이너의 로컬 경로에 저장하는 함수의 예제입니다.

```python
def get_from_document(conn, document_account, remote_path, local_file_path):
    # accounts = conn.document.view.shared_accounts()
    remote_file = base64.b64decode(
        conn.document.view.download(
            account_id=document_account,
            path=remote_path,
        )
    )
    with open(local_file_path, 'wb') as output_file:
        output_file.write(remote_file)

    return local_file_path
```
