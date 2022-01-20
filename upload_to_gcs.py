from google.cloud import storage

PATH_TO_CREDS = './creds/credentials.json'
BUCKET_NAME = 'birdcam-storage'
FILE_NAME = 'test.txt'
storage_client = storage.Client.from_service_account_json(PATH_TO_CREDS)
bucket = storage_client.get_bucket(BUCKET_NAME)
blob = bucket.blob(FILE_NAME)
blob.upload_from_filename('./pics/test.txt')
print('uploaded file: ' + blob.public_url)