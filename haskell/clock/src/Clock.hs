module Clock (addDelta, fromHourMin, toString) where

import Text.Printf

data Clock = Clock Int Int
  deriving (Eq)

fromHourMin :: Int -> Int -> Clock
fromHourMin hour min = Clock ((hour + min `div` 60) `mod` 24) (min `mod` 60)

toString :: Clock -> String
toString (Clock hour minutes) = printf "%02d:%02d" hour minutes

addDelta :: Int -> Int -> Clock -> Clock
addDelta hour min (Clock oHour oMin) = Clock newHour newMin
  where
    newHour = (hour + oHour + ((min + oMin) `div` 60)) `mod` 24
    newMin = (min + oMin) `mod` 60
