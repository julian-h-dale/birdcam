from google.cloud import storage

PATH_TO_CREDS = './creds/credentials.json'
BUCKET_NAME = 'birdcam-storage'
FILE_NAME = 'test.txt'
storage_client = storage.Client.from_service_account(PATH_TO_CREDS)
bucket = storage_client.get(BUCKET_NAME)
blob = bucket.blob(FILE_NAME)
blob.upload('./pics/test.txt')
print('uploaded file: ' + blob.public_url)