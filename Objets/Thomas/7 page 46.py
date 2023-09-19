class Point:

    def __init__(self, pos : tuple) -> None:
        
        self.x, self.y = pos

    def __str__(self) -> str:
        
        return f"({self.x};{self.y})"
    
print(Point((50,50)))