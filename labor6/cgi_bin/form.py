import cgi
import html

form = cgi.FieldStorage()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Gym</title>
        </head>
        <body>""")

print("<h1>Hello world</h1>")


print("""</body>
        </html>""")