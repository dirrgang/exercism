module Robot
  ( Bearing (East, North, South, West),
    bearing,
    coordinates,
    mkRobot,
    move,
  )
where

data Bearing
  = North
  | East
  | South
  | West
  deriving (Eq, Show, Enum)

data Robot = Robot
  { b :: Bearing,
    x :: Integer,
    y :: Integer
  }
  deriving (Show, Eq)

bearing :: Robot -> Bearing
bearing = b

coordinates :: Robot -> (Integer, Integer)
coordinates r = (x r, y r)

mkRobot :: Bearing -> (Integer, Integer) -> Robot
mkRobot direction (x, y) = Robot direction x y

move :: Robot -> String -> Robot
move r [] = r
move r ('A' : xs) = move (move' r) xs
  where
    move' :: Robot -> Robot
    move' r
      | b r == North = r {y = y r + 1}
      | b r == East = r {x = x r + 1}
      | b r == South = r {y = y r - 1}
      | b r == West = r {x = x r - 1}
      | otherwise = r
move r (x : xs) = move (turn r x) xs
  where
    turn :: Robot -> Char -> Robot
    turn (Robot West x y) 'R' = Robot North x y
    turn (Robot North x y) 'L' = Robot West x y
    turn r 'L' = r {b = pred (b r)}
    turn r 'R' = r {b = succ (b r)}
    turn r _ = r