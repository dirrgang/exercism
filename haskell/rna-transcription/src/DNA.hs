module DNA (toRNA) where

toRNA :: String -> Either Char String
toRNA = traverse trans
  where
    trans :: Char -> Either Char Char
    trans  'G' = Right 'C'
    trans  'C' = Right 'G'
    trans  'T' = Right 'A'
    trans  'A' = Right 'U'
    trans x = Left x