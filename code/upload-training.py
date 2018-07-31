import os, requests
import json
import xml.etree.ElementTree as ET

pathToAnnotations = './annotations/xmls'
pathToImages = './images'
model_id = os.environ.get('NANONETS_MODEL_ID')
api_key = os.environ.get('NANONETS_API_KEY')
extentions = ['.jpeg', '.jpg', '.png', '.JPG', '.PNG', '.JPEG']

def get_xml_file_name(image_file):
    return os.path.join(pathToAnnotations, "%s.xml"%(image_file.rsplit('.', 1)[0]))

def create_xml_to_object(image_file):
    object_list = []
    xml_file_name = get_xml_file_name(image_file)
    if not os.path.isfile(xml_file_name):
        return object_list

    tree = ET.parse(xml_file_name)
    root = tree.getroot()
    
    ### here if you find any problem here, just check with xml file format and change the code 
    ### to access member an elements 
    
    for member in root.findall('object'):
        label = member[0].text
        print label
        bndbox = {}
        try:
            bndbox['xmin'] = int(member[4][0].text)
            bndbox['ymin'] = int(member[4][1].text)
            bndbox['xmax'] = int(member[4][2].text)
            bndbox['ymax'] = int(member[4][3].text)
        except:
            bndbox['xmin'] = int(member[1][0].text)
            bndbox['ymin'] = int(member[1][1].text)
            bndbox['xmax'] = int(member[1][2].text)
            bndbox['ymax'] = int(member[1][3].text)
        object_list.append({'name': label, 'bndbox': bndbox})
    return object_list

def upload_objects_by_file(model_id):
    image_count = 0
    print "uploading images...."
    for f in os.listdir(pathToImages):
        if not f.endswith(tuple(extentions)):
            print("%s has not valid extention"%f)
            continue

        filename = os.path.join(pathToImages, f)
        file = open(filename, 'rb')

        object_data = json.dumps(create_xml_to_object(f))

        data = {'file' : file,
                'data' :('', '[{"filename":"%s", "object": %s}]'%(f, object_data)),
                'modelId' :('', '%s'%model_id)}
        response = requests.post('https://app.nanonets.com/api/v2/ObjectDetection/Model/%s/UploadFile/'%(model_id), auth=requests.auth.HTTPBasicAuth(api_key, ''), files=data)
        image_count += 1

    print "Number of Uploaded Images : ", image_count
    return response.text

if __name__=="__main__":
    upload_objects_by_file(model_id)
    print("\n\n\nNEXT RUN: python ./code/train-model.py")