# -*- coding: utf-8 -*-

import urllib
import base64

from odoo import fields, models, api, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'
   
    image_url_template = fields.Char(
        string='Image Url',
        copy=False,
    )
    
    @api.model
    def create(self, vals):
        if not vals.get('image_1920'):
            image_url_template = vals.get('image_url_template')
            if image_url_template:
                try:
                    image = base64.encodebytes(urllib.request.urlopen(image_url_template).read())
                    vals['image_1920'] = image
                except:
                    pass
        return super(ProductTemplate, self).create(vals)
            

    def write(self, vals):
        image_url_template = vals.get('image_url_template')
        if image_url_template:
            print('image_url_template==========================>',image_url_template)
            try:
                # print('--------------------------[[[[[[[[[============]]]]]]]]]]========================')
                # print('base64.encodebytes(urllib.request.urlopen(image_url_template).read',base64.encodebytes(urllib.request.urlopen(image_url_template).read()))
                image = base64.encodebytes(urllib.request.urlopen(image_url_template).read())
                # print('image=====================================',image)
                vals.update({'image_1920': image})
            except:
                pass
        return super(ProductTemplate, self).write(vals)
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
