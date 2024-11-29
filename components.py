def listComponents(container, depth=0):
    for component in container.getComponents():
        print("{}Name: {}, Type: {}".format("  " * depth, component.name, type(component)))
        if hasattr(component, 'getComponents'):  # Check if the component is a container
            listComponents(component, depth + 1)

# Start with the current container
listComponents(event.source.parent)