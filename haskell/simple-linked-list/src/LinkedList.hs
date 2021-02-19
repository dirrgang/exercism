module LinkedList
  ( LinkedList,
    datum,
    fromList,
    isNil,
    new,
    next,
    nil,
    reverseLinkedList,
    toList,
  )
where

data LinkedList a = Empty | Cons a (LinkedList a)
  deriving (Eq, Show)

datum :: LinkedList a -> a
datum (Cons x _) = x
datum Empty = error "Cannot retrieve data from empty list."

fromList :: [a] -> LinkedList a
fromList [] = Empty
fromList xs = fromList' (reverse xs) Empty
  where
    fromList' :: [a] -> LinkedList a -> LinkedList a
    fromList' [] ll = ll
    fromList' (x : xs) Empty = fromList' xs (Cons x Empty)
    fromList' (x : xs) ll = fromList' xs (Cons x ll)

isNil :: LinkedList a -> Bool
isNil Empty = True
isNil _ = False

new :: a -> LinkedList a -> LinkedList a
new = Cons

next :: LinkedList a -> LinkedList a
next (Cons _ xs) = xs
next Empty = Empty

nil :: LinkedList a
nil = Empty

reverseLinkedList :: LinkedList a -> LinkedList a
reverseLinkedList ll = reverseLinkedList' ll Empty
  where
    reverseLinkedList' :: LinkedList a -> LinkedList a -> LinkedList a
    reverseLinkedList' Empty acc = acc
    reverseLinkedList' (Cons x xs) acc = reverseLinkedList' xs (Cons x acc)

toList :: LinkedList a -> [a]
toList ll = toList' ll []
  where
    toList' :: LinkedList a -> [a] -> [a]
    toList' Empty xs = reverse xs
    toList' (Cons y ys) xs = toList' ys (y : xs)
