"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #18 - MTG Mana Cost (manacost.py)


Author: Ainsley Ward

Difficulty Level: 6/10

Prompt: In a popular cardgame, Magic: The Gathering, “mana” is used as a resource to cast spells. 
There are six types of mana in Magic: white (W), blue (U), black (B), red (R), green (G), and colorless (C).
The mana cost of a spell indicates the amount and type(s) of mana that must be paid to cast the spell. 
If the mana cost contains a number (such as "3"), that number must be paid with that total amount of mana 
in any combination of types. If the mana cost contains a mana type ("W", "U", "B", "R", "G", or "C"), that 
symbol must be paid with one mana of the corresponding type. Each individual mana in the player's mana pool 
can only pay one part of the cost. For example, the mana cost "3WW" requires two white (W) mana and 3 
additional mana in any combination of types. The two white mana used to pay the "WW" do not also contribute 
to the "3". In this problem, you will be taking 2 string inputs (the player’s mana pool and mana cost), 
and returning a Boolean value that determines if you can afford to cast the spell.

Notes: Letters must be uppercase; If there is a number in the cost, it will always be at the beginning; Colorless, 'C' mana cannot be used for anything other than 'C' or digits:
       so mana_cost('C', 'W') would output "False", mana_cost('C', '1') would output "True"

Test Cases:
Input: player_mana = 'WWGR'; cost = '2WWG'; W
Output: False

Input: player_mana = 'CCWGR'; cost = '3WB';
Output: True

Input: player_mana = 'R'; cost = '1'; 
Output: True
"""

import numbers


class Solution:
    def mana_cost(self,pool, cost):
        # type pool: string
        # type cost: string
        # return: bool
    
        # TODO: Write code below to return a bool with the solution to the prompt
      
        num = 0 
        if cost[0].isnumeric():
            num = int(cost[0])
        pl = []

        for i in pool:
            pl.append(i)

        cs = []
        for i in cost:
            if i.isalpha():
                cs.append(i)

        for c in cost: 
            if c in pl: 
                pl.remove(c)
                cs.remove(c)
        
        if len(cs) > 0: 
            return False 

        if num != 0:

            if len(pl) >= num: 
                return True
            return False

        return True


    




        

def main():
    string1 = input().strip()
    string2 = input().strip()

    tc1 = Solution()
    ans = tc1.mana_cost(string1,string2)
    print(ans)

if __name__ == "__main__":
    main()