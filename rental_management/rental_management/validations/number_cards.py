import frappe
from frappe.utils import nowdate, add_days
from frappe import _

# Reusable
def get_expiring_count(start_date, end_date, employee_only=False):
    filters = {
        "date_of_expiry": ["between", [start_date, end_date]],
        "mark_as_not_renew": 0 
    }
    if employee_only:
        filters["employee"] = ["is", "set"]
    else:
        filters["employee"] = ["is", "not set"]
    return frappe.db.count("Existing Certificates", filters=filters)

def get_expired_count(employee_only=False):
    filters = {
        "date_of_expiry": ["<", nowdate()],
        "mark_as_not_renew": 0  
    }
    if employee_only:
        filters["employee"] = ["is", "set"]
    else:
        filters["employee"] = ["is", "not set"]
    return frappe.db.count("Existing Certificates", filters=filters)

def get_total_employee_certs():
    return frappe.db.count("Existing Certificates", filters={"employee": ["is", "set"]})

# ========== VEHICLE CERTIFICATE CARDS ==========
@frappe.whitelist()
def expired():
    count = get_expired_count()
    return {
        "value": count,
        "fieldtype": "Int",
        "route": ["List", "Existing Certificates"],
        "route_options": {
            "date_of_expiry": ["<", nowdate()],
            "employee": ["is", "not set"],
            "mark_as_not_renew": 0
        }
    }

@frappe.whitelist()
def expire_in_10_days():
    today = nowdate()
    ten_days = add_days(today, 10)
    count = get_expiring_count(today, ten_days)
    return {
        "value": count,
        "fieldtype": "Int",
        "route": ["List", "Existing Certificates"],
        "route_options": {
            "date_of_expiry": ["between", [today, ten_days]],
            "employee": ["is", "not set"],
            "mark_as_not_renew": 0
        }
    }

@frappe.whitelist()
def expire_in_30_days():
    today = nowdate()
    thirty_days = add_days(today, 30)
    count = get_expiring_count(today, thirty_days)
    return {
        "value": count,
        "fieldtype": "Int",
        "route": ["List", "Existing Certificates"],
        "route_options": {
            "date_of_expiry": ["between", [today, thirty_days]],
            "employee": ["is", "not set"],
            "mark_as_not_renew": 0
        }
    }

@frappe.whitelist()
def expire_in_60_days():
    today = nowdate()
    sixty_days = add_days(today, 60)
    count = get_expiring_count(today, sixty_days)
    return {
        "value": count,
        "fieldtype": "Int",
        "route": ["List", "Existing Certificates"],
        "route_options": {
            "date_of_expiry": ["between", [today, sixty_days]],
            "employee": ["is", "not set"],
            "mark_as_not_renew": 0
        }
    }

# ========== EMPLOYEE CERTIFICATE CARDS ==========

@frappe.whitelist()
def total_employee_certifications():
    count = get_total_employee_certs()
    return {
        "value": count,
        "fieldtype": "Int",
        "route": ["List", "Existing Certificates"],
        "route_options": {
            "employee": ["is", "set"],
            "mark_as_not_renew": 0
        }
    }

@frappe.whitelist()
def employee_expired():
    count = get_expired_count(employee_only=True)
    return {
        "value": count,
        "fieldtype": "Int",
        "route": ["List", "Existing Certificates"],
        "route_options": {
            "date_of_expiry": ["<", nowdate()],
            "employee": ["is", "set"],
            "mark_as_not_renew": 0
        }
    }

@frappe.whitelist()
def employee_expire_in_10_days():
    today = nowdate()
    ten_days = add_days(today, 10)
    count = get_expiring_count(today, ten_days, employee_only=True)
    return {
        "value": count,
        "fieldtype": "Int",
        "route": ["List", "Existing Certificates"],
        "route_options": {
            "date_of_expiry": ["between", [today, ten_days]],
            "employee": ["is", "set"],
            "mark_as_not_renew": 0
        }
    }

@frappe.whitelist()
def employee_expire_in_30_days():
    today = nowdate()
    thirty_days = add_days(today, 30)
    count = get_expiring_count(today, thirty_days, employee_only=True)
    return {
        "value": count,
        "fieldtype": "Int",
        "route": ["List", "Existing Certificates"],
        "route_options": {
            "date_of_expiry": ["between", [today, thirty_days]],
            "employee": ["is", "set"],
            "mark_as_not_renew": 0
        }
    }

@frappe.whitelist()
def employee_expire_in_60_days():
    today = nowdate()
    sixty_days = add_days(today, 60)
    count = get_expiring_count(today, sixty_days, employee_only=True)
    return {
        "value": count,
        "fieldtype": "Int",
        "route": ["List", "Existing Certificates"],
        "route_options": {
            "date_of_expiry": ["between", [today, sixty_days]],
            "employee": ["is", "set"],
            "mark_as_not_renew": 0
        }
    }


@frappe.whitelist()
def marked_not_renew():
    count = frappe.db.count("Existing Certificates", filters={
        "mark_as_not_renew": 1,
        "employee": ["is", "not set"]
    })
    return {
        "value": count,
        "fieldtype": "Int",
        "label": _("Marked Not for Renewal"),
        "route": ["List", "Existing Certificates"],
        "route_options": {
            "mark_as_not_renew": 1,
            "employee": ["is", "not set"]
        }
    }

@frappe.whitelist()
def marked_not_renew_employees():
    count = frappe.db.count("Existing Certificates", filters={
        "mark_as_not_renew": 1,
        "employee": ["is", "set"]
    })
    return {
        "value": count,
        "fieldtype": "Int",
        "label": _("Marked Not for Renewal (Employees)"),
        "route": ["List", "Existing Certificates"],
        "route_options": {
            "mark_as_not_renew": 1,
            "employee": ["is", "set"]
        }
    }
