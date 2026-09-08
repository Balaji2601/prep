# https://leetcode.com/problems/distinct-subsequences-ii/description/

from functools import cache

# Revise
# About mod and prev, lastseen how they were used.
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        result = set()

        @cache
        def solve(i,temp):
            if i == n:
                if temp not in result:
                    result.add(temp)
                return
            

            temp += s[i]
            pick = solve(i+1,temp)
            temp = temp[:-1]
            skip = solve(i+1,temp)
        
        solve(0,"")
        return len(result)-1

# Optimized(Explanation with comments below)
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        last_seen = [0]*26
        prev = [0]*(n+1)
        MOD = 10**9 + 7

        @cache
        def solve(n):
            if n == 0:
                return 1

            total = (2*solve(n-1)) % MOD
            
            duplicates = 0
            if prev[n] != 0:
                duplicates = solve(prev[n]-1)
            total = (total - duplicates + MOD) % MOD

            return total

        for i in range(1, n+1):
            idx = ord(s[i-1]) - ord("a")
            prev[i] = last_seen[idx]
            last_seen[idx] = i

        return (solve(n) - 1 + MOD) % MOD

# Explanation
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # How does a subsequence get BUILT from scratch? Start with just the empty
        # subsequence {""}. When a new character c comes into the picture, for every
        # subsequence we already have there are two options: don't append c (keep it
        # as it is), or append c. So every existing subsequence produces two, which
        # means: count(n) = 2 * count(n-1).
        #   s = "abc":  1 -> 2 -> 4 -> 8   (each step just doubles the previous)
        #
        # solve(n) = number of subsequences (including "") formed from the first n
        # characters. If we don't know solve(n), we ask the recursion for solve(n-1)
        # and multiply by 2.
        #
        # The catch: the problem wants DISTINCT subsequences, and the string can
        # have duplicate characters. Take s = "xaba" (1-based). When the LAST 'a'
        # (position 4) comes in, it asks the same question the FIRST 'a' (position 2)
        # already asked: "append me to the empty subsequence, or not". That repeats
        # exactly the strings that existed just before the first 'a' appeared, each
        # now regenerated with an 'a' stuck on -> those are duplicates.
        #   How many? Exactly the number of subsequences that existed just before
        #   the previous occurrence of this character. The previous 'a' is at
        #   position 2, so "just before" it means the first (2-1)=1 characters,
        #   i.e. solve(prev[n] - 1). Subtract that from total.
        #
        # prev[i]      : 1-based position where s[i-1] appeared the previous time
        #                (0 if this is the first time we see that letter). This is
        #                the value the recursion reads.
        # last_seen[c] : 1-based position where letter c was most recently seen while
        #                scanning left to right (0 = not yet). Only used to fill prev[].
        #
        # Example s = "xaba"  ->  prev = [_, 0, 0, 0, 2]
        #   solve(0) = 1                                    {""}
        #   solve(1) = 2*1              = 2    ('x' first)   {"", x}
        #   solve(2) = 2*2              = 4    ('a' first)   {"", x, a, xa}
        #   solve(3) = 2*4             = 8    ('b' first)   {"", x, a, xa, b, xb, ab, xab}
        #   solve(4) = 2*8 - solve(2-1) = 16 - solve(1) = 16 - 2 = 14
        #             (the 2 removed are the regenerated "a" and "xa")
        #   answer = solve(4) - 1 = 13   (drop the empty subsequence)
        n = len(s)
        last_seen = [0]*26        # last_seen[c]: most recent 1-based position of letter c, 0 if unseen
        prev = [0]*(n+1)          # prev[i]: previous occurrence of s[i-1] (1-based), 0 if first time
        MOD = 10**9 + 7

        @cache
        def solve(n):
            if n == 0:
                return 1                              # empty subsequence

            total = (2*solve(n-1)) % MOD              # every prior subseq -> keep it + append current char

            duplicates = 0
            if prev[n] != 0:                          # current char seen before -> some strings regenerated
                # subseqs that existed just before that previous occurrence
                duplicates = solve(prev[n]-1)
            total = (total - duplicates + MOD) % MOD  # + MOD so the value stays non-negative before %

            return total

        # Building prev[] from last_seen[]
        #
        # We scan the string left to right with 1-based positions i = 1..n.
        #
        # last_seen[] is a 26-slot table, one slot per lowercase letter, every slot
        # starting at 0 ("this letter has not appeared yet"). As we walk past each
        # character we keep this table up to date so that at any moment
        # last_seen[c] holds the 1-based position of the LAST time we saw letter c.
        #
        # For the current character at position i:
        #   idx           = which of the 26 slots this letter uses (0 for 'a', 1 for 'b', ...)
        #   prev[i]       = last_seen[idx]   -> read BEFORE we overwrite it, so it is
        #                   the position of the PREVIOUS occurrence of this same letter
        #                   (still 0 if this is the first occurrence).
        #   last_seen[idx] = i               -> now record that this letter's most
        #                   recent position is i, ready for the NEXT time it appears.
        #
        # Order matters: read last_seen[idx] into prev[i] first, then write i into
        # last_seen[idx]. If you overwrote first, prev[i] would wrongly point at i itself.
        #
        # Walkthrough for s = "xaba"  (letters at positions 1,2,3,4):
        #   i=1 'x': idx=23, prev[1]=last_seen[23]=0 ; last_seen[23]=1
        #   i=2 'a': idx=0 , prev[2]=last_seen[0] =0 ; last_seen[0] =2
        #   i=3 'b': idx=1 , prev[3]=last_seen[1] =0 ; last_seen[1] =3
        #   i=4 'a': idx=0 , prev[4]=last_seen[0] =2 ; last_seen[0] =4   <- 'a' last seen at pos 2
        #   => prev = [_, 0, 0, 0, 2]   (index 0 is unused padding)
        #
        # So in solve(4) the check `prev[4] != 0` is true, and solve(prev[4]-1) =
        # solve(1) gives the 2 subsequences that existed just before position 2 -
        # exactly the count of duplicates the second 'a' regenerates.
        #
        # Why 1-based: prev[i] = 0 cleanly means "no previous occurrence" because a
        # real position is always >= 1. With 0-based indexing a position could BE 0,
        # colliding with the sentinel. It also makes prev[i]-1 read naturally as
        # "the number of characters sitting before that previous occurrence".
        for i in range(1, n+1):
            idx = ord(s[i-1]) - ord("a")             # s[i-1]: 1-based i maps to 0-based string index i-1
            prev[i] = last_seen[idx]                  # previous position of this letter (0 if first time)
            last_seen[idx] = i                        # this letter's newest position is now i

        return (solve(n) - 1 + MOD) % MOD             # -1 removes the empty subsequence
            