from gcs_tool import gcs_upload, gcs_download

local_path = './testfolder/'
bucket_name = 'test_bucket'
destination_path = ''
source_path = 'ccc/'
local_destination_path = 'aaa/bb'

service_account_json = 'env/sa.json'

gcs_upload(local_path, bucket_name, destination_path, service_account_json)

gcs_download(bucket_name, source_path, local_destination_path, service_account_json)


