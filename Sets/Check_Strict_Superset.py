# Problem: Check Strict Superset
# Platform: HackerRank

A = set(map(int, input().split()))
n = int(input())

result = True

for _ in range(n):
    m = set(map(int, input().split()))
    if not A > m:  
        result = False
        break

print(result)

# -------------------------
# Alternatives (for learning)
# -------------------------

# Method 3: issuperset + length check
# for _ in range(n):
#     m = set(map(int, input().split()))
#     if not A.issuperset(m) or len(A) <= len(m):
#         result = False
#         break

# Method 1: manual element checking
# for _ in range(n):
#     m = set(map(int, input().split()))
#     for x in m:
#         if x not in A:
#             result = False
#             break
#     if len(A) <= len(m):
#         result = False
#     if not result:
#         break
