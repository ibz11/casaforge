// Copyright (c) 2025, Ibrahim and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Listings", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Property Listing", {
    // Trigger after save
        validate(frm) {
        frappe.msgprint(" Validate event triggered before saving!");
    },
    after_save(frm) {
        frappe.msgprint(" Property Listing has been saved successfully!");
    }
});
