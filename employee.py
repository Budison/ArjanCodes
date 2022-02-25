from dataclasses import dataclass
from operator import truediv

@dataclass
class Employee:
    name: str
    employee_id: int
    pay_rate: float = 100.0
    hours_worked: float = 0.0
    employer_cost: float = 1000.0
    has_commission: bool = True
    commission: float = 100.0
    contracts_landed: int = 0


    def compute_payout(self) -> float:
        payout = self.pay_rate * self.hours_worked + self.employer_cost
        if self.has_commission:
            payout += self.commission * self.contracts_landed
        return payout
