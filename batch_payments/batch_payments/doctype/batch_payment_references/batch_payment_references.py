# Copyright (c) 2022, Fiedler Consulting and contributors
# For license information, please see license.txt

import frappe
from frappe import _

from frappe.model.document import Document


#
# Do not bother to create event handlers here e.g. for on_trash 
# They do not work!  
# https://discuss.erpnext.com/t/hooks-on-child-table-not-working/37293
#
class BatchPaymentReferences(Document):
	pass
		