# Copyright (c) 2022, Fiedler Consulting and contributors
# For license information, please see license.txt

import frappe
from frappe import _

from frappe.model.document import Document

class BatchPaymentReferences(Document):
	def on_trash(self):
		frappe.throw(_("I cannot allow you to do that Dave"))

		#pymt = frappe.get_doc(self.reference_type, self.reference_name)
		#pymt.cancel()
		#pymt.delete_doc()
		