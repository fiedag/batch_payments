// Copyright (c) 2022, Fiedler Consulting and contributors
// For license information, please see license.txt

frappe.ui.form.on('Batch Payments', {
	refresh: function(frm) {
		frm.add_custom_button(__("Get Bills"), function() {
			get_bills(frm);
		});
		frm.add_custom_button(__("Get Bills2"), function() {
                        get_bills2(frm);
                });

	}
});


function get_bills(frm) {

	//alert("get bills, save first then iterate through the Batch Payment Items" + frm);
	frappe.call({
		method: 'get_bills',
		doc: frm.doc,
		callback: function (r) {
			console.log('get_bills call back ' + r);
		}
	})
}

function get_bills2(frm) {

        //alert("get bills, save first then iterate through the Batch Payment Items" + frm);
        frappe.call({
                method: 'get_bills2',
                doc: frm.doc,
                callback: function (r) {
			console.log('get_bills2 callnback' + r);
		}
        })
}
