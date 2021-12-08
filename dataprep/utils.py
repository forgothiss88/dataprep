import json
import glob
import os
import logging
import xml.etree.ElementTree as ET
from PIL import Image

from dataprep.const import MAX_WIDTH, MAX_HEIGHT

log = logging.getLogger(__name__)


def find_files(dir, pattern):
    path = os.path.realpath(dir)
    files = glob.glob(pathname=os.path.join(path, pattern), recursive=False)
    return files

def parse_xml(filename):
    it = ET.parse(filename).getroot()
    return it

def find_in_xml(root, tags):
    ret = []
    for t in tags:
        for type_tag in root.findall(t):
            ret.append(type_tag.text)
    return ret

def scale_image(path, width, heigth):
    x_scaling, y_scaling = (MAX_WIDTH/width), (MAX_HEIGHT/heigth)

    scaling = max(x_scaling, y_scaling)

    image = Image.open(path)
    resized_image = image

    if scaling < 1.0:
        resized_image = image.resize((int(width * scaling), int(heigth * scaling)))

    return resized_image, scaling

def save_images(images, dir):
    path = os.path.realpath(dir)
    for name, image in images.items:
        image.save(path.join(name))

def create_coco(categories, images, annotations, output_file_path):
    coco = {
        "annotations": annotations,
        "categories": categories,
        "images": images
    }

    with open(output_file_path, 'w') as outfile:
        json.dump(coco, outfile)






