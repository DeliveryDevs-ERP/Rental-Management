import frappe
from frappe.model.document import Document

class CICPA(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.
	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		document: DF.Attach | None
		driver: DF.Link | None
		expiry_date: DF.Date
		issue_date: DF.Date
		loa: DF.Link
		vehicle: DF.Link | None
	# end: auto-generated types
	pass
	# def on_change(self):
	# 	if self.loa:
	# 		loa_doc = frappe.get_doc("LOA", self.loa)

	# 		cicpa_list = frappe.get_all(
	# 			"CICPA",
	# 			filters={"loa": self.loa},
	# 			fields=["name", "vehicle", "driver"]
	# 		)

	# 		allocated_vehicle = sum(1 for d in cicpa_list if d.vehicle)
	# 		allocated_driver = sum(1 for d in cicpa_list if d.driver)

	# 		loa_doc.allocated_vehicle_quota = allocated_vehicle
	# 		loa_doc.remaining_vehicle_quota = loa_doc.total_vehicle_quota - allocated_vehicle

	# 		loa_doc.allocated_driver_quota = allocated_driver
	# 		loa_doc.remaining_driver_quota = loa_doc.total_driver_quota - allocated_driver

	# 		loa_doc.save(ignore_permissions=True)
	# 		frappe.db.commit()

	# def validate(self):
	# 	if self.loa:
	# 		loa_doc = frappe.get_doc("LOA", self.loa)

	# 		cicpa_list = frappe.get_all(
	# 			"CICPA",
	# 			filters={"loa": self.loa},
	# 			fields=["name", "vehicle", "driver"]
	# 		)

	# 		allocated_vehicle = sum(1 for d in cicpa_list if d.vehicle)
	# 		allocated_driver = sum(1 for d in cicpa_list if d.driver)

	# 		loa_doc.allocated_vehicle_quota = allocated_vehicle
	# 		loa_doc.remaining_vehicle_quota = loa_doc.total_vehicle_quota - allocated_vehicle

	# 		loa_doc.allocated_driver_quota = allocated_driver
	# 		loa_doc.remaining_driver_quota = loa_doc.total_driver_quota - allocated_driver

	# 		loa_doc.save(ignore_permissions=True)
	# 		frappe.db.commit()