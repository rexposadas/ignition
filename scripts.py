# These are the scripts used for the examples.

# List components
def listComponents(container, depth=0):
    for component in container.getComponents():
        print("{}Name: {}, Type: {}".format("  " * depth, component.name, type(component)))
        if hasattr(component, 'getComponents'):  # Check if the component is a container
            listComponents(component, depth + 1)

# Start with the current container
listComponents(event.source.parent)


# Fetch and log alerts
query = "SELECT * FROM alarm_events ORDER BY id DESC LIMIT 10;"
results = system.db.runQuery(query, "Sample_SQLite_Database")
output = "\n".join([", ".join(map(str, row)) for row in results])
print(output)


# Display message in a popup

system.gui.messageBox("This is a python script triggered by an onclick event")

