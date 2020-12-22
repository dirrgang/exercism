module CryptoSquare (encode) where

import qualified Data.Text as T

stringNormalizer :: String -> String
stringNormalizer s = T.unpack $ T.filter (/= ' ') $ T.toLower $ T.pack s

encode :: String -> String
encode xs = undefined 
