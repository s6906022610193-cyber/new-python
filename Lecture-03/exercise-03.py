hour_work = int(input("Enter the number of hours worked: "))
houlry_rate = int(input("Enter the hourly pay rate: "))
if hour_work <= 40:
    total_pay =  hour_work * houlry_rate
else:
    overtime_hours = hour_work - 40
    total_pay = (40 * houlry_rate) + (overtime_hours * houlry_rate * 1.5)

print("Total pay: $", total_pay)

    