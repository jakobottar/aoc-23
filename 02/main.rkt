#lang racket

;; part 1
;; only false if individual draw is greater than the bag total
(define bag '(12 13 14))

(define (count-valid-game line)
  (let ([id (string->number (second (string-split (first (string-split line ":")) " ")))])
    (define (helper cubes)
        (cond [(empty? cubes) id]
              [(and (equal? (second (string-split (first cubes) " ")) "red") (> (string->number (first (string-split (first cubes) " "))) (first bag))) 0]
              [(and (equal? (second (string-split (first cubes) " ")) "green") (> (string->number (first (string-split (first cubes) " "))) (second bag))) 0]
              [(and (equal? (second (string-split (first cubes) " ")) "blue") (> (string->number (first (string-split (first cubes) " "))) (third bag))) 0]
              [else (helper (rest cubes))]))
    
    (helper (string-split (string-replace (second (string-split line ":")) ";" ",") ","))))

(printf "part 1 example: ~a\n" (apply + (map count-valid-game (file->lines "example.txt"))))
(printf "part 1: ~a\n" (apply + (map count-valid-game (file->lines "input.txt"))))

;; part 2
(define (power-of-cubes line)
  (define (helper draws maxes)
    (if (empty? draws)
        (apply * maxes)
        (let ([col (second (string-split (first draws) " "))]
              [num (string->number (first (string-split (first draws) " ")))])
          (cond
            [(equal? col "red") (helper (rest draws) (list-set maxes 0 (max num (first maxes))))]
            [(equal? col "green") (helper (rest draws) (list-set maxes 1 (max num (second maxes))))]
            [(equal? col "blue") (helper (rest draws) (list-set maxes 2 (max num (third maxes))))]))))

  (helper (string-split (string-replace (second (string-split line ":")) ";" ",") ",") '(0 0 0)))

(printf "part 2 example: ~a\n" (apply + (map power-of-cubes (file->lines "example.txt"))))
(printf "part 2: ~a\n" (apply + (map power-of-cubes (file->lines "input.txt"))))
