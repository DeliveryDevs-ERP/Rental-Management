// Copyright (c) 2025, osama.ahmed@deliverydevs.com and contributors
// For license information, please see license.txt

frappe.ui.form.on("LOA", {
    refresh: function(frm) {
        if (!frm.is_new() && frm.doc.docstatus === 1) { 
            frm.add_custom_button(__('CICPA'), function() {
                frappe.new_doc("CICPA", {
                    loa: frm.doc.name
                });
            }, __("Create"));  
        }
    }
});
