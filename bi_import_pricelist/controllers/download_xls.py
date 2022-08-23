# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import content_disposition
import base64
import os, os.path
import csv
from os import listdir
import sys

class Download_xls(http.Controller):
    
    @http.route('/web/binary/download_document', type='http', auth="public")
    def download_document(self,model,id, **kw):

        Model = request.env[model]
        res = Model.browse(int(id)).sudo()

        if res.sample_option == 'xls' and model == 'import.vendor.pricelist':
            invoice_xls = request.env['ir.attachment'].sudo().search([('name','=','vendor_pricelist.xls')])
            filecontent = invoice_xls.datas
            filename = 'vendor_pricelist.xls'
            filecontent = base64.b64decode(filecontent)

        elif res.sample_option == 'csv' and model == 'import.vendor.pricelist':
            invoice_xls = request.env['ir.attachment'].sudo().search([('name','=','vendor_pricelist.csv')])
            filecontent = invoice_xls.datas
            filename = 'vendor_pricelist.csv'
            filecontent = base64.b64decode(filecontent)
            
            
        elif res.sample_option == 'xls' and model == 'import.product.pricelist':
            invoice_xls = request.env['ir.attachment'].sudo().search([('name','=','product_pricelist.xls')])
            filecontent = invoice_xls.datas
            filename = 'product_pricelist.xls'
            filecontent = base64.b64decode(filecontent)

        elif res.sample_option == 'csv' and model == 'import.product.pricelist':
            invoice_xls = request.env['ir.attachment'].sudo().search([('name','=','product_pricelist.csv')])
            filecontent = invoice_xls.datas
            filename = 'product_pricelist.csv'
            filecontent = base64.b64decode(filecontent)
            
            
        elif res.sample_option == 'xls' and model == 'import.sale.pricelist':
            invoice_xls = request.env['ir.attachment'].sudo().search([('name','=','sale_pricelist_formula.xls')])
            filecontent = invoice_xls.datas
            filename = 'sale_pricelist_formula.xls'
            filecontent = base64.b64decode(filecontent)

        elif res.sample_option == 'csv' and model == 'import.sale.pricelist':
            invoice_xls = request.env['ir.attachment'].sudo().search([('name','=','sale_pricelist_formula.csv')])
            filecontent = invoice_xls.datas
            filename = 'sale_pricelist_formula.csv'
            filecontent = base64.b64decode(filecontent)
            
            
            
        elif res.sample_option == 'xls' and model == 'import.sale.pricelist.wizard':
            invoice_xls = request.env['ir.attachment'].sudo().search([('name','=','sale_pricelist_wizard_option.xls')])
            filecontent = invoice_xls.datas
            filename = 'sale_pricelist_wizard_option.xls'
            filecontent = base64.b64decode(filecontent)

        elif res.sample_option == 'csv' and model == 'import.sale.pricelist.wizard':
            invoice_xls = request.env['ir.attachment'].sudo().search([('name','=','sale_pricelist_wizard_option.csv')])
            filecontent = invoice_xls.datas
            filename = 'sale_pricelist_wizard_option.csv'
            filecontent = base64.b64decode(filecontent)
            

        return request.make_response(filecontent,
            [('Content-Type', 'application/octet-stream'),
            ('Content-Disposition', content_disposition(filename))])
        
        
        