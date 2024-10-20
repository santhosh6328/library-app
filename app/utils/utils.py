from datetime import date


def calculate_fee(issue_date, return_date):
   delta = (return_date - issue_date).days
   return delta * 10  # Assuming Rs.10 rent per day


def check_outstanding_debt(member):
   return member.outstanding_debt <= 500