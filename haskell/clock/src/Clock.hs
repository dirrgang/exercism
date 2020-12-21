module Clock (addDelta, fromHourMin, toString) where

import Text.Printf

newtype Clock = Clock Int
  deriving (Eq, Show)

fromHourMin :: Int -> Int -> Clock
fromHourMin hour min = Clock ((min + hour * 60) `mod` 1440)

toString :: Clock -> String
toString (Clock time) = printf "%02d:%02d" hour minute
  where
    hour = time `div` 60
    minute = time `mod` 60

addDelta :: Int -> Int -> Clock -> Clock
addDelta hour min (Clock time) = Clock ((time + min + hour * 60) `mod` 1440)