import os    

file_in = "docs/DefaultApi.md"
file_out = 'docs/temp.md'

original_string = '''
# Configure API key authorization: api_key
configuration = demisto_client.demisto_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = demisto_client.demisto_api.DefaultApi(demisto_client.demisto_api.ApiClient(configuration))
'''

replacement_string = '''
api_key = 'YOUR API KEY'
base_url = 'YOUR DEMISTO URL'

# create an instance of the API class
api_instance = demisto_client.configure(base_url=base_url, api_key=api_key, debug=True)
'''
with open(file_in, "rt") as fin:
    with open(file_out, "wt") as fout:
        text = fin.read()
        text = text.replace(original_string, replacement_string)
        fout.write(text)

os.rename(file_out, file_in)
