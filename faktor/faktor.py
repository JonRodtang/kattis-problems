import math
papers, impact_factor = map(int, input().split())
generated_impact = 0
citations = 0

while impact_factor > generated_impact:
    citations += 1
    generated_impact = math.ceil(citations/papers)


print(citations)


