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

# - Sumarizarea cheltuielilor lunare
#
# - Actualizare suma pentru o cheltuiala
#     * Permite modificarea sumei sau a descrierii unei cheltuieli existente
#
# - Stergere cheltuiala
#     * Permite eliminarea unei inregistrari din baza de date
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