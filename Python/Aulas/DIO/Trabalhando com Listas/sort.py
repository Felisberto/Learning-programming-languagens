linguagens = ["Python", "JavaScript", "Java", "csharp"]
linguagens.sort() # ["C", "csharp", "Java", "JavaScript", "Python"]

linguagens = ["Python", "JavaScript", "C", "Java", "csharp"]
linguagens.sort(reverse=True) # ["Python", "JavaScript", "Java", "csharp", "C"]

linguagens = ["Python", "JavaScript", "C", "Java", "csharp"]
linguagens.sort(key=lambda x: len(x)) # ["C", "Java", "Python", "csharp", "JavaScript"]

linguagens = ["Python", "JavaScript", "C", "Java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) # ["JavaScript", "csharp", "Python", "Java", "C"]
