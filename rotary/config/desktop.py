from frappe import _

def get_data():
	return {
		"Monthly Report": {
			"color": "#ff9a00",
			"icon": "octicon octicon-organization",
			"label": _("Monthly Report"),
			"link": "List/Monthly Report",
			"doctype": "Monthly Report",
			"type": "list"
		}
	}
