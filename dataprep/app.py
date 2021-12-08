import os
import runpy
from .args import get_args
from .utils import find_files, parse_xml, find_in_xml, scale_image, create_coco
from sys import argv


current = os.path.realpath(os.path.dirname(__file__))

__version__ = \
    runpy.run_path(os.path.join(current, "version.py"))["__version__"]


def main(imagedir, xmldir, outputdir):
    xmls = find_files(xmldir, '*.xml')
    annotations = []
    categories = {}
    images = []
    image_id = 0

    for path in xmls:
        it = parse_xml(path)
        w, h = find_in_xml(it, ['size/width', 'size/height'])
        image_filename, = find_in_xml(it, ['filename'])
        bnd_boxes = []
        bnd_box_id = 0

        # scaling image
        image_path = os.path.join(imagedir, image_filename)
        res_img, scale, = scale_image(image_path, 1100, 618)

        images.append({
            "id": image_id,
            "width": res_img.width,
            "height": res_img.height,
            "file_name": os.path.join(outputdir, image_filename)
        })

        # get annotations
        for obj in it.findall('object'):
            xmin, ymin, xmax, ymax = find_in_xml(obj, ['bndbox/xmin', 'bndbox/ymin', 'bndbox/xmax', 'bndbox/ymax'])
            cat_name, = find_in_xml(obj, ['name'])
            cat = categories.get(cat_name, None)
            if cat is None:
                cat = {
                    "id": len(categories),
                    "name": cat_name,
                    "supercategory": cat_name
                }
                categories[cat_name] = cat

            bnd_boxes.append({
                "id": bnd_box_id,
                "image_id": image_id,
                "category_id": cat["id"],
                "bbox": [int(int(xmin) * scale), int(int(ymin) * scale), int(int(xmax) * scale), int(int(ymax) * scale)]
            })
            bnd_box_id += 1
            annotations.extend(bnd_boxes)
        image_id += 1

    output_file = os.path.join(outputdir, 'coco.json')
    create_coco(list(categories.values()), images, annotations, output_file)


if __name__ == "__main__":
    args = get_args(argv[1:])
    main(args.IMAGE_DIR, args.XML_DIR, args.OUTPUT_DIR)
