# varsom_avalanche_client.WarningApi

All URIs are relative to *https://api01.nve.no/hydrology/forecast/avalanche/v5.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**warning_all**](WarningApi.md#warning_all) | **GET** /api/Warning/All/{langkey}/{startdate}/{enddate} | 
[**warning_id**](WarningApi.md#warning_id) | **GET** /api/Warning/Id/{id}/{langkey} | 
[**warning_region**](WarningApi.md#warning_region) | **GET** /api/Warning/Region/{id}/{langkey}/{startdate}/{enddate} | 

# **warning_all**
> list[AvalancheWarningDetail] warning_all(langkey, startdate, enddate)



### Example
```python
from __future__ import print_function
import time
import varsom_avalanche_client
from varsom_avalanche_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_avalanche_client.WarningApi()
langkey = 56 # int | 
startdate = '2013-10-20T19:20:30+01:00' # datetime | 
enddate = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.warning_all(langkey, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarningApi->warning_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **langkey** | **int**|  | 
 **startdate** | **datetime**|  | 
 **enddate** | **datetime**|  | 

### Return type

[**list[AvalancheWarningDetail]**](AvalancheWarningDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warning_id**
> AvalancheWarningDetail warning_id(id, langkey)



### Example
```python
from __future__ import print_function
import time
import varsom_avalanche_client
from varsom_avalanche_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_avalanche_client.WarningApi()
id = 56 # int | 
langkey = 56 # int | 

try:
    api_response = api_instance.warning_id(id, langkey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarningApi->warning_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **langkey** | **int**|  | 

### Return type

[**AvalancheWarningDetail**](AvalancheWarningDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **warning_region**
> list[AvalancheWarningDetail] warning_region(id, langkey, startdate, enddate)



### Example
```python
from __future__ import print_function
import time
import varsom_avalanche_client
from varsom_avalanche_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_avalanche_client.WarningApi()
id = 56 # int | 
langkey = 56 # int | 
startdate = '2013-10-20T19:20:30+01:00' # datetime | 
enddate = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.warning_region(id, langkey, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WarningApi->warning_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **langkey** | **int**|  | 
 **startdate** | **datetime**|  | 
 **enddate** | **datetime**|  | 

### Return type

[**list[AvalancheWarningDetail]**](AvalancheWarningDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

