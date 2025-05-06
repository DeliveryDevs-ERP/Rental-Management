# Copyright (c) 2025, osama.ahmed@deliverydevs.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class VehicleMovement(Document):
    
    def on_submit(self):
        try:
            self.update_vehicle()
        except Exception as e:
            frappe.db.rollback()
            frappe.throw(_(f"Vehicle Movement submission failed due to: {str(e)}"))

    def update_vehicle(self):
        if self.status == "Mobilise":
            if not self.vehicle:
                frappe.throw(_("Vehicle is not specified."))

            frappe.db.set_value("Vehicle", self.vehicle, {
                "custom_last_location": self.location_to,
                "custom_state": "With Client"
            })
            frappe.db.commit()
