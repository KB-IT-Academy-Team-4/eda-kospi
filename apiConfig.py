
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
URL_KOSPI_DAILY_TRADING                = "http://data-dbg.krx.co.kr/svc/apis/sto/stk_bydd_trd"                                    # 유가증권 일별매매정보
URL_KOSDAQ_DAILY_TRADING               = "http://data-dbg.krx.co.kr/svc/apis/sto/ksq_bydd_trd"                                    # 코스닥 일별매매정보
URL_KONEX_DAILY_TRADING                = "http://data-dbg.krx.co.kr/svc/apis/sto/knx_bydd_trd"                                    # 코넥스 일별매매정보
URL_SW_DAILY_TRADING                   = "http://data-dbg.krx.co.kr/svc/apis/sto/sw_bydd_trd"                                     # 신주인수권증권 일별매매정보
URL_SR_DAILY_TRADING                   = "http://data-dbg.krx.co.kr/svc/apis/sto/sr_bydd_trd"                                     # 신주인수권증서 일별매매정보
URL_KOSPI_BASE_INFO                    = "http://data-dbg.krx.co.kr/svc/apis/sto/stk_isu_base_info"                               # 유가증권 종목기본정보
URL_KOSDAQ_BASE_INFO                   = "http://data-dbg.krx.co.kr/svc/apis/sto/ksq_isu_base_info"                               # 코스닥 종목기본정보
URL_KONEX_BASE_INFO                    = "http://data-dbg.krx.co.kr/svc/apis/sto/knx_isu_base_info"                               # 코넥스 종목기본정보
URL_ETF_DAILY_TRADING                  = "http://data-dbg.krx.co.kr/svc/apis/etp/etf_bydd_trd"                                    # ETF 일별매매정보
URL_ETN_DAILY_TRADING                  = "http://data-dbg.krx.co.kr/svc/apis/etp/etn_bydd_trd"                                    # ETN 일별매매정보
URL_ELW_DAILY_TRADING                  = "http://data-dbg.krx.co.kr/svc/apis/etp/elw_bydd_trd"                                    # ELW 일별매매정보
URL_GOV_BOND_DAILY_TRADING             = "http://data-dbg.krx.co.kr/svc/apis/bon/kts_bydd_trd"                                    # 국채전문유통시장 일별매정보
URL_GENERAL_BOND_DAILY_TRADING         = "http://data-dbg.krx.co.kr/svc/apis/bon/kts_bydd_trd"                                    # 일반채권시장 일별매매정보
URL_SMALL_BOND_DAILY_TRADING           = "http://data-dbg.krx.co.kr/svc/apis/bon/smb_bydd_trd"                                    # 소액채권시장 일별매매정보
# 선물 일별매매정보 (주식선물 외)
# 주식선물(유가) 일별매매정보
# 주식선물(코스닥) 일별매매정보
# 옵션 일별매매정보 (주식옵션 외)
# 주식옵션(유가) 일별매매정보
# 주식옵션(코스닥) 일별매매정보
URL_PETROLEUM_MARKET_DAILY_TRADING     = "http://data-dbg.krx.co.kr/svc/apis/gen/oil_bydd_trd"                                    # 석유시장 일별매매정보
URL_GOLD_MARKET_DAILY_TRADING          = "http://data-dbg.krx.co.kr/svc/apis/gen/gold_bydd_trd"                                   # 금시장 일별매매정보
URL_CARBON_CREDIT_MARKET_DAILY_TRADING = "http://data-dbg.krx.co.kr/svc/apis/gen/ets_bydd_trd"                                    # 배출권 시장 일별매매정보

# * * *   Contants   * * *
# The number of Maximum Items in Korea Stock Exchange (KOSPI/KOSDAQ/KONEX)
# http://data.krx.co.kr/contents/MDC/MAIN/main/index.cmd
KOSPI_ITEMS   = 939
KOSDAQ_ITEMS  = 1582
KONEX_ITEMS   = 125
ALL_STOCKS_KR = KOSPI_ITEMS + KOSDAQ_ITEMS + KONEX_ITEMS

# The number of Maximum Corporations in Korea
ALL_CORPS = 160000

# Tickers of World Indexes
WORLD_INDEX_TICKERS = ['DJI',      # Dow Jones (US)
                       'IXIC',     # NASDAQ (US)
                       'US500',    # S&P 500 (US)
                       'VIX',      # S&P 500 VIX (US)
                       'KS11',     # KOSPI (Korea)
                       'KQ11',     # KOSDAQ (Korea)
                       'KS50',     # KOSPI 50 (Korea)
                       'KS100',    # KOSPI 100 (Korea)
                       'KRX100',   # KRX 100 (Korea)
                       'KS200',    # KOSPI 200 (Korea)
                       'JP225',    # NIKKEI 225 Futures (Japan)
                       'STOXX50E', # Euro Stoxx 50  (Europe)
                       'CSI300',	  # CSI 300        (China)
                       'HSI',	  # Hang Seng (Hong Kong)
                       'FTSE',	  # FTSE (England)
                       'DAX',	  # DAX 30 (Germany)
                       'CAC'	      # CAC 40 (France)
]