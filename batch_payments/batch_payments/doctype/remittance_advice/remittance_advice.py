# Copyright (c) 2023, Fiedler Consulting and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.email.doctype.email_template.email_template import get_email_template
from frappe.core.doctype.communication.email import make


class RemittanceAdvice(Document):
	pass


@frappe.whitelist()
def send_remittance(payment, linked_document):
    sender = frappe.utils.get_formatted_email(linked_document.owner)
    supplier = frappe.get_doc("Supplier", payment.party)
    
    result = get_email_template("Remittance Advice", payment.as_dict())
    print(result)
    subject = result["subject"]
    content = result["message"]

    make(
        recipients = supplier.send_remittance_to,
        subject=subject,
        content = content,
        doctype="Payment Entry",
        name=payment.name,
        send_email=1,
        send_me_a_copy=0,
        print_format="Remittance Advice",
        sender="alex@fiedlerconsulting.com.au",
        email_template="Remittance Advice",
        print_letterhead=1
    )
    frappe.msgprint('remittance for supplier ' + supplier.name + ' sent from ' + sender + ' to  ' + supplier.send_remittance_to)



@frappe.whitelist()
def send_remittance_hide(payment, linked_document):
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