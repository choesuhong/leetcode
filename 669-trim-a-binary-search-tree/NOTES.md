if not low <= val <= high :
return None
근데 자식 노드가 있다면?
return root.right or root.left
​