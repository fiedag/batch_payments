# Copyright (c) 2023, Fiedler Consulting and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class BAI2FileFormatter(Document):
	pass


@frappe.whitelist()
def generate_content(batch_payment):
	bank_account = frappe.get_doc("Bank Account", batch_payment.bank_account)
	bank = frappe.get_doc("Bank", bank_account.bank)
	descriptive_record = "01"               # File Header
	descriptive_record += "," + sender_bank
	descriptive_record += "," + receiver_bank 
	descriptive_record += "," + file_creation_date
	descriptive_record += "," + file_creation_time
	descriptive_record += "," + "1"
	descriptive_record += "," + phys_rec_length
	descriptive_record += "," + blocking_factor
	descriptive_record += "\n"

	descriptive_record = "02"              # Group Header
	descriptive_record += "," + ultimate_receiver
	descriptive_record += "," + originator_id   # SWIFT code usually
	descriptive_record += "," + "1"   # group status always 1
	descriptive_record += "," + as_of_date  # yymmdd
	descriptive_record += "," + as_of_time  # hhmm but almost always 0000
	descriptive_record += "\n"

	descriptive_record = "03"              # account identifier and summary status
	descriptive_record += "," + commercial_account_number   # customer commerc acc num at bank of origin
	descriptive_record += "," + currency_code   # SWIFT currency
	descriptive_record += "," + transaction_codes   # 3 digit account summary code
	descriptive_record += "," + amounts  # amount with implied decimals (2)
	descriptive_record += "\n"


	# detail record
	total_paid = 0
	for r in batch_payment.references:
		descriptive_record += "16"   # Payment detail
		payment = frappe.get_doc("Payment Entry", r.reference_name)
		supplier = frappe.get_doc("Supplier", payment.party)
		payee_account = frappe.get_doc("Bank Account", supplier.payee_account)
	
		descriptive_record += "," + transaction_code
		descriptive_record += "," + amount
		descriptive_record += "," + funds_type # 0 is immediately available
		descriptive_record += "," + reference_number 
		descriptive_record += "," + text
		descriptive_record += "\n"

		descriptive_record += "49"   # Account Trailer
		descriptive_record += "," + control_total_a
		descriptive_record += "," + control_total_b
		descriptive_record += "\n"
		total_paid += payment.paid_amount


	# Group Trailer
	descriptive_record += "98"
	descriptive_record += "," + group_control_total_a
	descriptive_record += "," + group_control_total_b
	descriptive_record += "\n"

	# File Trailer
	descriptive_record += "99"
	descriptive_record += "," + file_control_total_a
	descriptive_record += "," + file_control_total_b
	descriptive_record += "\n"

	return descriptive_record

