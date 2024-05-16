crear(X, Y, [X, Y]).


:- begin_tests(lists).

test(crear) :-
        crear(1, 2, [1,2]).

:- end_tests(lists).