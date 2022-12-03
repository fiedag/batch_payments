# Copyright (c) 2022, Fiedler Consulting and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class BatchPayments(Document):

    @frappe.whitelist()
    def get_bills2(self):
	frappe.msgprint('The message title 2', 'FROM SERVER PYTHON SCRIPT 2')

    @frappe.whitelist()
    def get_bills(self):
        frappe.msgprint('get_bills2', 'FROM SERVER PYTHON SCRIPT')

