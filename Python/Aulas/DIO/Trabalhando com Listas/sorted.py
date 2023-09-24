linguagens = ["Python", "JavaScript", "C", "Java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x))) # ['C', 'Java', 'Python', 'csharp', 'JavaScript']


print(sorted(linguagens, key=lambda x: len(x), reverse=True)) # ['JavaScript', 'Python', 'csharp', 'Java', 'C']
