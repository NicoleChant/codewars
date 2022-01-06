from __future__ import annotations
from dataclasses import dataclass
from typing import Tuple
from math import ceil

@dataclass
class Potion:
    
    """Hogwarts Potion
      ---------------------------
               Arguments
      ---------------------------
      color: List of 3 integers
      volume: integer
      ---------------------------
               Methods
      ---------------------------
      mix
      """
    
    color:Tuple[int]
    volume:int

    def _blend(self,c1:int,c2:int,v2:int) -> int:
        return ceil((c1*self.volume+c2*v2)/(self.volume+v2))

    
    def mix(self, other:Potion) -> Potion:
        """General description
        --------------------------
        Takes another potion as arguments and mixes it. 
        The resulting magic potion has a new color and larger volume.
        --------------------------------------------------------------
        Arguments: Accepts another object Potion class as an argument.
        ---------------------------------------------------------------
        Color calculation: Weight Average of RGB tuple values with volumes
        as the weights.
        ------------------------------------------------------------------
        Returns: A new Potion class object with blended color and added volumes.
        """

        mixed_color = tuple([self._blend(c,w,other.volume) for (c,w) in zip(self.color,other.color)])
        return Potion( mixed_color , self.volume + other.volume)


def main():
    potion1 = Potion((153,210,199),32)
    potion2 = Potion((135,34,0),17)
    mixed = potion1.mix(potion2)
    assert mixed.color == (147,149,130)



if __name__ == "__main__": main()