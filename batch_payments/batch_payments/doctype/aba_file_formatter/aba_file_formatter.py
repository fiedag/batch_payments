# Copyright (c) 2023, Fiedler Consulting and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime


class ABAFileFormatter(Document):
	pass


@frappe.whitelist()
def generate_content(batch_payment):
	bank_account = frappe.get_doc("Bank Account", batch_payment.bank_account)
	bank = frappe.get_doc("Bank", bank_account.bank)
	descriptive_record = "0"
	descriptive_record += " "*17  # 17 blank characters
	descriptive_record += " "*2   # reel sequence number
	descriptive_record += bank.financial_institution_abbreviation.ljust(3)  # 3 characters
	descriptive_record += " "*7
	descriptive_record += bank_account.company[0:26].ljust(26) # 26 characters left just blank filled
	descriptive_record += bank_account.apca_payer_number[0:6].ljust(6) # 6 characters left just and blank filled
	descriptive_record += bank_account.company[0:12].ljust(12) # 12 characters left just blank filled
	posting_date = datetime.strptime(batch_payment.posting_date,"%Y-%m-%d")
	descriptive_record += posting_date.strftime("%d%m%y")
	descriptive_record += " "*40
	descriptive_record += "\n"
	# detail record
	total_paid = 0
	for r in batch_payment.references:
		descriptive_record += "1"
		payment = frappe.get_doc("Payment Entry", r.reference_name)
		supplier = frappe.get_doc("Supplier", payment.party)
		payee_account = frappe.get_doc("Bank Account", supplier.payee_account)
		descriptive_record += payee_account.branch_code[0:7].ljust(7)
		descriptive_record += payee_account.bank_account_no[0:9].rjust(9)
		descriptive_record += " "
		descriptive_record += "53"
		descriptive_record += str(round(payment.paid_amount * 100))[0:10].rjust(10,"0")
		descriptive_record += payee_account.account_name[0:32].ljust(32)
		descriptive_record += bank_account.branch_code[0:7].ljust(7)
		descriptive_record += bank_account.bank_account_no[0:9].rjust(9)
		descriptive_record += bank_account.company[0:16].ljust(16)
		descriptive_record += "0"*8
		descriptive_record += "\n"
		total_paid += payment.paid_amount
	# File Total Record (type 7)
	descriptive_record += "7"
	descriptive_record += "999-999"
	descriptive_record += " "*12
	descriptive_record += str(round(total_paid * 100))[0:10].rjust(10,"0") # net total
	descriptive_record += str(round(total_paid * 100))[0:10].rjust(10,"0") # credit total
	descriptive_record += "0"*10 # debit total
	descriptive_record += " "*24
	descriptive_record += str(round(len(batch_payment.references))).rjust(6,"0")
	descriptive_record += " "*40
	return descriptive_record

