crear(X, Y, [X, Y]).


insertar_ordenado([], Ys, Ys).
insertar_ordenado(Xs, [], Xs).
insertar_ordenado([X | Xs], [Y | Ys], [X | Zs]):-
        X < Y,
    	!,
        insertar_ordenado(Xs, [Y | Ys], Zs).
insertar_ordenado([X | Xs], [Y | Ys], [Y | Zs]):-
        insertar_ordenado([X | Xs], Ys, Zs).


word(astante, a,s,t,a,n,t,e).
word(astoria, a,s,t,o,r,i,a).
word(baratto, b,a,r,a,t,t,o).
word(cobalto, c,o,b,a,l,t,o).
word(pistola, p,i,s,t,o,l,a).
word(statale, s,t,a,t,a,l,e).

crossword(V1, V2, V3, H1, H2, H3):-
	word(V1, _, A1, _, A2, _, A3, _),
	word(V2, _, B1, _, B2, _, B3, _),
	word(V3, _, C1, _, C2, _, C3, _),
	word(H1, _, A1, _, B1, _, C1, _),
	word(H2, _, A2, _, B2, _, C2, _),
	word(H3, _, A3, _, B3, _, C3, _),
    V1 \= H1,
    V2 \= H2,
    V3 \= H3.