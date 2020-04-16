# varsom_avalanche_client.RegionSummaryApi

All URIs are relative to *https://api01.nve.no/hydrology/forecast/avalanche/v5.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**region_summary_detail**](RegionSummaryApi.md#region_summary_detail) | **GET** /api/RegionSummary/Detail/{langkey}/{startdate}/{enddate} | 
[**region_summary_obs**](RegionSummaryApi.md#region_summary_obs) | **GET** /api/RegionSummary/Obs/{langkey}/{startdate}/{enddate} | 
[**region_summary_simple**](RegionSummaryApi.md#region_summary_simple) | **GET** /api/RegionSummary/Simple/{langkey}/{startdate}/{enddate} | 
[**region_summary_summary**](RegionSummaryApi.md#region_summary_summary) | **GET** /api/RegionSummary/Summary/{langkey}/{startdate}/{enddate} | 

# **region_summary_detail**
> list[RegionSummary] region_summary_detail(langkey, startdate, enddate)



### Example
```python
from __future__ import print_function
import time
import varsom_avalanche_client
from varsom_avalanche_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_avalanche_client.RegionSummaryApi()
langkey = 56 # int | 
startdate = '2013-10-20T19:20:30+01:00' # datetime | 
enddate = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.region_summary_detail(langkey, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionSummaryApi->region_summary_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **langkey** | **int**|  | 
 **startdate** | **datetime**|  | 
 **enddate** | **datetime**|  | 

### Return type

[**list[RegionSummary]**](RegionSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **region_summary_obs**
> list[RegionSummaryObs] region_summary_obs(langkey, startdate, enddate)



### Example
```python
from __future__ import print_function
import time
import varsom_avalanche_client
from varsom_avalanche_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_avalanche_client.RegionSummaryApi()
langkey = 56 # int | 
startdate = '2013-10-20T19:20:30+01:00' # datetime | 
enddate = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.region_summary_obs(langkey, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionSummaryApi->region_summary_obs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **langkey** | **int**|  | 
 **startdate** | **datetime**|  | 
 **enddate** | **datetime**|  | 

### Return type

[**list[RegionSummaryObs]**](RegionSummaryObs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **region_summary_simple**
> list[RegionSummary] region_summary_simple(langkey, startdate, enddate)



### Example
```python
from __future__ import print_function
import time
import varsom_avalanche_client
from varsom_avalanche_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_avalanche_client.RegionSummaryApi()
langkey = 56 # int | 
startdate = '2013-10-20T19:20:30+01:00' # datetime | 
enddate = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.region_summary_simple(langkey, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionSummaryApi->region_summary_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **langkey** | **int**|  | 
 **startdate** | **datetime**|  | 
 **enddate** | **datetime**|  | 

### Return type

[**list[RegionSummary]**](RegionSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **region_summary_summary**
> Summary region_summary_summary(langkey, startdate, enddate)



### Example
```python
from __future__ import print_function
import time
import varsom_avalanche_client
from varsom_avalanche_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_avalanche_client.RegionSummaryApi()
langkey = 56 # int | 
startdate = '2013-10-20T19:20:30+01:00' # datetime | 
enddate = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.region_summary_summary(langkey, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionSummaryApi->region_summary_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **langkey** | **int**|  | 
 **startdate** | **datetime**|  | 
 **enddate** | **datetime**|  | 

### Return type

[**Summary**](Summary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

