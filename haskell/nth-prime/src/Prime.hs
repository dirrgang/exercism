module Prime (nth) where

primeTest :: Int -> Bool
primeTest 1 = False
primeTest 2 = True
primeTest n = not $ or [n `mod` x == 0 | x <- [2 .. n - 1]]

nth :: Int -> Maybe Integer
nth 0 = Nothing
nth n = Just (toInteger (nth' 2 0))
  where
    nth' :: Int -> Int -> Int
    nth' x acc
      | n == (acc + 1) && isPrime = x
      | isPrime = nth' (x + 1) (acc + 1)
      | otherwise = nth' (x + 1) acc
      where
        isPrime = primeTest x