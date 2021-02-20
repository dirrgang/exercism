{-# LANGUAGE TupleSections #-}
module DNA (nucleotideCounts, Nucleotide (..)) where

import Data.Either ( fromRight, isRight )
import qualified Data.Map as M

data Nucleotide = A | C | G | T deriving (Eq, Ord, Show)

trans :: Char -> Either Char Nucleotide
trans 'G' = Right G
trans 'C' = Right C
trans 'T' = Right T
trans 'A' = Right A
trans x = Left x

nucleotideCounts :: String -> Either String (M.Map Nucleotide Int)
nucleotideCounts xs
  -- | isRight nucleotides = Right (M.fromListWith (+) [(x, 1) | x <- fromRight [] nucleotides])
  -- | isRight nucleotides = Right (M.fromListWith (+) (map (, 1) (fromRight [] nucleotides)))
  | all (`elem` "GCTA") xs = Right (M.fromListWith (+) (map (\x -> (translate x, 1)) xs))
  | otherwise = Left []
  where
    translate :: Char -> Nucleotide
    translate x
      | isRight (trans x) = fromRight G $ trans x
      | otherwise = error "done fucked up."
  --   nucleotides = traverse trans xs