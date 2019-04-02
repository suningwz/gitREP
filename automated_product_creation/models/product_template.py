# -*- coding: utf-8 -*-

from odoo import models, fields, api
import csv
import os

class ProductCsvUpdate(models.Model):
    _inherit = 'product.template'

    def do_automated_product_creation(self):
        script_path = os.path.abspath(__file__)
        path_list = script_path.split(os.sep)
        script_directory =path_list[0:len(path_list)-2]
        rel_path = "static/csv/product_template.csv"
        path = "/".join(script_directory) + "/" + rel_path
        with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)            
            for row in reader:
                self.create(dict(row))

        
         
