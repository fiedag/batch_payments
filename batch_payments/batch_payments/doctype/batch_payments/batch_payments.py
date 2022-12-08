# Copyright (c) 2022, Fiedler Consulting and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class BatchPayments(Document):
    pass



# get bills based on the information passed in the filter, 
# where does the filter need to live?  On this document?
@frappe.whitelist()
def get_items(source_name, target_doc=None):
    doc = get_mapped_doc(
        "Purchase Invoice",
        source_name,
        {
            "Purchase Invoice": {"doctype": "Batch Payments", "validation": {"docstatus": ["=", 1]}},
            "Purchase Invoice Item": {
                "doctype": "Batch Payment Items"
            },
        },
        target_doc,
    )
    return doc


@frappe.whitelist()
def create_payments(self=None):
    frappe.msgprint('create_payments', 'from batch_payments')
@frappe.whitelist()
def generate_file(self=None):
    frappe.msgprint('generate_file', 'from batch_payments')
@frappe.whitelist()
def send_remittances(self=None):
    frappe.msgprint('send_remittances', 'from batch_payments')


