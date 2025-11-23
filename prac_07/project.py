from datetime import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion):
        self.name = name

        if isinstance(start_date, str):
            self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        else:
            self.start_date = start_date

        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion = int(completion)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion}%")

    def start_after(self, date):
        return self.start_date > date
