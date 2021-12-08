import unittest
from dataprep.app import main as app_main
from dataprep.utils import *


class SessionTest(unittest.TestCase):
    def setUp(self):
        self.tests_dir = os.path.dirname(__file__)

    def test_find_files(self):
        path = os.path.join(self.tests_dir, "xmldata")
        l = find_files(path, "*.xml")
        self.assertEqual(6, len(l))

    def test_parse_xml(self):
        path = os.path.join(self.tests_dir, "xmldata", "01.xml")
        it = parse_xml(path)
        w, h = find_in_xml(it, ['size/width','size/height'])
        self.assertEqual(w, '1100')
        self.assertEqual(h, '618')

    def test_scale_image(self):
        img = os.path.join(self.tests_dir, "images", "01.jpg")
        res_img, scale = scale_image(img, 1100, 618)
        self.assertLessEqual(res_img.width, 800)
        self.assertLessEqual(res_img.height, 450)

    def test_obtain_bnd_boxes(self):
        path = os.path.join(self.tests_dir, "xmldata", "06.xml")
        it = parse_xml(path)
        bnds = []
        for obj in it.findall('object'):
            bnds.append(find_in_xml(obj, ['bndbox/xmin','bndbox/ymin','bndbox/xmax','bndbox/ymax']))
        self.assertEqual(len(bnds), 5)
        self.assertEqual(len(bnds[0]), 4)


    def test_app_main(self):
        app_main(imagedir=os.path.join(self.tests_dir, "images"),
                 xmldir=os.path.join(self.tests_dir, "xmldata"),
                 outputdir=os.path.join(self.tests_dir, "output"))



