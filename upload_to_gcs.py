from google.cloud import storage

class FileUploader:
    PATH_TO_CREDS = './creds/credentials.json'
    BUCKET_NAME = 'birdcam-storage'

    def __init__(self):
        storage_client = storage.Client.from_service_account_json(self.PATH_TO_CREDS)
        self.bucket = storage_client.get_bucket(self.BUCKET_NAME)

    def upload(self, filename):
        # extract the blob name
        blob_name = filename.split('/')[-1]
        blob = self.bucket.blob(blob_name)
        blob.upload_from_filename(filename)
        print("uploaded: " + blob.public_url)


if __name__ == '__main__':
    uploader = FileUploader()
    uploader.upload('./pics/test.txt')
