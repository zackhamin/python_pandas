import pandas as pd

salaries = pd.read_csv("../../archive/Salaries.csv")
print(salaries)

sal = pd.DataFrame(salaries)
print(salaries)

salaries_head = salaries.head()
print(salaries_head)
print("----------------------------------")

entries = salaries.info()
print(entries)

print("------------Average Basepay----------------------")
sal["BasePay"] = pd.to_numeric(sal["BasePay"], errors = "coerce")
print(sal["BasePay"].mean())


print("--------------Overtime pay--------------------")
sal["OvertimePay"] = pd.to_numeric(sal["OvertimePay"], errors="coerce")
print(sal["OvertimePay"].max())