from datetime import date


def calculate_fee(issue_date, return_date):
   # charging 1 re per second
   return return_date - issue_date


def check_outstanding_debt(member):
   return member.outstanding_debt <= 500