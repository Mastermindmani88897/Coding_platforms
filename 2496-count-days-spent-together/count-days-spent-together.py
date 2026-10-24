class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_day(date_str: str) -> int:
            month = int(date_str[:2])
            day = int(date_str[3:])
            return sum(days_in_months[:month - 1]) + day
        
        alice_arrive = date_to_day(arriveAlice)
        alice_leave = date_to_day(leaveAlice)
        bob_arrive = date_to_day(arriveBob)
        bob_leave = date_to_day(leaveBob)
        
        # Overlap interval: [max(start1, start2), min(end1, end2)]
        start = max(alice_arrive, bob_arrive)
        end = min(alice_leave, bob_leave)
        
        return max(0, end - start + 1)