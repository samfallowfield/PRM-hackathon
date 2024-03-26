import boto3

def extract_text_from_image():
    textract_client = boto3.client('textract')

    s3_bucket = 'prm-hackathon-record'

    document_key = 'example7.png'
    response = textract_client.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': s3_bucket,
                'Name': document_key
            }
        })

    extracted_text = ''

    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            if item['Confidence'] > 90:
                extracted_text += item['Text'] + ' - Confidence Score:  ' + str(round(item['Confidence'])) + '% \n'
            else:
                extracted_text += ' WARNING : Confidence score is less than 90%, Please review this line :  ' + item[
                    'Text'] + '\n'
    return extracted_text

def upload_file_as_text(file_path, bucket_name, object_key):

    s3_client = boto3.client('s3')

    with open(file_path, 'r') as file:
        file_contents = file.read()

    s3_client.put_object(Body=file_contents, Bucket=bucket_name, Key=object_key)



final_extracted_text = extract_text_from_image()
upload_file_as_text('test.txt', 'prm-hackathon-record', 'test_object')
print(final_extracted_text)
