# varsom_avalanche_client.AvalancheWarningByRegionApi

All URIs are relative to *https://api01.nve.no/hydrology/forecast/avalanche/v5.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**avalanche_warning_by_region_detail**](AvalancheWarningByRegionApi.md#avalanche_warning_by_region_detail) | **GET** /api/AvalancheWarningByRegion/Detail/{regionid}/{langkey}/{startdate}/{enddate} | 
[**avalanche_warning_by_region_obs**](AvalancheWarningByRegionApi.md#avalanche_warning_by_region_obs) | **GET** /api/AvalancheWarningByRegion/Obs/{regionid}/{langkey}/{startdate}/{enddate} | 
[**avalanche_warning_by_region_simple**](AvalancheWarningByRegionApi.md#avalanche_warning_by_region_simple) | **GET** /api/AvalancheWarningByRegion/Simple/{regionid}/{langkey}/{startdate}/{enddate} | 

# **avalanche_warning_by_region_detail**
> list[AvalancheWarningDetail] avalanche_warning_by_region_detail(regionid, langkey, startdate, enddate)



### Example
```python
from __future__ import print_function
import time
import varsom_avalanche_client
from varsom_avalanche_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_avalanche_client.AvalancheWarningByRegionApi()
regionid = 56 # int | 
langkey = 56 # int | 
startdate = '2013-10-20T19:20:30+01:00' # datetime | 
enddate = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.avalanche_warning_by_region_detail(regionid, langkey, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvalancheWarningByRegionApi->avalanche_warning_by_region_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regionid** | **int**|  | 
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

# **avalanche_warning_by_region_obs**
> list[ObsWarning] avalanche_warning_by_region_obs(regionid, langkey, startdate, enddate)



### Example
```python
from __future__ import print_function
import time
import varsom_avalanche_client
from varsom_avalanche_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_avalanche_client.AvalancheWarningByRegionApi()
regionid = 56 # int | 
langkey = 56 # int | 
startdate = '2013-10-20T19:20:30+01:00' # datetime | 
enddate = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.avalanche_warning_by_region_obs(regionid, langkey, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvalancheWarningByRegionApi->avalanche_warning_by_region_obs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regionid** | **int**|  | 
 **langkey** | **int**|  | 
 **startdate** | **datetime**|  | 
 **enddate** | **datetime**|  | 

### Return type

[**list[ObsWarning]**](ObsWarning.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **avalanche_warning_by_region_simple**
> list[AvalancheWarningSimple] avalanche_warning_by_region_simple(regionid, langkey, startdate, enddate)



### Example
```python
from __future__ import print_function
import time
import varsom_avalanche_client
from varsom_avalanche_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_avalanche_client.AvalancheWarningByRegionApi()
regionid = 56 # int | 
langkey = 56 # int | 
startdate = '2013-10-20T19:20:30+01:00' # datetime | 
enddate = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.avalanche_warning_by_region_simple(regionid, langkey, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvalancheWarningByRegionApi->avalanche_warning_by_region_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regionid** | **int**|  | 
 **langkey** | **int**|  | 
 **startdate** | **datetime**|  | 
 **enddate** | **datetime**|  | 

### Return type

[**list[AvalancheWarningSimple]**](AvalancheWarningSimple.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

