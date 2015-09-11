# -*- encoding: utf-8 -*-

from openerp.osv import osv, fields
class cost_price(osv.Model):
	_name = 'product.template'
	_inherits = {'account.invoice.line': 'price_unit'}
	_inherit = 'product.template'
	_columns={
    #'standard_price': fields.property(type = 'float', digits_compute=dp.get_precision('Product Price'), 
                                          #help="Cost price of the product template used for standard stock valuation in accounting and used as a base price on purchase orders. "
                                           #    "Expressed in the default unit of measure of the product.",
                                          #groups="base.group_user", string="Cost Price"),
	'standard_price':fields.float('Cost Price'),
	'price_unit':fields.many2one('account.invoice.line', 'Price Unit'
             	,help="Link this employee to it's medical details", ondelete="cascade",),
    }
