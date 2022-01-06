from __future__ import annotations
from typing import List
from dataclasses import dataclass


@dataclass
class Student:

    name:str
    fives:int
    tens:int
    twenties:int
    
    def __post_init__(self) -> None:
        self.name = self.name.strip()
        if self.fives < 0 or self.tens < 0 or self.twenties < 0:
            raise ValueError("Bills cannot be negative!")
        
    def wealth(self) -> int:
        return self.tens*10 + self.twenties*20 + self.fives*5
    
    def compare(self,student:Student) -> str:
        try:
            return self.name if self.wealth()>=student.wealth() else student.name
        except AttributeError:
            raise AttributeError()
    
    def advanced_compare(self,students:List[Student]) -> List[str]:
        try:
            students.extend([self])
            return [student.name for student in sorted(
                students,reverse = True , key = lambda x:x.wealth())]
        except AttributeError:
            raise AttributeError()

    @staticmethod
    def sadvanced_compare(students:List[Student]) -> List[str]:
        pass


def main():
    one = Student('Amy', 5, 6, 7)
    two = Student('Bilbo', 3, 4, 5)
    three = Student('Chuck', 2, 3, 4)
    four = Student('Diane', 1, 2, 3)
    print(one.advanced_compare([two,three,four]))

if __name__ == "__main__": main()