class Solution:
    def stableMarriage(self, men, women):
        n = len(men)
        
        women_rank = [[0]*n for _ in range(n)]
        for w in range(n):
            for rank, m in enumerate(women[w]):
                women_rank[w][m] = rank
        
        free_men = list(range(n))
        next_proposal = [0]*n
        partner_woman = [-1]*n
        
        while free_men:
            m = free_men.pop(0)
            w = men[m][next_proposal[m]]
            next_proposal[m] += 1
            
            if partner_woman[w] == -1:
                partner_woman[w] = m
            else:
                current = partner_woman[w]
                if women_rank[w][m] < women_rank[w][current]:
                    partner_woman[w] = m
                    free_men.append(current)
                else:
                    free_men.append(m)
        
        result = [0]*n
        for w in range(n):
            result[partner_woman[w]] = w
        
        return result