# varsom_avalanche_client.ArchiveApi

All URIs are relative to *https://api01.nve.no/hydrology/forecast/avalanche/v5.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_all**](ArchiveApi.md#archive_all) | **GET** /api/Archive/Warning/All/{langkey}/{startdate}/{enddate}/{format} | 
[**archive_region_id**](ArchiveApi.md#archive_region_id) | **GET** /api/Archive/Warning/Region/{id}/{langkey}/{startdate}/{enddate}/{format} | 
[**archive_regions**](ArchiveApi.md#archive_regions) | **GET** /api/Archive/Region/{format} | 
[**archive_warning_id**](ArchiveApi.md#archive_warning_id) | **GET** /api/Archive/Warning/Id/{id}/{langkey}/{format} | 

# **archive_all**
> object archive_all(langkey, startdate, enddate, format)



### Example
```python
from __future__ import print_function
import time
import varsom_avalanche_client
from varsom_avalanche_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_avalanche_client.ArchiveApi()
langkey = 56 # int | 
startdate = '2013-10-20T19:20:30+01:00' # datetime | 
enddate = '2013-10-20T19:20:30+01:00' # datetime | 
format = 'format_example' # str | 

try:
    api_response = api_instance.archive_all(langkey, startdate, enddate, format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->archive_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **langkey** | **int**|  | 
 **startdate** | **datetime**|  | 
 **enddate** | **datetime**|  | 
 **format** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_region_id**
> object archive_region_id(id, langkey, startdate, enddate, format)



### Example
```python
from __future__ import print_function
import time
import varsom_avalanche_client
from varsom_avalanche_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_avalanche_client.ArchiveApi()
id = 56 # int | 
langkey = 56 # int | 
startdate = '2013-10-20T19:20:30+01:00' # datetime | 
enddate = '2013-10-20T19:20:30+01:00' # datetime | 
format = 'format_example' # str | 

try:
    api_response = api_instance.archive_region_id(id, langkey, startdate, enddate, format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->archive_region_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **langkey** | **int**|  | 
 **startdate** | **datetime**|  | 
 **enddate** | **datetime**|  | 
 **format** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_regions**
> object archive_regions(format)



### Example
```python
from __future__ import print_function
import time
import varsom_avalanche_client
from varsom_avalanche_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_avalanche_client.ArchiveApi()
format = 'format_example' # str | 

try:
    api_response = api_instance.archive_regions(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->archive_regions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_warning_id**
> object archive_warning_id(id, langkey, format)



### Example
```python
from __future__ import print_function
import time
import varsom_avalanche_client
from varsom_avalanche_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = varsom_avalanche_client.ArchiveApi()
id = 56 # int | 
langkey = 56 # int | 
format = 'format_example' # str | 

try:
    api_response = api_instance.archive_warning_id(id, langkey, format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArchiveApi->archive_warning_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **langkey** | **int**|  | 
 **format** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

