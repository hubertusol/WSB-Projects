class Elevator:
    limit_udzwigu = 8
    def __init__(self,liczba_pasazerow):
        self.liczba_pasazerow=liczba_pasazerow
        if liczba_pasazerow>8:
            print(f"Limit udźwigu przekroczony! {liczba_pasazerow-8} musi wysiąść!")
        else: print(f"Wsiadło {liczba_pasazerow} pasazerow. Jedziemy do góry")
print("Przypadek 1: Wsiada 10 osob:")
proba1 = Elevator(10)
print("Przypadek 1: Wsiada 6 osob:")
proba1 = Elevator(6)