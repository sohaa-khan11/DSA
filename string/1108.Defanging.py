"""
1108. Defanging an IP Address
link: https://leetcode.com/problems/defanging-an-ip-address/description/
"""
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")