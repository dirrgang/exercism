module BST
  ( BST,
    bstLeft,
    bstRight,
    bstValue,
    empty,
    fromList,
    insert,
    singleton,
    toList,
  )
where

data BST a = Leaf a (BST a) (BST a) | EmptyTree deriving (Eq, Show)

bstLeft :: BST a -> Maybe (BST a)
bstLeft EmptyTree = Nothing
bstLeft (Leaf _ left _) = Just left

bstRight :: BST a -> Maybe (BST a)
bstRight EmptyTree = Nothing
bstRight (Leaf _ _ right) = Just right

bstValue :: BST a -> Maybe a
bstValue EmptyTree = Nothing
bstValue (Leaf x _ _) = Just x

empty :: BST a
empty = EmptyTree

fromList :: Ord a => [a] -> BST a
fromList = foldl (flip insert) empty

insert :: Ord a => a -> BST a -> BST a
insert x EmptyTree = singleton x
insert x (Leaf val left right)
  | x <= val = Leaf val (insert x left) right
  | x > val = Leaf val left (insert x right)
  | otherwise = EmptyTree

singleton :: a -> BST a
singleton x = Leaf x EmptyTree EmptyTree

toList :: BST a -> [a]
toList EmptyTree = []
toList (Leaf val left right) = toList left ++ (val : toList right)