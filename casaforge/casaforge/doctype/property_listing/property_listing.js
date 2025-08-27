frappe.ui.form.on("Property Listing", {
    // Trigger after save
        validate(frm) {
        frappe.msgprint(" Validate event triggered before saving!");
    },
    after_save(frm) {
        frappe.msgprint(" Property Listing has been saved successfully!");
    }
});




// console.log("PropertyListing JS loaded");
// frappe.ui.form.on("Property Listing", {
//     setup(frm) {
//         frm.fields_dict["agent"].get_query = function() {
//             return {
//                 filters: {
//                     user: frappe.session.user   // only the agent mapped to logged-in user
//                 }
//             };
//         };
//     },

//     onload(frm) {
//         console.log("PropertyListing JS loaded");
//         if (frm.is_new() && !frm.doc.agent) {
//             frappe.db.get_value("Agent", { user: frappe.session.user }, "name")
//                 .then(r => {
//                     if (r && r.message && r.message.name) {
//                         frm.set_value("agent", r.message.name);
//                     }
//                 });
//         }
//     }
// });

