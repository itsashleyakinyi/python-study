# Write a program that takes input of someone's basic salary and benefits, adds them to fin
# d the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:  
# Write a normal program but use functions if you feel comfortable.

def calc_gross_salary(basic_salary,benefits):
    gross_salary=basic_salary + benefits
    return gross_salary
basic_salary=float(input("Enter basic salary: "))
benefits=float(input("Enter benefits: "))
total_salary=calc_gross_salary(basic_salary,benefits)
print(f"Total salary is ksh: {total_salary:.2f}")


# function to calculate NHIF
# // 5,999	150
# // 6,000 - 7,999	300
# // 8,000 - 11,999	400
# // 12,000 - 14,999	500
# // 15,000 - 19,999	600
# // 20,000 - 24,999	750
# // 25,000 - 29,999	850
# // 30,000 - 34,999	900
# // 35,000 - 39,999	950
# // 40,000 - 44,999	1,000
# // 45,000 - 49,999	1,100
# // 50,000 - 59,999	1,200
# // 60,000 - 69,999	1,300
# // 70,000 - 79,999	1,400
# // 80,000 - 89,999	1,500
# // 90,000 - 99,999	1,600
# // 100,000 and above	1,700

def calc_NHIF(k):
  if k > 0 and k <= 5999:
    nhif = 150
  elif k >= 6000 and k <= 7999:
    nhif = 300
  elif k >= 8000 and  k <= 11999:
    nhif = 400
  elif k >= 12000 and  k <= 14999:
    nhif = 500
  elif k >= 15000 and  k <= 19999: 
    nhif = 600
  elif k >= 20000 and k <= 24999:
    nhif = 750
  elif k >= 25000 and k <= 29999:
    nhif = 850
  elif k >= 30000 and k <= 34999:
    nhif = 900
  elif k >= 35000 and k <= 39999:
    nhif = 950
  elif k >= 40000 and k <= 44999:
    nhif = 1000
  elif k >= 50000 and k <= 59999:
    nhif = 1200
  elif k >= 60000 and k <= 69999:
    nhif = 1300
  elif k >= 70000 and k <= 79999:
    nhif = 1400
  elif k >= 80000 and k <= 89999:
    nhif = 1500
  elif k >= 90000 and k <= 99999:
    nhif = 1600
  else:
    nhif = 1700
  
  return nhif
total_nhif=calc_NHIF(total_salary)
print(f"NHIF is ksh: {total_nhif:.2f}")












# TASK 16: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF. 

# Write a normal program but use functions if you feel comfortable.
def calc_NSSF(k):
    if k<18000:
        nssf=0.06 * k
    else:
        nssf=0.06 * 18000
    return nssf
total_nssf=calc_NSSF(total_salary) 
print(f"NSSF is ksh: {total_nssf:.2f}")       








# Task 17: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015

# Write a normal program but use functions if you feel comfortable.

def calc_NHDF(k):
    nhdf=k * 0.015
    return nhdf
total_nhdf=calc_NHDF(total_salary)
print(f"NHDF is ksh: {total_nhdf:.2f}")










# Task 18: Using Python or PHP or Java or Ruby or JavaScript
# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF + NHIF) 

# Write a normal program but use functions if you feel comfortable.
def calc_taxable_income(a,b,c,d):
    taxable_income=a-(b+c+d)
    return taxable_income
taxable_income=calc_taxable_income(total_salary,total_nssf,total_nhdf,total_nhif)
print(f"taxable_income is ksh: {taxable_income:.2f}")    








# TASK 19: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and find the persons PAYEE using the taxable income above.
# Find the Kenya PAYEE Tax Rate using THIS LINK
# Write a normal program but use functions if you feel comfortable.



# 0 – 24,000	10%
# On the next 8,333	25%
# On the next 467,667	30%
# On the next 300,000	32.5%
# On amounts over 800,000	35%
# Personal Relief: KES 2,400.00 per month
# Minimum Taxable Income: KES 24,001.00 per month


def calc_PAYEE(t_income,relief=2400.00):
    if t_income<24000:
      payee=0
    elif t_income>24000 and t_income<=32333:
      payee=(24000 * 0.1 + (t_income-24000)*0.25)-relief
    elif t_income>32333 and t_income<=500000:
      payee=(24000 * 0.1  + 8333 * 0.25 +(t_income-32333) * 0.3)-relief
    elif t_income>500000 and t_income<=800000:
      payee=(24000 * 0.1 + 8333 * 0.25 + 467667 * 0.3 +(t_income-500000)*0.325)-relief
    else:
      payee=(24000 * 0.1 + 8333 * 0.25 + 467667 * 0.3 + 300000 * 0.325 +(t_income-800000)*0.35)-relief
    return payee
total_payee=calc_PAYEE(taxable_income)
print(f"Total payee is ksh: {total_payee:.2f}")     
           


# Task 20: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nhdf +  nssf + payee)

# Write a normal program but use functions if you feel comfortable.

def calc_net_salary(a,b,c,d,e):
  net_salary=a-(b+c+d+e)
  return net_salary

total_net_salary=calc_net_salary(total_salary,total_nhif,total_nhdf,total_nssf,total_payee)
print(f"Total net salary is ksh: {total_net_salary:.2f}")