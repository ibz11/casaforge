# Copyright (c) 2025, Ibrahim and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


# class Listing_Images(Document):
# 	pass

class PropertyListing(Document):
    def validate(self):
        # only restrict if user is not System Manager
        if "System Manager" not in frappe.get_roles(frappe.session.user):
            # find the agent record tied to this user
            agent = frappe.db.get_value("Agent", {"user": frappe.session.user}, "name")
            if not agent:
                frappe.throw("You are not linked to any Agent account.")
            if self.agent != agent:
                frappe.throw("You can only link this property to your own Agent account.")

