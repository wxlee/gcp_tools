## Service Account
```bash
mkdir env

# Service Account Json
env/sa.json
```

## Install requirements.txt
```bash
pip install -r requirements.txt
```

## How to use
```python
from gcs_tool import gcs_upload, gcs_download

gcs_upload(local_path, bucket_name, destination_path, service_account_json)
gcs_download(bucket_name, source_path, local_destination_path, service_account_json)

```