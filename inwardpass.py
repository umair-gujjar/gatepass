from openerp.osv import osv,fields
from datetime import date, datetime
class inwardpass(osv.Model):
	_name='inwardpass'
	_columns= {
	'date' : fields.date('Date', required=True),
	'document_type' : fields.boolean('LC or PO'),
	'invoice_ref' : fields.char('Invoice Ref #', size=32),
	'gin' : fields.char('GIN #',size=32 ),
	'lc' : fields.char('LC Ref.#/PO #',size=32),
	'bilty' : fields.char('Bilty ',size=32),
	'time_out' : fields.float('Time Out', required=True),
	'vehicle' : fields.char('Vehicle',size=32),
	'time_in' : fields.float('Time In', required=True),
	'vehicle_type' : fields.char('Vehicle Type',size=32),
	'supplier_details': fields.char('Supplier Details',size=32),
	'inward_id' : fields.one2many('inward','inwardpass_id',string='Details'),
	#'fleet_vehicle_id' : fields.many2one('fleet.vehicle','Vehicle Registration'),
	}

					

class inward(osv.Model):
    _name = 'inward'
    _columns= {
    'uom': fields.char('UOM'),
    'qty': fields.char('QTY'),
    'item': fields.char('Item Category'),
    'inwardpass_id' : fields.many2one('inwardpass','Item Category'),
    }

class inwardshop(osv.Model):
	_name='inwardshop'
	_columns= {
	'date' : fields.date('Date', required=True),
	#'document_type' : fields.boolean('LC or PO'),
	#'invoice_ref' : fields.char('Invoice Ref #', size=32),
	'gin' : fields.char('GIN #',size=32 ),
	'srin' : fields.char('SRIN #',size=32),
	'branch' : fields.char('Branch Name ',size=32),
	#'time_out' : fields.date('Time Out', required=True),
	'vehicle' : fields.char('Vehicle',size=32),
	'time_in' : fields.float('Time In', required=True),
	'vehicle_type' : fields.char('Vehicle Type',size=32),
	#'supplier_details': fields.char('Supplier Details',size=32),
	'inshop_id' : fields.one2many('inshop','inwardshop_id',string='Details'),
	'fleet_vehicle_id' : fields.many2one('fleet.vehicle','Vehicle Registration'),
	}

class inshop(osv.Model):
    _name = 'inshop'
    _columns= {
    'uom': fields.char('UOM'),
    'qty': fields.char('QTY'),
    'item': fields.char('Item Category'),
    'inwardshop_id' : fields.many2one('inwardshop','Item Category'),
    }

class outwardpass(osv.Model):
	_name='outwardpass'
	_columns= {
	'date' : fields.date('Date', required=True),
	'nature' : fields.boolean('Return or Rejection'),
	#'invoice_ref' : fields.char('Invoice Ref #', size=32),
	'gon' : fields.char('GON #',size=32 ),
	'sron' : fields.char('SRON Ref.',size=32),
	#'bilty' : fields.char('Bilty ',size=32),
	'time_out' : fields.float('Time Out', required=True),
	'vehicle' : fields.char('Vehicle',size=32),
	#'time_in' : fields.float('Time In', required=True),
	'vehicle_type' : fields.char('Vehicle Type',size=32),
	'supplier_details': fields.char('Supplier Details',size=32),
	'outward_id' : fields.one2many('outward','outwardpass_id',string='Details'),
	#'fleet_vehicle_id' : fields.many2one('fleet.vehicle','Vehicle Registration'),
	}

class outward(osv.Model):
    _name = 'outward'
    _columns= {
    'uom': fields.char('UOM'),
    'qty': fields.char('QTY'),
    'item': fields.char('Item Category'),
    'outwardpass_id' : fields.many2one('outwardpass','Item Category'),
    }

class outwardshop(osv.Model):
	_name='outwardshop'
	_columns= {
	'date' : fields.date('Date', required=True),
	#'document_type' : fields.boolean('LC or PO'),
	#'invoice_ref' : fields.char('Invoice Ref #', size=32),
	'gon' : fields.char('GON #',size=32 ),
	'sin' : fields.char('SIN #',size=32 ),
	#'bilty' : fields.char('Bilty ',size=32),
	'time_out' : fields.float('Time Out', required=True),
	'vehicle' : fields.char('Vehicle',size=32),
	#'time_in' : fields.float('Time In', required=True),
	'vehicle_type' : fields.char('Vehicle Type',size=32),
	#'supplier_details': fields.char('Supplier Details',size=32),
	'outshop_id' : fields.one2many('outshop','outwardshop_id',string='Details'),
	'fleet_vehicle_id' : fields.many2one('fleet.vehicle','Vehicle Registration'),
	}

class outshop(osv.Model):
    _name = 'outshop'
    _columns= {
    'uom': fields.char('UOM'),
    'qty': fields.char('QTY'),
    'item': fields.char('Item Category'),
    'outwardshop_id' : fields.many2one('outwardshop','Item Category'),
    }

class inwardgen(osv.Model):
	_name='inwardgen'
	_columns= {
	'date' : fields.date('Date', required=True),
	#'document_type' : fields.boolean('LC or PO'),
	#'invoice_ref' : fields.char('Invoice Ref #', size=32),
	'gin' : fields.char('GIN #',size=32 ),
	'document_ref' : fields.char('Document Ref #',size=32),
	#'bilty' : fields.char('Bilty ',size=32),
	#'time_out' : fields.float('Time Out', required=True),
	'vehicle' : fields.char('Vehicle',size=32),
	'time_in' : fields.float('Time In', required=True),
	'vehicle_type' : fields.char('Vehicle Type',size=32),
	#'supplier_details': fields.char('Supplier Details',size=32),
	'ingen_id' : fields.one2many('ingen','inwardgen_id',string='Details'),
	#'fleet_vehicle_id' : fields.many2one('fleet.vehicle','Vehicle Registration'),
	}

class ingen(osv.Model):
    _name = 'ingen'
    _columns= {
    'uom': fields.char('UOM'),
    'qty': fields.char('QTY'),
    'item': fields.char('Item Category'),
    'inwardgen_id' : fields.many2one('inwardgen','Item Category'),
    }

class outwardgen(osv.Model):
	_name='outwardgen'
	_columns= {
	'date' : fields.date('Date', required=True),
	#'document_type' : fields.boolean('LC or PO'),
	#'invoice_ref' : fields.char('Invoice Ref #', size=32),
	'gon' : fields.char('GON #',size=32 ),
	'document_ref' : fields.char('Document Ref #',size=32),
	#'bilty' : fields.char('Bilty ',size=32),
	'time_out' : fields.float('Time Out', required=True),
	'vehicle' : fields.char('Vehicle',size=32),
	#'time_in' : fields.float('Time In', required=True),
	'vehicle_type' : fields.char('Vehicle Type',size=32),
	#'supplier_details': fields.char('Supplier Details',size=32),
	'outgen_id' : fields.one2many('outgen','outwardgen_id',string='Details'),
	#'fleet_vehicle_id' : fields.many2one('fleet.vehicle','Vehicle Registration'),
	}

class outgen(osv.Model):
    _name = 'outgen'
    _columns= {
    'uom': fields.char('UOM'),
    'qty': fields.char('QTY'),
    'item': fields.char('Item Category'),
    'outwardgen_id' : fields.many2one('outwardgen','Item Category'),
    }

class inwardret(osv.Model):
	_name='inwardret'
	_columns= {
	#'name': fields.char('Name', size=32),
	'dept': fields.char('Department/Section', size=32),
	'date_out' : fields.date('Date Out', required=True),
	'date_in' : fields.date('Date In', required=True),
	#'document_type' : fields.boolean('LC or PO'),
	#'invoice_ref' : fields.char('Invoice Ref #', size=32),
	'gin' : fields.char('GIN #',size=32 ),
	'document_ref' : fields.char('Document Ref #',size=32),
	#'bilty' : fields.char('Bilty ',size=32),
	'time_out' : fields.float('Time Out', required=True),
	'vehicle' : fields.char('Vehicle',size=32),
	'time_in' : fields.float('Time In', required=True),
	'workers': fields.char('No of Workers',size=32),
	'vehicle_type' : fields.char('Vehicle Type',size=32),
	'inret_id' : fields.one2many('inret','inwardret_id',string='Details'),
	'stock_location_id' : fields.many2one('stock.location','Dept'),
	}

class inret(osv.Model):
    _name = 'inret'
    _columns= {
    'item_des': fields.char('Item Description'),
    'brought_in_qty': fields.integer('Brought In QTY'),
    'qty_used': fields.char('QTY Used'),
    'brought_out_qty': fields.integer('Brought OUT QTY'),
    'inwardret_id' : fields.many2one('inwardret','Item Category'),
    }

class outwardret(osv.Model):
	_name='outwardret'
	_columns= {
	'name': fields.char('Name', size=32),
	'dept': fields.char('Department/Section', size=32),
	'date_out' : fields.date('Date Out', required=True),
	'date_in' : fields.date('Date In', required=True),
	#'document_type' : fields.boolean('LC or PO'),
	#'invoice_ref' : fields.char('Invoice Ref #', size=32),
	'gon' : fields.char('GON #',size=32 ),
	'document_ref' : fields.char('Document Ref #',size=32),
	#'bilty' : fields.char('Bilty ',size=32),
	'time_out' : fields.float('Time Out', required=True),
	'vehicle' : fields.char('Vehicle',size=32),
	'time_in' : fields.float('Time In', required=True),
	#'workers': fields.char('No of Workers',size=32),
	'vehicle_type' : fields.char('Vehicle Type',size=32),
	'outret_id' : fields.one2many('outret','outwardret_id',string='Details'),
	'stock_location_id' : fields.many2one('stock.location','Dept'),
	}

class outret(osv.Model):
    _name = 'outret'
    _columns= {
    'item_des': fields.char('Item Description'),
    'brought_in_qty': fields.integer('Brought In QTY'),
    #'qty_used': fields.char('QTY Used'),
    'brought_out_qty': fields.integer('Brought OUT QTY'),
    'diff': fields.integer('Differenc (If any)'),
    'outwardret_id' : fields.many2one('inwardret','Item Category'),
    }


class fleet_vehicle(osv.Model):
	_inherit="fleet.vehicle"

class stock_warehouse(osv.Model):
	_inherit="stock.location"
