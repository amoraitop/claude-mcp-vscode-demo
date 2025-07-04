from mcp import ToolServer, tool, Resource

server = ToolServer()

@tool
def echo(text: str) -> str:
    """Επιστρέφει πίσω το κείμενο όπως δόθηκε."""
    return text

@tool
def count_lines(resource: Resource) -> int:
    """Μετράει πόσες γραμμές έχει ένα resource (π.χ. test.txt)."""
    content = resource.read()
    return len(content.splitlines())

# Δηλώνουμε το αρχείο test.txt ως διαθέσιμο resource με όνομα "sample"
server.add_resource(path="test.txt", name="sample")

if __name__ == "__main__":
    server.run_stdio()
