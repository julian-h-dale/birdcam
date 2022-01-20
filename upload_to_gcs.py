from google.cloud import storage

class FileUploader:
    PATH_TO_CREDS = './creds/credentials.json'
    BUCKET_NAME = 'birdcam-storage'
    DIRECTORY = "./pics/"

    def __init__(self):
        storage_client = storage.Client.from_service_account_json(self.PATH_TO_CREDS)
        self.bucket = storage_client.get_bucket(self.BUCKET_NAME)

    def upload(self, filename):
        blob = self.bucket.blob(filename)
        blob.upload_from_filename(self.DIRECTORY+filename)
        print("uploaded: " + blob.public_url)


if __name__ == '__main__':
    uploader = FileUploader()
    uploader.upload('test.txt')
