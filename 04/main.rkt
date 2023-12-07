#lang racket

(define (score_matches line)
  (let* ([decks (string-split (second (string-split line ":")) " | ")]
         [winning (list->set (filter number? (map string->number (string-split (first decks) " "))))]
         [mine (list->set (filter number? (map string->number (string-split (second decks) " "))))]
         [matches (length (set->list (set-intersect winning mine)))])
    (cond
      [(eq? matches 0) 0]
      [else (expt 2 (- matches 1))])))

(printf "part 1 example: ~a\n" (apply + (map score_matches (file->lines "example.txt"))))
(printf "part 1: ~a\n" (apply + (map score_matches (file->lines "input.txt"))))
