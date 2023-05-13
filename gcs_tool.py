import os
from google.cloud import storage
from google.oauth2 import service_account

def gcs_upload(local_path, bucket_name, destination_path, service_account_json):
    """
    Uploads a file or directory to Google Cloud Storage (GCS).

    Args:
        local_path (str): The local file or directory path to upload.
        bucket_name (str): The name of the GCS bucket.
        destination_path (str): The destination path in the GCS bucket.
        service_account_json (str): The path to the Service Account JSON file for authentication.

    Returns:
        None
    """
    # Load credentials from the Service Account JSON file
    credentials = service_account.Credentials.from_service_account_file(service_account_json)

    # Create a storage client with the provided credentials
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(bucket_name)

    if os.path.isfile(local_path):
        # Upload a single file to GCS
        blob = bucket.blob(destination_path)
        blob.upload_from_filename(local_path)
        print(f'File uploaded successfully: {local_path} -> gs://{bucket_name}/{destination_path}')
    elif os.path.isdir(local_path):
        # Upload directory and its contents to GCS
        for root, dirs, files in os.walk(local_path):
            for file in files:
                local_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_file_path, local_path)
                destination_blob_name = os.path.join(destination_path, relative_path).replace("\\", "/")
                blob = bucket.blob(destination_blob_name)
                blob.upload_from_filename(local_file_path)
                print(f'File uploaded successfully: {local_file_path} -> gs://{bucket_name}/{destination_blob_name}')
    else:
        print(f'File or directory does not exist: {local_path}')

def gcs_download(bucket_name, source_path, local_path, service_account_json):
    """
    Downloads a file or directory from Google Cloud Storage (GCS).

    Args:
        bucket_name (str): The name of the GCS bucket.
        source_path (str): The source path in the GCS bucket.
        local_path (str): The local destination path for downloading.
        service_account_json (str): The path to the Service Account JSON file for authentication.

    Returns:
        None
    """
    # Load credentials from the Service Account JSON file
    credentials = service_account.Credentials.from_service_account_file(service_account_json)

    # Create a storage client with the provided credentials
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(bucket_name)

    if source_path.endswith('/'):
        # Download a directory and its contents from GCS
        blobs = bucket.list_blobs(prefix=source_path)
        for blob in blobs:
            if not blob.name.endswith('/'):
                destination_file_path = os.path.join(local_path, blob.name)
                os.makedirs(os.path.dirname(destination_file_path), exist_ok=True)
                blob.download_to_filename(destination_file_path)
                print(f'File downloaded successfully: gs://{bucket_name}/{blob.name} -> {destination_file_path}')
    else:
        # Download a single file from GCS
        blob = bucket.blob(source_path)
        destination_file_path = local_path
        os.makedirs(os.path.dirname(destination_file_path), exist_ok=True)
        blob.download_to_filename(destination_file_path)
        print(f'File downloaded successfully: gs://{bucket_name}/{source_path} -> {destination_file_path}')

"""
# Example usage
local_path = '/path/to/local/file_or_directory'
bucket_name = 'your-bucket'
destination_path = 'path/to/destination
"""
