## Batch Payments

Permit multiple purchase invoices to be paid in one batch.
Produce an Australian Banking Association ABA file for outbound payments to multiple parties.
Generate and send remittance advice emails to parties.


#### Setup
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


- Create your first Batch Payment record and review the columns in the To be paid child table and the Payments made table.
- Using the cog icon, ensure all the hidden columns of the child tables are made visible.  

![image](https://user-images.githubusercontent.com/4979071/210536555-f7387d01-a4a3-4ba6-92c0-8e0ac4c7a5b4.png)


#### Usage

- Create a Batch Payment record, selecting a Bank Account for payments to be made from. Select a date, posting date and save the record.
- Select Get Items From  -> Purchase Invoice
![image](https://user-images.githubusercontent.com/4979071/210537022-a1c94272-c6c5-450e-8589-a9a2504b85a4.png)
- Filter the suppliers and purchase invoices as required, then select the ones you wish to pay
![image](https://user-images.githubusercontent.com/4979071/210537521-38d37d97-d8ec-44a6-837d-7c8468dea0f0.png)
- Save the record.
- Create the payments using Payments -> Create Payments
![image](https://user-images.githubusercontent.com/4979071/210538028-b5151ace-b4d8-4982-99f8-ddc6853a6937.png)
- A single payment is created for every supplier, containing all the purchase invoices (bills) selected for that supplier.
- Email remittance advice records using Payments -> Send Remittances
![image](https://user-images.githubusercontent.com/4979071/210538381-a3f0534f-2e79-4ba0-8f2a-04ba2bc91711.png)
- Note that currently no preview of the remittance advice emails is implemented.  You are able to preview the remittance advices by navigating to the Payment Entry and printing the remittance advice print format.
- 
- 




#### License

GNU
