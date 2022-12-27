// Copyright (c) 2022, Fiedler Consulting and contributors
// For license information, please see license.txt

frappe.ui.form.on('Batch Payments', {
	refresh: function(frm) {

		frm.add_custom_button(__('Purchase Invoice'), function() {
				erpnext.utils.map_current_doc({
					method: "batch_payments.batch_payments.doctype.batch_payments.batch_payments.get_items",
					source_doctype: "Purchase Invoice",
					target: frm,
					date_field: "supplier",
					setters: {
						supplier: frm.doc.supplier || undefined,

					},
					get_query_filters: {
						docstatus: 1,
						is_paid: 0,
						currency: ["=", frm.doc.currency],
						
						status: ["!=", "Paid"]
					}
				})
			}, __("Get Items From"));

		frm.add_custom_button(__('Create Payments'), function() {
				frm.call({
					doc: frm.doc,
					method: "create_payments",
					callback: function(r) {
						// here we want to populate the payment references child table
					}
				})
			}, __("Payments"));


		frm.add_custom_button(__('Delete Payments'), function() {
				
				frappe.confirm(
					"Do you wish to delete the existing payments?",
					() => frm.call({
							doc: frm.doc,
							method: "delete_payments",
							callback: function(r) {
								
							}
						}),
					() => {}
				)

				
			}, __("Payments"));


		frm.add_custom_button(__('Generate File'), function() {
				frm.call({
					doc: frm.doc,
					method: "generate_file",
					callback: function(r) {
						
						frappe.show_alert("Bank File generated.",5);
					}
				})
			}, __("Bank File"));

		frm.add_custom_button(__('Download File'), function() {

			window.open(frm.doc.file_url, "_blank");
			}, __("Bank File"));
		
		
	}
});

