# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Amount In Words - Multi Language Supported",
   
    "author": "Softhealer Technologies",
    
    "website": "https://www.softhealer.com",    
    
    "support": "support@softhealer.com",   
    
    "version": "13.0.2",
    
    "category": "Extra Tools",
    
    "summary": "Sale Order Amount In Words Module, Purchase Order Amount In Words, Invoice Total Amount In Words App, Customer Language Selector Application,PO Amount In Words, So Amount In Words, Request For Quotation Amount In Words Odoo",   

    "description": """Convert Final Amount into Words as per Language of selected Customer/vendor.
        Amount in words available in Form and Report. This module supports Multi Languages.
 Amount In Words - Multi Language Supported Odoo
 Convert Amount In Words In Sale Order Module, Transform Total Amount In Words In Purchase Order, Convert Total Amount In Words In Invoice, Select Language For Customer, Convert PO Total Amount In Words, Transform So Amount In Words Odoo.
 Sale Order Amount In Words Module, Purchase Order Amount In Words, Invoice Total Amount In Words App, Customer Language Selector Application,PO Amount In Words, So Amount In Words Odoo.
""",
         
    "depends": ['sale_management','purchase','account'],
    
    "data": [
        "views/amount_in_words.xml",        
        "reports/sale_order_report.xml",        
        "reports/purchase_order_report.xml",        
        "reports/account_invoice_report.xml",        
    ],    
    "images": ["static/description/background.jpg",],
                 
    "installable": True,
    "auto_install": False,
    "application": True,    
    
    "price": "18",
    "currency": "EUR" 
}
