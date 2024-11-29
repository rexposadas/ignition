
query = "SELECT * FROM alarm_events ORDER BY id DESC LIMIT 10;"

# Use the sample SQLite DB
results = system.db.runQuery(query, "Sample_SQLite_Database")

output = "\n".join([", ".join(map(str, row)) for row in results])

print(output)