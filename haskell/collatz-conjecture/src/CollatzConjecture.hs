module CollatzConjecture (collatz) where

collatz :: Integer -> Maybe Integer
collatz n = helper n 0
  where
    helper :: Integer -> Integer -> Maybe Integer
    helper n acc
      | n <= 0 = Nothing
      | n == 1 = Just acc
      | even n = helper (n `div` 2) (acc + 1)
      | otherwise = helper (3 * n + 1) (acc + 1)
