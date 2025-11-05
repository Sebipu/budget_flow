# Aplicatie pentru gestiunea bugetului personal
# ==========================================================
# Scop:
# Aceasta aplicatie permite utilizatorului sa isi inregistreze si sa isi urmareasca cheltuielile zilnice.
# Fiecare utilizator are propriul cont si isi poate adauga, vizualiza, modifica sau sterge cheltuielile.
#
# Functionalitati:
# - Autentificare utilizator
#     * Login cu username si parola stocata in baza de date
#     * Accesul la aplicatie este permis doar dupa autentificare
#
# - Adaugare cheltuiala
#     * Utilizatorul introduce categoria, suma si o descriere (ex: "Mancare", 50.00, "Pranz la restaurant")
#
# - Vizualizare cheltuieli
#     * Se afiseaza toate cheltuielile utilizatorului curent
#     * Poate include si filtrare dupa categorie sau suma
#
# - Actualizare suma pentru o cheltuiala
#     * Permite modificarea sumei sau a descrierii unei cheltuieli existente
#
# - Stergere cheltuiala
#     * Permite eliminarea unei inregistrari din baza de date
#
# - Sumarizarea cheltuielilor lunare
#
# - Deconectare utilizator
#     * Revine la ecranul principal de autentificare
#
# Exemple de utilizare:
# 1. Userul "ana" se logheaza
# 2. Adauga o cheltuiala la "Transport" de 120 RON
# 3. Vizualizeaza cheltuielile lunii curente
# 4. Modifica suma pentru transport
# 5. Se deconecteaza
#
# Tabele:
# users(id, username, password)
# expenses(id, user_id, category, amount, description)
#
# Tehnologii:
# Python + pymysql
# bcrypt (optional pentru criptarea parolelor)

#Conectare la baza de date
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='budget_flow'
    )

#Functie autentificare
def auth():
    conn = connect_db()
    cursor = conn.cursor()

    while True:
        username = input("Introduceti numele de utilizator: ")
        password = input("Introduceti parola: ")

        query = "SELECT * FROM users WHERE username = %s AND password = %s;"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
            print("Bine ati venit!")
            return True
        else:
            print("Autentificare esuata")
            return False



#Functie adaugare cheltuiala
def expense():
    conn = connect_db()
    cursor = conn.cursor()

    user_id = int(input("Introduceti id utilizator pentru care doriti sa adaugati cheltuliala: "))
    category = input("Introduceti categoria cheltuielilor: ")
    amount = int(input("Introduceti valoarea cheltuielilor: "))
    description = input("Introduceti descrierea cheltuielilor: ")
    month = int(input("Introduceti luna in care ati facut cheltuiala: "))
    year = int(input("Introduceti anul in care ati facut cheltuiala: "))


    query = 'INSERT INTO expenses (user_id, category, amount, description, month, year) VALUES (%s, %s, %s, %s, %s, %s)'
    cursor.execute(query, (user_id, category, amount, description, month, year))

    conn.commit()

    print(f"Cheltuiala: {category} a fost adaugata in data de: {month}.{year} pentru userul cu ID: {user_id}")
    cursor.close()
    conn.close()

#Functie vizualizare cheltuieli
def view():
    conn = connect_db()
    cursor = conn.cursor()

    query = 'SELECT * FROM expenses'
    cursor.execute(query)

    expenses = cursor.fetchall()
    if expenses:
        for c in expenses:
            print (f"ID: {c[0]} | Categorie: {c[1]} | Valoare: {c[2]} | Descriere: {c[3]} | Luna: {c[4]}| Anul{c[5]} | ID Utilizator: {c[6]}")
    else:
        print("Nu exista cheltuieli")

#Functie editare cheltuiala
def edit():
    conn = connect_db()
    cursor = conn.cursor()

    id_cheltuiala = int(input("Introduceti ID cheltuieli: "))
    noua_valoare = float(input("Introduceti noua valoare: "))

    query = 'UPDATE expenses SET amount = %s WHERE id = %s'
    cursor.execute(query, (noua_valoare, id_cheltuiala))
    conn.commit()

    if cursor.rowcount > 0:
        print("Cheltuliala actualizata")
    else:
        print("Actualizare nereusita")

    cursor.close()
    conn.close()

#Functie stergere cheltuiala:
def delete():
    conn = connect_db()
    cursor = conn.cursor()

    id_cheltuia = int(input("Introduceti ID cheltuieli pe care doriti sa o stergeti: "))

    query = 'DELETE FROM expenses WHERE id = %s'
    cursor.execute(query, (id_cheltuia,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Cheltuiala a fost stearsa")
    else:
        print("Produsul nu exista")

    cursor.close()
    conn.close()

#Functie vizualizare cheltuieli totale
def monthly_expenses():
    conn = connect_db()
    cursor = conn.cursor()

    query = 'SELECT amount,month,year FROM expenses'
    cursor.execute(query)

    expenses = cursor.fetchall()

    if expenses:
        totals = {}
        for expense in expenses:
            key = f"{expense[1]}.{expense[2]}"
            totals[key] = totals.get(key, 0) + float(expense[0])
        for key,value in totals.items():
            print(f"In luna: {key} avem cheltuieli in valoare de: {value} RON")
    else:
        print("Nu exista cheltuieli")

meniu = """
|BudgetFlow| meniu principal

1. Adauga cheltuiala
2. Vizualizare cheltuieli
3. Editeaza o cheltuiala
4. sterge o cheltuiala
5. Vizualizeaza cheltuieli lunare 
6. Delogare
"""

def main():
    print(15*'=','Autentificare',15*'=')

    if auth():
        while True:
            print(meniu)
            option = input("Selectati optiunea ")

            if option == "1":
                expense()
            elif option == "2":
                view()
            elif option == "3":
                edit()
            elif option == "4":
                delete()
            elif option == "5":
                monthly_expenses()
            elif option == "6":
                print("La Revedere")
                break
            else:
                print("Alageti o optiune valida (1-6)")

main()


