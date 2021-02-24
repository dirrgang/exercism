module ListOps
  ( length,
    reverse,
    map,
    filter,
    foldr,
    foldl',
    (++),
    concat,
  )
where

import Prelude hiding
  ( concat,
    filter,
    foldr,
    length,
    map,
    reverse,
    (++),
  )

foldl' :: (b -> a -> b) -> b -> [a] -> b
foldl' _ acc [] = acc
foldl' f acc (x : xs) = acc' `seq` foldl' f acc' xs
  where
    acc' = f acc x

foldr :: (a -> b -> b) -> b -> [a] -> b
foldr _ acc [] = acc
foldr f acc (x : xs) = f x (foldr f acc xs)

length :: [a] -> Int
length xs = sum [1 | _ <- xs]

reverse :: [a] -> [a]
reverse [] = []
reverse (x : xs) = reverse xs ++ [x]

map :: (a -> b) -> [a] -> [b]
map _ [] = []
map f (x : xs) = f x : map f xs

filter :: (a -> Bool) -> [a] -> [a]
filter p xs = [x | x <- xs, p x]

(++) :: [a] -> [a] -> [a]
xs ++ [] = xs
[] ++ ys = ys
(x : xs) ++ ys = x : xs ++ ys

concat :: [[a]] -> [a]
concat = foldl' (++) []
