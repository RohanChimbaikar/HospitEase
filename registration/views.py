from django.shortcuts import render
import mysql.connector as sql

# Create your views here.
def signtxt(request):
    if request.method == "POST":
        try:
            fn = request.POST.get("fname","")
            ln = request.POST.get("lname", "")
            un = request.POST.get("un", "")
            pw = request.POST.get("pw", "")
            pn = request.POST.get("pn", "")
            g1 = request.POST.get("g1", "")
            

            # Connect to the database
            m = sql.connect(host="localhost", user="root", password="123456789", database="hospitease")
            cursor = m.cursor()

            # Insert data into the database using parameterized query
            c = "INSERT INTO registration VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(c, (fn, ln, un, pw, pn, g1))
            m.commit()

        except sql.Error as e:
            # Handle database errors
            print("Database error:", e)

        finally:
            # Close the cursor and database connection
            if cursor:
                cursor.close()
            if m:
                m.close()

    return render(request, "registration.html")
