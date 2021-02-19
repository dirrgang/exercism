module Anagram (anagramsFor) where

import qualified Data.MultiSet as MultiSet
import qualified Data.Text as T

normalizeString :: String -> String
normalizeString xs = T.unpack $ T.toLower $ T.pack xs

anagramsFor :: String -> [String] -> [String]
anagramsFor xs yss =
  [ ys | ys <- yss, MultiSet.fromList (normalizeString ys) == MultiSet.fromList (normalizeString xs), normalizeString xs /= normalizeString ys
  ]
