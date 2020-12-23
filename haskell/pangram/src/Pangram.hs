module Pangram (isPangram) where

import qualified Data.Char as C
import qualified Data.Set as Set

isPangram :: String -> Bool
isPangram text = alphabet `Set.isSubsetOf` normalizedText
  where
    normalizedText = Set.fromList $ map C.toLower text
    alphabet = Set.fromList ['a' .. 'z']