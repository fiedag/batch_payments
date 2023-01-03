# Copyright (c) 2023, Fiedler Consulting and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RemittanceAdvice(Document):
	pass




@frappe.whitelist()
def send_remittance(payment, linked_document):
    #attachment = generate_remittance_pdf(payment)
    sender = frappe.utils.get_formatted_email(linked_document.owner)
    supplier = frappe.get_doc("Supplier", payment.party)
    
    payment_html = get_email_template("Remittance Advice", payment)

    frappe.sendmail(
        subject="Remittance Advice",
        sender=sender,
        recipients=supplier.send_remittance_to,
        #attachments=generate_remittance_pdf(payment),
        #template="remittance_advice",
        #add_unsubscribe_link=self.send_unsubscribe_link,
        #unsubscribe_method="/unsubscribe",
        #unsubscribe_params={"name": self.name},
        #reference_doctype=payment.doctype,
        #reference_name=payment.name,
        queue_separately=True,
        send_priority=0,
        message=payment_html,
    )
    frappe.msgprint('remittance for supplier ' + supplier.name + ' sent from ' + sender + ' to  ' + supplier.send_remittance_to)