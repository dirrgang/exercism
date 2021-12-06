open Base

type bst = Empty | Node of int * bst * bst

let empty = Empty

let value = function
| Empty -> (0, Int.to_string 0)
| Node (i, _, _) -> (i, Int.to_string i)

let left = function 
  | Empty -> Empty
  | Node (_, l, _) -> l

let right = function
  | Empty -> Empty
  | Node (_, _, r) -> r

let rec insert x = function
  | Empty -> Node (x, Empty, Empty)
  | Node (i, l, r) -> if x < i then insert x l else insert x r

let rec to_list = function
| Empty -> []
| Node (i, l, r) -> to_list l @ (i :: to_list r)
