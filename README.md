## Batch Payments

Permit multiple purchase invoices to be paid in one batch.
Produce an Australian Banking Association ABA file for outbound payments to multiple parties.
Generate and send remittance advice emails to parties.


Requires standard Bank Account record type to have currency and file_format fields.

- Create a bank record and populate the `Financial Institution Abbreviation` custom field with a max 3 char abbreviation for the bank e.g. CBA, ANZ 
- Create a bank account linked to this bank, and populate the `Branch Code` with the BSB number in 000-000 format e.g. 065-125 
- Populate the `Bank Account No` field with the account number. 
- Populate the `ACPA Payer Number` field with the number the bank has issued you. 
- Populate the `Currency` custom field with the currency of the payments being made using your bank file.  In practice only AUD is currently implemented.
- Populate the custom `File Format` field with the file format you wish to generate, e.g. ABA, MT940, SWIFT.  In practice only the ABA file format is currently implemented.
- Create a bank account record for every vendor you wish to pay, and for each of these bank accounts, specify the Branch Code and Account number.  There is no need to specify the currency, file format or ACPA code for these bank accounts.
- Specify this bank account in the custom `Payee Bank Account` field of the Supplier.
- For each vendor ensure you specify a destination email address in the custom `Send Remittance To` field.
- Navigate to the Email Template list and edit the `Remittance Advice` email template to suit.
- Navigate to the Print Format list and edit the `Remittance Advice` print format to suit. 


#### License

GNU
