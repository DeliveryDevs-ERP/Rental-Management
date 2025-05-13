# Copyright (c) 2025, osama.ahmed@deliverydevs.com and contributors
# For license information, please see license.txt

from frappe.model.document import Document
import frappe
from frappe import _


class DriverMovement(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        amended_from: DF.Link | None
        date: DF.Date
        driver: DF.Link
        employment_type: DF.Link | None
        mobilization_status: DF.Literal["", "Mobilize", "Demobilize"]
        ownership_status: DF.Data | None
        project: DF.Link
        shift: DF.Link
        vehicle: DF.Link
        vehicle_type: DF.Data | None
    # end: auto-generated types

    def on_submit(self):
        try:                
            # Default submission functions 
            self.update_driver_shift_vehicle()
            if self.mobilization_status == "Mobilize":
                #only on Mob
                self.create_shift_assignment()
            else:
                # self.edit_shift_assignment()
                print()
        except Exception as e:
            frappe.db.rollback()
            frappe.throw(_(f"Vehicle Movement submission failed due to: {str(e)}"))

    def update_driver_shift_vehicle(self):
        if self.mobilization_status == "Mobilize":
            if not self.vehicle:
                frappe.throw(_("Vehicle is not specified."))

            if not self.driver or not self.shift:
                frappe.throw(_("Driver and Shift must be specified."))
            vehicle_doc = frappe.get_doc("Vehicle", self.vehicle)
            vehicle_doc.append("custom_driver_shifts", {
                "driver": self.driver,
                "mobilization": self.name,
                "shift": self.shift
            })
            vehicle_doc.save(ignore_permissions=True)

    def create_shift_assignment(self):
        driver_doc = frappe.get_doc("Driver", self.driver)
        if not driver_doc.employee:
            frappe.throw(_("No employee linked to this driver."))

        employee_doc = frappe.get_doc("Employee", driver_doc.employee)

        shift_assignment = frappe.get_doc({
            "doctype": "Shift Assignment",
            "employee": driver_doc.employee,
            "shift_type": self.shift,
            "status": "Active",
            "start_date": self.date,
            "company": employee_doc.company,
            "custom_mobilization": self.name,
            "docstatus": 0
        })

        shift_assignment.insert(ignore_permissions=True)
        shift_assignment.save()
        
    # def edit_shift_assignment(self):
    #     driver_doc = frappe.get_doc("Driver", self.driver)
    #     if not driver_doc.employee:
    #         frappe.throw(_("No employee linked to this driver."))

    #     employee_doc = frappe.get_doc("Employee", driver_doc.employee)

    #     shift_assignment = frappe.get_doc({
    #         "doctype": "Shift Assignment",
    #         "employee": driver_doc.employee,
    #         "shift_type": self.shift,
    #         "status": "Active",
    #         "start_date": self.date,
    #         "company": employee_doc.company,
    #         "custom_mobilization": self.name,
    #         "docstatus": 0
    #     })

    #     shift_assignment.insert(ignore_permissions=True)
    #     shift_assignment.save()