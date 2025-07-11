import frappe

@frappe.whitelist()
def get_customer_focal_person(party_name):
    """
    Given a Customer name, find the first Contact linked to it
    and return the formatted string for custom_customer_focal_person.
    """
    # find the Dynamic Link record
    links = frappe.get_all(
        "Dynamic Link",
        filters={
            "parenttype": "Contact",
            "link_doctype": "Customer",
            "link_name": party_name
        },
        fields=["parent"],
        limit_page_length=1
    )

    if not links:
        return ""

    # load the Contact doc
    contact = frappe.get_doc("Contact", links[0].parent)

    lines = []
    # full name
    full_name = " ".join(filter(None, [
        contact.first_name, contact.middle_name, contact.last_name
    ]))
    if full_name:
        lines.append(full_name)

    # designation (+ company)
    if contact.get("designation"):
        if contact.get("company_name"):
            lines.append(f"{contact.designation} - {contact.company_name}")
        else:
            lines.append(contact.designation)

    # phone / mobile / email
    if contact.get("phone"):
        lines.append(f"Phone: {contact.phone}")
    if contact.get("mobile_no"):
        lines.append(f"Mobile: {contact.mobile_no}")
    if contact.get("email_id"):
        lines.append(f"Email: {contact.email_id}")

    return "\n".join(lines)