frappe.ui.form.on('Listing_Images', {
  attached_image: function (frm, cdt, cdn) {
    const row = locals[cdt][cdn];
    // Set the preview_image to match the attached image path
    row.preview_image = row.attached_image;
    frm.refresh_field('Images'); // Refresh the whole child table
  }
});

