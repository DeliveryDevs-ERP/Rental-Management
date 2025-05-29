# Copyright (c) 2025, osama.ahmed@deliverydevs.com and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ExistingCertificates(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		certificate_name: DF.Data | None
		customer: DF.Link | None
		date_of_expiry: DF.Date | None
		date_of_issue: DF.Date | None
		driver: DF.Link | None
		reference_no: DF.Data | None
		row_name: DF.Data | None
		vehicle: DF.Link | None
	# end: auto-generated types
	pass
