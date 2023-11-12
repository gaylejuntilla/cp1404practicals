"""Project class"""


class Project:
    """Project class"""
    def __init__(self, name="", start_date="%d/%m/%Y", priority=0, cost_estimate=0.0, completion_percent=0):
        """Initialise project object"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percent = completion_percent

    def __repr__(self):
        """Display string representation of project object"""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: {self.cost_estimate}" \
               f", completion: {self.completion_percent}"

    def __gt__(self, other):
        """Determine if start date is later"""
        return self.start_date > other.start_date
