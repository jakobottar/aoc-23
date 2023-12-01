#lang racket

(define (cv line)
  (let ([line (filter char-numeric? (string->list line))])
    (string->number (list->string (list (first line) (first (reverse line)))))))

(printf "part 1 example: ~a\n" (apply + (map cv (file->lines "example1.txt"))))
(printf "part 1: ~a\n" (apply + (map cv (file->lines "input.txt"))))

(define (cv2 line)
    (cv (regexp-replaces line '([#rx"one" "o1e"]
                                [#rx"two" "t2o"]
                                [#rx"three" "t3e"]
                                [#rx"four" "f4r"]
                                [#rx"five" "f5e"]
                                [#rx"six" "s6x"]
                                [#rx"seven" "s7n"]
                                [#rx"eight" "e8t"]
                                [#rx"nine" "n9e"]))))

(printf "part 2 example: ~a\n" (apply + (map cv2 (file->lines "example2.txt"))))
(printf "part 2: ~a\n" (apply + (map cv2 (file->lines "input.txt"))))
