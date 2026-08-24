class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        parent = {}
        rank = {}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1
        email_to_name = {}
        # Create nodes and connect emails belonging
        # to the same account.
        for account in accounts:
            name = account[0]
            first_email = account[1]
            if first_email not in parent:
                parent[first_email] = first_email
                rank[first_email] = 0
            email_to_name[first_email] = name
            for email in account[2:]:
                if email not in parent:
                    parent[email] = email
                    rank[email] = 0
                email_to_name[email] = name
                union(first_email, email)
        # Group emails according to their root.
        groups = defaultdict(list)
        for email in parent:
            root = find(email)
            groups[root].append(email)
        # Build final answer.
        result = []
        for emails in groups.values():
            emails.sort()
            name = email_to_name[emails[0]]
            result.append([name] + emails)
        return result        
