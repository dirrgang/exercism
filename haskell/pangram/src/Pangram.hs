module Pangram (isPangram) where

import Data.Set (Set)
import qualified Data.Set as Set
import qualified Data.Text as T

normalizeString :: String -> T.Text
normalizeString xs = T.toLower $ T.pack xs

isPangram :: String -> Bool
isPangram text = True
  where
    normalizedText = normalizeString text
    alphabet = Set.fromList ['a' .. 'z']