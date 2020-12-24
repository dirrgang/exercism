module Prime (nth) where

import Data.List (\\)

sieveOfEratosthenes :: Int -> [Int]
sieveOfEratosthenes n = sieve [2 .. n] 
  where
      sieve (x : xs) = x : sieve (xs \\ [x , x + x .. n])
      sieve [] = []
  

-- nth :: Int -> Maybe Integer
nth :: Int -> [Int]
nth n = result where
