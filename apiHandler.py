
# apiHandler.py
# https://www.data.go.kr    (공공데이터포털)
# https://openapi.krx.co.kr (한국거래소 정보데이터시스템 Open API)

# Author  : Byeong Heon Lee
# Contact : lww7438@gmail.com



# Required Modules
import requests
import json                        # JSON Parser
import xml.etree.ElementTree as ET # XML Parser                     
import pandas                as pd
import time
import sys

from apiConfig      import *
from dataManager    import *



# * * *   Functions   * * *
def request_data_to_api(serviceUrl:str, queryParams:dict):
    response = requests.get(set_query_url(service_url=serviceUrl, params=queryParams))

    # Parsing
    try:
        items = json.loads(response.text)['OutBlock_1']
    except:
        return None

    # Assertion & Logging
    if len(items) > 0:
        print(f"Success: {serviceUrl[4:]}")
        return items
    else:
        print(f"Fail: {serviceUrl[4:]}")
        return None

def get_krx_series_daily_price(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    KRX 시리즈 일별시세정보 검색 결과를 반환한다.
    * KRX 시리즈 일별시세정보 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES001_S2.cmd?BO_ID=SsgXTEspyJESKvyXZtCU)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : KRX 시리즈 일별시세정보 (list of dict)
        BAS_DD        (str) : 기준일자 (YYYYMMDD)
        IDX_CLSS      (str) : 계열구분
        IDX_NM        (str) : 지수명
        CLSPRC_IDX    (str) : 종가
        CMPPREVDD_IDX (str) : 대비
        FLUC_RT       (str) : 등락률
        OPNPRC_IDX    (str) : 시가
        HGPRC_IDX     (str) : 고가
        LWPRC_IDX     (str) : 저가
        ACC_TRDVOL    (str) : 거래량
        ACC_TRDVAL    (str) : 거래대금
        MKTCAP        (str) : 상장시가총액  
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"     : basDd,     # 기준일자
    }

    # Request
    return request_data_to_api(URL_KRX_SERIES_DAILY_PRICE, query_params)

def get_kospi_series_daily_price(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    KOSPI 시리즈 일별시세정보 검색 결과를 반환한다.
    * KOSPI 시리즈 일별시세정보 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES001_S2.cmd?BO_ID=EREKZauXnMmxyIlqzeDN)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : KOSPI 시리즈 일별시세정보 (list of dict)
        BAS_DD        (str) : 기준일자 (YYYYMMDD)
        IDX_CLSS      (str) : 계열구분
        IDX_NM        (str) : 지수명
        CLSPRC_IDX    (str) : 종가
        CMPPREVDD_IDX (str) : 대비
        FLUC_RT       (str) : 등락률
        OPNPRC_IDX    (str) : 시가
        HGPRC_IDX     (str) : 고가
        LWPRC_IDX     (str) : 저가
        ACC_TRDVOL    (str) : 거래량
        ACC_TRDVAL    (str) : 거래대금
        MKTCAP        (str) : 상장시가총액  
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"     : basDd,     # 기준일자
    }

    # Request
    return request_data_to_api(URL_KOSPI_SERIES_DAILY_PRICE, query_params)

def get_kosdaq_series_daily_price(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    KOSDAQ 시리즈 일별시세정보 검색 결과를 반환한다.
    * KOSDAQ 시리즈 일별시세정보 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES001_S2.cmd?BO_ID=nimebcamqFNIPNcRrHoO)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : KOSDAQ 시리즈 일별시세정보 (list of dict)
        BAS_DD        (str) : 기준일자 (YYYYMMDD)
        IDX_CLSS      (str) : 계열구분
        IDX_NM        (str) : 지수명
        CLSPRC_IDX    (str) : 종가
        CMPPREVDD_IDX (str) : 대비
        FLUC_RT       (str) : 등락률
        OPNPRC_IDX    (str) : 시가
        HGPRC_IDX     (str) : 고가
        LWPRC_IDX     (str) : 저가
        ACC_TRDVOL    (str) : 거래량
        ACC_TRDVAL    (str) : 거래대금
        MKTCAP        (str) : 상장시가총액  
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"     : basDd,     # 기준일자
    }

    # Request
    return request_data_to_api(URL_KOSDAQ_SERIES_DAILY_PRICE, query_params)

def get_bond_index_daily_price(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    채권지수 시세정보 검색 결과를 반환한다.
    * 채권지수 시세정보 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES001_S2.cmd?BO_ID=vMxIKCtPBUeRytCqkoFv)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : 채권지수 시세정보 (list of dict)
        BAS_DD                     (str) : 기준일자 (YYYYMMDD)
        BND_IDX_GRP_NM             (str) : 지수명	
        TOT_EARNG_IDX              (str) : 총수익지수_종가	
        TOT_EARNG_IDX_CMPPREVDD    (str) : 총수익지수_대비	
        NETPRC_IDX                 (str) : 순가격지수_종가	
        NETPRC_IDX_CMPPREVDD       (str) : 순가격지수_대비	
        ZERO_REINVST_IDX           (str) : 제로재투자지수_종가	
        ZERO_REINVST_IDX_CMPPREVDD (str) : 제로재투자지수_대비	
        CALL_REINVST_IDX           (str) : 콜재투자지수_종가	
        CALL_REINVST_IDX_CMPPREVDD (str) : 콜재투자지수_대비	
        MKT_PRC_IDX	               (str) : 시장가격지수_종가
        MKT_PRC_IDX_CMPPREVDD      (str) : 시장가격지수_대비
        AVG_DURATION               (str) : 듀레이션
        AVG_CONVEXITY_PRC          (str) : 컨벡시티
        BND_IDX_AVG_YD             (str) : YTM
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"     : basDd,     # 기준일자
    }

    # Request
    return request_data_to_api(URL_BOND_INDEX_DAILY_PRICE, query_params)

def get_derivative_index_daily_price(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    파생상품지수 시세정보 검색 결과를 반환한다.
    * 파생상품지수 시세정보 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES001_S2.cmd?BO_ID=rPBjbLtScMwmSXWDOYPd)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : 파생상품지수 시세정보 (list of dict)
        BAS_DD        (str) : 기준일자 (YYYYMMDD)
        IDX_CLSS      (str) : 계열구분	
        IDX_NM        (str) : 지수명	
        CLSPRC_IDX    (str) : 종가	
        CMPPREVDD_IDX (str) : 대비	
        FLUC_RT       (str) : 등락률	
        OPNPRC_IDX    (str) : 시가	
        HGPRC_IDX     (str) : 고가	
        LWPRC_IDX     (str) : 저가	
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"     : basDd,     # 기준일자
    }

    # Request
    return request_data_to_api(URL_BOND_INDEX_DAILY_PRICE, query_params)

def get_kospi_daily_trading(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    유가증권 일별매매정보 검색 결과를 반환한다.
    * 유가증권 일별매매정보 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES002_S2.cmd?BO_ID=JvJFzlAENzZlPBDNGAWC)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : 유가증권 일별매매정보 (list of dict)
        BAS_DD        (str) : 기준일자 (YYYYMMDD)
        ISU_CD        (str) : 종목코드	
        ISU_NM        (str) : 종목명	
        MKT_NM        (str) : 시장구분	
        SECT_TP_NM    (str) : 소속부	
        TDD_CLSPRC    (str) : 종가	
        CMPPREVDD_PRC (str) : 대비	
        FLUC_RT       (str) : 등락률	
        TDD_OPNPRC    (str) : 시가	
        TDD_HGPRC     (str) : 고가	
        TDD_LWPRC	  (str) : 저가
        ACC_TRDVOL    (str) : 거래량
        ACC_TRDVAL    (str) : 거래대금
        MKTCAP        (str) : 시가총액
        LIST_SHRS     (str) : 상장주식수
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"     : basDd,     # 기준일자
    }

    # Request
    return request_data_to_api(URL_KOSPI_DAILY_TRADING, query_params)

def get_kosdaq_daily_trading(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    코스닥 일별매매정보 검색 결과를 반환한다.
    * 코스닥 일별매매정보 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES002_S2.cmd?BO_ID=hZjGpkllgCBCWqeTsYFj)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : 코스닥 일별매매정보 (list of dict)
        BAS_DD        (str) : 기준일자 (YYYYMMDD)
        ISU_CD        (str) : 종목코드	
        ISU_NM        (str) : 종목명	
        MKT_NM        (str) : 시장구분	
        SECT_TP_NM    (str) : 소속부	
        TDD_CLSPRC    (str) : 종가	
        CMPPREVDD_PRC (str) : 대비	
        FLUC_RT       (str) : 등락률	
        TDD_OPNPRC    (str) : 시가	
        TDD_HGPRC     (str) : 고가	
        TDD_LWPRC	  (str) : 저가
        ACC_TRDVOL    (str) : 거래량
        ACC_TRDVAL    (str) : 거래대금
        MKTCAP        (str) : 시가총액
        LIST_SHRS     (str) : 상장주식수
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"     : basDd,     # 기준일자
    }

    # Request
    return request_data_to_api(URL_KOSDAQ_DAILY_TRADING, query_params)

def get_konex_daily_trading(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    코넥스 일별매매정보 검색 결과를 반환한다.
    * 코넥스 일별매매정보 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES002_S2.cmd?BO_ID=hZjGpkllgCBCWqeTsYFj)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : 코넥스 일별매매정보 (list of dict)
        BAS_DD        (str) : 기준일자 (YYYYMMDD)
        ISU_CD        (str) : 종목코드	
        ISU_NM        (str) : 종목명	
        MKT_NM        (str) : 시장구분	
        SECT_TP_NM    (str) : 소속부	
        TDD_CLSPRC    (str) : 종가	
        CMPPREVDD_PRC (str) : 대비	
        FLUC_RT       (str) : 등락률	
        TDD_OPNPRC    (str) : 시가	
        TDD_HGPRC     (str) : 고가	
        TDD_LWPRC	  (str) : 저가
        ACC_TRDVOL    (str) : 거래량
        ACC_TRDVAL    (str) : 거래대금
        MKTCAP        (str) : 시가총액
        LIST_SHRS     (str) : 상장주식수
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"     : basDd,     # 기준일자
    }

    # Request
    return request_data_to_api(URL_KONEX_DAILY_TRADING, query_params)

def get_sw_daily_trading(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    신주인수권증권 일별매매정보 검색 결과를 반환한다.
    * 신주인수권증권 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES002_S2.cmd?BO_ID=erXKnEAzTqcGnkcoSdGA)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : 신주인수권증권 (list of dict)
        BAS_DD               (str) : 기준일자 (YYYYMMDD)
        MKT_NM               (str) : 시장구분	
        ISU_CD               (str) : 종목코드	
        ISU_NM               (str) : 종목명	
        TDD_CLSPRC	         (str) : 종가	
        CMPPREVDD_PRC        (str) : 대비	
        FLUC_RT              (str) : 등락률	
        TDD_OPNPRC           (str) : 시가	
        TDD_HGPRC            (str) : 고가	
        TDD_LWPRC            (str) : 저가	
        ACC_TRDVOL		     (str) : 거래량
        ACC_TRDVAL	         (str) : 거래대금
        MKTCAP               (str) : 시가총액
        LIST_SHRS            (str) : 상장증권수
        EXER_PRC             (str) : 행사가격
        EXST_STRT_DD         (str) : 존속기간_시작일	
        EXST_END_DD          (str) : 존속기간_종료일
        TARSTK_ISU_SRT_CD    (str) : 목적주권_종목코드
        TARSTK_ISU_NM        (str) : 목적주권_종목명	
        TARSTK_ISU_PRSNT_PRC (str) : 목적주권_종가	
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"    : basDd,      # 기준일자
    }

    # Request
    return request_data_to_api(URL_SW_DAILY_TRADING, query_params)

def get_sr_daily_trading(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    신주인수권증서 일별매매정보 검색 결과를 반환한다.
    * 신주인수권증서 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES002_S2.cmd?BO_ID=YieGrzzJtKhbaNLuKmhz)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : 신주인수권증서 (list of dict)
        BAS_DD               (str) : 기준일자 (YYYYMMDD)
        MKT_NM               (str) : 시장구분	
        ISU_CD               (str) : 종목코드	
        ISU_NM               (str) : 종목명	
        TDD_CLSPRC	         (str) : 종가	
        CMPPREVDD_PRC        (str) : 대비	
        FLUC_RT              (str) : 등락률	
        TDD_OPNPRC           (str) : 시가	
        TDD_HGPRC            (str) : 고가	
        TDD_LWPRC            (str) : 저가	
        ACC_TRDVOL		     (str) : 거래량
        ACC_TRDVAL	         (str) : 거래대금
        MKTCAP               (str) : 시가총액
        LIST_SHRS            (str) : 상장증서수
        ISU_PRC              (str) : 신주발행가
        DELIST_DD            (str) : 상장폐지일
        TARSTK_ISU_SRT_CD    (str) : 목적주권_종목코드
        TARSTK_ISU_NM        (str) : 목적주권_종목명	
        TARSTK_ISU_PRSNT_PRC (str) : 목적주권_종가	
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"    : basDd,      # 기준일자
    }

    # Request
    return request_data_to_api(URL_SR_DAILY_TRADING, query_params)

def get_kospi_base_info(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    유가증권 종목기본정보 검색 결과를 반환한다.
    * 유가증권 종목기본정보 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES002_S2.cmd?BO_ID=PiwgMdTwmsenXhmqqxuj)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : 유가증권 종목기본정보 (list of dict)
        ISU_CD             (str) : 표준코드
        ISU_SRT_CD         (str) : 단축코드	
        ISU_NM             (str) : 한글 종목명	
        ISU_ABBRV	       (str) : 한글 종목약명	
        ISU_ENG_NM         (str) : 영문 종목명	
        LIST_DD            (str) : 상장일	
        MKT_TP_NM          (str) : 시장구분	
        SECUGRP_NM         (str) : 증권구분	
        SECT_TP_NM         (str) : 소속부	
        KIND_STKCERT_TP_NM (str) : 주식종류
        PARVAL	           (str) : 액면가
        LIST_SHRS          (str) : 상장주식수
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"    : basDd,      # 기준일자
    }

    # Request
    return request_data_to_api(URL_KOSPI_BASE_INFO, query_params)

def get_kosdaq_base_info(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    코스닥 종목기본정보 검색 결과를 반환한다.
    * 코스닥 종목기본정보 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES002_S2.cmd?BO_ID=CifLHplnUFMgpHIMMPXs)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : 코스닥 종목기본정보 (list of dict)
        ISU_CD             (str) : 표준코드
        ISU_SRT_CD         (str) : 단축코드	
        ISU_NM             (str) : 한글 종목명	
        ISU_ABBRV	       (str) : 한글 종목약명	
        ISU_ENG_NM         (str) : 영문 종목명	
        LIST_DD            (str) : 상장일	
        MKT_TP_NM          (str) : 시장구분	
        SECUGRP_NM         (str) : 증권구분	
        SECT_TP_NM         (str) : 소속부	
        KIND_STKCERT_TP_NM (str) : 주식종류
        PARVAL	           (str) : 액면가
        LIST_SHRS          (str) : 상장주식수
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"    : basDd,      # 기준일자
    }

    # Request
    return request_data_to_api(URL_KOSDAQ_BASE_INFO, query_params)

def get_konex_base_info(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    코넥스 종목기본정보 검색 결과를 반환한다.
    * 코넥스 종목기본정보 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES002_S2.cmd?BO_ID=COgTLqgmGlqyJvaEFNIc)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : 코넥스 종목기본정보 (list of dict)
        ISU_CD             (str) : 표준코드
        ISU_SRT_CD         (str) : 단축코드	
        ISU_NM             (str) : 한글 종목명	
        ISU_ABBRV	       (str) : 한글 종목약명	
        ISU_ENG_NM         (str) : 영문 종목명	
        LIST_DD            (str) : 상장일	
        MKT_TP_NM          (str) : 시장구분	
        SECUGRP_NM         (str) : 증권구분	
        SECT_TP_NM         (str) : 소속부	
        KIND_STKCERT_TP_NM (str) : 주식종류
        PARVAL	           (str) : 액면가
        LIST_SHRS          (str) : 상장주식수
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"    : basDd,      # 기준일자
    }

    # Request
    return request_data_to_api(URL_KONEX_BASE_INFO, query_params)

def get_etf_daily_trading(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    ETF 일별매매정보 검색 결과를 반환한다.
    * ETF 일별매매정보 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES003_S2.cmd?BO_ID=nrEpCLaZpoLCTzPUMxuF)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : ETF 일별매매정보 (list of dict)
        BAS_DD                   (str) : 기준일자 (YYYYMMDD)
        ISU_CD                   (str) : 종목코드
        ISU_NM                   (str) : 종목명
        TDD_CLSPRC	             (str) : 종가
        CMPPREVDD_PRC            (str) : 대비
        FLUC_RT                  (str) : 등락률
        NAV                      (str) : 순자산가치 (NAV)
        TDD_OPNPRC               (str) : 시가
        TDD_HGPRC                (str) : 고가
        TDD_LWPRC                (str) : 저가
        ACC_TRDVOL	             (str) : 거래량
        ACC_TRDVAL               (str) : 거래대금
        MKTCAP                   (str) : 시가총액
        INVSTASST_NETASST_TOTAMT (str) : 순자산총액
        LIST_SHRS                (str) : 상장좌수
        IDX_IND_NM               (str) : 기초지수_지수명
        OBJ_STKPRC_IDX           (str) : 기초지수_종가
        CMPPREVDD_IDX            (str) : 기초지수_대비
        FLUC_RT_IDX	             (str) : 기초지수_등락률
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"    : basDd,      # 기준일자
    }

    # Request
    return request_data_to_api(URL_ETF_DAILY_TRADING, query_params)

def get_etn_daily_trading(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    ETN 일별매매정보 검색 결과를 반환한다.
    * ETN 일별매매정보 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES003_S2.cmd?BO_ID=VujebrcOsZQMybnUuwLk)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : ETN 일별매매정보 (list of dict)
        BAS_DD                   (str) : 기준일자 (YYYYMMDD)
        ISU_CD                   (str) : 종목코드
        ISU_NM                   (str) : 종목명
        TDD_CLSPRC	             (str) : 종가
        CMPPREVDD_PRC            (str) : 대비
        FLUC_RT                  (str) : 등락률
        NAV                      (str) : 순자산가치 (NAV)
        TDD_OPNPRC               (str) : 시가
        TDD_HGPRC                (str) : 고가
        TDD_LWPRC                (str) : 저가
        ACC_TRDVOL	             (str) : 거래량
        ACC_TRDVAL               (str) : 거래대금
        MKTCAP                   (str) : 시가총액
        INVSTASST_NETASST_TOTAMT (str) : 순자산총액
        LIST_SHRS                (str) : 상장좌수
        IDX_IND_NM               (str) : 기초지수_지수명
        OBJ_STKPRC_IDX           (str) : 기초지수_종가
        CMPPREVDD_IDX            (str) : 기초지수_대비
        FLUC_RT_IDX	             (str) : 기초지수_등락률
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"    : basDd,      # 기준일자
    }

    # Request
    return request_data_to_api(URL_ETN_DAILY_TRADING, query_params)

def get_elw_daily_trading(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    ELW 일별매매정보 검색 결과를 반환한다.
    * ELW 일별매매정보 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES003_S2.cmd?BO_ID=brBhSEuDCUNpmfsCslfM)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : ELW 일별매매정보 (list of dict)
        BAS_DD                   (str) : 기준일자 (YYYYMMDD)
        ISU_CD                   (str) : 종목코드
        ISU_NM                   (str) : 종목명
        TDD_CLSPRC	             (str) : 종가
        CMPPREVDD_PRC            (str) : 대비
        FLUC_RT                  (str) : 등락률
        NAV                      (str) : 순자산가치 (NAV)
        TDD_OPNPRC               (str) : 시가
        TDD_HGPRC                (str) : 고가
        TDD_LWPRC                (str) : 저가
        ACC_TRDVOL	             (str) : 거래량
        ACC_TRDVAL               (str) : 거래대금
        MKTCAP                   (str) : 시가총액
        INVSTASST_NETASST_TOTAMT (str) : 순자산총액
        LIST_SHRS                (str) : 상장좌수
        IDX_IND_NM               (str) : 기초지수_지수명
        OBJ_STKPRC_IDX           (str) : 기초지수_종가
        CMPPREVDD_IDX            (str) : 기초지수_대비
        FLUC_RT_IDX	             (str) : 기초지수_등락률
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"    : basDd,      # 기준일자
    }

    # Request
    return request_data_to_api(URL_ELW_DAILY_TRADING, query_params)

def get_gov_bond_daily_trading(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    국채전문유통시장 일별매매정보 검색 결과를 반환한다.
    * 국채전문유통시장 일별매매정보 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES004_S2.cmd?BO_ID=CEnOyORzHgXWpdbUfWyf)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : 국채전문유통시장 일별매매정보 (list of dict)
        BAS_DD           (str) : 기준일자 (YYYYMMDD)
        MKT_NM           (str) : 시장구분
        ISU_CD           (str) : 종목코드
        ISU_NM	         (str) : 종목명
        BND_EXP_TP_NM    (str) : 만기년수
        GOVBND_ISU_TP_NM (str) : 종목구분
        CLSPRC           (str) : 종가_가격
        CMPPREVDD_PRC    (str) : 종가_대비
        CLSPRC_YD        (str) : 종가_수익률
        OPNPRC           (str) : 시가_가격
        OPNPRC_YD	     (str) : 시가_수익률
        HGPRC            (str) : 고가_가격
        HGPRC_YD         (str) : 고가_수익률
        LWPRC            (str) : 저가_가격
        LWPRC_YD         (str) : 저가_수익률	
        ACC_TRDVOL       (str) : 거래량
        ACC_TRDVAL       (str) : 거래대금
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"    : basDd,      # 기준일자
    }

    # Request
    return request_data_to_api(URL_GOV_BOND_DAILY_TRADING, query_params)

def get_general_bond_daily_trading(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    일반채권시장 일별매매정보 검색 결과를 반환한다.
    * 일반채권시장 일별매매정보 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES004_S2.cmd?BO_ID=JfStBNhXISpVVfBHgspT)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : 일반채권시장 일별매매정보 (list of dict)
        BAS_DD           (str) : 기준일자 (YYYYMMDD)
        MKT_NM           (str) : 시장구분
        ISU_CD           (str) : 종목코드
        ISU_NM	         (str) : 종목명
        CLSPRC           (str) : 종가_가격
        CMPPREVDD_PRC    (str) : 종가_대비
        CLSPRC_YD        (str) : 종가_수익률
        OPNPRC           (str) : 시가_가격
        OPNPRC_YD	     (str) : 시가_수익률
        HGPRC            (str) : 고가_가격
        HGPRC_YD         (str) : 고가_수익률
        LWPRC            (str) : 저가_가격
        LWPRC_YD         (str) : 저가_수익률	
        ACC_TRDVOL       (str) : 거래량
        ACC_TRDVAL       (str) : 거래대금
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"    : basDd,      # 기준일자
    }

    # Request
    return request_data_to_api(URL_GENERAL_BOND_DAILY_TRADING, query_params)

def get_small_bond_daily_trading(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    소액채권시장 일별매매정보 검색 결과를 반환한다.
    * 소액채권시장 일별매매정보 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES004_S2.cmd?BO_ID=yrTTOsXuYzHprbWLuYzd)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : 소액채권시장 일별매매정보 (list of dict)
        BAS_DD           (str) : 기준일자 (YYYYMMDD)
        MKT_NM           (str) : 시장구분
        ISU_CD           (str) : 종목코드
        ISU_NM	         (str) : 종목명
        CLSPRC           (str) : 종가_가격
        CMPPREVDD_PRC    (str) : 종가_대비
        CLSPRC_YD        (str) : 종가_수익률
        OPNPRC           (str) : 시가_가격
        OPNPRC_YD	     (str) : 시가_수익률
        HGPRC            (str) : 고가_가격
        HGPRC_YD         (str) : 고가_수익률
        LWPRC            (str) : 저가_가격
        LWPRC_YD         (str) : 저가_수익률	
        ACC_TRDVOL       (str) : 거래량
        ACC_TRDVAL       (str) : 거래대금
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"    : basDd,      # 기준일자
    }

    # Request
    return request_data_to_api(URL_SMALL_BOND_DAILY_TRADING, query_params)

def get_petroleum_market_daily_trading(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    석유시장 일별매매정보 검색 결과를 반환한다.
    * 석유시장 일별매매정보 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES006_S2.cmd?BO_ID=rTvrZvAFKfcaLPOggJtW)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : 석유시장 일별매매정보 (list of dict)
        BAS_DD         (str) : 기준일자 (YYYYMMDD)
        OIL_NM         (str) : 유종구분
        WT_AVG_PRC     (str) : 가중평균가격_경쟁
        WT_DIS_AVG_PRC (str) : 가중평균가격_합의
        ACC_TRDVOL     (str) : 거래량
        ACC_TRDVAL     (str) : 거래대금
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"     : basDd,     # 기준일자
    }

    # Request
    return request_data_to_api(URL_PETROLEUM_MARKET_DAILY_TRADING, query_params)

def get_gold_market_daily_trading(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    금시장 일별매매정보 검색 결과를 반환한다.
    * 금시장 일별매매정보 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES006_S2.cmd?BO_ID=sxveSnWzWNzWxQASsgEG)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : 금시장 일별매매정보 (list of dict)
        BAS_DD        (str) : 기준일자 (YYYYMMDD)
        ISU_CD        (str) : 종목코드	
        ISU_NM        (str) : 종목명	
        TDD_CLSPRC    (str) : 종가	
        CMPPREVDD_PRC (str) : 대비	
        FLUC_RT       (str) : 등락률	
        TDD_OPNPRC    (str) : 시가	
        TDD_HGPRC     (str) : 고가	
        TDD_LWPRC     (str) : 저가	
        ACC_TRDVOL    (str) : 거래량	
        ACC_TRDVAL	  (str) : 거래대금
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"     : basDd,     # 기준일자
    }

    # Request
    return request_data_to_api(URL_GOLD_MARKET_DAILY_TRADING, query_params)

def get_carbon_credit_market_daily_trading(serviceKey:str, basDd:str=PREVIOUS_BUSINESS_DAY):
    """
    배출권 시장 일별매매정보 검색 결과를 반환한다.
    * 배출권 시장 일별매매정보 (http://openapi.krx.co.kr/contents/OPP/USES/service/OPPUSES006_S2.cmd?BO_ID=IZiYdcgRQFMeENJPEMKG)
        
    [Parameters]
    serviceKey (str) : 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키 (Mandatory) 
    basDd      (str) : 기준일자 (Default: YESTERDAY; 이전 영업일)

    [Returns]
    item : 배출권 시장 일별매매정보 (list of dict)
        BAS_DD        (str) : 기준일자 (YYYYMMDD)
        ISU_CD        (str) : 종목코드	
        ISU_NM        (str) : 종목명	
        TDD_CLSPRC    (str) : 종가	
        CMPPREVDD_PRC (str) : 대비	
        FLUC_RT       (str) : 등락률	
        TDD_OPNPRC    (str) : 시가	
        TDD_HGPRC     (str) : 고가	
        TDD_LWPRC     (str) : 저가	
        ACC_TRDVOL    (str) : 거래량	
        ACC_TRDVAL	  (str) : 거래대금
    """

    # Parameter Setting
    query_params = {
        "AUTH_KEY" : serviceKey, # 한국거래소 정보데이터시스템 Open API에서 인가받은 인증키
        "basDd"     : basDd,     # 기준일자
    }

    # Request
    return request_data_to_api(URL_CARBON_CREDIT_MARKET_DAILY_TRADING, query_params)

def get_corp_outline(serviceKey:str, pageNo=1, numOfRows=1, resultType="json", basDt="", crno="", corpNm=""):
    """
    금융위원회_기업기본정보_기업개요조회 검색 결과를 반환한다.
    * 금융위원회_기업기본정보_기업개요조회 (https://www.data.go.kr/data/15043184/openapi.do)
        
    [Parameters]
    serviceKey (str) : 공공데이터 포털에서 받은 인증키 (Mandatory) 
    pageNo     (int) : 페이지 번호 (Default: 1)
    numOfRows  (int) : 한 페이지 결과 수 (Default: ALL_CORPS (한국 전체 법인 수))
    resultType (str) : 구분 (xml, json) (Default: json)
    basDt      (str) : 검색값과 기준일자가 일치하는 데이터를 검색 (Default: "")
    crno       (str) : 법인등록번호 (Default: "")
    corpNm     (str) : 법인의 명칭 (Default: "")

    [Returns]
    item : 한국 주식시장에 상장된 종목들의 기업개요정보 (list of dict)
        basDt               (str) : 기준일자 (YYYYMMDD)
        crno                (str) : 법인등록번호
        corpNm              (str) : 법인명
        corpEnsnNm          (str) : 법인영문명
        enpPbanCmpyNm       (str) : 기업공시회사명
        enpRprFnm           (str) : 기업대표자성명
        corpRegMrktDcd      (str) : 법인등록시장구분코드
        corpRegMrktDcdNm    (str) : 법인등록시장구분코드명
        corpDcd             (str) : 법인구분코드
        corpDcdNm           (str) : 법인구분코드명
        bzno                (str) : 사업자등록번호
        enpOzpno            (str) : 기업구우편번호
        enpBsadr            (str) : 기업기본주소
        enpDtadr            (str) : 기업상세주소
        enpHmpgUrl          (str) : 기업홈페이지URL
        enpTlno             (str) : 기업전화번호
        enpFxno             (str) : 기업팩스번호
        sicNm               (str) : 표준산업분류명
        enpEstbDt           (str) : 기업설립일자
        enpStacMm           (str) : 기업결산월
        enpXchgLstgDt       (str) : 기업거래소상장일자
        enpXchgLstgAbolDt   (str) : 기업거래소상장폐지일자
        enpKosdaqLstgDt     (str) : 기업코스닥상장일자
        enpKosdaqLstgAbolDt (str) : 기업코스닥상장폐지일자
        enpKrxLstgDt        (str) : 기업KONEX상장일자
        enpKrxLstgAbolDt    (str) : 기업KONEX상장폐지일자
        smenpYn             (str) : 중소기업여부
        enpMntrBnkNm        (str) : 기업주거래은행명
        enpEmpeCnt          (str) : 기업종업원수
        empeAvgCnwkTermCtt  (str) : 종업원평균근속기간내용
        enpPn1AvgSlryAmt    (str) : 기업1인평균급여금액
        actnAudpnNm         (str) : 회계감사인명
        audtRptOpnnCtt      (str) : 감사보고서의견내용
        enpMainBizNm        (str) : 기업주요사업명
        fssCorpUnqNo        (str) : 금융감독원법인고유번호
        fssCorpChgDtm       (str) : 금융감독원법인변경일시     
    """
    
    # Parameter Setting
    query_params_corp_outline = {
        "serviceKey" : serviceKey, # 공공데이터 포털에서 받은 인증키
        "pageNo"     : pageNo,     # 페이지 번호
        "numOfRows"  : numOfRows,  # 한 페이지 결과 수
        "resultType" : resultType, # 구분 (xml, json) (Default: json)
        "basDt"      : basDt,      # 검색값과 기준일자가 일치하는 데이터를 검색
        "crno"       : crno,       # 법인등록번호
        "corpNm"     : corpNm      # 법인의 명칭
    }

    # Request
    response_corp_outline = requests.get(set_query_url(service_url=URL_CORP_OUTLINE, params=query_params_corp_outline))

    # Parsing
    try:
        header = json.loads(response_corp_outline.text)["response"]["header"]
        body = json.loads(response_corp_outline.text)["response"]["body"]
        item = body["items"]["item"] # Information of each corporation
    except:
        return None

    # Assertion
    if len(item) == 0:
        return None
    
    # Print Result to Console
    print("Running: Get Corp Outline")
    print("Result Code : %s" % header["resultCode"])   # 결과코드
    print("Result Message : %s" % header["resultMsg"]) # 결과메시지 
    print("numOfRows : %d" % body["numOfRows"])        # 한 페이지 결과 수
    print("pageNo : %d" % body["pageNo"])              # 페이지번호
    print("totalCount : %d" % body["totalCount"])      # 전체 결과 수
    print() # Newline

    return item

def get_stoc_issu_stat(serviceKey:str, pageNo=1, numOfRows=1, resultType="json", basDt="", crno="", stckIssuCmpyNm=""):
    """
    금융위원회_주식발행정보: 주식발행현황조회 검색 결과를 반환한다.
    * 금융위원회_주식발행정보: 주식발행현황조회 (https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15043423)
        
    [Parameters]
    serviceKey     (str) : 공공데이터 포털에서 받은 인증키 (Mandatory)
    pageNo         (int) : 페이지 번호 (Default: 1)
    numOfRows      (int) : 한 페이지 결과 수 (Default: ALL_ITEMS (한국시장 전체 종목 수))
    resultType     (str) : 구분 (xml, json) (Default: json)
    basDt          (str) : 검색값과 기준일자가 일치하는 데이터를 검색 (Default: "")
    crno           (str) : 검색값과 법인등록번호가 일치하는 데이터를 검색 (Default: "")
    stckIssuCmpyNm (str) : 주식발행회사명이 일치하는 데이터를 검색 (Default: "")

    [Returns]
    item : 한국 주식시장에 상장된 종목들의 기본정보 (list of dict)
        basDt          (str) : YYYYMMDD, 조회의 기준일, 통상 거래일
        crno           (str) : 종목의 법인등록번호
        stckIssuCmpyNm (str) : 주식 발행 회사명
        onskTisuCnt    (str) : 보통주 총 발행수
        pfstTisuCnt    (str) : 우선주 총 발행수
    """
    
    # Parameter Setting
    query_params_stoc_issu_stat = {
        "serviceKey"     : serviceKey,      # 공공데이터 포털에서 받은 인증키
        "pageNo"         : pageNo,          # 페이지 번호
        "numOfRows"      : numOfRows,       # 한 페이지 결과 수
        "resultType"     : resultType,      # 구분 (xml, json) (Default: xml)
        "basDt"          : basDt,           # 검색값과 기준일자가 일치하는 데이터를 검색
        "crno"           : crno,            # 검색값과 법인등록번호가 일치하는 데이터를 검색 
        "stckIssuCmpyNm" : stckIssuCmpyNm   # 주식발행회사명이 일치하는 데이터를 검색
    }

    # Request
    response_stoc_issu_stat = requests.get(set_query_url(service_url=URL_STOC_ISSU_STAT, params=query_params_stoc_issu_stat))

    # Parsing
    try:
        header = json.loads(response_stoc_issu_stat.text)["response"]["header"]
        body = json.loads(response_stoc_issu_stat.text)["response"]["body"]
        item = body["items"]["item"] # Information of each stock items
    except:
        return None

    # Assertion
    if len(item) == 0:
        return None
    
    # Print Result to Console
    print("Running: Get Stoc Issu Stat")
    print("Result Code : %s" % header["resultCode"])   # 결과코드
    print("Result Message : %s" % header["resultMsg"]) # 결과메시지 
    print("numOfRows : %d" % body["numOfRows"])        # 한 페이지 결과 수
    print("pageNo : %d" % body["pageNo"])              # 페이지번호
    print("totalCount : %d" % body["totalCount"])      # 전체 결과 수
    print() # Newline

    return item

def get_krx_listed_info(serviceKey:str, pageNo=1, numOfRows=1, resultType="json", basDt="", beginBasDt="", endBasDt="", likeBasDt="", likeSrtnCd="", isinCd="", likeIsinCd="", itmsNm="", likeItmsNm="", crno="", corpNm="", likeCorpNm=""):
    """
    금융위원회_KRX상장종목정보 검색 결과를 반환한다.
    * 금융위원회_KRX상장종목정보 (https://www.data.go.kr/data/15094775/openapi.do)
        
    [Parameters]
    serviceKey (str) : 공공데이터 포털에서 받은 인증키 (Mandatory)
    pageNo     (int) : 페이지 번호 (Default: 1)
    numOfRows  (int) : 한 페이지 결과 수 (Default: ALL_ITEMS (한국시장 전체 종목 수))
    resultType (str) : 구분 (xml, json) (Default: json)
    basDt      (str) : 검색값과 기준일자가 일치하는 데이터를 검색 (Default: "")
    beginBasDt (str) : 기준일자가 검색값보다 크거나 같은 데이터를 검색 (Default: "")
    endBasDt   (str) : 기준일자가 검색값보다 작은 데이터를 검색 (Default: "")
    likeBasDt  (str) : 기준일자값이 검색값을 포함하는 데이터를 검색 (Default: "")
    likeSrtnCd (str) : 단축코드가 검색값을 포함하는 데이터를 검색 (Default: "")
    isinCd     (str) : 검색값과 ISIN코드이 일치하는 데이터를 검색 (Default: "")
    likeIsinCd (str) : ISIN코드가 검색값을 포함하는 데이터를 검색 (Default: "")
    itmsNm     (str) : 검색값과 종목명이 일치하는 데이터를 검색 (Default: "")
    likeItmsNm (str) : 종목명이 검색값을 포함하는 데이터를 검색 (Default: "")
    crno       (str) : 검색값과 법인등록번호가 일치하는 데이터를 검색 (Default: "")
    corpNm     (str) : 검색값과 법인명이 일치하는 데이터를 검색 (Default: "")
    likeCorpNm (str) : 법인명이 검색값을 포함하는 데이터를 검색 (Default: "")

    [Returns]
    item : 한국 주식시장에 상장된 종목들의 기본정보 (dict)
        basDt     (str) : YYYYMMDD, 조회의 기준일, 통상 거래일
        shortIsin (str) : 종목 코드보다 짧으면서 유일성이 보장되는 코드
        srtnCd    (str) : 현선물 통합상품의 종목 코드(12자리)
        mrktCtg   (str) : 시장 구분 (KOSPI/KOSDAQ/KONEX 등)
        itmsNm    (str) : 종목의 명칭
        crno      (str) : 종목의 법인등록번호
        corpNm    (str) : 종목의 법인 명칭
        shotnIsin (str) : 단축 ISIN 코드 (6자리)
    """
    
    # Parameter Setting
    query_params_krx_listed_info = {
        "serviceKey" : serviceKey,  # 공공데이터 포털에서 받은 인증키
        "pageNo"     : pageNo,      # 페이지 번호
        "numOfRows"  : numOfRows,   # 한 페이지 결과 수
        "resultType" : resultType,  # 구분 (xml, json) (Default: xml)
        "basDt"      : basDt,       # 검색값과 기준일자가 일치하는 데이터를 검색
        "beginBasDt" : beginBasDt,  # 기준일자가 검색값보다 크거나 같은 데이터를 검색
        "endBasDt"   : endBasDt,    # 기준일자가 검색값보다 작은 데이터를 검색
        "likeBasDt"  : likeBasDt,   # 기준일자값이 검색값을 포함하는 데이터를 검색
        "likeSrtnCd" : likeSrtnCd,  # 단축코드가 검색값을 포함하는 데이터를 검색
        "isinCd"     : isinCd,      # 검색값과 ISIN코드이 일치하는 데이터를 검색
        "likeIsinCd" : likeIsinCd,  # ISIN코드가 검색값을 포함하는 데이터를 검색
        "itmsNm"     : itmsNm,      # 검색값과 종목명이 일치하는 데이터를 검색
        "likeItmsNm" : likeItmsNm,  # 종목명이 검색값을 포함하는 데이터를 검색
        "crno"       : crno,        # 검색값과 법인등록번호가 일치하는 데이터를 검색 
        "corpNm"     : corpNm,      # 검색값과 법인명이 일치하는 데이터를 검색
        "likeCorpNm" : likeCorpNm,  # 법인명이 검색값을 포함하는 데이터를 검색
    }

    # Request
    response_krx_listed_info = requests.get(set_query_url(service_url=URL_KRX_LISTED_INFO, params=query_params_krx_listed_info))

    # Parsing
    try:
        header = json.loads(response_krx_listed_info.text)["response"]["header"]
        body = json.loads(response_krx_listed_info.text)["response"]["body"]
        item = body["items"]["item"] # Information of each stock items
    except:
        return None

    # Assertion
    if len(item) == 0:
        return None

    # Make new pair (Short ISIN Code made by srtnCd)
    for data in item:
        data["shotnIsin"] = data["srtnCd"][1:] 
    
    # Print Result to Console
    print("Running: Get KRX Listed Info")
    print("Result Code : %s" % header["resultCode"])   # 결과코드
    print("Result Message : %s" % header["resultMsg"]) # 결과메시지 
    print("numOfRows : %d" % body["numOfRows"])        # 한 페이지 결과 수
    print("pageNo : %d" % body["pageNo"])              # 페이지번호
    print("totalCount : %d" % body["totalCount"])      # 전체 결과 수
    print() # Newline

    # Print Result to JSON File
    # with open("krx_listed_info.json", "w", encoding="utf-8") as json_file:
    #     json_file.write("[") # Start of .json file
    #     totalCount = body["totalCount"]
    #     for i in range(0, totalCount): # Iteration for each item
    #         json_file.write("{")
    #         json_file.write('"id":{},'.format(i+1))
    #         json_file.write('"srtnCd":"'  + item[i]["srtnCd"]  + '",')
    #         json_file.write('"isinCd":"'  + item[i]["isinCd"]  + '",')
    #         json_file.write('"itmsNm":"'  + item[i]["itmsNm"]  + '",')
    #         json_file.write('"corpNm":"'  + item[i]["corpNm"]  + '",')
    #         json_file.write('"crno":"'    + item[i]["crno"]    + '",')
    #         json_file.write('"mrktCtg":"' + item[i]["mrktCtg"] + '",')
    #         json_file.write('"basDt":"'   + item[i]["basDt"]   + '"' )
    #         json_file.write("}")

    #         if(i != numOfRows - 1):
    #             json_file.write(",")

    #     json_file.write("]") # End of .json file

    return item

def get_item_basi_info(serviceKey:str, pageNo=1, numOfRows=1, resultType="json", basDt="", crno="", corpNm="", stckIssuCmpyNm=""):
    """
    금융위원회_주식발행정보: 종목기본정보조회 검색 결과를 반환한다.
    * 금융위원회_KRX상장종목정보 (https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15043423)
        
    [Parameters]
    serviceKey     (str) : 공공데이터 포털에서 받은 인증키 (Mandatory)
    pageNo         (int) : 페이지 번호 (Default: 1)
    numOfRows      (int) : 한 페이지 결과 수 (Default: ALL_ITEMS (한국시장 전체 종목 수))
    resultType     (str) : 구분 (xml, json) (Default: json)
    basDt          (str) : 검색값과 기준일자가 일치하는 데이터를 검색 (Default: YESTERDAY)
    crno           (str) : 검색값과 법인등록번호가 일치하는 데이터를 검색 (Default: "")
    corpNm         (str) : 검색값과 법인명이 일치하는 데이터를 검색 (Default: "")
    stckIssuCmpyNm (str) : 주식발행회사명이 검색값을 포함하는 데이터를 검색 (Default: "")

    [Returns]
    item : 한국 주식시장에 상장된 종목들의 기본정보 (dict)
        basDt          (str) : YYYYMMDD, 조회의 기준일, 통상 거래일
        crno           (str) : 종목의 법인등록번호
        isinCd         (str) : ISIN코드
        stckIssuCmpyNm (str) : 주식발행회사명
        isinCdNm       (str) : ISIN코드명
        scrsItmsKcd    (str) : 유가증권종목종류코드
        scrsItmsKcdNm  (str) : 유가증권종목종류코드명
        stckParPrc     (str) : 주식액면가
        issuStckCnt    (str) : 발행주식수
        lstgDt         (str) : 상장일자
        lstgAbolDt     (str) : 상장폐지일자
        dpsgRegDt      (str) : 예탁등록일자
        dpsgCanDt      (str) : 예탁취소일자
        issuFrmtClsfNm (str) : 발행형태구분명
    """

    # Parameter Setting
    query_params_item_basi_info = {
        "serviceKey"     : serviceKey,    # 공공데이터 포털에서 받은 인증키
        "pageNo"         : pageNo,        # 페이지 번호
        "numOfRows"      : numOfRows,     # 한 페이지 결과 수
        "resultType"     : resultType,    # 구분 (xml, json) (Default: xml)
        "basDt"          : basDt,         # 검색값과 기준일자가 일치하는 데이터를 검색
        "crno"           : crno,          # 법인등록번호
        "corpNm"         : corpNm,        # 법인의 명칭
        "stckIssuCmpyNm" : stckIssuCmpyNm # 주식발행회사명
    }

    # Request
    response_item_basi_info = requests.get(set_query_url(service_url=URL_ITEM_BASI_INFO, params=query_params_item_basi_info))

    # Parsing
    try:
        header = json.loads(response_item_basi_info.text)["response"]["header"]
        body = json.loads(response_item_basi_info.text)["response"]["body"]
        item = body["items"]["item"] # Information of each corporation
    except:
        return None

    # Assertion
    if len(item) == 0:
        return None

    # Print Result to Console
    print("Running: Get Item Basi Info")
    print("Result Code : %s" % header["resultCode"])   # 결과코드
    print("Result Message : %s" % header["resultMsg"]) # 결과메시지 
    print("numOfRows : %d" % body["numOfRows"])        # 한 페이지 결과 수
    print("pageNo : %d" % body["pageNo"])              # 페이지번호
    print("totalCount : %d" % body["totalCount"])      # 전체 결과 수
    print() # Newline

    return item

def get_summ_fina_stat(serviceKey:str, pageNo=1, numOfRows=2, resultType="json", crno="", bizYear=LAST_YEAR, type="ALL"):
    """
    금융위원회_기업 재무정보: 요약재무제표조회 검색 결과를 반환한다.
    * 금융위원회_기업 재무정보: 요약재무제표조회 (https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15043459)
        
    [Parameters]
    0. serviceKey (str) : 공공데이터 포털에서 받은 인증키 (Mandatory) 
    1. pageNo     (int) : 페이지 번호 (Default: 1)
    2. numOfRows  (int) : 한 페이지 결과 수 (Default: ALL_CORPS (한국 전체 법인 수))
    3. resultType (str) : 구분 (xml, json) (Default: json)
    4. crno       (str) : 법인등록번호 (Default: "")
    5. bizYear    (str) : 사업연도 (Default: "")
    6. type       (str) : 재무제표 유형 (전체: "ALL", 연결: "CONSOLIDATED", 요약: "SEPARATE") (Default: ALL)

    [Returns]
    item : 한국 주식시장에 상장된 종목들의 기업개요정보 (list of dict)
         0. resultCode    (str) : 결과코드
         1. resultMsg     (str) : 결과메시지
         2. numOfRows     (int) : 한 페이지 결과 수
         3. pageNo        (int) : 페이지 번호
         4. totalCount    (int) : 전체 결과 수
         5. basDt         (str) : 기준일자 (YYYYMMDD)
         6. crno          (str) : 법인등록번호
         7. bizYear       (str) : 사업연도
         8. fnclDcd       (str) : 재무제표구분코드
         9. fnclDcdNm     (str) : 재무제표구분코드명
        10. enpSaleAmt    (str) : 기업매출금액
        11. enpBzopPft    (str) : 기업영업이익
        12. iclsPalClcAmt (str) : 포괄손익계산금액
        13. enpCrtmNpf    (str) : 기업당기순이익
        14. enpTastAmt    (str) : 기업총자산금액
        15. enpTdbtAmt    (str) : 기업총부채금액
        16. enpTcptAmt    (str) : 기업총자본금액
        17. enpCptlAmt    (str) : 기업자본금액
        18. fnclDebtRto   (str) : 재무제표부채비율  
    """
        
    # Parameter Setting
    query_params_summ_fina_stat = {
        "serviceKey" : serviceKey, # 공공데이터 포털에서 받은 인증키
        "pageNo"     : pageNo,     # 페이지 번호
        "numOfRows"  : numOfRows,  # 한 페이지 결과 수
        "resultType" : resultType, # 구분 (xml, json) (Default: xml)
        "crno"       : crno,       # 법인등록번호
        "bizYear"    : bizYear     # 사업연도
    }
    
    # Request
    response_summ_fina_stat = requests.get(set_query_url(service_url=URL_SUMM_FINA_STAT, params=query_params_summ_fina_stat))

    # Parsing
    try:
        header = json.loads(response_summ_fina_stat.text)["response"]["header"]
        body = json.loads(response_summ_fina_stat.text)["response"]["body"]
        item = body["items"]["item"] # Information of each corporation
    except:
        return None

    # Assertion
    if len(item) == 0:
        return None
    
    # Print Result to Console (Logging)
    print("Running: Get Summ Fina Stat")
    print("Result Code : %s" % header["resultCode"])   # 결과코드
    print("Result Message : %s" % header["resultMsg"]) # 결과메시지 
    print("numOfRows : %d" % body["numOfRows"])        # 한 페이지 결과 수
    print("pageNo : %d" % body["pageNo"])              # 페이지번호
    print("totalCount : %d" % body["totalCount"])      # 전체 결과 수
    print() # Newline

    # Return depends on Option 'type'
    if type == "CONSOLIDATED":
        if item[0]["fnclDcd"] in ["110", "ifrs_ConsolidatedMember", "999"]:
            return item
                
    elif type == "SEPARATE":
        if item[0]["fnclDcd"] in ["120", "ifrs_SeparateMember", "999"]:
            return item

    else: # Default is "ALL"
        return item
    
def get_issuco_basic_info(serviceKey:str, issucoCustno=""):
    """
    한국예탁결제원_기업정보서비스: 기업기본정보 기업개요 조회 검색 결과를 반환한다.
    * 한국예탁결제원_기업정보서비스: 기업기본정보 기업개요 조회 (https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15001153)
        
    [Parameters]
    serviceKey   (str) : 공공데이터 포털에서 받은 인증키 (Mandatory)
    issucoCustno (str) : 발행회사번호 (Mandatory)

    [Returns]
    item : 한국 주식시장에 상장된 종목들의 기본정보 (dict)
        agOrgTpcd           (str) : 대행기관구분코드
        agOrgTpcdNm         (str) : 대행기관명
        apliDt              (str) : 상장일
        apliDtY             (str) : 예탁지정일
        bizno               (str) : 사업자번호
        caltotMartTpcd      (str) : 시장구분코드
        caltotMartTpcdNm    (str) : 시장구분명
        ceoNm               (str) : CEO명
        custXtinDt          (str) : 회사소멸일
        engCustNm           (str) : 영문회사명
        engLegFormNm        (str) : 법인형태구분영문명
        founDt              (str) : 설립일
        homepAddr           (str) : 홈페이지주소
        issucoCustno        (str) : 발행회사번호
        pval                (str) : 액면가
        pvalStkqty          (str) : 수권자본금
        repSecnNm           (str) : 발행회사명
        rostCloseTerm       (str) : 명부폐쇄기간
        rostCloseTermTpcd   (str) : 명부폐쇄기간구분코드
        rostCloseTermUnitCd (str) : 명부폐쇄기간단위구분코드
        rostCloseTermUnitNm (str) : 명부폐쇄기간단위구분명
        rostCloseTerms      (str) : 명부폐쇄기간수
        setaccMmdd          (str) : 결산월
        shotnIsin           (str) : 단축코드
        totalStkCnt         (str) : 총발행주식수

    """

    # Parameter Setting
    query_params_issuco_basic_info = {
        "serviceKey"   : serviceKey,  # 공공데이터 포털에서 받은 인증키 (Mandatory) 
        "issucoCustno" : issucoCustno # 발행 번호 (Default: "")
    }

    # Request
    response_issuco_basic_info = requests.get(set_query_url(service_url=URL_ISSUCO_BASIC_INFO, params=query_params_issuco_basic_info))

    # Parsing
    try:
        root = ET.fromstring(response_issuco_basic_info.text)
        header = root.find("header")
        body = root.find("body")
    except:
        return None
    
    items = body.find("item") # Information of each index item

    # Assertion
    if items is None:
        return None

    item = dict()
    for data in items:
        item[data.tag] = data.text

    # Print Result to Console (Logging)
    print("Running: Get ISSUCO BASIC INFO")
    print("Result Code : %s" % header.find("resultCode").text)   # 결과코드
    print("Result Message : %s" % header.find("resultMsg").text) # 결과메시지 
    print() # Newline

    return item

def get_issuco_custno_by_short_isin(serviceKey:str, shortIsin:str):
    """
    한국예탁결제원_기업정보서비스: 단축번호로 발행회사번호 조회 검색 결과를 반환한다.
    * 한국예탁결제원_기업정보서비스: 단축번호로 발행회사번호 조회 (https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15001153)
        
    [Parameters]
    serviceKey (str) : 공공데이터 포털에서 받은 인증키 (Mandatory) 
    shortIsin  (str) : 종목 코드보다 짧으면서 유일성이 보장되는 코드 (Mandatory) 

    [Returns]
    item : 단축번호에 해당되는 발행회사정보 (dict)
        issucoCustno  (str) : 발행회사번호
        issucoNm      (str) : 발행회사명
        listNm        (str) : 상장시장명
    """
    
    # Parameter Setting
    query_params_issuco_custno_by_short_isin = {
        "serviceKey" : serviceKey, # 공공데이터 포털에서 받은 인증키 (Mandatory) 
        "shortIsin"  : shortIsin   # 종목 코드보다 짧으면서 유일성이 보장되는 코드 (Mandatory) 
    }

    # Request
    response_issuco_custno_by_short_isin = requests.get(set_query_url(service_url=URL_ISSUCO_CUSTNO_BY_SHORT_ISIN, params=query_params_issuco_custno_by_short_isin))

    # Parsing
    try:
        root = ET.fromstring(response_issuco_custno_by_short_isin.text)
        header = root.find("header")
        body = root.find("body")
        items = body.find("item") # Information of each index item
    except:
        return None

    # Assertion
    if items is None: 
        return None

    item = dict()
    for data in items:
        item[data.tag] = data.text

    # Print Result to Console (Logging)
    print("Running: Get ISSUCO CUSTNO BY SHORT ISIN")
    print("Result Code : %s" % header.find("resultCode").text)   # 결과코드
    print("Result Message : %s" % header.find("resultMsg").text) # 결과메시지 
    print() # Newline

    return item

def get_financials_kr(serviceKey:str, numOfRow:int=ALL_STOCKS_KR):
    list_financial_data = []

    # 금융위원회_KRX상장종목정보
    # list_financial_data = get_krx_listed_info(serviceKey=serviceKey, numOfRows=ALL_STOCKS_KR)
    list_financial_data = get_krx_listed_info(serviceKey=serviceKey, numOfRows=numOfRow)
    list_financial_data = filter_params(list_financial_data, ["srtnCd", "isinCd", "mrktCtg", "itmsNm", "crno", "corpNm", "shotnIsin"])

    item_id = 1
    for financial_data in list_financial_data:
        # Logging
        print("Collecting data for %s" % financial_data["corpNm"])

        # Give Index
        financial_data['id'] = item_id
        item_id += 1
        
        try:
            # 금융위원회_기업기본정보: 기업개요조회
            if financial_data.get("crno", None) is not None:
                corp_outline = get_corp_outline(serviceKey=serviceKey, crno=financial_data["crno"])
                if corp_outline is not None:
                    financial_data.update(corp_outline[0])
            time.sleep(INTERVAL_API_CALL)

            # 한국예탁결제원_기업정보서비스: 기업기본정보 기업개요 조회
            if financial_data.get("shotnIsin", None) is not None:
                issucoCustno = get_issuco_custno_by_short_isin(serviceKey=serviceKey, shortIsin=financial_data["shotnIsin"])
                if getattr(issucoCustno, "issucoCustno", None) is not None:
                    issuco_basic_info = get_issuco_basic_info(serviceKey=serviceKey, issucoCustno=issucoCustno["issucoCustno"])
                    if issuco_basic_info is not None:
                        financial_data.update(issuco_basic_info)
            time.sleep(INTERVAL_API_CALL)

            # 금융위원회_주식발행정보: 주식발행현황조회
            if financial_data.get("crno", None) is not None:
                stoc_issu_stat = get_stoc_issu_stat(serviceKey=serviceKey, crno=financial_data["crno"])
                if stoc_issu_stat is not None:
                    financial_data.update(stoc_issu_stat[0])
            time.sleep(INTERVAL_API_CALL)

            # 금융위원회_주식발행정보: 종목기본정보조회
            if financial_data.get("crno", None) is not None:
                item_basi_info = get_item_basi_info(serviceKey=serviceKey, crno=financial_data["crno"])
                if item_basi_info is not None:
                    financial_data.update(item_basi_info[0])
            time.sleep(INTERVAL_API_CALL)

            # 금융위윈회_기업 재무정보: 요약재무제표조회
            if financial_data.get("crno", None) is not None:
                summ_fina_stat = get_summ_fina_stat(serviceKey=serviceKey, numOfRows="", crno=financial_data["crno"], type="ALL")
                if summ_fina_stat is not None:
                    financial_data.update(summ_fina_stat[0])
            time.sleep(INTERVAL_API_CALL)

            # 금융위원회_주식시세정보: 주식시세
            if financial_data.get("isinCd", None) is not None:
                stock_price_info = get_stock_price_info(serviceKey=serviceKey, isinCd=financial_data["isinCd"])
                if stock_price_info is not None:
                    financial_data.update(stock_price_info)
            time.sleep(INTERVAL_API_CALL)
        except Exception as err_msg:
            print("Error Detected:", err_msg)
            continue

    return list_financial_data

def get_stock_price_info(serviceKey:str, pageNo=1, numOfRows=1, resultType="json", basDt=PREVIOUS_BUSINESS_DAY, beginBasDt="", endBasDt="", likeBasDt="", likeSrtnCd="", isinCd="", likeIsinCd="", itmsNm="", likeItmsNm="", mrktCls="", beginVs="", endVs="", beginFltRt="", endFltRt="", beginTrqu="", endTrqu="", beginTrPrc="", endTrPrc="", beginLstgStCnt="", endLstgStCnt="", beginMrktTotAmt="", endMrktTotAmt=""):
    """
    금융위원회_주식시세정보: 주식시세 검색 결과를 반환한다.
    * 금융위원회_주식시세정보: 주식시세 (https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15094808)
        
    [Parameters]
    serviceKey      (str) : 공공데이터 포털에서 받은 인증키 (Mandatory) 
    pageNo          (int) : 페이지 번호 (Default: 1)
    numOfRows       (int) : 한 페이지 결과 수 (Default: ALL_CORPS (한국 전체 법인 수))
    resultType      (str) : 구분 (xml, json) (Default: json)
    basDt           (str) : 검색값과 기준일자가 일치하는 데이터를 검색 (Default: "")
    beginBasDt      (str) : 기준일자가 검색값보다 크거나 같은 데이터를 검색 (Default: "")
    endBasDt        (str) : 기준일자가 검색값보다 작은 데이터를 검색 (Default: "")
    likeBasDt       (str) : 기준일자값이 검색값을 포함하는 데이터를 검색 (Default: "")
    likeSrtnCd      (str) : 단축코드가 검색값을 포함하는 데이터를 검색 (Default: "")
    isinCd          (str) : 검색값과 ISIN코드이 일치하는 데이터를 검색 (Default: "")
    likeIsinCd      (str) : ISIN코드가 검색값을 포함하는 데이터를 검색 (Default: "")
    itmsNm          (str) : 검색값과 종목명이 일치하는 데이터를 검색 (Default: "")
    likeItmsNm      (str) : 종목명이 검색값을 포함하는 데이터를 검색 (Default: "")
    mrktCls         (str) : 검색값과 시장구분이 일치하는 데이터를 검색 (Default: "")
    beginVs         (str) : 대비가 검색값보다 크거나 같은 데이터를 검색 (Default: "")
    endVs           (str) : 대비가 검색값보다 작은 데이터를 검색 (Default: "")
    beginFltRt      (str) : 등락률이 검색값보다 크거나 같은 데이터를 검색 (Default: "")
    endFltRt        (str) : 등락률이 검색값보다 작은 데이터를 검색 (Default: "")
    beginTrqu       (str) : 거래량이 검색값보다 크거나 같은 데이터를 검색 (Default: "")
    endTrqu         (str) : 거래량이 검색값보다 작은 데이터를 검색 (Default: "")
    beginTrPrc      (str) : 거래대금이 검색값보다 크거나 같은 데이터를 검색 (Default: "")
    endTrPrc        (str) : 거래대금이 검색값보다 작은 데이터를 검색 (Default: "")
    beginLstgStCnt  (str) : 상장주식수가 검색값보다 크거나 같은 데이터를 검색 (Default: "")
    endLstgStCnt    (str) : 상장주식수가 검색값보다 작은 데이터를 검색 (Default: "")
    beginMrktTotAmt (str) : 시가총액이 검색값보다 크거나 같은 데이터를 검색 (Default: "")
    endMrktTotAmt   (str) : 시가총액이 검색값보다 작은 데이터를 검색 (Default: "")

    [Returns]
    basDt      (string) : 기준일자
    srtnCd     (string) : 종목 코드보다 짧으면서 유일성이 보장되는 코드(6자리)
    isinCd     (string) : 국제 채권 식별 번호. 유가증권(채권)의 국제인증 고유번호
    itmsNm     (string) : 유가증권 국제인증 고유번호 코드 이름
    mrktCtg    (string) : 주식의 시장 구분 (KOSPI/KOSDAQ/KONEX 중 1)
    clpr       (string) : 정규시장의 매매시간종료시까지 형성되는 최종가격
    vs         (number) : 전일 대비 등락
    fltRt      (number) : 전일 대비 등락에 따른 비율
    mkp        (number) : 정규시장의 매매시간개시후 형성되는 최초가격
    hipr       (number) : 하루 중 가격의 최고치
    lopr       (number) : 하루 중 가격의 최저치
    trqu       (number) : 체결수량의 누적 합계
    trPrc      (number) : 거래건 별 체결가격 * 체결수량의 누적 합계
    lstgStCnt  (number) : 종목의 상장주식수
    mrktTotAmt (number) : 종가 * 상장주식수
    """
        
    # Parameter Setting
    query_params_stock_price_info = {
        "serviceKey"      : serviceKey,      # 공공데이터 포털에서 받은 인증키
        "pageNo"          : pageNo,          # 페이지 번호
        "numOfRows"       : numOfRows,       # 한 페이지 결과 수
        "resultType"      : resultType,      # 구분 (xml, json)
        "basDt"           : basDt,           # 검색값과 기준일자가 일치하는 데이터를 검색
        "beginBasDt"      : beginBasDt,      # 기준일자가 검색값보다 크거나 같은 데이터를 검색
        "endBasDt"        : endBasDt,        # 기준일자가 검색값보다 작은 데이터를 검색
        "likeBasDt"       : likeBasDt,       # 기준일자값이 검색값을 포함하는 데이터를 검색
        "likeSrtnCd"      : likeSrtnCd,      # 단축코드가 검색값을 포함하는 데이터를 검색
        "isinCd"          : isinCd,          # 검색값과 ISIN코드이 일치하는 데이터를 검색
        "likeIsinCd"      : likeIsinCd,      # ISIN코드가 검색값을 포함하는 데이터를 검색
        "itmsNm"          : itmsNm,          # 검색값과 종목명이 일치하는 데이터를 검색
        "likeItmsNm"      : likeItmsNm,      # 종목명이 검색값을 포함하는 데이터를 검색
        "mrktCls"         : mrktCls,         # 검색값과 시장구분이 일치하는 데이터를 검색
        "beginVs"         : beginVs,         # 대비가 검색값보다 크거나 같은 데이터를 검색
        "endVs"           : endVs,           # 대비가 검색값보다 작은 데이터를 검색
        "beginFltRt"      : beginFltRt,      # 등락률이 검색값보다 크거나 같은 데이터를 검색
        "endFltRt"        : endFltRt,        # 등락률이 검색값보다 작은 데이터를 검색
        "beginTrqu"       : beginTrqu,       # 거래량이 검색값보다 크거나 같은 데이터를 검색
        "endTrqu"         : endTrqu,         # 거래량이 검색값보다 작은 데이터를 검색
        "beginTrPrc"      : beginTrPrc,      # 거래대금이 검색값보다 크거나 같은 데이터를 검색
        "endTrPrc"        : endTrPrc,        # 거래대금이 검색값보다 작은 데이터를 검색
        "beginLstgStCnt"  : beginLstgStCnt,  # 상장주식수가 검색값보다 크거나 같은 데이터를 검색
        "endLstgStCnt"    : endLstgStCnt,    # 상장주식수가 검색값보다 작은 데이터를 검색
        "beginMrktTotAmt" : beginMrktTotAmt, # 시가총액이 검색값보다 크거나 같은 데이터를 검색
        "endMrktTotAmt"   : endMrktTotAmt    # 시가총액이 검색값보다 작은 데이터를 검색
    }

    # Request
    response_stock_price_info = requests.get(set_query_url(service_url=URL_STOCK_PRICE_INFO, params=query_params_stock_price_info))

    # Parsing
    header = json.loads(response_stock_price_info.text)["response"]["header"]
    body = json.loads(response_stock_price_info.text)["response"]["body"]
    item = body["items"]["item"] # Information of each stock item

    # Assertion
    if len(item) == 0 or item is None:
        return None

    # Formatting on Field 'fltRt' (전일 대비 등락에 따른 비율)
    item = item[0]
    item['fltRt'] = str(item['fltRt'])

    # Case: -d.dd% (Already Complete)
    if (len(item['fltRt']) == 5):
        pass

    # Case: -.dd || d.dd || -d.d
    elif(len(item['fltRt']) == 4):
        # Case: -.dd
        if (item['fltRt'][0:2] == "-."):
            item['fltRt'] = "-0" + item['fltRt'][1:]
        # Case: d.dd
        elif (item['fltRt'][0] != "-"):
            item['fltRt'] = "+" + item['fltRt'][:]
        # Case: -d.d
        elif (item['fltRt'][0] == "-"):
            item['fltRt'] += "0"

    # Case: .dd || -.d || d.d
    elif(len(item['fltRt']) == 3):
        # Case: .dd
        if (item['fltRt'][0] == "."):
            item['fltRt'] = "+0" + item['fltRt'][:]
        # Case: -.d
        elif (item['fltRt'][0:2] == "-."):
            item['fltRt'] = "-0" + item['fltRt'][1:] + "0"
        # Case: d.d
        elif (item['fltRt'][1] == "."):
            item['fltRt'] = "+" + item['fltRt'][:] + "0"
                    
    # Case: .d
    elif(len(item['fltRt']) == 2):
        # Case: .d
        if (item['fltRt'][0] == "."):
            item['fltRt'] = "+0" + item['fltRt'][:] + "0"

    # Case: 0
    elif (item['fltRt'] == "0"):
        item['fltRt'] = "0.00"

    # Add Percentage Symbol
    item['fltRt'] += "%"

    # Print Result to Console (Logging)
    print("Running: Get Stock Price Info")
    print("Result Code : %s" % header["resultCode"])   # 결과코드
    print("Result Message : %s" % header["resultMsg"]) # 결과메시지 
    print("numOfRows : %d" % body["numOfRows"])        # 한 페이지 결과 수
    print("pageNo : %d" % body["pageNo"])              # 페이지번호
    print("totalCount : %d" % body["totalCount"])      # 전체 결과 수
    print() # Newline

    return item

def get_stock_market_index(serviceKey:str, pageNo=1, numOfRows=1, resultType="json", basDt="", beginBasDt="", endBasDt="", likeBasDt="", idxNm="", likeIdxNm="", beginEpyItmsCnt="", endEpyItmsCnt="", beginFltRt="", endFltRt="", beginTrqu="", endTrqu="", beginTrPrc="", endTrPrc="", beginLstgMrktTotAmt="", endLstgMrktTotAmt="", beginLsYrEdVsFltRg="", endLsYrEdVsFltRg="", beginLsYrEdVsFltRt="", endLsYrEdVsFltRt=""):
    """
    금융위원회_지수시세정보: 주가지수시세 검색 결과를 반환한다.
    * 금융위원회_지수시세정보: 주가지수시세 (https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15094807)
        
    [Parameters]
    serviceKey          (str) : 공공데이터 포털에서 받은 인증키 (Mandatory) 
    pageNo              (int) : 페이지 번호 (Default: 1)
    numOfRows           (int) : 한 페이지 결과 수 (Default: ALL_CORPS (한국 전체 법인 수))
    resultType          (str) : 구분 (xml, json) (Default: json)
    basDt               (str) : 검색값과 기준일자가 일치하는 데이터를 검색 (Default: "")
    beginBasDt          (str) : 기준일자가 검색값보다 크거나 같은 데이터를 검색 (Default: "")
    endBasDt            (str) : 기준일자가 검색값보다 작은 데이터를 검색 (Default: "")
    likeBasDt           (str) : 기준일자값이 검색값을 포함하는 데이터를 검색 (Default: "")
    idxNm               (str) : 검색값과 지수명이 일치하는 데이터를 검색
    likeIdxNm           (str) : 지수명이 검색값을 포함하는 데이터를 검색
    beginEpyItmsCnt     (str) : 채용종목수가 검색값보다 크거나 같은 데이터를 검색
    endEpyItmsCnt       (str) : 채용종목수가 검색값보다 작은 데이터를 검색
    beginFltRt          (str) : 등락률이 검색값보다 크거나 같은 데이터를 검색
    endFltRt            (str) : 등락률이 검색값보다 작은 데이터를 검색
    beginTrqu           (str) : 거래량이 검색값보다 크거나 같은 데이터를 검색
    endTrqu             (str) : 거래량이 검색값보다 작은 데이터를 검색
    beginTrPrc          (str) : 거래대금이 검색값보다 크거나 같은 데이터를 검색
    endTrPrc            (str) : 거래대금이 검색값보다 작은 데이터를 검색
    beginLstgMrktTotAmt (str) : 상장시가총액이 검색값보다 크거나 같은 데이터를 검색
    endLstgMrktTotAmt   (str) : 상장시가총액이 검색값보다 작은 데이터를 검색
    beginLsYrEdVsFltRg  (str) : 전년말대비_등락폭이 검색값보다 크거나 같은 데이터를 검색
    endLsYrEdVsFltRg    (str) : 전년말대비_등락폭이 검색값보다 작은 데이터를 검색
    beginLsYrEdVsFltRt  (str) : 전년말대비_등락률이 검색값보다 크거나 같은 데이터를 검색
    endLsYrEdVsFltRt    (str) : 전년말대비_등락률이 검색값보다 작은 데이터를 검색

    [Returns]
    item : 주가지수시세에 대한 정보 (dict)
        lsYrEdVsFltRt  (number) : 지수의 전년말대비 등락율
        basPntm        (string) : 지수를 산출하기 위한 기준시점
        basIdx         (number) : 기준시점의 지수값
        basDt          (string) : 기준일자
        idxCsf         (string) : 지수의 분류명칭
        idxNm          (string) : 지수의 명칭
        epyItmsCnt     (number) : 지수가 채용한 종목 수
        clpr           (number) : 정규시장의 매매시간종료시까지 형성되는 최종가격
        vs             (number) : 전일 대비 등락
        fltRt          (string) : 전일 대비 등락에 따른 비율
        mkp            (number) : 정규시장의 매매시간개시후 형성되는 최초가격
        hipr           (number) : 하루 중 지수의 최고치
        lopr           (number) : 하루 중 지수의 최저치
        trqu           (number) : 지수에 포함된 종목의 거래량 총합
        trPrc          (number) : 지수에 포함된 종목의 거래대금 총합
        lstgMrktTotAmt (number) : 지수에 포함된 종목의 시가총액
        lsYrEdVsFltRg  (number) : 지수의 전년말대비 등락폭
        yrWRcrdHgst    (number) : 지수의 연중최고치
        yrWRcrdHgstDt  (string) : 지수가 연중최고치를 기록한 날짜
        yrWRcrdLwst    (number) : 지수의 연중최저치
        yrWRcrdLwstDt  (string) : 지수가 연중최저치를 기록한 날짜
    """

    # Parameter Setting
    query_params_stock_market_index = {
        "serviceKey"          : serviceKey,          # 공공데이터 포털에서 받은 인증키 (Mandatory) 
        "pageNo"              : pageNo,              # 페이지 번호 (Default: 1)
        "numOfRows"           : numOfRows,           # 한 페이지 결과 수 (Default: ALL_CORPS (한국 전체 법인 수))
        "resultType"          : resultType,          # 구분 (xml, json) (Default: json)
        "basDt"               : basDt,               # 검색값과 기준일자가 일치하는 데이터를 검색 (Default: "")
        "beginBasDt"          : beginBasDt,          # 기준일자가 검색값보다 크거나 같은 데이터를 검색 (Default: "")
        "endBasDt"            : endBasDt,            # 기준일자가 검색값보다 작은 데이터를 검색 (Default: "")
        "likeBasDt"           : likeBasDt,           # 기준일자값이 검색값을 포함하는 데이터를 검색 (Default: "")
        "idxNm"               : idxNm,               # 검색값과 지수명이 일치하는 데이터를 검색
        "likeIdxNm"           : likeIdxNm,           # 지수명이 검색값을 포함하는 데이터를 검색
        "beginEpyItmsCnt"     : beginEpyItmsCnt,     # 채용종목수가 검색값보다 크거나 같은 데이터를 검색
        "endEpyItmsCnt"       : endEpyItmsCnt,       # 채용종목수가 검색값보다 작은 데이터를 검색
        "beginFltRt"          : beginFltRt,          # 등락률이 검색값보다 크거나 같은 데이터를 검색
        "endFltRt"            : endFltRt,            # 등락률이 검색값보다 작은 데이터를 검색
        "beginTrqu"           : beginTrqu,           # 거래량이 검색값보다 크거나 같은 데이터를 검색
        "endTrqu"             : endTrqu,             # 거래량이 검색값보다 작은 데이터를 검색
        "beginTrPrc"          : beginTrPrc,          # 거래대금이 검색값보다 크거나 같은 데이터를 검색
        "endTrPrc"            : endTrPrc,            # 거래대금이 검색값보다 작은 데이터를 검색
        "beginLstgMrktTotAmt" : beginLstgMrktTotAmt, # 상장시가총액이 검색값보다 크거나 같은 데이터를 검색
        "endLstgMrktTotAmt"   : endLstgMrktTotAmt,   # 상장시가총액이 검색값보다 작은 데이터를 검색
        'beginLsYrEdVsFltRg'  : beginLsYrEdVsFltRg,  # 전년말대비_등락폭이 검색값보다 크거나 같은 데이터를 검색
        "endLsYrEdVsFltRg"    : endLsYrEdVsFltRg,    # 전년말대비_등락폭이 검색값보다 작은 데이터를 검색
        "beginLsYrEdVsFltRt"  : beginLsYrEdVsFltRt,  # 전년말대비_등락률이 검색값보다 크거나 같은 데이터를 검색
        "endLsYrEdVsFltRt"    : endLsYrEdVsFltRt     # 전년말대비_등락률이 검색값보다 작은 데이터를 검색
    }

    # Request
    response_stock_market_index = requests.get(set_query_url(service_url=URL_STOCK_MARKET_INDEX, params=query_params_stock_market_index))

    # Parsing
    header = json.loads(response_stock_market_index.text)["response"]["header"]
    body = json.loads(response_stock_market_index.text)["response"]["body"]
    item = body["items"]["item"] # Information of each index item

    # Assertion
    if len(item) == 0 or item is None:
        return None

    # Print Result to Console (Logging)
    print("Running: Get Stock Price Info")
    print("Result Code : %s" % header["resultCode"])   # 결과코드
    print("Result Message : %s" % header["resultMsg"]) # 결과메시지 
    print("numOfRows : %d" % body["numOfRows"])        # 한 페이지 결과 수
    print("pageNo : %d" % body["pageNo"])              # 페이지번호
    print("totalCount : %d" % body["totalCount"])      # 전체 결과 수
    print() # Newline

    return item