
from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        count = defaultdict(int)

        for domain in cpdomains:
            visits, address = domain.split()
            visits = int(visits)

            parts = address.split('.')

            for i in range(len(parts)):
                subdomain = '.'.join(parts[i:])
                count[subdomain] += visits

        return [
            f"{visits} {domain}"
            for domain, visits in count.items()
        ]
