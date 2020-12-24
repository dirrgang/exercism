module Bob (responseFor) where

import qualified Data.Char as C
import Data.Text (Text)
import qualified Data.Text as T

responseFor :: Text -> Text
responseFor xs
  | invalid = T.pack "Fine. Be that way!"
  | yelling && question = T.pack "Calm down, I know what I'm doing!"
  | question = T.pack "Sure."
  | yelling = T.pack "Whoa, chill out!"
  | otherwise = T.pack "Whatever."
  where
    stripped = T.strip xs
    yelling = not (T.any C.isLower stripped) && T.any C.isLetter stripped
    question = T.last stripped == '?'
    invalid = not (T.any (\x -> C.isAlphaNum x || C.isPunctuation x) stripped)