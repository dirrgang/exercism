module CollatzConjecture (collatz) where

collatz :: Integer -> Maybe Integer
collatz n
  | n <= 0 = Nothing
  | otherwise = Just $ collatz' n 0
  where
    collatz' :: Integer -> Integer -> Integer
    collatz' 1 acc = acc
    collatz' n acc
      | even n = collatz' (n `div` 2) (acc + 1)
      | otherwise = collatz' (3 * n + 1) (acc + 1)
