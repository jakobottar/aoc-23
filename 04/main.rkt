#lang racket

(define (get-num-matches decks)
  (let* ([winning (list->set (filter number? (map string->number (string-split (first decks) " "))))]
         [mine (list->set (filter number? (map string->number (string-split (second decks) " "))))]
         [matches (length (set->list (set-intersect winning mine)))])
    matches))

(define (score_matches line)
  (let* ([decks (string-split (second (string-split line ":")) " | ")]
         [matches (get-num-matches decks)])
    (cond
      [(eq? matches 0) 0]
      [else (expt 2 (- matches 1))])))

(printf "part 1 example: ~a\n" (apply + (map score_matches (file->lines "example.txt"))))
(printf "part 1: ~a\n" (apply + (map score_matches (file->lines "input.txt"))))

(define (part-2 filename)
  (define (helper lines acc)
    (cond
      [(empty? lines) acc]
      [else
       (let* ([line (first lines)]
              [decks (string-split (second (string-split line ":")) " | ")]
              [matches (get-num-matches decks)])
         (cond
           [(eq? matches 0) (helper (rest lines) acc)]
           [else (let* ([lines (rest lines)]
                        [won (take lines matches)])
                   (+ (helper lines acc) 1))]))]))

  (helper (file->lines filename) 0))

(printf "part 2 example: ~a\n" (part-2 "example.txt"))
(printf "part 2: ~a\n" (part-2 "input.txt"))
