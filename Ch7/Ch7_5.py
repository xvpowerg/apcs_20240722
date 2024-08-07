str1 = "This is his dogs"
print(str1)
search1 = "is"
strCount = str1.count(search1)
print(f"{search1}出現{strCount}幾次")

strCount = str1.count("his")
print(f"his出現{strCount}幾次")

strCount = str1.count("aaa")
print(f"aaa出現{strCount}幾次")
