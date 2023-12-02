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
    (let ([red-max 0][blue-max 0][green-max 0])
        (for ([cubes (string-split (string-replace (second (string-split line ":")) ";" ",") ",")])
            (cond [(equal? (second (string-split cubes " ")) "red") (set! red-max (max red-max (string->number (first (string-split cubes " ")))))]
                  [(equal? (second (string-split cubes " ")) "blue") (set! blue-max (max blue-max (string->number (first (string-split cubes " ")))))]
                  [(equal? (second (string-split cubes " ")) "green") (set! green-max (max green-max (string->number (first (string-split cubes " ")))))]))
        (* red-max blue-max green-max)))

(printf "part 2 example: ~a\n" (apply + (map power-of-cubes (file->lines "example.txt"))))
(printf "part 2: ~a\n" (apply + (map power-of-cubes (file->lines "input.txt"))))