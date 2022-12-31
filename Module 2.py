import ast
# Parse a string containing a Python expression into an AST
node = ast.parse("2 + 3 * 4")
# Print the AST in a readable format
print(ast.dump(node))
left = node.body[0].value.left
right = node.body[0].value.right
print(left, right)  # Outputs: (2, 3)
