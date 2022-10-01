
# dataManager.py

# Author  : Byeong Heon Lee
# Contact : lww7438@gmail.com

# Required Modules
import requests
import json                        # JSON Parser
import xml.etree.ElementTree as ET # XML Parser      



# * * *   Functions   * * *
def set_query_url(service_url : str, params : dict):

    # Set URL with Parameters
    request_url = service_url + '?'    
    for k, v in params.items():
        request_url += str(k) + '=' + str(v) + '&'

    return request_url[:-1] # Eliminate last '&' character 

def filter_params(data_list:list, params:list):
    filtered_list=[]

    for data in data_list:
        new_dict = dict()

        for k, v in data.items():
            if k in params:
                new_dict[k] = v
            else:
                continue
        
        filtered_list.append(new_dict)

    return filtered_list

def left_join_by_key(ldata:list, rdata:list, key:str):
    merged_list = []

    for data in ldata:
        merged_list.append(data)

    for item in merged_list:
        for data in rdata:
            if item[key] == data[key]:
                for k, v in data.items():
                    item[k] = v

    return merged_list

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