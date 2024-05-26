crear(X, Y, [X, Y]).


insertar_ordenado([], Ys, Ys).
insertar_ordenado(Xs, [], Xs).
insertar_ordenado([X | Xs], [Y | Ys], [X | Zs]):-
        X < Y,
        insertar_ordenado(Xs, [Y | Ys], Zs).
insertar_ordenado([X | Xs], [Y | Ys], [Y | Zs]):-
        insertar_ordenado([X | Xs], Ys, Zs).
