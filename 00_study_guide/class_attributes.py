class Config:
    tags = []             # shared across ALL instances

c1 = Config()
c2 = Config()
c1.tags.append("x")
c2.tags.append("x")

print(f'c1 == c2: {c1 == c2}')
print(f'c1 is c2: {c1 is c2}')
print(f'c1.tags == c2.tags: {c1.tags == c2.tags}')