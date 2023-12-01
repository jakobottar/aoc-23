#lang racket

(define (cv line)
  (let ([line (filter char-numeric? (string->list line))])
    (string->number (list->string (list (first line) (first (reverse line)))))))

(printf "part 1 example: ~a\n" (apply + (map cv (file->lines "example1.txt"))))
(printf "part 1: ~a\n" (apply + (map cv (file->lines "input.txt"))))

(define (cv2 line)
  ; todo: fix later
  (let* ([line (regexp-replace* #rx"one" line "o1e")]
         [line (regexp-replace* #rx"two" line "t2o")]
         [line (regexp-replace* #rx"three" line "t3hree")]
         [line (regexp-replace* #rx"four" line "f4ur")]
         [line (regexp-replace* #rx"five" line "f5ve")]
         [line (regexp-replace* #rx"six" line "s6x")]
         [line (regexp-replace* #rx"seven" line "s7ven")]
         [line (regexp-replace* #rx"eight" line "e8ght")]
         [line (regexp-replace* #rx"nine" line "n9ne")])

    (cv line)))

(printf "part 2 example: ~a\n" (apply + (map cv2 (file->lines "example2.txt"))))
(printf "part 2: ~a\n" (apply + (map cv2 (file->lines "input.txt"))))
