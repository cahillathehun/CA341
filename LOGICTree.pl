% Binary Tree in Prolog
% have to have:
%
%	-insert
%	-search(return True if in tree)
%
%	-preorder
%	-inorder
%	-psotorder
istree(nil).
istree(tree(_,Left,Right)) :- istree(Left), istree(Right).

bTree(tree(nil,N,nil)).
bTree(tree(Left,N,nil)) :- Left @=< N
bTree(tree(nil,N,Right)) :- N @< Right
bTree(tree(Left,_,Right)) :- bTree(Left), bTree(Right).
bTree(tree(Left,N,Right)) :- Left @=<N, N @< Right.


% insert
insert(nil,N,bTree(nil,N,nil)).			% insert if N is root

insert(bTree(L,M,R), N, bTree(L1,M,R)):-		% called if 1st clause fails
	N @=< M, insert(L,N,L1).		% if N =< root, try to put in L subtree

insert(bTree(L,M,R), A, bTree(L,M,R1)):-		% called if above fails, try to put in R subtree
	insert(R,N,R1).

% search
search(N,bTree(nil,N,nil).			% return True if a is root

search(N,bTree(L,M,nil)):-			% called if 1st clause fails
	N @=< M, search(N,L).			% if A =< root, search L subtree

search(N,bTree(nil,nil,R)):-			% called if A not in L or root, search R subtree
	search(N,R).

% preorder traversal
preorder(nil,[]).

preorder(bTree(L,N,R),[X|Lst]) :-
   preorder(L,LLst),
   preorder(R,RLst),
   append(LLst,RLst,Lst).

& inorder traversal
inorder(T,S) :- inorder_tl(T,L), atom_chars(S,L).
inorder_tl(nil,[]).

inorder_tl(bTree(L,N,R),Lst) :-
   inorder_tl(L,LLst),
   inorder_tl(R,RLst),
   append(LLst,[N|RLst],Lst).
