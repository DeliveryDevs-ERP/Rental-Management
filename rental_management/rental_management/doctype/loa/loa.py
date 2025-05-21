# Copyright (c) 2025, osama.ahmed@deliverydevs.com and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LOA(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from rental_management.rental_management.doctype.loa_locations_cdt.loa_locations_cdt import LOAlocationscdt

		allocated_driver_quota: DF.Int
		allocated_vehicle_quota: DF.Int
		amended_from: DF.Link | None
		document: DF.Attach
		end_user: DF.Data
		expiry_date: DF.Date
		issue_date: DF.Date
		issuing_authority: DF.Link
		locations: DF.Table[LOAlocationscdt]
		remaining_driver_quota: DF.Int
		remaining_vehicle_quota: DF.Int
		total_driver_quota: DF.Int
		total_vehicle_quota: DF.Int
	# end: auto-generated types
	pass
