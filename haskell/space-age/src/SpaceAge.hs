module SpaceAge (Planet (..), ageOn) where

data Planet
  = Mercury
  | Venus
  | Earth
  | Mars
  | Jupiter
  | Saturn
  | Uranus
  | Neptune
  deriving (Show, Eq)

earthOrbitRatio :: Planet -> Float
earthOrbitRatio Mercury = 0.2408467
earthOrbitRatio Venus = 0.61519726
earthOrbitRatio Earth = 1.0
earthOrbitRatio Mars = 1.8808158
earthOrbitRatio Jupiter = 11.862615
earthOrbitRatio Saturn = 29.447498
earthOrbitRatio Uranus = 84.016846
earthOrbitRatio Neptune = 164.79132

ageOn :: Planet -> Float -> Float
ageOn planet seconds = earthOrbits / earthOrbitRatio planet
  where
    earthOrbitInSeconds = 31557600
    earthOrbits = seconds / earthOrbitInSeconds