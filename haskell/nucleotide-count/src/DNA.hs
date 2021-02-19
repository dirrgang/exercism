module DNA (nucleotideCounts, Nucleotide (..)) where

import qualified Data.Map as M
import Data.Maybe

data Nucleotide = A | C | G | T deriving (Eq, Ord, Show)

trans :: Char -> Maybe Nucleotide
trans 'G' = Just G
trans 'C' = Just C
trans 'T' = Just T
trans 'A' = Just A
trans _ = Nothing

nucleotideCounts :: String -> Either String (M.Map Nucleotide Int)
nucleotideCounts xs
  | all (`elem` "ACGT") xs && isJust nucleotides = Right (nucleotideCounts' (fromJust nucleotides) (M.fromList [(A, 0), (C, 0), (G, 0), (T, 0)]))
  | otherwise = Left []
  where
    nucleotides = traverse trans xs
    nucleotideCounts' :: [Nucleotide] -> M.Map Nucleotide Int -> M.Map Nucleotide Int
    nucleotideCounts' [] acc = acc
    nucleotideCounts' (x : xs) acc = nucleotideCounts' xs (M.adjust (1 +) x acc)