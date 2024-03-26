import boto3


# def extract_text_from_image(image_path=none):
def extract_text_from_image():
    textract_client = boto3.client('textract')

    # read image file
    # with open(image_path, 'rb') as image_file:
    #     image_bytes = image_file.read()

    # call textract
    # response = textract_client.detect_document_text(Document={'Bytes': image_bytes})

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


# image_path = 'images/gp_note5.png'
# final_extracted_text = extract_text_from_image(image_path)
final_extracted_text = extract_text_from_image()
with open("test.txt", "w") as f:
    f.write(final_extracted_text)


uplo
print(final_extracted_text)
