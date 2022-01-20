from google.cloud import storage

# PATH_TO_CREDS = './creds/credentials.json'
# BUCKET_NAME = 'birdcam-storage'
# FILE_NAME = 'test.txt'
# storage_client = storage.Client.from_service_account_json(PATH_TO_CREDS)
# bucket = storage_client.get_bucket(BUCKET_NAME)
# blob = bucket.blob(FILE_NAME)
# blob.upload_from_filename('./pics/test.txt')
# print('uploaded file: ' + blob.public_url)

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
