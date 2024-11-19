import xml.dom.minidom

doc = xml.dom.minidom.parse("bt3.xml")

company_name = doc.getElementsByTagName("name")[0].firstChild.data
print(f"Company Name: {company_name}")

staffs = doc.getElementsByTagName("staff")

for staff in staffs:
    staff_id = staff.getAttribute("id")
    name = staff.getElementsByTagName("name")[0].firstChild.data
    salary = staff.getElementsByTagName("salary")[0].firstChild.data
    print(f"Staff ID: {staff_id}, Name: {name}, Salary: {salary}")
