%%% some tree predicates %%%

% empty tree predicate
emptyBTree :- nil.
%non empty tree
bTree(Tl,N,Tr) :-
  Tl @=< N,
  Tr @> N.

% insert element to tree
%inset(curr tree, val, new tree)
insert(nil,N,bTree(nil,N,nil)).
insert(bTree(L,C,R),N,bTree(NewL,C,R)) :-
  N @=< C,
  !,
  insert(L,N,NewL).
insert(bTree(L,C,R),N,bTree(L,C,NewR)) :-
  insert(R,N,NewR).

% search if element is in tree
% returns True if N is in bTree
search(N,bTree(_,N,_)).
search(N,bTree(L,C,_)):-
  N @=< C,
  search(N,L).
search(N,bTree(_,_,R)):-
  search(N,R).


%%% traversals %%%
%preorder traversal
preorder(nil,[]).
preorder(bTree(L,N,R),Lst) :-
 preorder(L,LLst),
 preorder(R,RLst),
 append([N|LLst],RLst,Lst).

%inorder traversal
inorder(nil,[]).

inorder(bTree(L,N,R),Lst) :-
 inorder(L,LLst),
 inorder(R,RLst),
 append(LLst,[N|RLst],Lst).

%postorder traversal
postorder(nil,[]).
postorder(bTree(L,N,R),Lst) :-
  postorder(L,LLst),
  postorder(R,RLst),
  append(LLst,RLst,RN),
  append(RN,[N],Lst)
