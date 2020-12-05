import requests
from supermarktconnector.jumbo import JumboConnector
import base64
import os
import sys
from dotenv import load_dotenv
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


connector = JumboConnector()

load_dotenv()

VAR_GROCY_API_KEY = os.getenv('GROCY-API-KEY')
VAR_HOST = os.getenv('HOST')


headers = { "GROCY-API-KEY" : " " }

headers['GROCY-API-KEY'] = VAR_GROCY_API_KEY

dict_output = {}
known_barcodes = (8710391936834, 8710742020069, 8718449086937)


# searching through the jumbo.com API for the product and appending those items to a dictionary.

def ean_jumbo_search(eancode):
    item_output = connector.get_product_by_barcode(eancode)

    dict_output["title"] = item_output['title']
    dict_output["item_image"] = item_output['imageInfo']['primaryView'][0]['url']
    dict_output["item_weight"] = item_output['quantity']
    dict_output["item_type"] = item_output['productType']
    dict_output['ean_code'] = eancode

ean_jumbo_search(sys.argv[1])



productdata =    {
    "name": "{}",
    "description": "niks",
    "location_id": "2",
    "qu_id_purchase": "2",
    "qu_id_stock": "3",
    "qu_factor_purchase_to_stock": "1.0",
    "barcode": "cok1",
    "min_stock_amount": "8",
    "default_best_before_days": "0",
    "row_created_timestamp": "2019-05-02 20:12:26",
    "product_group_id": "0",
    "picture_file_name": "{}",
    "default_best_before_days_after_open": "0",
    "allow_partial_units_in_stock": "0",
    "enable_tare_weight_handling": "0",
    "tare_weight": "0.0",
    "not_check_stock_fulfillment_for_recipes": "0",
    "shopping_location_id": "jumbo"}
 
productdata["name"] = dict_output["title"] 
productdata["picture_file_name"] = str(dict_output["ean_code"]) + '.jpg'.strip( ) 
productdata["barcode"] = dict_output["ean_code"] 


## Posting the picture to the grocy website
def image_post(inp_url, ean_code):
    # Saving the image to the local PC
    f = open("ean_pictures/" + ean_code + '.jpg','wb')
    f.write(requests.get(inp_url).content)
    f.close()

    with open("ean_pictures/" + ean_code + '.jpg', "rb") as f:
        # setting the headers that are needed to put images to the API
        headers_image = {"GROCY-API-KEY" : " ", 'Content-Type': 'application/octet-stream', "accept ": "*/*"}
        headers_image['GROCY-API-KEY'] = VAR_GROCY_API_KEY
        
        #setting a variable for the loaded image
        img = f.read()

        # getting the hash of the filename "<eancode>.jpg" and writing that hash to "<eancode>.txt" in the folder ean_pictures
        filename = str(dict_output["ean_code"]) + '.jpg' 
        filename_bytes = filename.encode("utf-8")
        ean_base64 = base64.b64encode(filename_bytes)
        ean_hash_file = open("ean_pictures/" + ean_code + '.txt', "wb")
        ean_hash_file.write(ean_base64)
        ean_hash_file.close()

        # reading the hash of the filename and posting the image to the API
        with open("ean_pictures/" + ean_code + '.txt', "r") as ean_hash:
            ean_hash_final = ean_hash.readline()
            r = requests.put('{}/api/files/productpictures/{}'.format(VAR_HOST, ean_hash_final), data=img, verify=False, headers=headers_image, timeout=None)
            # print(r.status_code)


image_post(dict_output["item_image"], str(dict_output["ean_code"]))

# posting the product data
r = requests.post("{}/api/objects/products".format(VAR_HOST),json=productdata,headers=headers, verify=False)
# print(r.content)