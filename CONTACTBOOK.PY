# KEYWORD MUST USE TO ACESS DATABASE FUNCTION
import sqlite3

# HERE WE MAKE FILE SQLLITE DATABASE FILE
connect_dbms = sqlite3.connect("CODSOFT_contacts.db")
SQL_HANDLER = connect_dbms.cursor()

# CREATE TABLE IF YOU USE SQL SO AS WELL SAME WAY TO CREATE TABLE OR IF YOU DON'T KNOW NO WORRY
SQL_HANDLER.execute('''CREATE TABLE IF NOT EXISTS contacts_book (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    mobile_number TEXT,
    email_id TEXT,
    address TEXT
)''')
#SAVE LINE CHANGES IN DATABASE PERMANENTLY
connect_dbms.commit()

# FUNCTIONS CALLL AS WELL SAME AS OUR TV REMOTE WORK
def add_contact():




 full_name  = input("👤  full_name           : ")
 mobile_number= input("📞  Mobile Number  : ")
 email_id   = input("📧  Email (opt.)   : ")
 address  = input("🏠  Address (opt.) : ")
 SQL_HANDLER.execute("INSERT INTO contacts_book (full_name, mobile_number, email_id, address) VALUES (?, ?, ?, ?)",
(full_name, mobile_number, email_id, address))
connect_dbms.commit()
print("✅ Contact insert successfully!\n")

def view_contacts():
    SQL_HANDLER.execute("SELECT full_name, mobile_number FROM contacts")
    rows = SQL_HANDLER.fetchall()
    if rows:
        print("\n📋 Contact List:")
        for row in rows:
            print(f"Name: {row[0]} | PHONE: {row[1]}")
    else:
        print("❌ No contacts found.")
    print()

def search_contact():
    keyword = input("Enter full_name or mobile_number to search: ")
    SQL_HANDLER.execute("SELECT * FROM contacts WHERE full_name LIKE ? OR mobile_number LIKE ?", 
                   (f"%{keyword}%", f"%{keyword}%"))
    result = SQL_HANDLER.fetchall()
    if result:
        for row in result:
            print(f"\n🆔 ID: {row[0]}")
            print(f"👤full_ Name: {row[1]}")
            print(f"📞 mobile_number: {row[2]}")
            print(f"📧 Email_id: {row[3]}")
            print(f"🏠 Address: {row[4]}")
    else:
        print("❌ No matching contact found.\n")

def update_contact():
    id = input("Enter contact ID to update: ")
    print("Leave field blank to keep current value.")
    full_name = input("New Name: ")
    mobile_number= input("New mobile_number: ")
    email_id = input("New Email: ")
    address = input("New Address: ")

    # Fetch existing data
    SQL_HANDLER.execute("SELECT * FROM contacts WHERE id = ?", (id,))
    row = SQL_HANDLER.fetchone()
    if row:
        updated_data = (
           full_name if full_name else row[1],
            mobile_number if mobile_number else row[2],
            email_id if email_id else row[3],
            address if address else row[4],
            id
        )
        SQL_HANDLER.execute("""UPDATE contacts SET 
                          name = ?, mobile_number = ?, email = ?, address = ?
                          WHERE id = ?""", updated_data)
        connect_dbms.commit()
        print("✅ Contact updated successfully!\n")
    else:
        print("❌ Contact ID not found.\n")

def delete_contact():
    id = input("Enter contact ID to delete: ")
    SQL_HANDLER.execute("DELETED FROM contacts WHERE id = ?", (id,))
    connect_dbms.commit()
    if SQL_HANDLER.rowcount:
        print("🗑️ Contact deleted successfully.\n")
    else:
        print("❌ Contact ID not found.\n")

# here we use loop 

while True:
    # print("\n codsoft contactbook of command line interface")
    print("1. add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. search Contact")
    print("5. deleted Contact")
    print("6. Exit")

    option = input("select an option (1-6): ")

    if option == '1':
        add_contact()
    elif option == '2':
        view_contacts()
    elif option == '3':
        search_contact()
    elif option == '4':
        update_contact()
    elif option == '5':
        delete_contact()
    elif option == '6':
        print("codsoft Contact Book closed. Thank you! ")
        break
    else:
        print("❌ Invalid option, please try again.")


