
#find out how many people are in each department
#Python script that reads a CSV file containing a list of the employees
#The output of this script will be a plain text file.

# names = ['John', 'Alice', 'Bob', 'Mary', 'David', 'Emily']
# departments = ['Sales', 'Marketing', 'Engineering', 'Human Resources', 'Finance']
# job_titles = ['Manager', 'Engineer', 'Accountant', 'Analyst', 'Coordinator']

#!/usr/bin/env python3
import csv
def read_employees(csv_file_location):
  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
  employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
  employee_list = []
  for data in employee_file:
    employee_list.append(data)
  return employee_list
  return employee_list
employee_list = read_employees('/home/touk/Desktop/employees.csv')

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['department'])
    department_data = {}
    for department_name in set(department_list):
      department_data[department_name] = department_list.count(department_name)
    return department_data
dictionary = process_data(employee_list)

def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
      for k in sorted(dictionary):
        f.write(str(k)+':'+str(dictionary[k])+'\n')
      f.close()
write_report(dictionary, '/home/touk/Desktop/report.txt')

