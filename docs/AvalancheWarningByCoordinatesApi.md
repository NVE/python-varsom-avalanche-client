# varsom_avalanche_client.AvalancheWarningByCoordinatesApi

All URIs are relative to *https://api01.nve.no/hydrology/forecast/avalanche/v5.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**avalanche_warning_by_coordinates_detail**](AvalancheWarningByCoordinatesApi.md#avalanche_warning_by_coordinates_detail) | **GET** /api/AvalancheWarningByCoordinates/Detail/{x}/{y}/{langkey}/{startdate}/{enddate} | 
[**avalanche_warning_by_coordinates_obs**](AvalancheWarningByCoordinatesApi.md#avalanche_warning_by_coordinates_obs) | **GET** /api/AvalancheWarningByCoordinates/Obs/{x}/{y}/{langkey}/{startdate}/{enddate} | 
[**avalanche_warning_by_coordinates_simple**](AvalancheWarningByCoordinatesApi.md#avalanche_warning_by_coordinates_simple) | **GET** /api/AvalancheWarningByCoordinates/Simple/{x}/{y}/{langkey}/{startdate}/{enddate} | 

# **avalanche_warning_by_coordinates_detail**
> list[AvalancheWarningDetail] avalanche_warning_by_coordinates_detail(x, y, langkey, startdate, enddate)



### Example
```python
from __future__ import print_function
import time
import varsom_avalanche_client
from varsom_avalanche_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_avalanche_client.AvalancheWarningByCoordinatesApi()
x = 1.2 # float | 
y = 1.2 # float | 
langkey = 56 # int | 
startdate = '2013-10-20T19:20:30+01:00' # datetime | 
enddate = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.avalanche_warning_by_coordinates_detail(x, y, langkey, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvalancheWarningByCoordinatesApi->avalanche_warning_by_coordinates_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x** | **float**|  | 
 **y** | **float**|  | 
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

# **avalanche_warning_by_coordinates_obs**
> list[ObsWarning] avalanche_warning_by_coordinates_obs(x, y, langkey, startdate, enddate)



### Example
```python
from __future__ import print_function
import time
import varsom_avalanche_client
from varsom_avalanche_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_avalanche_client.AvalancheWarningByCoordinatesApi()
x = 1.2 # float | 
y = 1.2 # float | 
langkey = 56 # int | 
startdate = '2013-10-20T19:20:30+01:00' # datetime | 
enddate = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.avalanche_warning_by_coordinates_obs(x, y, langkey, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvalancheWarningByCoordinatesApi->avalanche_warning_by_coordinates_obs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x** | **float**|  | 
 **y** | **float**|  | 
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

# **avalanche_warning_by_coordinates_simple**
> list[AvalancheWarningSimple] avalanche_warning_by_coordinates_simple(x, y, langkey, startdate, enddate)



### Example
```python
from __future__ import print_function
import time
import varsom_avalanche_client
from varsom_avalanche_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_avalanche_client.AvalancheWarningByCoordinatesApi()
x = 1.2 # float | 
y = 1.2 # float | 
langkey = 56 # int | 
startdate = '2013-10-20T19:20:30+01:00' # datetime | 
enddate = '2013-10-20T19:20:30+01:00' # datetime | 

try:
    api_response = api_instance.avalanche_warning_by_coordinates_simple(x, y, langkey, startdate, enddate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvalancheWarningByCoordinatesApi->avalanche_warning_by_coordinates_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x** | **float**|  | 
 **y** | **float**|  | 
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

