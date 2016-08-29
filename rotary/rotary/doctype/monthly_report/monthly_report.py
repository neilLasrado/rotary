# -*- coding: utf-8 -*-
# Copyright (c) 2015, Neil Lasrado and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import now

class MonthlyReport(Document):
	def on_submit(self):
		self.date = now()
