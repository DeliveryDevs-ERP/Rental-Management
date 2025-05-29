import frappe
from frappe.utils import nowdate, add_days
from frappe import _

def get_expiring_count(start_date, end_date):
    return frappe.db.count(
        "Existing Certificates",
        filters={
            "date_of_expiry": ["between", [start_date, end_date]]
        }
    )

def get_expired_count():
    return frappe.db.count(
        "Existing Certificates",
        filters={
            "date_of_expiry": ["<", nowdate()]
        }
    )

@frappe.whitelist()
def expired():
    count = get_expired_count()
    return {
        "value": count,
        "fieldtype": "Int",
        "route": ["List", "Existing Certificates"],
        "route_options": {
            "date_of_expiry": ["<", nowdate()]
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
            "date_of_expiry": ["between", [today, ten_days]]
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
            "date_of_expiry": ["between", [today, thirty_days]]
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
            "date_of_expiry": ["between", [today, sixty_days]]
        }
    }
