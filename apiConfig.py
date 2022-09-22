
# apiConfig.py
# https://www.data.go.kr (공공데이터포털)

# Author  : Byeong Heon Lee
# Contact : lww7438@gmail.com

# Required Modules
from pytz        import timezone
from datetime    import datetime, timedelta

# * * *   Network Configuration   * * *
INTERVAL_API_CALL = 0.05 # 0.05 Second = 50ms

# * * *   Date Strings   * * *
YESTERDAY             = datetime.strftime(datetime.now(timezone('Asia/Seoul')) - timedelta(1)  , "%Y%m%d") # Yesterday (Format:"YYYYMMDD")
PREVIOUS_BUSINESS_DAY = datetime.strftime(datetime.now(timezone('Asia/Seoul')) - timedelta(3)  , "%Y%m%d") if datetime.now(timezone('Asia/Seoul')).weekday() == 0 else YESTERDAY # Previous Business Day (Format:"YYYYMMDD")
TODAY                 = datetime.strftime(datetime.now(timezone('Asia/Seoul'))                 , "%Y%m%d") # Yesterday (Format:"YYYYMMDD")
TOMORROW              = datetime.strftime(datetime.now(timezone('Asia/Seoul')) + timedelta(1)  , "%Y%m%d") # Yesterday (Format:"YYYYMMDD")
LAST_YEAR             = datetime.strftime(datetime.now(timezone('Asia/Seoul')) - timedelta(365), "%Y")     # Last year (Format:"YYYY")
CURRENT_YEAR          = datetime.strftime(datetime.now(timezone('Asia/Seoul'))                 , "%Y")     # This year (Format:"YYYY")

# * * *   API URLs   * * *
URL_CORP_OUTLINE                       = "http://apis.data.go.kr/1160100/service/GetCorpBasicInfoService/getCorpOutline"          # 금융위원회_기업기본정보: 기업개요조회
URL_STOC_ISSU_STAT                     = "http://apis.data.go.kr/1160100/service/GetStocIssuInfoService/getStocIssuStat"          # 금융위원회_주식발행정보: 주식발행현황조회
URL_KRX_LISTED_INFO                    = "http://apis.data.go.kr/1160100/service/GetKrxListedInfoService/getItemInfo"             # 금융위원회_KRX상장종목정보
URL_ITEM_BASI_INFO                     = "http://apis.data.go.kr/1160100/service/GetStocIssuInfoService/getItemBasiInfo"          # 금융위원회_주식발행정보: 종목기본정보조회
URL_SUMM_FINA_STAT                     = "http://apis.data.go.kr/1160100/service/GetFinaStatInfoService/getSummFinaStat"          # 금융위원회_기업 재무정보: 요약재무제표조회
URL_STOCK_PRICE_INFO                   = "http://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo" # 금융위원회_주식시세정보: 주식시세
URL_STOCK_MARKET_INDEX                 = "http://apis.data.go.kr/1160100/service/GetMarketIndexInfoService/getStockMarketIndex"   # 금융위원회_지수시세정보: 주가지수시세
URL_ISSUCO_BASIC_INFO                  = "http://api.seibro.or.kr/openapi/service/CorpSvc/getIssucoBasicInfo"                     # 한국예탁결제원_기업정보서비스: 기업기본정보 기업개요 조회
URL_ISSUCO_CUSTNO_BY_SHORT_ISIN        = "http://api.seibro.or.kr/openapi/service/CorpSvc/getIssucoCustnoByShortIsin"             # 한국예탁결제원_기업정보서비스: 단축번호로 발행회사번호 조회
URL_KRX_SERIES_DAILY_PRICE             = "http://data-dbg.krx.co.kr/svc/apis/idx/krx_dd_trd"                                      # KRX 시리즈 일별시세정보
URL_KOSPI_SERIES_DAILY_PRICE           = "http://data-dbg.krx.co.kr/svc/apis/idx/kospi_dd_trd"                                    # KOSPI 시리즈 일별시세정보
URL_KOSDAQ_SERIES_DAILY_PRICE          = "http://data-dbg.krx.co.kr/svc/apis/idx/kosdaq_dd_trd"                                   # KOSDAQ 시리즈 일별시세정보
URL_BOND_INDEX_DAILY_PRICE             = "http://data-dbg.krx.co.kr/svc/apis/idx/bon_dd_trd"                                      # 채권지수 시세정보
URL_DERIVATIVE_INDEX_DAILY_PRICE       = "http://data-dbg.krx.co.kr/svc/apis/idx/drvprod_dd_trd"                                  # 파생상품지수 시세정보
URL_PETROLEUM_MARKET_DAILY_TRADING     = "http://data-dbg.krx.co.kr/svc/apis/gen/oil_bydd_trd"                                    # 석유시장 일별매매정보
URL_GOLD_MARKET_DAILY_TRADING          = "http://data-dbg.krx.co.kr/svc/apis/gen/gold_bydd_trd"                                   # 금시장 일별매매정보
URL_CARBON_CREDIT_MARKET_DAILY_TRADING = "http://data-dbg.krx.co.kr/svc/apis/gen/ets_bydd_trd"                                    # 배출권 시장 일별매매정보

# * * *   Contants   * * *
# The number of Maximum Items in Korea Stock Exchange (KOSPI/KOSDAQ/KONEX)
# http://data.krx.co.kr/contents/MDC/MAIN/main/index.cmd
KOSPI_ITEMS   = 939
KOSDAQ_ITEMS  = 1581
KONEX_ITEMS   = 125
ALL_STOCKS_KR = KOSPI_ITEMS + KOSDAQ_ITEMS + KONEX_ITEMS

# The number of Maximum Corporations in Korea
ALL_CORPS = 160000
