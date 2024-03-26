import boto3


def extract_text_from_image(image_path):
    textract_client = boto3.client('textract')

    # read image file
    with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()

    # call textract
    response = textract_client.detect_document_text(Document={'Bytes': image_bytes})

    extracted_text = ''
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            extracted_text += item['Text'] + '\n'
            print(item['Confidence'])
    return extracted_text


image_path = 'images/gp_note4.png'
final_extracted_text = extract_text_from_image(image_path)
print(final_extracted_text)
