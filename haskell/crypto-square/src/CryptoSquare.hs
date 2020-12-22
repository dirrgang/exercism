module CryptoSquare (encode) where

import qualified Data.Char as C
import qualified Data.Text as T

stringNormalizer :: String -> T.Text
stringNormalizer s = T.filter C.isAlphaNum $ T.toLower $ T.pack s

encode :: String -> String
encode xs = T.unpack $ T.intercalate (T.pack " ") encRect
  where
    normRect = T.chunksOf r $ stringNormalizer xs
    encRect = T.transpose normRect
    len = length xs
    r = floor $ sqrt $ fromIntegral len
