// Copyright (c) 2025, osama.ahmed@deliverydevs.com and contributors
// For license information, please see license.txt

frappe.ui.form.on("Driver Movement", {

     driver(frm) {
        if (frm.doc.driver) {
            frappe.db.get_doc("Driver", frm.doc.driver).then(driver_doc => {
                if (driver_doc.employee) {
                    frappe.db.get_doc("Employee", driver_doc.employee).then(employee_doc => {
                        frm.set_value("employment_type", employee_doc.employment_type);
                    });
                }
            });
        }
    },


	refresh(frm) {

	},
});
