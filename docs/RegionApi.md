# varsom_avalanche_client.RegionApi

All URIs are relative to *https://api01.nve.no/hydrology/forecast/avalanche/v5.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**region_all**](RegionApi.md#region_all) | **POST** /api/Region/{regionTypeId} | 
[**region_get**](RegionApi.md#region_get) | **GET** /api/Region/{regionTypeId} | 

# **region_all**
> list[Region] region_all(region_type_id)



### Example
```python
from __future__ import print_function
import time
import varsom_avalanche_client
from varsom_avalanche_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_avalanche_client.RegionApi()
region_type_id = 'region_type_id_example' # str | 

try:
    api_response = api_instance.region_all(region_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionApi->region_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_type_id** | **str**|  | 

### Return type

[**list[Region]**](Region.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **region_get**
> list[Region] region_get(region_type_id)



### Example
```python
from __future__ import print_function
import time
import varsom_avalanche_client
from varsom_avalanche_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_avalanche_client.RegionApi()
region_type_id = 56 # int | 

try:
    api_response = api_instance.region_get(region_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionApi->region_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_type_id** | **int**|  | 

### Return type

[**list[Region]**](Region.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

