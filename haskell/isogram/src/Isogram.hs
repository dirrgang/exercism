module Isogram (isIsogram) where

import qualified Data.Char as C
import qualified Data.Set as Set

isIsogram :: String -> Bool
isIsogram xs = length noHyphen == length normalizedText
  where
    noHyphen = filter (`notElem` "- ") xs
    normalizedText = (Set.fromList . map C.toLower) noHyphen