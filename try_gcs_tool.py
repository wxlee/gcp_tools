from gcs_tool import gcs_upload, gcs_download

local_path = './testfolder/'
bucket_name = 'queue_size'
destination_path = ''
# source_path = 'path/to/source'
local_destination_path = '/path/to/local/destination'

service_account_json = 'env/e2e-testing-383807-b0aee978a1fc.json'

gcs_upload(local_path, bucket_name, destination_path, service_account_json)

# gcs_download(bucket_name, source_path, local_destination_path, service_account_json)


