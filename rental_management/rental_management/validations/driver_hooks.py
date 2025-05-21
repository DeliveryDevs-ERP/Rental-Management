import frappe

def validate_driver(doc, method):
    loa_to_recalc = None
    linked_cicpa_name = None
    remarks = ""
    cicpa_doc = None

    if doc.custom_cicpa:
        try:
            cicpa_doc = frappe.get_doc("CICPA", doc.custom_cicpa)
            loa_to_recalc = cicpa_doc.loa
            linked_cicpa_name = cicpa_doc.name
        except frappe.DoesNotExistError:
            pass

    if doc.custom_has_cicpa and cicpa_doc:
        frappe.db.set_value("CICPA", cicpa_doc.name, "driver", doc.name)
        remarks = "Adding Driver"

        if hasattr(doc, "custom_certification_list"):
            already_exists = any(
                row.reference_no == cicpa_doc.name
                for row in doc.custom_certification_list
            )
            if not already_exists:
                new_row = doc.append("custom_certification_list", {})
                new_row.certification_name = "CICPA"
                new_row.date_of_issue = cicpa_doc.issue_date
                new_row.date_of_expiry = cicpa_doc.expiry_date
                new_row.attachment = cicpa_doc.document
                new_row.reference_no = cicpa_doc.name

    else:
        cicpa_docs = frappe.get_all("CICPA", filters={"driver": doc.name}, fields=["name", "loa"])
        for cicpa in cicpa_docs:
            frappe.db.set_value("CICPA", cicpa.name, "driver", None)
            loa_to_recalc = cicpa.loa or loa_to_recalc
            linked_cicpa_name = cicpa.name
            remarks = "Removing Driver"

            # Remove matching certification row
            if hasattr(doc, "custom_certification_list"):
                doc.custom_certification_list = [
                    row for row in doc.custom_certification_list
                    if row.reference_no != cicpa.name
                ]

    if loa_to_recalc:
        cicpa_list = frappe.get_all(
            "CICPA",
            filters={"loa": loa_to_recalc},
            fields=["vehicle", "driver"]
        )

        allocated_vehicle = sum(1 for d in cicpa_list if d.vehicle)
        allocated_driver = sum(1 for d in cicpa_list if d.driver)

        loa_doc = frappe.get_doc("LOA", loa_to_recalc)
        loa_doc.allocated_vehicle_quota = allocated_vehicle
        loa_doc.remaining_vehicle_quota = loa_doc.total_vehicle_quota - allocated_vehicle
        loa_doc.allocated_driver_quota = allocated_driver
        loa_doc.remaining_driver_quota = loa_doc.total_driver_quota - allocated_driver

        loa_doc.save(ignore_permissions=True)

    # Create CICPA Log
    if linked_cicpa_name and remarks:
        cicpa_record = frappe.get_doc("CICPA", linked_cicpa_name)
        frappe.get_doc({
            "doctype": "CICPA Logs",
            "cicpa": cicpa_record.name,
            "loa": cicpa_record.loa,
            "vehicle": cicpa_record.vehicle,
            "driver": cicpa_record.driver,
            "remarks": remarks,
            "docstatus": 1
        }).insert(ignore_permissions=True)
