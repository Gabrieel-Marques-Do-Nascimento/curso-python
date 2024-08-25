# try:
#     print(20/0)
# except Exception as erro:
#     print(erro.__class__)

# number = 10
# if number > 5:
#     raise Exception(f"The number should not exceed 5. ({number=})")
# print(number)

try:
    print(20/0)
except (NameError , TypeError , ZeroDivisionError) as erro:
    print(erro.__class__)