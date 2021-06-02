class User:
    def __init__(self, user_name, budget, id=None):
        self.user_name = user_name
        self.budget = budget
        self.id = id

    def budget_status(self, total_spending):
        budget = self.budget
        total_spending = total_spending
        status = budget - total_spending

        userstatus = ""
        if status <= 0:
            userstatus = "Not good"
        elif status > 0 and status <= 50:
            userstatus = "Red"
        elif status >= 51 and status <= 150:
            userstatus = "Amber"
        else:
            userstatus = "Green"
        return userstatus
