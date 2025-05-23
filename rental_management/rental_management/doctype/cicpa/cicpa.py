import frappe
from frappe import _
from frappe.model.document import Document

class CICPA(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		active: DF.Check
		amended_from: DF.Link | None
		cicpa_status: DF.Literal["", "Active", "Expired"]
		cicpa_type: DF.Literal["", "Driver", "Vehicle"]
		document: DF.Attach | None
		driver: DF.Link | None
		expiry_date: DF.Date
		issue_date: DF.Date
		loa: DF.Link
		vehicle: DF.Link | None
	# end: auto-generated types
 
	def on_submit(self):
		if self.loa:
			try:
				loa_doc = frappe.get_doc("LOA", self.loa)

				if self.cicpa_type == "Vehicle":
					loa_doc.total_created_vehicle_cicpa = (loa_doc.total_created_vehicle_cicpa or 0) + 1

				elif self.cicpa_type == "Driver":
					loa_doc.total_created_driver_cicpa = (loa_doc.total_created_driver_cicpa or 0) + 1

				loa_doc.save(ignore_permissions=True)
			except Exception as e:
				frappe.log_error(frappe.get_traceback(), "Error updating LOA CICPA count on submit")
				frappe.throw(_("Failed to update LOA record: {0}").format(str(e)))

	def on_trash(self):
		if self.loa:
			try:
				loa_doc = frappe.get_doc("LOA", self.loa)

				if self.cicpa_type == "Vehicle" and loa_doc.total_created_vehicle_cicpa:
					loa_doc.total_created_vehicle_cicpa = max(0, (loa_doc.total_created_vehicle_cicpa or 0) - 1)

				elif self.cicpa_type == "Driver" and loa_doc.total_created_driver_cicpa:
					loa_doc.total_created_driver_cicpa = max(0, (loa_doc.total_created_driver_cicpa or 0) - 1)

				loa_doc.save(ignore_permissions=True)
			except Exception as e:
				frappe.log_error(frappe.get_traceback(), "Error updating LOA CICPA count on delete")
				frappe.throw(_("Failed to update LOA record during deletion: {0}").format(str(e)))

	def on_change(self):
		# --- Update Vehicle Certification if cicpa_type is Vehicle ---
		if self.cicpa_type == "Vehicle" and self.vehicle:
			try:
				vehicle_doc = frappe.get_doc("Vehicle", self.vehicle)
				updated = False

				for row in vehicle_doc.get("custom_vehicle_certifications", []):
					if row.certification_name == "CICPA" and row.reference_no == self.name:
						row.date_of_expiry = self.expiry_date
						updated = True
						break

				if updated:
					vehicle_doc.save(ignore_permissions=True)
			except Exception as e:
				frappe.log_error(frappe.get_traceback(), "Error updating CICPA expiry date in Vehicle")
				frappe.throw(_("Failed to update CICPA expiry date in Vehicle: {0}").format(str(e)))

		# --- Update Driver Certification if cicpa_type is Driver ---
		if self.cicpa_type == "Driver" and self.driver:
			try:
				driver_doc = frappe.get_doc("Driver", self.driver)
				updated = False

				for row in driver_doc.get("custom_certification_list", []):
					if row.certification_name == "CICPA" and row.reference_no == self.name:
						row.date_of_expiry = self.expiry_date
						updated = True
						break

				if updated:
					driver_doc.save(ignore_permissions=True)
			except Exception as e:
				frappe.log_error(frappe.get_traceback(), "Error updating CICPA expiry date in Driver")
				frappe.throw(_("Failed to update CICPA expiry date in Driver: {0}").format(str(e)))
