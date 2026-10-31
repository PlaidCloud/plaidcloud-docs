---
title: Jupyter 노트북
description: PlaidCloud에서 Jupyter 노트북을 실행하여 대화형 데이터 분석, 시각화, Python 기반 데이터 탐색 워크플로를 수행합니다.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/jupyter-notebook.md
---

Jupyter 노트북과 Jupyter Lab은 데이터를 분석, 탐색, 설명, 보고하는 뛰어난 대화형 기능을 제공합니다.  PlaidCloud를 사용하면 노트북에서 정보를 직접 활용할 수 있습니다.

PlaidCloud는 사용 설정된 경우 각 테넌트 워크스페이스 안에서 JupyterHub를 제공합니다.  아래 문서는 데스크톱이나 별도의 서버에 Jupyter를 따로 설정하는 방법을 안내합니다.

## Jupyter 노트북 설치
Jupyter 노트북이 이미 정상적으로 설치되어 있다고 가정합니다.

### 독립 실행형 Jupyter 노트북 설치
Jupyter 노트북을 로컬에 설치하는 방법은 [Jupyter 설치 문서](https://jupyter.org/install)를 참조하십시오.

### VS Code에 추가
VS Code도 VS Code 안에서 노트북을 직접 실행할 수 있는 확장 기능을 제공합니다.  [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)에서 확장 기능을 설치하십시오.


## PlaidCloud 유틸리티 설치
표준 OAuth 및 JSON-RPC 요청으로도 PlaidCloud에 접근할 수 있지만, 더 간편하게 접근할 수 있도록 미리 만들어진 라이브러리를 사용하시기를 권장합니다.  또한 PlaidCloud 유틸리티 라이브러리에는 Pandas 데이터프레임에서 쓸 수 있는 유용한 데이터 도우미가 포함되어 있습니다.

PlaidCloud 유틸리티를 설치하려면 다음 pip 설치를 수행하십시오.

```bash
pip install plaidcloud-rpc@git+https://github.com/PlaidCloud/plaid-rpc.git@v1.4.0#egg=plaidcloud-rpc
```

```bash
pip install plaidcloud-utilities@git+https://github.com/PlaidCloud/plaid-utilities.git@v1.5.2#egg=plaidcloud-utilities
```

## OAuth 토큰 얻기

OAuth 토큰을 얻는 방법과 자동 인증을 위해 시스템을 구성하는 방법은 [OAuth 설정](/ko/reference/cli/jupyter/oauth-setup/)을 참조하십시오.


## Jupyter 노트북 사용자 인터페이스 열기

노트북 서버를 시작하십시오.



Jupyter 노트북 서버에 로그인한 후 UI에서 새 노트북을 만드십시오.

그러면 빈 노트북이 열립니다.



API 엔드포인트를 통해 PlaidCloud와 통신하는 연결을 만듭니다.

```python
from plaidcloud.utilities.connect import PlaidConnection

conn = PlaidConnection()
```


로컬 테이블 객체를 만든 다음 쿼리하면 결과가 자동으로 [Pandas](https://pandas.pydata.org/) 데이터프레임에 담깁니다.

```python
tbl_sf_cust_master = conn.get_table('Salesforce_Customer_Master') # This gets a table object
df_sf_cust_master = conn.get_data(tbl_sf_cust_master) # This retrieves all the data into a dataframe
```


같은 테이블 객체로 표준 SQLAlchemy 구문을 사용하여 더 고급 쿼리도 작성할 수 있습니다.

```python
df_sf_cust_master_w_sales = conn.get_data(
    tbl_sf_cust_master.select().with_only_columns(
        [tbl_sf_cust_master.c.Id, tbl_sf_cust_master.c.CurrencyIsoCode, tbl_sf_cust_master.c.SyDSalesRegion]
    ).where(
        tbl_sf_cust_master.c.TotalSalesPast3Years > 0
    )
)
```
