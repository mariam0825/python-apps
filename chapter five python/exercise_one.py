def missing_code (height):
    return (height, height * 0.0254)

heights = [69, 77, 54]

result = list(map(missing_code, heights))

print(result)

    
