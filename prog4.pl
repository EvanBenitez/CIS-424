male(mushu).
male(tangdee).
male(X):-father(X,_).
female(mulan).
female(beumei).
female(gugu).
female(X):-mother(X,_).

father(baba,mushu).
father(baba,mulan).
father(yeye,baba).
father(yeye,gugu).
father(yeye,susu).
father(susu,tangdee).
father(zengzufu,yeye).
father(jojo,beumei).

mother(mama,mushu).
mother(mama,mulan).
mother(popo,mama).
mother(popo,jojo).


parent(X,Y):- mother(X,Y).
parent(X,Y):- father(X,Y).
sibling(X,Y):- parent(Z,X), parent(Z,Y), not(X=Y).
brother(X,Y):- sibling(X,Y), male(X).
aunt(X,Y):- parent(Z,Y), sibling(X,Z), female(X).
aunt(X,Y):- parent(P,Y), sibling(P,S), parent(S,C), parent(X,C), female(X).
grandson(X,Y):- parent(Y,Z), parent(Z,X), male(X).
descendant(X,Y):- parent(Y,X).
descendant(X,Y):- parent(Z,X), descendant(Z,Y).



listend([L|[]],L).
listend([H|T],E):- listend(T,E).



match(X,[X|T],T).
x(X,Y):-match(p,X,Y).
x(X,Y):-match(p,X,X1),x(X1,Y).
y(X,Y):-match(q,X,X1),match(r,X1,Y).
z(X,Y):-match(t,X,Y).
z(X,Y):-match(t,X,X1),z(X1,Y).
s(X,Y):-x(X,X1),y(X1,X2),z(X2,Y).



tests(3).
democrats=[1,2,3,4,5].
member(ELEM,[ELEM|_]):-!.
member(ELEM,[_|T]):- member(ELEM,T).
dem_candidate(X):- member(X, [1,2,3,4,5]), tests(X).
