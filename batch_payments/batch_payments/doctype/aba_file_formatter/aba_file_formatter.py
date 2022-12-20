# Copyright (c) 2022, Fiedler Consulting and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime


class ABAFileFormatter(Document):

	def __init__(self, batch_payment):
		self.batch_payment = batch_payment

	@frappe.whitelist()
	def generate_content(self):

		bank_account = frappe.get_doc("Bank Account", self.batch_payment.bank_account)

		self.descriptive_record = "0"
		self.descriptive_record += " "*17  # 17 blank characters
		self.descriptive_record += " "*2   # reel sequence number
		self.descriptive_record += bank_account.account_type.ljust(3)  # 3 characters
		self.descriptive_record += " "*7
		self.descriptive_record += bank_account.company[0:26].ljust(26) # 26 characters left just blank filled
		self.descriptive_record += bank_account.apca_payer_number[0:6].ljust(6) # 6 characters left just and blank filled
		self.descriptive_record += bank_account.company[0:12].ljust(12) # 12 characters left just blank filled
		posting_date = datetime.strptime(self.batch_payment.posting_date,"%Y-%m-%d")
		self.descriptive_record += posting_date.strftime("%d%m%y")
		self.descriptive_record += " "*40
		self.descriptive_record += "\n"

		# detail record
		total_paid = 0
		for r in self.batch_payment.references:
			self.descriptive_record += "1"
			payment = frappe.get_doc("Payment Entry", r.reference_name)
			supplier = frappe.get_doc("Supplier", payment.party)
			payee_account = frappe.get_doc("Bank Account", supplier.payee_account)

			self.descriptive_record += payee_account.branch_code[0:7].ljust(7)
			self.descriptive_record += payee_account.bank_account_no[0:9].rjust(9)
			self.descriptive_record += " "
			self.descriptive_record += "53"
			self.descriptive_record += str(round(payment.paid_amount * 100))[0:10].rjust(10,"0")
			self.descriptive_record += payee_account.account_name[0:32].ljust(32)
			self.descriptive_record += bank_account.branch_code[0:7].ljust(7)
			self.descriptive_record += bank_account.bank_account_no[0:9].rjust(9)
			self.descriptive_record += bank_account.company[0:16].ljust(16)
			self.descriptive_record += "0"*8

			self.descriptive_record += "\n"
			total_paid += payment.paid_amount


		# File Total Record (type 7)
		self.descriptive_record += "7"
		self.descriptive_record += "999-999"
		self.descriptive_record += " "*12
		self.descriptive_record += str(round(total_paid * 100))[0:10].rjust(10,"0") # net total
		self.descriptive_record += str(round(total_paid * 100))[0:10].rjust(10,"0") # credit total
		self.descriptive_record += "0"*10 # debit total
		self.descriptive_record += " "*24
		self.descriptive_record += str(round(len(self.batch_payment.references))).rjust(6,"0")
		self.descriptive_record += " "*40


		return self.descriptive_record


